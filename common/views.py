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
        def get_pares_impares(row):
            pares = sum(1 for num in row if num % 2 == 0)
            impares = len(row) - pares
            return pares, impares
        
        def get_mestre(row):
            values = []
            for value in row:
                if value in DEFAULT_LIST.get('mestres'):
                    values.append(value)
            data = {
                    'numbers':[values],
                    'total_mestre':sum(values)
                    }
            return data
        
        def get_quadrant(row):
            dict_quadrant = {
                "quadrant1":{"values":[],"total":0},
                "quadrant2":{"values":[],"total":0},
                "quadrant3":{"values":[],"total":0},
                "quadrant4":{"values":[],"total":0},
            }
            for value in row:
                if value in DEFAULT_LIST.get('first_quadrant'):
                    dict_quadrant['quadrant1']['values'].append(value)
                elif value in DEFAULT_LIST.get('second_quadrant'):
                    dict_quadrant['quadrant2']['values'].append(value)
                elif value in DEFAULT_LIST.get('third_quadrant'):
                    dict_quadrant['quadrant3']['values'].append(value)
                elif value in DEFAULT_LIST.get('fourth_quadrant'):
                    dict_quadrant['quadrant4']['values'].append(value)
            
            for key, value in dict_quadrant.items():
                value['total'] = sum(value['values'])
            return dict_quadrant
        
        def get_columns(row):
            dict_columns = {
                "colum1":{"values":[],"total":0},
                "colum2":{"values":[],"total":0},
                "colum3":{"values":[],"total":0},
                "colum4":{"values":[],"total":0},
                "colum5":{"values":[],"total":0},
                "colum6":{"values":[],"total":0},
                "colum7":{"values":[],"total":0},
                "colum8":{"values":[],"total":0},
                "colum9":{"values":[],"total":0},
                "colum10":{"values":[],"total":0},
            }
            for value in row:
                if value in DEFAULT_LIST.get('first_colum'):
                    dict_columns['colum1']['values'].append(value)
                elif value in DEFAULT_LIST.get('second_colum'):
                    dict_columns['colum2']['values'].append(value)
                elif value in DEFAULT_LIST.get('third_colum'):
                    dict_columns['colum3']['values'].append(value)
                elif value in DEFAULT_LIST.get('fourth_colum'):
                    dict_columns['colum4']['values'].append(value)
                elif value in DEFAULT_LIST.get('fifth_colum'):
                    dict_columns['colum5']['values'].append(value)
                elif value in DEFAULT_LIST.get('sixth_colum'):
                    dict_columns['colum6']['values'].append(value)
                elif value in DEFAULT_LIST.get('seventh_colum'):
                    dict_columns['colum7']['values'].append(value)
                elif value in DEFAULT_LIST.get('octave_colum'):
                    dict_columns['colum8']['values'].append(value)
                elif value in DEFAULT_LIST.get('ninth_colum'):
                    dict_columns['colum9']['values'].append(value)
                elif value in DEFAULT_LIST.get('tenth_colum'):
                    dict_columns['colum10']['values'].append(value)
            
            for key, value in dict_columns.items():
                value['total'] = sum(value['values'])
            return dict_columns
        
        def get_lines(row):
            dict_lines = {
                "line1":{"values":[],"total":0},
                "line2":{"values":[],"total":0},
                "line3":{"values":[],"total":0},
                "line4":{"values":[],"total":0},
                "line5":{"values":[],"total":0},
                "line6":{"values":[],"total":0},
                "line7":{"values":[],"total":0},
                "line8":{"values":[],"total":0},
                "line9":{"values":[],"total":0},
                "line10":{"values":[],"total":0},
            }
            for value in row:
                if value in [i for i in range(1, 11)]:
                    dict_lines['line1']['values'].append(value)
                elif value in [i for i in range(11, 21)]:
                    dict_lines['line2']['values'].append(value)
                elif value in [i for i in range(21, 31)]:
                    dict_lines['line3']['values'].append(value)
                elif value in [i for i in range(31, 41)]:
                    dict_lines['line4']['values'].append(value)
                elif value in [i for i in range(41, 51)]:
                    dict_lines['line5']['values'].append(value)
                elif value in [i for i in range(51, 61)]:
                    dict_lines['line6']['values'].append(value)
                elif value in [i for i in range(61, 71)]:
                    dict_lines['line7']['values'].append(value)
                elif value in [i for i in range(71, 81)]:
                    dict_lines['line8']['values'].append(value)
                elif value in [i for i in range(81, 91)]:
                    dict_lines['line9']['values'].append(value)
                elif value in [i for i in range(91, 101)]:
                    dict_lines['line10']['values'].append(value)
            
            for key, value in dict_lines.items():
                value['total'] = sum(value['values'])
            return dict_lines

        file = self.request.FILES.get('file')
        dataframe = pd.read_excel(file)
        dataframe[['pares', 'impares']] = dataframe.apply(get_pares_impares, axis=1, result_type='expand')
        dataframe['mestre'] = dataframe.apply(get_mestre, axis=1)
        dataframe['quadrantes'] = dataframe.apply(get_quadrant, axis=1)
        dataframe['lines'] = dataframe.apply(get_lines, axis=1)
        dataframe['coluns'] = dataframe.apply(get_columns, axis=1)
        return render(request, 'index.html')