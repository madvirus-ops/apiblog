from django.contrib import admin
from .models import Post,Product,sendMaill,Comment,Profile

# Register your models here.
#admin.site.register(Post)
admin.site.register(Product)
admin.site.register(sendMaill)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','title','description','owner','publish')
    search_fields= ('title','content')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields= ('owner',)
    date_hierarchy= 'publish'
    ordering=('publish',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
 list_display = ('name', 'email', 'post', 'created', 'active')
 list_filter = ('active', 'created', 'updated')
 search_fields = ('name', 'email', 'body')

@admin.register(Profile)
class ProlieAdmin(admin.ModelAdmin):
    list_display= ('user','bio')
    


