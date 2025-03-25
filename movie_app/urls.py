from django.urls import path
from movie_app import views

urlpatterns = [
    path('movies/reviews/', views.movies_reviews_view),
    path('movies/', views.movies_api_view),
    path('movies/<int:id>/', views.movie_detail),

    path('directors/', views.directors_api_view),
    path('directors/<int:id>/', views.director_detail),

    path('reviews/', views.reviews_api_view),
    path('reviews/<int:id>/', views.review_detail),
]
