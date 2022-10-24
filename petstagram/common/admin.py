from django.contrib import admin

# Register your models here.
from petstagram.common.models import Comment


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    pass