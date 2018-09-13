from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=150, db_index=True)
    last_name = models.CharField(max_length=150, db_index=True)
    number_of_login= models.IntegerField()

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.first_name