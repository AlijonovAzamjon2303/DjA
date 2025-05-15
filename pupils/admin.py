from django.contrib import admin
from .models import Pupil, Book

# Register your models here.
class PupilAdmin(admin.ModelAdmin):
    search_fields = ['name']

class BookAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pupil']

admin.site.register(Pupil, PupilAdmin)
admin.site.register(Book, BookAdmin)