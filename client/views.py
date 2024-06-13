from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from converter.converter import get_video_from_text
from client.models import ShortVideo


def index(request):
    text = str(request.GET.get("text", ''))
    video = get_video_from_text(text)
    response_video = ShortVideo(name=video['name'], text=text, content=video['path'])
    response_video.save()
    return render(request, 'client/index.html', context={'object': response_video})



def download_video(request, pk):
    content = ShortVideo.objects.get(pk=pk)
    response = HttpResponse(content.content, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename="{content.content.name}"'
    return response


class VideoView(ListView):
    model = ShortVideo

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        print(queryset)
        return queryset
