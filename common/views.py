from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class CommonIndexView(View):
    def get(self, request, *args, **kwargs):
        # Implemente a lógica para a resposta do método GET
        return render(request, 'index.html')