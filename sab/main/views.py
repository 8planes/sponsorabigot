from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
import django.utils.simplejson as json
from main.forms import PledgeForm
from main import models
from boto.ses import SESConnection

def _send_email(email, amount, confirm_code):
    if not settings.DEBUG:
        context = {
            'confirm_url': reverse('main:confirm_pledge', args=[confirm_code]) }
        connection = SESConnection(
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY)
        connection.send_email(
            source="pledges@sponsorabigot.org",
            subject="Please confirm your pledge",
            body=render_to_string('pledge_email.html', context),
            to_addresses=[email],
            format='html',
            cc_addresses=['pledges@sponsorabigot.org'])
    else:
        print('Sent email to {0} about {1} with confirm code {2}'.format(
                email, amount, confirm_code))

def pledge(request):
    form = PledgeForm(request.POST)
    if form.is_valid():
        pledge = form.save(request)
        _send_email(pledge.email,
                    pledge.amount,
                    pledge.confirm_code)
        output = dict(success=True)
    else:
        output = dict(success=False, errors=form.get_errors())
    return HttpResponse(json.dumps(output), 'text/javascript')

def donate(request):
    return render_to_response(
        'donate0.html',
        { 'form': PledgeForm() },
        context_instance=RequestContext(request))

def confirm_pledge(request, confirm_code):
    try:
        pledge = models.Pledge.objects.get(confirm_code=confirm_code)
    except ObjectDoesNotExist:
        return redirect('main:confirm_fail', confirm_code=confirm_code)
    return render_to_response(
        'confirm.html',
        { 'pledge': pledge },
        context_instance=RequestContext(request))

def confirm_fail(request, confirm_code):
    return render_to_response(
        'confirm_fail.html',
        context_instance=RequestContext(request))
