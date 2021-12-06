from django.db import models


class TimestampModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 設定為抽象，此model就可以被繼承
