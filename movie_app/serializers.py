from rest_framework import serializers
from .models import Movie, Review, Director


class ReviewSerializer(serializers.ModelSerializer):
    def validate_stars(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Значение stars должно быть от 1 до 5.")
        return value

    class Meta:
        model = Review
        fields = ['id', 'text', 'stars']


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.IntegerField(source='movies.count',
                                            read_only=True)  # Добавляем поле для подсчета фильмов

    class Meta:
        model = Director
        fields = ['id', 'name', 'movies_count']


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)
    rating = serializers.SerializerMethodField()  # Используем SerializerMethodField для динамического вычисления рейтинга
    director = DirectorSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rating(self, obj):
        # Вычисляем рейтинг на основе отзывов
        reviews = obj.reviews.all()
        if reviews:
            total_stars = sum(review.stars for review in reviews)
            return total_stars / len(reviews)
        return 0  # Если нет отзывов, то возвращаем рейтинг 0
