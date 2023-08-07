import pandas as pd

from django.views import View
from django.shortcuts import render

from common.models import File
from common.parameters import DEFAULT_LIST



class CommonIndexView(View):
    def get(self, request, *args, **kwargs):
        # Implemente a lógica para a resposta do método GET
        return render(request, 'index.html')

class ImportFile(View):
    model = File
    
    def post(self, request):
        def contar_pares_impares(row):
            pares = sum(1 for num in row if num % 2 == 0)
            impares = len(row) - pares
            return pares, impares
        
        def contem_mestre(row):
            for value in row:
                if value in DEFAULT_LIST.get('mestres'):
                    return 1
            return 0
        
        def contem_mestre(row):
            for value in row:
                if value in DEFAULT_LIST.get('mestres'):
                    return 1
            return 0

        file = self.request.FILES.get('file')
        dataframe = pd.read_excel(file)
        dataframe[['pares', 'impares']] = dataframe.apply(contar_pares_impares, axis=1, result_type='expand')
        dataframe['mestre'] = dataframe.apply(contem_mestre, axis=1)
        return render(request, 'index.html')

    
    


    # def parans(self):
    #     "upper_quadrant":[1 a 50],
    #     "lower_quadrant":[51 a 100],
    
    #     "first_line": [1 a 10],
    #     "second_line": [11 a 20],
    #     "third_line": [21 a 30],
    #     "fourth_line": [31 a 40],
    #     "fifth_line": [41 a 50],
    #     "sixth_line": [51 a 60],
    #     "seventh_line": [61 a 70],
    #     "octave_line": [71 a 80],
    #     "ninth_line": [81 a 90],
    #     "tenth_line": [91 a 100],