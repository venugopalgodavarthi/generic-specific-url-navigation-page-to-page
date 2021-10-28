from django.urls import path
from calls import views
urlpatterns=[
    path('sample1/',views.sample1,name="sample1"),
    path('sample2/',views.sample2,name="sample2"),
]