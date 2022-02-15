from django.db import models


class SocialNetwork(models.Model):
    name = models.CharField(max_length=25, unique=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Social Networks'

    def __str__(self):
        return self.name
