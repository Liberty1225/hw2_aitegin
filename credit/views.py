from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from .models import Client, Account, Credit


def hello(request):
    return HttpResponse("Добро пожаловать!")


class ClientView(generic.ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'client_list'


class ClientDetailView(generic.DetailView):
    model = Client
    context_object_name = 'detail'
    template_name = 'detail.html'
    pk_url_kwarg = 'id'


