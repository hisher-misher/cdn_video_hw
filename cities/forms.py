from django.forms import ModelForm
from cities.models import City, Point

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name', ]

class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = ["x_coord", "y_coord"]