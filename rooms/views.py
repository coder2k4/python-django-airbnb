from pprint import pprint

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from rooms.forms import SearchForm
from rooms.models import Room


class RoomView(ListView):
    model = Room  # Модель
    paginate_orphans = 2  # Если останется N элементов, то присоединять их к концу последней странице
    paginate_by = 12  # Элементов на странице
    context_object_name = 'rooms'  # как в теплейте будет отображать имя object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hello'] = 'Hello new query!'
        return context


class RoomDetail(DetailView):
    model = Room


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):
        rooms = []
        country = request.GET.get('country')
        if country:
            form = SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data.get('city')
                country = form.cleaned_data.get('country')
                price = form.cleaned_data.get('price')
                room_type = form.cleaned_data.get('room_type')
                guests = form.cleaned_data.get('guests')
                beds = form.cleaned_data.get('beds')
                bedrooms = form.cleaned_data.get('bedrooms')
                baths = form.cleaned_data.get('baths')
                instant_book = form.cleaned_data.get('instant_book')
                superhost = form.cleaned_data.get('superhost')
                amenities = form.cleaned_data.get('amenities')
                facilities = form.cleaned_data.get('facilities')

                filter_args = {}

                if city != 'Anywhere':
                    filter_args['city_startswith'] = city

                filter_args['country'] = country

                if room_type is not None:
                    filter_args['room_type'] = room_type

                if price is not None:
                    filter_args['price__lte'] = price

                if guests is not None:
                    filter_args['guests__gte'] = guests

                if beds is not None:
                    filter_args['beds__gte'] = beds

                if bedrooms is not None:
                    filter_args['bedrooms__gte'] = bedrooms

                if baths is not None:
                    filter_args['baths__gte'] = baths

                if instant_book is True:
                    filter_args['instant_book'] = True

                if superhost is True:
                    filter_args['host__superhost'] = True

                for amenity in amenities:
                    filter_args["amenity"] = amenity

                for facility in facilities:
                    filter_args["facility"] = facility

                qs = Room.objects.filter(**filter_args)

                paginator = Paginator(qs, 10, orphans=5)
                page = request.GET.get("page", 1)
                rooms = paginator.get_page(page)

        else:
            form = SearchForm()
        return render(request, 'rooms/search.html',
                      {
                          'form': form,
                          'rooms': rooms
                      })
