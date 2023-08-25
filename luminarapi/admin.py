from django.contrib import admin
# from django.contrib.auth.models import User
from .models import DemoClass,Course,VideoScreenClass,Logo,LiveClass,Module,Batch,VideoScreen

admin.site.register(VideoScreen)

admin.site.register(DemoClass)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Batch)
admin.site.register(VideoScreenClass)
admin.site.register(Logo)
admin.site.register(LiveClass)



# Register your models here.
