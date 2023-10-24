from django.apps import AppConfig


class TaskSchedulerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "task_scheduler"

    def ready(self):
        from task_scheduler.scheduler import start_scheduler

        start_scheduler()
