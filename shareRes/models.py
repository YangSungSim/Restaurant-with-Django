from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)

class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT,default=3)
    # 참조되는 요소가 삭제될 때 참조값을 설정해둔 default 값으로 설정한다. 레스토랑 요소가 참조하는 카테고리가 삭제될 때 자동으로 id값이 3인
    # 카테고리를 참조한다.
    restaurant_name = models.CharField(max_length= 100)
    restaurant_link = models.CharField(max_length= 500)
    restaurant_content = models.TextField()
    restaurant_keyword = models.CharField(max_length= 50)