from django.urls import path
from throttleguideapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('create_cars', views.create_cars),
    path('read_cars', views.read_cars),
    path('read_detail_cars/<rid>', views.read_detail_cars),
    path('update_cars/<rid>', views.update_cars),
    path('delete_cars/<rid>', views.delete_cars),
    path('register', views.user_register),
    path('login', views.user_login),
    path('logout', views.user_logout),
    path('create_profile', views.create_profile),
    path('read_profile', views.read_profile),
    path('show_users', views.show_users),
    path('show_detail_users/<rid>', views.show_detail_users),
    path('likes_count/<post_id>', views.likes_count),
    path('follow_user/<rid>', views.follow_user),
    path('forgot_password', views.forgot_password),
    path('otp_verification', views.otp_verification),
    path('new_password', views.new_password)
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)