from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import Q


class CustomUserManager(BaseUserManager):
    def create_user(self, email, account_type, password=str(uuid4)):
        if not email:
            raise ValueError('Email address is required to create a user')

        if not account_type:
            raise ValueError('Account Type is required to create a user')

        user = self.model(email=self.normalize_email(email), account_type=account_type)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a super User with the given email and password.
        """

        email = self.normalize_email(email)
        user = self.model(email=email, is_admin=True, is_active=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    ACCOUNT_TYPES = [(1, 'Administrator'), (2, 'General User'), (3, 'News Admin')]

    username = models.CharField(max_length=250, blank=True, null=True, verbose_name='User Name')
    account_type = models.IntegerField(choices=ACCOUNT_TYPES)
    email = models.EmailField(max_length=250, unique=True, db_index=True)
    password_reset = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False, verbose_name='Is Active')
    is_admin = models.BooleanField(default=False, verbose_name='Is Superuser', help_text='Django admin user.')
    dt_created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Date/Time Created')
    dt_updated = models.DateTimeField(auto_now=True, blank=True, verbose_name='Date/Time Updated')
    dt_last_login = models.DateTimeField(blank=True, null=True, verbose_name='Date/Time Last Login')
    dt_password_reset = models.DateTimeField(verbose_name='Date/Time Password Reset', blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['account_type']

    @property
    def get_full_name(self):
        return self.email

    @property
    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def email_link(self):
        return '<a href="mailto:{}">{}</a>'.format(self.email, self.email)

    email_link.allow_tags = True

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_superuser(self):
        """
        This mirror `is_admin` attribute
        :return: Boolean
        """
        return self.is_admin

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        unique_together = ['email', 'account_type']
        ordering = ['email', ]
