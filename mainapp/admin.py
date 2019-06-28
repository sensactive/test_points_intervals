from django.contrib import admin

# Register your models here.
from mainapp.models import Comment, Point, Interval

admin.site.register(Comment)
admin.site.register(Point)
admin.site.register(Interval)
