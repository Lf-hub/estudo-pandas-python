from django.views import View
from django.shortcuts import render

from common.models import File
from common.forms import ImportFileForm


class CommonIndexView(View):
    def get(self, request, *args, **kwargs):
        # Implemente a lógica para a resposta do método GET
        return render(request, 'index.html')

class ImportFile(View):
    model = File
    
    def post(self, request):
        # form = ImportFileForm
        import pandas as pd
        file = self.request.FILES.get('file')

        # Dentro do process
        dataframe = pd.read_excel(file)
        dt = dataframe

        def contar_pares_impares(numero):
            if numero % 2 == 0:
                return 'Par'
            else:
                return 'Ímpar'



        return render(request, 'index.html')