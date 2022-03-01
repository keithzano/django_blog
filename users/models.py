from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default ='default.jpg', upload_to='profile_pics')
	address = models.TextField(max_length=100, default='Cape Town, South Africa')
	phone = models.TextField(max_length=100, default= '(021) 234-5678')
	tel = models.TextField(max_length=100, default= '(021) 234-5678')



	def __str__(self):
		return f'{self.user.username} Profile'