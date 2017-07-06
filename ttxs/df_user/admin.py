from django.contrib import admin

# Register your models here.

from models import UserInfo, ReceInfo


# #
# # class AdminShowUser(admin.StackedInline):
# #     model = ReceInfo
#
#
class AdminUserInfo(admin.ModelAdmin):
    list_display = ["id", "uname", "umail"]

    # inlines = [AdminShowUser]
    list_per_page = 10


class AdminRecvInfo(admin.ModelAdmin):

    list_display = ["rshou", "rphone", "raddr", "ruser"]

    list_per_page = 10



admin.site.register(UserInfo, AdminUserInfo)

admin.site.register(ReceInfo, AdminRecvInfo)
# admin.site.register(UserInfo)
# admin.site.register(ReceInfo)