from django.db import models
from db.AbstractModel import *
from utils.wrapper import *

# Create your models here.


class UserManager(models.Manager):

    def user_register(self, request):
        user = User()
        user.u_name = post(request, 'u_name')
        user.u_tele = post(request, 'u_phone')
        user.u_pass = password_encryption(post(request, 'u_pass'))
        user.save()

    def user_update_recv(self, request):
        pass

    def user_by_name(self, u_name):
        try:
            return self.get(u_name=u_name)
        except User.DoesNotExist:
            return None


class User(BaseModel):
    u_name = models.CharField(max_length=20)
    u_pass = models.CharField(max_length=80)
    u_tele = models.CharField(max_length=11)
    u_recv = models.CharField(max_length=20)
    u_addr = models.CharField(max_length=50)
    u_recv_tele = models.CharField(max_length=11)

    objects = UserManager()


class Contact(BaseModel):
    c_uname = models.CharField(max_length=20)
    c_tel = models.CharField(max_length=20)
    c_message = models.CharField(max_length=20)
