from django.urls import path

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('admin-portal/login/', admin_login_view, name='admin_login'),
    path('packages/', packages, name='packages'),
    path('packages/<int:package_id>/book/', book_package, name='book_package'),
    path('admin-portal/packages/', manage_packages, name='manage_packages'),
    path('admin-portal/packages/edit/<int:package_id>/', edit_package, name='edit_package'),
    path('admin-portal/packages/delete/<int:package_id>/', delete_package, name='delete_package'),
    path('packages/manage/', manage_packages, name='manage_packages_legacy'),
    path('packages/manage/edit/<int:package_id>/', edit_package, name='edit_package_legacy'),
    path('packages/manage/delete/<int:package_id>/', delete_package, name='delete_package_legacy'),
    path('logout/', logout_view, name='logout'),
]
