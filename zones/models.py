from django.db import models

class SmokingZone(models.Model):
    address = models.CharField(max_length=35, null=False)
    detail_address = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to="smokingzone_image/", null=True)

class Review(models.Model):
    content = models.CharField(max_length=300, null=True)
    RATING_NUM = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    rating = models.IntegerField(choices=RATING_NUM)
    smoking_zone = models.ForeignKey("zones.SmokingZone", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
