from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from ..managers import UserManager

class User(AbstractBaseUser):
    avatar = models.TextField(default='/media/avatars/default-avatar.png')
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    last_access = models.DateTimeField(auto_now_add=True)
    
    # Manager settings
    objects = UserManager()
    USERNAME_FIELD = 'email'
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    def __str__(self):
        return self.email
    
    @property
    def is_staff(self):
        return self.is_superuser
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'