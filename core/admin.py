from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(userProfiles)
admin.site.register(BlogModel)
admin.site.register(commentsModel)
admin.site.register(likeModel)
