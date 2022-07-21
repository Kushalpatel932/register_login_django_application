from django.db import models

# Create your models here.
class register(models.Model):
    user_name = models.CharField(max_length=25)
    user_email = models.EmailField()
    user_phone_no = models.IntegerField(default=0)
    user_dob = models.DateField(default=0)
    user_password1 = models.CharField(max_length=25)
    user_password2 = models.CharField(max_length=25)
    

    def __str__(self):
        return self.user_name
