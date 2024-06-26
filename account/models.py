from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser, BaseUserManager
import datetime

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self,email, birth_dt,national_id,phone_number,first_name,last_name, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            birth_dt=birth_dt,
            national_id=national_id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, birth_dt,national_id,phone_number,first_name,last_name, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            birth_dt=birth_dt,
            national_id=national_id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_dt = models.DateField(default=datetime.date.today)
    email = models.EmailField(
        unique=True, max_length=255, null=False, blank=False)
    national_id = models.CharField(
        max_length=15, unique=True, null=False, blank=False)
    phone_number = models.CharField(
        max_length=11, unique=True, null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)
    register_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "national_id"
    REQUIRED_FIELDS = ['first_name', 'last_name','email','phone_number','birth_dt']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


