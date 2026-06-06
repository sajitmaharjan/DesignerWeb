from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Logo)

class ProjectImagesAdmin(admin.TabularInline):
    model=ProjectImages
    extra=1
    
@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectImagesAdmin]
    
class UiImageAdmin(admin.TabularInline):
    model=UiImages
    extra=1
    
@admin.register(UiDesign)
class UiDesign(admin.ModelAdmin):
    inlines = [UiImageAdmin]