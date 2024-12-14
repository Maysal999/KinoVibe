from django.contrib import admin


from .models import Category, Videofile, Personaj, Genre, Country, Careers, UserAction

# Register your models here.

    

@admin.register(Videofile)
class VideofileAdmin(admin.ModelAdmin):
    '''Admin View for Videofile'''

    list_display = ('title','video')
    list_filter = ('title',)
    prepopulated_fields  = {"slug" : ["title", "country_1"],}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''Admin View for Genre'''

    list_display = ('genre',)
    list_filter = ('genre',)
    prepopulated_fields  = {"slug" : ["genre"],}
    
@admin.register(Personaj)
class ActoreAdmin(admin.ModelAdmin):
    '''Admin View for Actior'''

    list_display = ('fio','bio','date_borth','date_dead')
    list_filter = ('fio',)
    prepopulated_fields  = {"slug" : ["fio"],}

@admin.register(Careers)
class ActoreAdmin(admin.ModelAdmin):
    '''Admin View for Actior'''

    list_display = ('career',)
    list_filter = ('career',)
    prepopulated_fields  = {"slug" : ["career"],}


@admin.register(Country)
class ActoreAdmin(admin.ModelAdmin):
    '''Admin View for Actior'''

    list_display = ('title_country',)
    list_filter = ('title_country',)
    prepopulated_fields  = {"slug" : ["title_country"],}

@admin.register(UserAction)
class ActoreAdmin(admin.ModelAdmin):
    '''Admin View for Actior'''



