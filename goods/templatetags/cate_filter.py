from django.template import Library

register = Library()


# 计算类别的总宽度
@register.filter
def cate_width(count):
    return 50 * int(count) + 600


# 计算类别应该出现的位置
@register.filter
def cate_left(index):
    index = int(index)
    if index > 1:
        return 50 * (index-1) + 600
    return 0


