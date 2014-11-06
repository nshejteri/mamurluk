from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)

	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)

	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	#country = models.CharField(max_length=20, blank=True)
	#sity = models.CharField(max_length=20, blank=True)

	User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
