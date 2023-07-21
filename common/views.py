from django.views import View
from django.shortcuts import render

from common.forms import ImportFileForm


class CommonIndexView(View):
    def get(self, request, *args, **kwargs):
        # Implemente a lógica para a resposta do método GET
        return render(request, 'index.html')

class ImportFile(View):

    def get(self, request):
        form = ImportFileForm
        return render(request, 'index.html')