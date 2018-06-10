from django.contrib import admin
from .models import Banner, BlogCategory, Tags, FriendlyLink, Comment, Post

# Register your models here.


admin.site.register(Banner)
admin.site.register(Post)
admin.site.register(BlogCategory)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(FriendlyLink)
