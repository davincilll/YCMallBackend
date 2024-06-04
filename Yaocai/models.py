import random

from django.db import models


def price_default():
    # 设置价格范围
    min_price = 10  # 最低价格
    max_price = 100  # 最高价格
    # 生成随机价格
    price = random.randint(min_price, max_price)
    return price


class CategoryType(models.Model):
    # 分类的标题
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# Create your models here.
class Yaocai(models.Model):
    # 药材名字
    name = models.CharField(max_length=20)
    description = models.TextField()
    inventory = models.IntegerField(default=100)
    # 价格
    price = models.DecimalField(max_digits=6, decimal_places=2, default=price_default)  # 价格()
    # 药材的图片url
    image = models.URLField(max_length=200)
    categoryType = models.ForeignKey(CategoryType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
