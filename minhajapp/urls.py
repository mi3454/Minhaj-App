from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('profile/', views.profile),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),   # 👈 এই name টা খুব গুরুত্বপূর্ণ
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

]
