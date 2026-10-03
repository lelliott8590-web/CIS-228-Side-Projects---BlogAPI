from django.contrib.auth.models import AbstractUser

class Customuser(AbstractUser):
    pass 

    def __str__(self):
        return self.username