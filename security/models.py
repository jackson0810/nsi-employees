from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from shared.utilities import make_uuid


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
    username = models.CharField(max_length=250, blank=True, null=True, verbose_name='User Name')
    user_uuid = models.CharField(max_length=36, default=make_uuid, db_index=True)
    account_type = models.IntegerField()
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    office_phone = models.CharField(max_length=14, null=True, blank=True, verbose_name='office phone')
    mobile_phone = models.CharField(max_length=14, null=True, blank=True, verbose_name='mobile phone')
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
    def get_account_type_string(self):
        at = self.account_type

        return 'Administrator' if at == 1 else 'General User'

    @property
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

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
