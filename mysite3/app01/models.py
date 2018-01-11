from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class BBS(models.Model): # BBS
    title = models.CharField(max_length=50) # 标题
    summary = models.CharField(max_length=200,blank=True,null=True) # 摘要.可以为空,blank是admin中可为空,null是表里可为空
    content = models.TextField()
    author = models.ForeignKey('BBS_user',on_delete=models.CASCADE,) # 作者,外键到BBS_user中,用到还未定义的表要用引号
    view_count = models.IntegerField() # 浏览次数
    ranking = models.IntegerField() # 排名
    created_at = models.DateTimeField() # 创建时间
    update_at = models.DateTimeField() # 更新时间
    def __str__(self):
        return self.title


class Category(models.Model): # 模板
    name = models.CharField(max_length=10,unique=True) # 板块名称,unique是不能重复
    administrator = models.ForeignKey('BBS_user',on_delete=models.CASCADE,) # 版主
    def __str__(self):
        return self.name

class BBS_user(models.Model): # 用户表,继承Django自带的用户认证系统
    user = models.OneToOneField(User,on_delete=models.CASCADE,) # 用户
    signature = models.CharField(max_length=100,default='这家伙没有签名') # 签名
    photo = models.ImageField(upload_to="upload_imgs/", default="upload_imas/user_1.jpg") # 头像默认一个图片,upload_to会自动在根目录创建一个文件夹,支持上传
    def __str__(self):
        return self.user.name