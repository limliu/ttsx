from django.contrib import admin

# Register your models here.

from models import UserInfo, ReceInfo


class AdminShowRecv(admin.TabularInline):
    model = ReceInfo


class AdminUserInfo(admin.ModelAdmin):
    list_display = ["id", "uname", "umail"]

    inlines = [AdminShowRecv, ]
    list_per_page = 10


admin.site.register(UserInfo, AdminUserInfo)

