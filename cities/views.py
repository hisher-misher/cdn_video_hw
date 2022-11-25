from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from cities.models import City
from cities.forms import CityForm, PointForm
from cities.utils import get_2_clothest_cities


def city_list(request, template_name='cities/city_list.html'):
    cities = City.objects.all()
    data = {}
    data['object_list'] = cities
    return render(request, template_name, data)

def city_view(request, pk, template_name='cities/city_detail.html'):
    city = get_object_or_404(City, pk=pk)
    return render(request, template_name, {'object':city})

def city_create(request, template_name='cities/city_form.html'):
    form = CityForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('city_list')
    return render(request, template_name, {'form':form})

def city_update(request, pk, template_name='cities/city_form.html'):
    city = get_object_or_404(City, pk=pk)
    form = CityForm(request.POST or None, instance=city)
    if form.is_valid():
        form.save()
        return redirect('city_list')
    return render(request, template_name, {'form':form})

def city_delete(request, pk, template_name='cities/city_confirm_delete.html'):
    city = get_object_or_404(City, pk=pk)
    if request.method == 'POST':
        city.delete()
        return redirect('city_list')
    return render(request, template_name, {'object':city})


def clothest_cities(request, template_name='cities/clothest_city.html'):
    city1 = city2 = None
    if request.method == "POST":
        clothest_form = PointForm(request.POST)
        if clothest_form.is_valid():
            print(f"data: {clothest_form.cleaned_data}")
            cities = City.objects.all()
            print("cities", cities)
            x, y = clothest_form.cleaned_data['x_coord'], clothest_form.cleaned_data['y_coord']
            city1, city2 = get_2_clothest_cities(cities, (x, y))
            print(f"cities: {city1, city2}")
            # print("form: ", clohtest_form)
            # form.save()
    else:
        clothest_form = PointForm()
    return render(request, template_name, {'form': clothest_form, 'city1': city1, 'city2': city2})