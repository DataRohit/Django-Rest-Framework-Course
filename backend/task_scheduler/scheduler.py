from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from tokenauth.models import ExpiringToken


def clear_expired_tokens():
    queryset = ExpiringToken.objects.filter(expiration__lt=timezone.now())
    queryset.delete()


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.start()

    scheduler.add_job(
        clear_expired_tokens,
        "interval",
        minutes=5,
        id="token_clear_job",
        replace_existing=True,
    )
