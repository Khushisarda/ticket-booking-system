from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)


class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # New field for an image URL:
    image_url = models.URLField(blank=True, null=True)
    datetime = models.DateTimeField()
    total_seats = models.IntegerField()
    available_seats = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.seats_booked} seats for {self.show.title}"

