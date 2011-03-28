from django.forms import ModelForm
from django import forms
from main.models import Pledge
from uuid import uuid4

class PledgeForm(ModelForm):
    class Meta:
        model = Pledge
        fields = ('email', 'amount',)

    def save(self, request):
        obj = Pledge(
            ip_address=request.META.get('REMOTE_ADDR', 'no ip address'),
            email=self.cleaned_data['email'],
            amount=self.cleaned_data['amount'],
            confirm_code = str(uuid4()).replace('-', ''))
        obj.save()
        return obj

    def get_errors(self):
        from django.utils.encoding import force_unicode        
        output = {}
        for key, value in self.errors.items():
            output[key] = '/n'.join([force_unicode(i) for i in value])
        return output
