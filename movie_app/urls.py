from django.urls import path
from movie_app.views import (
    DirectorListCreateView, DirectorDetailView,
    MovieListCreateView, MovieDetailView,
    ReviewListCreateView, ReviewDetailView,
    MoviesWithReviewsView
)

urlpatterns = [
    path('movies/reviews/', MoviesWithReviewsView.as_view(), name='movies-reviews'),
    path('movies/', MovieListCreateView.as_view(), name='movies-list'),
    path('movies/<int:id>/', MovieDetailView.as_view(), name='movie-detail'),

    path('directors/', DirectorListCreateView.as_view(), name='directors-list'),
    path('directors/<int:id>/', DirectorDetailView.as_view(), name='director-detail'),

    path('reviews/', ReviewListCreateView.as_view(), name='reviews-list'),
    path('reviews/<int:id>/', ReviewDetailView.as_view(), name='review-detail'),
]
