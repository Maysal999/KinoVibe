from django.urls import path

from users import views as v

urlpatterns = [
    path('login/',v.UserLoginView.as_view(),name='login'),
    path('register/',v.RegisterView.as_view(),name='register'),
    path('logout/',v.logout_user,name='logout'),
    # path('profile/<int:pk>',  (v.Profile.as_view()), name='profile'),
]