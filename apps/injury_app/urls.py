from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('process/reg', views.process_register),
    path('signin', views.signin),
    path('process/signin', views.process_signin),
    path('dashboard', views.main),
    path('add_athlete', views.add_athlete),
    path('process/athlete', views.process_athlete),
    path('athlete/<int:id>', views.athlete),
    path('athlete/<int:id>/update', views.ath_update),
    path('athlete/<int:id>/update/process', views.process_ath_update),
    path('athlete/<int:id>/cleared', views.cleared),
    path('add_user', views.add_user),
    path('process/user', views.process_user),
    path('user/<int:id>', views.user),
    path('user/<int:id>/update', views.update_user),
    path('user/admin', views.user_admin),
    path('user/<int:id>/admin', views.update_user_admin),
    path('user/<int:id>/update/admin', views.update_user_admin_process),
    path('logout', views.logout),
]