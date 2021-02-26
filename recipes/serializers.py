from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):

    recipe_url = serializers.ModelSerializer.serializer_url_field(
    view_name='recipe_detail'
    )

    class Meta:
        model = Recipe
        fields = ('id', 'recipe_url', 'name', 'description', 'cuisine', 'ingredients', 'directions', 'image',)
