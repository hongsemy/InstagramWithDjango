from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Djangostagram."""
    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('C', 'Custom'),     
        # Users will see the second element in each tuple (e.g. MALE) 
        # and db will save the value of the first element in each tuple (e.g. M).
    ]   

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_pic = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = models.CharField(blank=True, max_length=255)
    phone_number = models.CharField(blank=True, max_length=255)
    gender = models.CharField(blank=True, choices = GENDER_CHOICES, max_length=255)
    # parameter choices will limit the user to choose only from the given choices 
    # based on what is passed as an argument.
    followers = models.ManyToManyField("self")
    following = models.ManyToManyField("self")


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
