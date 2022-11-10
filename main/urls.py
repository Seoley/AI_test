from django.urls import path, include
from .views import CA_model, index, CA_result, HF_model, HF_result, file_download

app_name = 'main'

urlpatterns = [
    path("", index.as_view()),
    path("CAtest/", CA_model.as_view()),
    path("CAresult/", CA_result.as_view()),
    path("HFtest/", HF_model.as_view()),
    path("HFresult/", HF_result.as_view()),
    path("download/", file_download, name='file_download'),
]