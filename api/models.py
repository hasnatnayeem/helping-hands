from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
    phone = models.CharField(max_length=45, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100, default='Bangladesh', blank=True)
    token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Donation(models.Model):
    donor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField()
    collector = models.ForeignKey(User, on_delete=models.CASCADE)
    collected_at = models.DateField()
    logged_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.donor) + ' - ' + str(self.amount)
