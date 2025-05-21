from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class MyModel(models.Model):
    GENDER = [
        ('F', 'FEMALE'),
        ('M', 'MALE'),
        ('O', 'OTHER'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')   
    bio = models.TextField(max_length=200)
    sex = models.CharField(max_length=2, choices=GENDER, default='F')  
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

# One to Many

class Posts(models.Model):
    user = models.ForeignKey(MyModel, on_delete=models.CASCADE, related_name='posts')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    post_description = models.TextField()
    date_added = models.DateTimeField(timezone.now)

    def __str__(self):
        return f'post for {self.user.name}'
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    post = models.ManyToManyField(MyModel, related_name='comment')

    def __str__(self):
        return self.name
    
class VerifiedBadge(models.Model):
    badge = models.OneToOneField(MyModel, on_delete=models.CASCADE, related_name='verify_badge')
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Badge for {self.badge.name}'
