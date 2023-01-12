from django.db import models
from django.contrib.auth.models import BaseUserManager , AbstractBaseUser
from rest_framework.utils import field_mapping

# Create your models here.

class Myusermanager(BaseUserManager):
    def normalize_phone(self,name):
        return name.lower().strip()

    def __create(self,phone,email,password):
        if not email:
            raise ValueError("user shoudld have a email")
        if not phone:
            raise ValueError("user should have a phone")

        user = self.model(
            email = self.normalize_email(email)  , phone = self.normalize_phone(phone)
        )

        user.set_password(password)
        user.save ( using = self._db)
        return user

    def create_user(self,phone,email,password=None):
        user = self.__create(phone,email,password)
        user.save()
        return user

    def create_superuser(self,phone,email,password=None):
        user = self.__create(phone,email,password)
        user.is_admin = True
        user.save()
        return user

class MyUser(AbstractBaseUser):
    email  = models.EmailField(unique=True)
    phone = models.CharField(unique=True , max_length=15)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)

    objects = Myusermanager()

    USERNAME_FIELD = "phone"

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.email

    def has_perm(self , obj=None):
        return True

    def has_module_perms(self , app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

#image
def upload_pic(instance , filename):
    return "accounts/{user}/{filename}".format(
        user = instance.user.id , filename = filename
    )


class profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    user = models.OneToOneField(MyUser ,on_delete=models.CASCADE)
    profile_pic = models.FileField(upload_to=upload_pic)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name