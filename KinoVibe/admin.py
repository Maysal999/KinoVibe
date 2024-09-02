from django.contrib import admin


from .models import Category, Videofile, Actore, Genre

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('category',)
    list_filter = ('category',)
   
    search_fields = ('category',)
    

@admin.register(Videofile)
class VideofileAdmin(admin.ModelAdmin):
    '''Admin View for Videofile'''

    list_display = ('title','video')
    list_filter = ('title',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''Admin View for Genre'''

    list_display = ('genre',)
    list_filter = ('genre',)
 
@admin.register(Actore)
class ActoreAdmin(admin.ModelAdmin):
    '''Admin View for Actior'''

    list_display = ('fio','bio','date_borth','date_dead')
    list_filter = ('fio',)

