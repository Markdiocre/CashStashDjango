from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Ipon, Money

# Register your models here.

class IponAdmin(admin.ModelAdmin):
    list_display = ['fld_ipon_id','fld_user_id','fld_title','fld_ipon','fld_ipon_desc']

class MoneyAdmin(admin.ModelAdmin):
    list_display = ['fld_money_id','fld_user_id','fld_title','fld_value','fld_type','fld_date_added']

# class UserAdmin(BaseUserAdmin):

#     ordering = ['-username']
#     list_display=[
#         'fld_user_id','username','fld_fname','fld_lname','fld_email','is_active','is_staff','last_login'
#     ]
#     list_filter = ['is_staff','is_active']
#     search_fields=[
#         'username','fld_fname','fld_lname','fld_email'
#     ]
#     fieldsets=[
#         [None,{'fields':['username','fld_fname','fld_lname','fld_email','password','last_login']}],
#         ['Permissions', {'fields':['is_active','is_staff']}],
#     ]
#     add_fieldsets = [
#         [None,{
#             'classes':['wide',],
#             'fields':['username','fld_fname','fld_lname','fld_email','last_login','password1','password2','is_staff','is_active']
#         }]
#     ] 

# admin.site.register(User,UserAdmin)
admin.site.register(Ipon,IponAdmin)
admin.site.register(Money,MoneyAdmin)