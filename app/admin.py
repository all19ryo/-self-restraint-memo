from django.contrib import admin
from .models import Memo
# Register your models here.
class MemoAdmin(admin.ModelAdmin):
    list_display=('id','title','created_datetime','updated_datetime')
    list_desplay_links=('id','title')

admin.site.register(Memo,MemoAdmin)