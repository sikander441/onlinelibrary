from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Books_technical)
admin.site.register(Books_non_technical)
admin.site.register(Book_record)
admin.site.register(Curr_user)
admin.site.register(Search)
