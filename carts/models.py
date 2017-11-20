from django.db import models
from db.AbstractModel import BaseModel

# Create your models here.


class Carts(BaseModel):
    u_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_num = models.IntegerField()
