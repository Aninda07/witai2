from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .import views

urlpatterns = [
    path('chat/', views.ContactList.as_view()),
    path('myapi/', views.ContactDetail.as_view()),
    path('mon/', views.MontactList.as_view()),
    path('fb/', views.MontactDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

