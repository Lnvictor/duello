from email.policy import default
from django.db import models
from django.contrib.auth import base_user


class Claims(models.Model):
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_battle = models.BooleanField(default=True)
    can_battle_in_own = models.BooleanField(default=False)

    def __repr__(self) -> str:
        return self.description


class Roles(models.Model):
    description = models.CharField(max_length=150)
    claim_id = models.OneToOneField(Claims, on_delete=models.CASCADE)

    def __repr__(self) -> str:
        return self.description


class Users(base_user.AbstractBaseUser):
    user_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.EmailField(unique=True)
    last_sended_token = models.CharField(max_length=6, null=True)
    verified = models.BooleanField(default=False)
    role_id = models.ForeignKey(Roles, on_delete=models.DO_NOTHING, default=1)

    def __repr__(self) -> str:
        return self.user_email