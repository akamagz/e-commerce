from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as authentication_views
from users import views as user_views
from shop import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    path("<int:id>/", views.detail, name='detail'),
    path("checkout/", views.checkout, name='checkout'),
    path("register/", user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
