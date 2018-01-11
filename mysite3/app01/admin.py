from django.contrib import admin

# Register your models here.
from app01 import models


class BBS_admin(admin.ModelAdmin):
    list_display = ('title','summary','author','view_count','ranking','created_at','update_at')
    # 上面一行作用是在admin中显示的字段
    list_filter = ('created_at', ) # 是一个元组, 末尾要加逗号
    search_fields = ('title','summary','author__user__username')
    # 在admin中创建搜索,如果是外键的字段则用'author__user__username'形式,此处要注意

admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
