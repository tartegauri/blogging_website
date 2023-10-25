from django.urls import path
from . import views

urlpatterns = [
    path("",views.all_blogs,name="all_blogs"),
    path('login/', views.login , name ="login"),
    path("checkuser",views.checkuser, name="profile"),
    path('register/',views.register , name="register"),
    path("registeruser",views.registeruser, name="profile"),
    path("profile/<int:id>",views.profile,name="profile_details"),
    path("create_blog/<str:name>/<int:id>",views.create_blog,name="create_blog"),
    path("insert_blog/<str:name>/<int:id>",views.insert_blog,name="insert_blog"),
]