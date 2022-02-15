from urllib.parse import urlparse

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email_address'), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class RSSFeeds(models.Model):
    url = models.URLField(max_length=1000)

    def __str__(self):
        return self.parse_domain(self.url)

    def parse_domain(self, url):
        return urlparse(url).netloc


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rssfeed = models.ForeignKey(RSSFeeds, on_delete=models.CASCADE)
