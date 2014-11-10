from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	gender = models.CharField(max_length=1, choices=(('m', 'Male'), ('f', 'Female')))
	date_of_birth = models.DateField('date_of_birth', default=datetime(9999, 12, 31, 0, 0))

	User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
