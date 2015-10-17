from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique = True)
    fullName = models.CharField(max_length=50, blank = False)
    phoneNumber = models.CharField(max_length=10, blank = True,
                    validators=[RegexValidator(r'^[0-9]*$', 'Only 0-9 allowed', 'Invalid Number')])
    website = models.URLField("Website", blank = True)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
