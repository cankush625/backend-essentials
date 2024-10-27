from django.apps import AppConfig


class CoreAppConfig(AppConfig):
    name = "backend_essentials.core"
    verbose_name = "Backend Essentials Core App"

    def ready(self):
        # Import async task modules to register the tasks
        # like signals, celery task files, etc.
        # E.g.
        # import backend_essentials.common.signals  # noqa

        ...
