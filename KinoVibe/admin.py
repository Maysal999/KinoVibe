from django.contrib import admin


from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('category',)
    list_filter = ('category',)
   
    search_fields = ('category',)
    