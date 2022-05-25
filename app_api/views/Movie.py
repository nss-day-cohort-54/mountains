from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from app_api.models import Movie, Genre


class MovieView(ViewSet):

    def list(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def create(self, request):
        # genre = Genre.objects.get(pk=request.data['genre']
        # movie = Movie.objects.create(
        #     title=request.data['title'],
        #     genre=genre,
        #     ...
        # )
        user = request.auth.user
        serializer = CreateMovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
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

class CreateMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'run_time',
                   'date_released', 'genre')
        

