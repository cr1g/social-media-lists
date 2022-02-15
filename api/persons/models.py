from django.db import models


class Person(models.Model):
    username = models.CharField(max_length=50, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class PersonsCollection(models.Model):
    name = models.CharField(max_length=50, unique=True)
    persons = models.ManyToManyField(
        Person, related_name='collections', related_query_name='collections')

    class Meta:
        verbose_name = 'Persons Collection'
        verbose_name_plural = 'Persons Collections'

    def __str__(self):
        return self.name


class Account(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    person = models.ForeignKey(
        Person, related_name='accounts', on_delete=models.DO_NOTHING)
    network = models.ForeignKey(
        'common.SocialNetwork', related_name='accounts', 
        on_delete=models.DO_NOTHING)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('email', 'network')

    def __str__(self):
        return f'{self.person.username}/{self.email}'

    def get_avatar(self):
        if self.avatar:
            return f'/media/{self.avatar.name}'

        return None
