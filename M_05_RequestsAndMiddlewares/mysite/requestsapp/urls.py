from django.urls import path
from .views import upload_file_view

app_name = "requestsapp"

urlpatterns = [
    path("upload/", upload_file_view, name="upload-file")
]