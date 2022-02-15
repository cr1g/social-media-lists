from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=255)
    url = models.URLField()
    date_posted = models.DateTimeField()
    account = models.ForeignKey(
        'persons.Account', related_name='posts', on_delete=models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return \
            f'[{self.date_posted.strftime("%Y-%m-%d %H:%M:%S")}]: ' \
            f'{self.content[:10]}'
