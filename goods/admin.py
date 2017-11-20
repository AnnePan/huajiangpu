from django.contrib import admin
from .models import *


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'anno_title', 'anno_detail', 'anno_image']

#
# @admin.register(Goods)
# class GoodsAdmin(admin.ModelAdmin):
#     list_display = ['g_name', 'g_cate', 'g_unit', 'g_price', 'g_look', 'g_desc', 'g_detail', 'g_image', 'g_florid']


admin.site.register(Category)
admin.site.register(Activity)



