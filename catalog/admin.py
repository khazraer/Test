from django.contrib import admin
from catalog.models import  Book,BookInstance,Genre,Author
# Register your models here.
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
# admin.site.register(Author)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name' , 'first_name' , 'date_of_birth' , 'date_of_death')
    fields      = ['first_name','last_name',('date_of_birth','date_of_death')]
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title' , 'author' , 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status' , 'due_back')
