from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from phonenumber_field.modelfields import PhoneNumberField

# accounts.models.py

class UserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name, phone, college_name,password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError("Name Cannot Be left Blank")
        if not phone:
            raise ValueError("Phone Number Cannot Be left Blank")
        if not college_name:
            raise ValueError("College name must be selected")

        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,
            college_name = college_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,first_name,last_name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name,last_name, password):

        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

COLLEGE_CHOICES = (
    ('','Select College'),
    ('nitkkr','NIT KURUKSHETRA'),
    ('thappar', 'THAPPAR , PATIALA')
)
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    college_name = models.CharField(max_length=20, choices=COLLEGE_CHOICES, default='')
    phone = PhoneNumberField(unique = True, null=True, blank = False, region = 'IN', max_length = 13) 
    first_name = models.CharField( max_length=20 , null = True, blank = False)
    last_name = models.CharField(max_length = 20 , null = True, blank = False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','college_name','phone'] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
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
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active