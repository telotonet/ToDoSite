from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, is_active=True, is_staff=False,  is_admin=False):
        # if not email:
        #     raise ValueError('Users must have email address!')
        if not password:
            raise ValueError('Users must have a password!')
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.staff     = is_staff
        user_obj.username  = username
        user_obj.is_active = is_active
        user_obj.admin     = is_admin
        user_obj.save()
        return user_obj
    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(
            email    = email,
            username = username,
            password = password,
            is_admin = True,
            is_staff = True,
        )
        return user
    def create_staffuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            username,
            password = password,
            is_admin = True,
        )
        return user

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, blank=True)
    username    = models.CharField(max_length=255, unique=True)
    is_active   = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username' 

    objects = UserManager()


    def __str__(self):
        return self.username
    
    def get_full_name(self):
        if self.username:
            return self.username
        return self.email
    
    def get_short_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    # @property
    # def is_active(self):
    #     return self.is_active
    
    @property
    def is_admin(self):
        return self.admin