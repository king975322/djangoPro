import hashlib

from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Users"

    def set_password(self, password):
        # 使用加密算法对password进行加密
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def check_password(self, password):
        # 使用相同的加密算法对输入的password进行加密，并与数据库中的password进行比较
        encrypted_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return encrypted_password == self.password


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name_plural = "User Profiles"
