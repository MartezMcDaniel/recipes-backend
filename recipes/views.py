from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe
# Create your views here.

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

# def recipe_detail(request, pk):
#     recipe = Recipe.objects.get(id=pk)
#     return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
