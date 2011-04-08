from django.core.cache import cache
from django.db.models import Sum
from django.db.models.signals import post_save
from main import models

AMOUNT_KEY = 'amount'

def get_total_amount():
    amount = cache.get(AMOUNT_KEY)
    if amount is None:
        agg_dict = models.Pledge.objects.filter(
            confirm_date__isnull=False).aggregate(Sum('amount'))
        amount = int(agg_dict['amount__sum'] or 0)
        # 24 hours
        cache.set(AMOUNT_KEY, amount, 24 * 60 * 60)
    return amount

def _pledge_post_save(sender, **kwargs):
    cache.set(AMOUNT_KEY, None)

post_save.connect(_pledge_post_save, models.Pledge)
