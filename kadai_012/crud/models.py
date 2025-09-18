from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, blank=True, null=True)
    # 画像フィールドを追加する（追加する画像は省略可能で、省略時はデフォルト画像としてnoImage.pngを使用）
    # blank属性がTrueの場合必須入力とならない
    img = models.ImageField(blank=True, default='noImage.png')

    def __str__(self):
        return self.name
    
    # 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')


