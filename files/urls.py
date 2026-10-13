from .views import FileUploadView
from django.urls import path

urlpatterns=[
    path("upload/", FileUploadView.as_view(), name="File_upload"),
]


