from django.db import models
from django.contrib.auth.models import (
AbstractBaseUser,BaseUserManager
)
# Create your models here.
class MyUserManger(BaseUserManager):

    def create_user(self,email,contact_no,password=None):
        if not email:
            raise ValueError("user must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            contact_no=contact_no,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,contact_no,password=None):
        user = self.create_user(
            email = email,
            password=password,
            contact_no=contact_no
        )
        user.is_admin=True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    contact_no = models.CharField(verbose_name="contact no",unique=True,max_length=14)
    is_active =  models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact_no']

    def __str__(self):
        return self.email


    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
