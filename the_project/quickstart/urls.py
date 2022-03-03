from django.urls import path, include

from the_project.quickstart import views

urlpatterns = [
    path('some_endpoint_name/', views.example_view),
]
