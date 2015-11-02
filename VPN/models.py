from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = model.EmailField()
    password = models.CharField(max_length=50)

    FEMALE = 'F'
    MALE = 'M'
    SEX_CHOICE = ((FEMALE, 'female'),(MALE, 'male'))
    sex = models.CharField(max_length=1, choice=SEX_CHOICE, defalt=FEMALE,blank=True)

    joined_date = models.DateTimeField(editable=False)
    last_login = models.DateTimeField()
    user_level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
    """On save, update timestamps """
        if not self.user_id:
            self.created = timezone.now()
        self.last_login = timezone.now()
        return super(User, self).save(*args, **kwargs)
