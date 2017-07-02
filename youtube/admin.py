from django.contrib import admin
from .models import Comment

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["video", "timestamp"]
    class Meta:
        model = Comment

admin.site.register(Comment, CommentModelAdmin)