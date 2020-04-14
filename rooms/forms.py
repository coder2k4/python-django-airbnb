from django import forms
from django_countries.fields import CountryField

from rooms.models import RoomType, Amenity, Facility


class SearchForm(forms.Form):
    city = forms.CharField(initial='Anywhere')
    country = CountryField(default='KR').formfield()
    price = forms.IntegerField(required=False, min_value=0, max_value=10)
    room_type = forms.ModelChoiceField(required=False, empty_label="Any kind",
                                       queryset=RoomType.objects.all())
    guests = forms.IntegerField(required=False, min_value=0, max_value=10)
    beds = forms.IntegerField(required=False, min_value=0, max_value=10)
    bedrooms = forms.IntegerField(required=False, min_value=0, max_value=10)
    baths = forms.IntegerField(required=False, min_value=0, max_value=10)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(required=False,
                                               queryset=Amenity.objects.all(),
                                               widget=forms.CheckboxSelectMultiple)
    facilities = forms.ModelMultipleChoiceField(required=False,
                                                queryset=Facility.objects.all(),
                                                widget=forms.CheckboxSelectMultiple)
