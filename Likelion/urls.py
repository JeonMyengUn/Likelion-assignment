
from django.contrib import admin
from django.urls import path, include
import article.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article.views.index, name="index"),
    path('about/', article.views.about, name="about"),
    path('result/', article.views.result, name="result"),
]
