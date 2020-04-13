from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from rooms.models import Room


class RoomView(ListView):
    model = Room  # Модель
    paginate_orphans = 2  # Если останется N элементов, то присоединять их к концу последней странице
    paginate_by = 5  # Элементов на странице
    context_object_name = 'rooms'  # как в теплейте будет отображать имя object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RoomDetail(DetailView):
    model = Room


def room_search(request):
    return render(request, 'rooms/search.html')
