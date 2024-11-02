from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from blog.models import Post, Category, Comments, Contact, Profile, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','display_title', 'author', 'category', 'isPublished', 'createdAt', 'updatedAt', 'display_tags_count', 'display_action')
    list_filter = ('isPublished', 'category', 'tags')
    list_editable = ('isPublished',)
    list_per_page = 10
    list_max_show_all = 100
    search_fields= ('title', 'content')
    def display_title(self, post):
        no_icon = '<img src="/public/admin/img/icon-no.svg" alt="False">'
        yes_icon = '<img src="/public/admin/img/icon-yes.svg" alt="True">'
       
        if post.isPublished:
            title = '<span style="color:green;">'+post.title+'</span>'
            return format_html(title+yes_icon)
        else:
           title = '<span style="color:red;">'+post.title+'</span>'
           return format_html(title+no_icon) 
    
    def display_tags_count(self, post):
        return post.tags.count()
    
   
    
    def display_action(self, post):
        return format_html(
            '<a class ="addLink" href="{}" >View</a> &nbsp; '
            '<a class ="addLink" href="{}">Edit</a> &nbsp; '
            '<a class ="addLink" href="{}">Delete</a> &nbsp; ',
            reverse('admin:blog_post_change', args = [post.id]),
            reverse('admin:blog_post_change', args = [post.id]),
            reverse('admin:blog_post_delete', args = [post.id])
            )
    
    display_tags_count.short_description = 'tags_count'
    display_action.short_description = 'action'
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description',  'createdAt', 'updatedAt')
    list_filter = ('createdAt', 'updatedAt')
    list_per_page = 10
    list_max_show_all = 100
    search_fields= ('name', 'description')
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',  'createdAt', 'updatedAt')
    list_filter = ('createdAt', 'updatedAt')
    list_per_page = 10
    list_max_show_all = 100
    search_fields= ('name', 'description')
class ContactAdmin(admin.ModelAdmin):
    list_display = ('civility','name', 'email',  'subject', 'file','message', 'createdAt')
    list_filter = ('civility', 'name', 'email')
    list_per_page = 10
    list_max_show_all = 100
    search_fields= ('name', 'civility', 'email', 'subject')
# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comments)
admin.site.register(Profile)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Post, PostAdmin)