from django.shortcuts import render, redirect
from .forms import NewPlaceForm
from .models import Place
# Create your views here.

def place_list(request):
    if request.method == 'POST':
        form = NewPlaceForm(request.POST)
        place = form.save()
        if form.is_valid():
            place.save()
            return redirect('place_list')

    places = Place.objects.filter(visited=False)
    new_place_form = NewPlaceForm()
    return render(request, 'travel_wishlist/wishlist.html', {'places':places, 'new_place_form':new_place_form})

def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html',{'visited':visited})

def place_was_visited(request):
    if request.method == 'POST':
        pk = request.POST.get('pk')
        place = Place.objects.get(pk=pk)
        place.visited = True
        place.save()
    return redirect('place_list')