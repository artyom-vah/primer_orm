from django.db import models
from app_primer.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='user_images')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self):
        super().save()
        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

