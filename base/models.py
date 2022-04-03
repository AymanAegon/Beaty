from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    bio = models.TextField(null=True, default="")
    profile_img = models.ImageField(null=True, upload_to="images/")
    birthday=models.DateField(auto_now=False, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username


class Beat(models.Model):
    creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creater')
    name = models.CharField(max_length=200)
    img = models.ImageField(null=True, upload_to="images/")
    description = models.TextField(default="")
    members = models.ManyToManyField(User, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    beat = models.ForeignKey(Beat, on_delete=models.CASCADE)
    body = models.TextField()
    action = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.body[0:50]