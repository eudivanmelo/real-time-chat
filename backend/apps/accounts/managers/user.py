
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_superuser(self, email, password):
        user = self.model(email=self.normalize_email(email))
        
        user.set_password(password)
        user.is_superuser = True
        user.save(using=self._db)
        
        return user