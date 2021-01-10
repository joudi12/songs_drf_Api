from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializer import SongSerializer
from .models import Song

# Create your views here.
class SongsListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailsView(RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


