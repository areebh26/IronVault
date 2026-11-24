from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=25, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    profile_picture_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    roles = models.ManyToManyField("roles.Role", db_table="users_roles", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"



class PasswordResetCode(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=128, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expires_at = models.DateTimeField()
    used = models.BooleanField(default=False)

    class Meta:
        db_table = "password_reset_code"