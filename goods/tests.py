from django.test import TestCase
from .models import *
import random

# Create your tests here.

# 公告测试数据
# anno = Announcement()
# anno.anno_title = '公告！小花匠下周二出差！'
# anno.anno_detail = '小花匠下周二出差！小伙伴们周二来啦！小花匠下周一出差！小伙伴们周二来啦！小花匠下周一出差！小伙伴们周二来啦！小花匠下周一出差！小伙伴们周二来啦！'
# anno.anno_image = 'images/ann_1.jpg'
# anno.save()


# 活动测试数据
# acti = Activity()
# acti.act_title = '11月你好！买生日花束送可爱小熊！'
# acti.act_subtitle = '生日送花,你选对了吗?生日鲜花该如何送?这送花和送礼一样,也是有讲究,不能轻率随便了事。 下面就和小编一起来学习一下,这生日鲜花该如何送,才是最恰到好处的...'
# acti.act_activiting = True
# acti.act_detail = '11月1日-11月30日，买生日花束送可爱小熊！'
# acti.act_image = 'images/act_1.jpg'
# acti.save()

# 类别测试数据
# for name in ['鲜花','花束','花篮','婚车','手捧花','展台']:
#     c = Category()
#     c.cate_name = name
#     c.cate_desc = name + '的描述'
#     c.save()

# 商品测试数据
# for i in range(40):
#     g = Goods()
#     g.g_name = "花名{}".format(i)
#     g.g_cate_id = random.randint(2, 7)
#     g.g_image = "images/"+str(random.randint(1, 10))+".jpg"
#     g.g_desc = "这里是描述"+g.g_name
#     g.g_unit = "1朵"
#     g.g_price = 4.99
#     g.g_look = 2
#     g.save()


# l = [{'name': '台花', 'cate':6},
#  {'name': '春日', 'cate': 6},
#  {'name': '风信子', 'cate': 1},
#  {'name': '蝴蝶花', 'cate': 2},
#  {'name': '缤纷', 'cate': 2},
# {'name': '欢乐颂', 'cate':3},
#  {'name': '浪漫', 'cate': 3},
#  {'name': '爱情', 'cate': 2},
#  {'name': '太阳花', 'cate': 1}]
# for index, temp in enumerate(l):
#     g = Goods()
#     g.g_name = temp['name']
#     g.g_cate_id = temp['cate']
#     g.g_desc = '青青柔蔓绕修篁，刷翠成花着处芳。应是折从河鼓手，天孙斜插鬓云香。'
#     g.g_detail = '牵牛的花期长达数月（5～7月），花冠喇叭状；花形有单瓣、重瓣、瓣缘皱褶或呈不规则锯齿等; 花色有红、白、粉、紫及各种带'
#     g.g_florid = '牵牛花的花语：名誉/爱情永固'
#     g.g_image = 'images/'+str(index+2)+'.jpg'
#     g.g_price = 2.00
#     g.save()





