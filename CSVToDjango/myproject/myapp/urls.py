from django.urls import path
from .views import upload_csv
from .views import MyView

urlpatterns = [
    path('upload-csv/', upload_csv, name='upload_csv'),
    path('myview/', MyView.as_view(), name='myview'),
]
