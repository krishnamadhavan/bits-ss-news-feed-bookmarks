from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(
        _("Created At"), auto_now_add=True, help_text=_("Created Date and Time")
    )
    updated_at = models.DateTimeField(
        _("Updated At"), auto_now=True, help_text=_("Updated Date and Time")
    )

    class Meta:
        abstract = True
