from django.urls import path
from .views import index, job_detail

urlpatterns = [
    path("", index, name="index"),
    path('job/<int:pk>/', job_detail, name='job-detail')
]
