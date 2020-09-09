from django.contrib import admin
from .models import User,Articles,Bid,comments,WatchList,Won
# Register your models here.
admin.site.register(User)
admin.site.register(Articles)
admin.site.register(Bid)
admin.site.register(comments)
admin.site.register(WatchList)
admin.site.register(Won)
