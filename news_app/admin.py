from django.contrib import admin
from .models import Post, UserProfileInfo, User
from news_app.models import Post, UserProfileInfo, User
from django import forms

#class PostAdminForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        widgets = {
#            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
#        }
#        fields = '__all__'
#
#    class Media:
#        js = ('https://cdn.jsdelivr.net/medium-editor/latest/js/medium-editor.min.js',)
#        css = {
#            'all': ('https://cdn.jsdelivr.net/medium-editor/latest/css/medium-editor.min.css', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css',)
#        }

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'categories')
    ordering = ('-published_date',)
#    form = PostAdminForm

admin.site.register(Post, PostAdmin)
admin.site.register(UserProfileInfo)
