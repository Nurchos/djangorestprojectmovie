from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer


# Directors
class DirectorListCreateView(APIView):
    def get(self, request):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DirectorDetailView(APIView):
    def get(self, request, id):
        director = get_object_or_404(Director, id=id)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    def put(self, request, id):
        director = get_object_or_404(Director, id=id)
        serializer = DirectorSerializer(director, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        director = get_object_or_404(Director, id=id)
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Movies
class MovieListCreateView(APIView):
    def get(self, request):
        movies = Movie.objects.prefetch_related('reviews').all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    def get(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Reviews
class ReviewListCreateView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    def get(self, request, id):
        review = get_object_or_404(Review, id=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, id):
        review = get_object_or_404(Review, id=id)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        review = get_object_or_404(Review, id=id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Movies with Reviews
class MoviesWithReviewsView(APIView):
    def get(self, request):
        movies = Movie.objects.prefetch_related('reviews').all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
