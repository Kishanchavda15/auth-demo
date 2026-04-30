from django.contrib.auth.base_user import BaseUserManager


class UserManage(BaseUserManager):

    def _create_user_object(self, email, password, **extra_field):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_field):
        extra_field.setdefault("is_staff", False)
        extra_field.setdefault("is_superuser", False)
        return self._create_user_object(email, password, **extra_field)

    def create_superuser(self, email, password, **extra_field):
        extra_field.setdefault("is_staff", True)
        extra_field.setdefault("is_superuser", True)
        return self._create_user_object(email, password, **extra_field)
