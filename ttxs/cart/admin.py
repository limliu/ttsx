from django.contrib import admin

# Register your models here.

from models import CartInfo


class AdminCartInfo(admin.ModelAdmin):
    list_display = ["show_title", "id", "cart_num"]


admin.site.register(CartInfo, AdminCartInfo)