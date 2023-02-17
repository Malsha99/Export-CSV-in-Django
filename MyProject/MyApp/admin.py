
from django.contrib import admin
from .models import Post
from import_export import resources


# Create the resource class
class PostResource(resources.ModelResource):
    class Meta:
        model = Post
        fields = ('FirstName','LastName','City')
        export_order = ('FirstName','LastName','City')


# Register your models here.
admin.site.register(Post)



