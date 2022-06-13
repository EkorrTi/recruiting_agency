from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Account_Manager(BaseUserManager):
    def create_user(self, email, username, is_employer, is_manager, password=None):
        if not email:
            raise ValueError('Users must have an email!')
        if not username:
            raise ValueError('Need to have a username')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            is_employer = is_employer,
            is_manager = is_manager,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, is_employer, is_manager, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
            is_employer=False,
            is_manager=True
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    email               = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True)
    date_joined         = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_employer         = models.BooleanField(default=False)
    is_manager          = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'is_employer', 'is_manager']

    objects = Account_Manager()

    def __str__(self): 
        return self.email
    
    def name(self):
        return self.username       
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True