from django.contrib import admin

# 导入ArticlePost
from .models import ArticlePost

# 注册ArticlePost到 admin中
admin.site.register(ArticlePost)

