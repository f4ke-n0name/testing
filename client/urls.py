from django.urls import path
from client.apps import ClientConfig

from client.views import index, VideoView, download_video

app_name = ClientConfig.name


urlpatterns = [
    path('', index, name="index"),
    path('download/<int:pk>/', download_video, name='download_file'),
    path('videos/', VideoView.as_view(), name="videos"),
]