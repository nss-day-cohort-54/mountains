from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import serializers
from app_api.models import Movie, Genre
from rest_framework.decorators import action

class MovieView(ViewSet):

    def list(self, request):
        movies = Movie.objects.all()
        genre = request.query_params.get("genre", None)
        if genre is not None:
                movies = movies.filter(genre_id=genre)        
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
        movie = Movie.objects.get(pk=pk)
        serializer = CreateMovieSerializer(movie, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # movies/pk/my_movies detail=TruFalse  # movies/my_movies detail=False
    @action(methods=['get'], detail=False)
    def my_movies(self, request):
        movie=Movie.objects.filter(user=request.auth.user)
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
  
       
    
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
        

