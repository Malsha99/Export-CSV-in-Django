from django.urls import path
from .views import PostsListView

app_name = "MyApp"

urlpatterns =[
    path("",PostsListView.as_view(), name="main"),

]


