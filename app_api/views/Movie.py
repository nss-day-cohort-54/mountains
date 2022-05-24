from django.http import HttpResponseServerError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from app_api.models import Movie


class MovieView(ViewSet):

    def list(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk):
        pass

    def destroy(self, request, pk):
        pass


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'run_time',
                  'user', 'date_released', 'genre')
        depth = 1
