from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):
    # password=None in case we need an inactive user, that doesn't require a password.
    # **extra_fields says take any function that is passed in and passed into extra_fields
    # it makes it more flexible
    def create_user(self, email, password=None, **extra_fields):
        # creats and saves a new user

        # the way the management commands works is we can access the models that the manager
        # has, just by typing self.model

        if not email:
            raise ValueError('Users must hava an email address')

        # email is normalized with the provided normailze function
        user = self.model(email=self.normalize_email(email), **extra_fields)

        # set_password comes with the AbstractBaseUser
        # it does all the encryption thing because we cannot save password as plain text
        user.set_password(password)
        # if we have multiple db the 'using' command is essential
        user.save(using=self._db)

        return user


    def create_superuser(self, email, password):
        # creates and saves a new super user
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self.db)

        return user



class User(AbstractBaseUser, PermissionsMixin):
    # custom user model that supports email instead of user name
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # to determine weather is the user in the system is active or not
    is_active = models.BooleanField(default=True)
    # for staff user
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # by default the username field is username now we are changing it to email
    USERNAME_FIELD = 'email'
