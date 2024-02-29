from django.contrib import admin
from django.urls import path

from .views import *


urlpatterns = [
    path('',home,name="home"),
    path('search',search,name="search"),
    path("update/<int:id>",update,name="update_item"),
    path("delete/<int:id>",delete_item,name="delete_item"),
    path("create/",create,name="create")
]
