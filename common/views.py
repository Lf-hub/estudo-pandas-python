from django.shortcuts import render
from django.views.generic import View, ListView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
import pandas as pd
from common.models import File, Lines, Summary
from common.process import ProcessLine
from common.parameters import DEFAULT_LIST
import itertools
import random

class CommonIndexView(ListView):
    model = Lines
    template_name = "index.html"


class ImportFile(View):
    model = File
    
    def post(self, request):
        # Pega arquivo
        file = self.request.FILES.get("file")
        process = ProcessLine
        process.execute(file)
        return render(request, "index.html")


class SummaryDetail(ListView):
    model = Summary
    template_name = "summary_index.html"


class PlaygameView(View):
    model = Summary

    def get(self,request):
        # Busca JSON da sumarizacao
        data = self.model.objects.all().last().content_json
        # Ajusta JSON para criar o DF
        df_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    col_name = f"{key}_{sub_key}"
                    df_data[col_name] = sub_value
            else:
                df_data[key] = value
        
        # Criar o DataFrame
        df = pd.DataFrame([df_data])
        # Busca numeros do ultimo jogo
        last_game = Lines.objects.all().last().content_json.get('numeros')
        # Busca lista de numeros mestre
        mestre = DEFAULT_LIST.get('mestres')
        # Junta as listas
        remove_list = [last_game, mestre]
        # Cria lista com numeros de 1 a 100
        numeros = list(range(1, 101))
        
        for lista in remove_list:
            #Cria lista de numeros removendo do ultimo jogo e mestre
            numeros = [numero for numero in numeros if numero not in lista]
        
        sorteados = []
        par = 10
        impar = 10
        total_numeros = 20

        quad1_len = df.at[0,'quadrante_quad1']['media_quad1']
        quad2_len = df.at[0,'quadrante_quad2']['media_quad2']
        quad3_len = df.at[0,'quadrante_quad3']['media_quad3']
        quad4_len = df.at[0,'quadrante_quad4']['media_quad4']
        
        col1_len = df.at[0,'c1_media_coluna1']
        col2_len = df.at[0,'c2_media_coluna2']
        col3_len = df.at[0,'c3_media_coluna3']
        col4_len = df.at[0,'c4_media_coluna4']
        col5_len = df.at[0,'c5_media_coluna5']
        col6_len = df.at[0,'c6_media_coluna6']
        col7_len = df.at[0,'c7_media_coluna7']
        col8_len = df.at[0,'c8_media_coluna8']
        col9_len = df.at[0,'c9_media_coluna9']
        col10_len = df.at[0,'c10_media_coluna10']

        while total_numeros > 0:
            numero = random.choice(numeros)
            steps = 0
            nex_step = False
            # step1
            if par > 0 and numero % 2 == 0:
                nex_step = True
                numeros.remove(numero)
                total_numeros -= 1
                par -= 1
                steps +=1

            elif impar > 0 and numero % 2 != 0:
                nex_step = True
                numeros.remove(numero)
                total_numeros -= 1
                impar -= 1
                steps +=1
            
            if nex_step:
                # step2
                quad1 = [num for num in sorteados if num in DEFAULT_LIST.get('first_quadrant')]
                if quad1_len != 0:
                    for n in quad1:
                        if n in sorteados:
                            total_numeros += 1
                    if len(quad1) > quad1_len:
                        t = random.sample(quad1, quad1_len)
                        sorteados += list(t)
                        quad1_len = 0
                        total_numeros -= len(t)
                        quad1_len -= len(t)
                        steps +=1
                    
                    elif len(quad1):
                        steps +=1
                        sorteados += list(quad1)
                        quad1_len -= len(quad1)
                        total_numeros -= len(quad1)
                
                quad2 = [num for num in sorteados if num in DEFAULT_LIST.get('second_quadrant')]
                if quad2_len != 0:
                    for n in quad2:
                        if n in sorteados:
                            total_numeros += 1
                    if len(quad2) > quad2_len:
                        steps +=1
                        t = random.sample(quad2, quad2_len)
                        sorteados += list(t)
                        total_numeros -= len(t)
                        quad2_len -= len(t)
                    elif len(quad2):
                        steps +=1
                        sorteados += list(quad2)
                        total_numeros -= len(quad2)
                        quad2_len -= len(quad2)
            
                quad3 = [num for num in sorteados if num in DEFAULT_LIST.get('third_quadrant')]
                if quad3_len != 0:
                    for n in quad3:
                        if n in sorteados:
                            total_numeros += 1
                    if len(quad3) > quad3_len:
                        steps +=1
                        t = random.sample(quad3, quad3_len)
                        sorteados += list(t)
                        quad3_len = 0
                        total_numeros -= len(t)
                    elif len(quad3):
                        steps +=1
                        sorteados += list(quad3)
                        total_numeros -= len(quad3)
                        quad3_len -= len(quad3)
                        
                quad4 = [num for num in sorteados if num in DEFAULT_LIST.get('fourth_quadrant')]
                if quad4_len != 0:
                    for n in quad4:
                        if n in sorteados:
                            total_numeros += 1
                    if len(quad4) > quad4_len:
                        steps +=1
                        t = random.sample(quad4, quad4_len)
                        sorteados += list(t)
                        quad4_len = 0
                        total_numeros -= len(t)
                    else:
                        steps +=1
                        sorteados += list(quad4)
                        quad4_len -= len(quad4)
                        total_numeros -= len(quad4)
                # step 3
                col1 = [num for num in sorteados if num in DEFAULT_LIST.get('first_colum')]
                if col1_len != 0:
                    for n in col1:
                        if not n in sorteados:
                            steps +=1
                col2 = [num for num in sorteados if num in DEFAULT_LIST.get('second_colum')]
                if col2_len != 0:
                    for n in col2:
                        if not n in sorteados:
                            steps +=1
                col3 = [num for num in sorteados if num in DEFAULT_LIST.get('third_colum')]
                if col3_len != 0:
                    for n in col3:
                        if not n in sorteados:
                            steps +=1
                col4 = [num for num in sorteados if num in DEFAULT_LIST.get('fourth_colum')]
                if col4_len != 0:
                    for n in col4:
                        if not n in sorteados:
                            steps +=1
                col5 = [num for num in sorteados if num in DEFAULT_LIST.get('fifth_colum')]
                if col5_len != 0:
                    for n in col5:
                        if not n in sorteados:
                            steps +=1
                col6 = [num for num in sorteados if num in DEFAULT_LIST.get('sixth_colum')]
                if col6_len != 0:
                    for n in col6:
                        if not n in sorteados:
                            steps +=1
                col7 = [num for num in sorteados if num in DEFAULT_LIST.get('seventh_colum')]
                if col7_len != 0:
                    for n in col7:
                        if not n in sorteados:
                            steps +=1
                col8 = [num for num in sorteados if num in DEFAULT_LIST.get('octave_colum')]
                if col8_len != 0:
                    for n in col8:
                        if not n in sorteados:
                            steps +=1
                col9 = [num for num in sorteados if num in DEFAULT_LIST.get('ninth_colum')]
                if col9_len != 0:
                    for n in col9:
                        if not n in sorteados:
                            steps +=1
                col10 = [num for num in sorteados if num in DEFAULT_LIST.get('tenth_colum')]
                if col10_len != 0:
                    for n in col10:
                        if not n in sorteados:
                            steps +=1                            
                
            
            if steps == 3:
                sorteados.append(numero)
            
            if impar == 0 and\
                quad1_len == 0 and\
                quad2_len == 0 and\
                quad3_len == 0 and\
                quad4_len == 0:
                var = True
                break
        var = True
        # combined_results_quad_sup = []
        # for tuple1, tuple2 in zip(sorteado_first_quad, sorteado_second_quad):
        #     list_c = list(tuple1) + list(tuple2)
        #     if sum(list_c)< df.at[0, 'quad_sup_total_quadra_sup']:
        #         combined_results_quad_sup.append(list_c)
        
        # combined_results_quad_inf = []
        # for tuple3, tuple4 in zip(sorteado_third_quad, sorteado_fourth_quad):
        #     list_d = list(tuple3) + list(tuple4)
        #     if sum(list_d)< df.at[0, 'quad_inf_total_quadra_inf']:
        #         combined_results_quad_inf.append(list_d)
        
        # combineds = []
        # for t5, t6 in zip(combined_results_quad_sup, combined_results_quad_inf):
        #     list_cc = list(t5) + list(t6)
        #     if sum(list_cc)< df.at[0, 'media_total_por_jogo']:
        #         combineds.append(list_cc)



        # second_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('second_colum')]
        # comb2 = itertools.combinations(second_colum_common, df.at[0,'c2_media_coluna2'])
        # sorteado_second_colum = [c for c in comb2 if sum(c) <= df.at[0,'c2_total_c2']]

        # third_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('third_colum')]
        # comb3 = itertools.combinations(third_colum_common, df.at[0,'c3_media_coluna3'])
        # sorteado_third_colum = [c for c in comb3 if sum(c) <= df.at[0,'c3_media_c3']]

        # fourth_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('fourth_colum')]
        # comb4= itertools.combinations(fourth_colum_common, df.at[0,'c4_media_coluna4'])
        # sorteado_fourth_colum = [c for c in comb4 if sum(c) <= df.at[0,'c4_media_c4']]
        
        # fifth_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('fifth_colum')]
        # comb5 = itertools.combinations(fifth_colum_common, df.at[0,'c5_media_coluna5'])
        # sorteado_fifth_colum = [c for c in comb5 if sum(c) <= df.at[0,'c5_media_c5']]

        # sixth_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('sixth_colum')]
        # comb6 = itertools.combinations(sixth_colum_common, df.at[0,'c6_media_coluna6'])
        # sorteado_sixth_colum = [c for c in comb6 if sum(c) <= df.at[0,'c6_media_c6']]

        # seventh_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('seventh_colum')]
        # comb7 = itertools.combinations(seventh_colum_common, df.at[0,'c7_media_coluna7'])
        # sorteado_seventh_colum = [c for c in comb7 if sum(c) <= df.at[0,'c7_media_c7']]

        # octave_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('octave_colum')]
        # comb8 = itertools.combinations(octave_colum_common, df.at[0,'c8_media_coluna8'])
        # sorteado_octave_colum = [c for c in comb8 if sum(c) <= df.at[0,'c8_media_c8']]

        # ninth_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('ninth_colum')]
        # comb9 = itertools.combinations(ninth_colum_common, df.at[0,'c9_media_coluna9'])
        # sorteado_ninth_colum = [c for c in comb9 if sum(c) <= df.at[0,'c9_media_c9']]

        # tenth_colum_common = [num for num in numeros if num in DEFAULT_LIST.get('tenth_colum')]
        # comb10 = itertools.combinations(tenth_colum_common, df.at[0,'c10_media_coluna10'])
        # sorteado_tenth_colum = [c for c in comb10 if sum(c) <= df.at[0,'c10_media_c10']]


class SummaryView(View):
    model = Lines
    
    def get(self,request):
        lines = self.model.objects.all()
        total_lines = len(lines)
        total_par = 0
        total_impar = 0
        total_mestre = 0
        total_quadrante1 = 0
        total_quad1 = 0
        total_quadrante2 = 0
        total_quad2 = 0
        total_quadrante3 = 0
        total_quad3 = 0
        total_quadrante4 = 0
        total_quad4 = 0
        total_line1 = 0
        total_l1 = 0 
        total_line2 = 0
        total_l2 = 0 
        total_line3 = 0
        total_l3 = 0 
        total_line4 = 0
        total_l4 = 0 
        total_line5 = 0
        total_l5 = 0 
        total_line6 = 0
        total_l6 = 0 
        total_line7 = 0
        total_l7 = 0 
        total_line8 = 0
        total_l8 = 0 
        total_line9 = 0
        total_l9 = 0 
        total_line10 = 0
        total_l10 = 0
        total_colum1 = 0
        total_c1 = 0 
        total_colum2 = 0
        total_c2 = 0 
        total_colum3 = 0
        total_c3 = 0 
        total_colum4 = 0
        total_c4 = 0 
        total_colum5 = 0
        total_c5 = 0 
        total_colum6 = 0
        total_c6 = 0 
        total_colum7 = 0
        total_c7 = 0 
        total_colum8 = 0
        total_c8 = 0 
        total_colum9 = 0
        total_c9 = 0 
        total_colum10 = 0
        total_c10 = 0
        quadra_sup = 0
        quadra_inf = 0
        total_quadra_sup = 0
        total_quadra_inf = 0
        total_idem = 0
        
        for line in lines:
            linha = line.content_json["linhas"]
            coluna = line.content_json["colunas"]
            quadrante = line.content_json["quadrantes"]

            total_par += line.content_json["pares"]
            total_impar += line.content_json["impares"]
            total_mestre += len(line.content_json["mestre"]["numbers"])
            
            total_quadrante1 += len(quadrante["quadrant1"]["values"])
            total_quad1 += quadrante["quadrant1"]["total"]
            total_quadrante2 += len(quadrante["quadrant2"]["values"])
            total_quad2 += quadrante["quadrant2"]["total"]
            total_quadrante3 += len(quadrante["quadrant3"]["values"])
            total_quad3 += quadrante["quadrant3"]["total"]
            total_quadrante4 += len(quadrante["quadrant4"]["values"])
            total_quad4 += quadrante["quadrant4"]["total"]
            
            total_line1 += len(linha["line1"]["values"])
            total_l1 += linha["line1"]["total"]
            total_line2 += len(linha["line2"]["values"])
            total_l2 += linha["line2"]["total"]
            total_line3 += len(linha["line3"]["values"])
            total_l3 += linha["line3"]["total"]
            total_line4 += len(linha["line4"]["values"])
            total_l4 += linha["line4"]["total"]
            total_line5 += len(linha["line5"]["values"])
            total_l5 += linha["line5"]["total"]
            total_line6 += len(linha["line6"]["values"])
            total_l6 += linha["line6"]["total"]
            total_line7 += len(linha["line7"]["values"])
            total_l7 += linha["line7"]["total"]
            total_line8 += len(linha["line8"]["values"])
            total_l8 += linha["line8"]["total"]
            total_line9 += len(linha["line9"]["values"])
            total_l9 += linha["line9"]["total"]
            total_line10 += len(linha["line10"]["values"])
            total_l10 += linha["line10"]["total"]

            total_colum1 += len(coluna["colum1"]["values"])
            total_c1 += coluna["colum1"]["total"]
            total_colum2 += len(coluna["colum2"]["values"])
            total_c2 += coluna["colum2"]["total"]
            total_colum3 += len(coluna["colum3"]["values"])
            total_c3 += coluna["colum3"]["total"]
            total_colum4 += len(coluna["colum4"]["values"])
            total_c4 += coluna["colum4"]["total"]
            total_colum5 += len(coluna["colum5"]["values"])
            total_c5 += coluna["colum5"]["total"]
            total_colum6 += len(coluna["colum6"]["values"])
            total_c6 += coluna["colum6"]["total"]
            total_colum7 += len(coluna["colum7"]["values"])
            total_c7 += coluna["colum7"]["total"]
            total_colum8 += len(coluna["colum8"]["values"])
            total_c8 += coluna["colum8"]["total"]
            total_colum9 += len(coluna["colum9"]["values"])
            total_c9 += coluna["colum9"]["total"]
            total_colum10 += len(coluna["colum10"]["values"])
            total_c10 += coluna["colum10"]["total"]
            
            quadra_sup += len(line.content_json["quadrant_sup_inf"]["upper"]["values"])
            total_quadra_sup += line.content_json["quadrant_sup_inf"]["upper"]["total"]
            quadra_inf += len(line.content_json["quadrant_sup_inf"]["lower"]["values"])
            total_quadra_inf += line.content_json["quadrant_sup_inf"]["lower"]["total"]

            total_idem += len(line.content_json["idem"])
        
        data = {
                "media_par":int(round(total_par/total_lines)),
                "media_impar":int(round(total_impar/total_lines)),
                "media_mestre":int(round(total_mestre/total_lines)),
                "quadrante":{
                    "quad1":{
                        "media_quad1":int(round(total_quadrante1/total_lines)),
                        "total_quad1":int(round(total_quad1))
                    },
                    "quad2":{
                        "media_quad2":int(round(total_quadrante2/total_lines)),
                        "total_quad2":int(round(total_quad2))
                    },
                    "quad3":{
                        "media_quad3":int(round(total_quadrante3/total_lines)),
                        "total_quad3":int(round(total_quad3))
                    },
                    "quad4":{
                        "media_quad4":int(round(total_quadrante4/total_lines)),
                        "total_quad4":int(round(total_quad4))
                    }
                },
                "quad_inf":{
                    "media_quad_inf":int(round(total_quadra_inf/total_lines)),
                    "total_quadra_inf":int(round(total_quadra_inf))
                },
                "quad_sup":{
                    "media_quad_sup":int(round(quadra_sup/total_lines)),
                    "total_quadra_sup":int(round(total_quadra_sup))
                },
                "l1":{"media_linha1":int(round(total_line1/total_lines)),"total_l1":int(round(total_l1/total_lines))},
                "l2":{"media_linha2":int(round(total_line2/total_lines)),"total_l2":int(round(total_l2/total_lines))},
                "l3":{"media_linha3":int(round(total_line3/total_lines)),"total_l3":int(round(total_l3/total_lines))},
                "l4":{"media_linha4":int(round(total_line4/total_lines)),"total_l4":int(round(total_l4/total_lines))},
                "l5":{"media_linha5":int(round(total_line5/total_lines)),"total_l5":int(round(total_l5/total_lines))},
                "l6":{"media_linha6":int(round(total_line6/total_lines)),"total_l6":int(round(total_l6/total_lines))},
                "l7":{"media_linha7":int(round(total_line7/total_lines)),"total_l7":int(round(total_l7/total_lines))},
                "l8":{"media_linha8":int(round(total_line8/total_lines)),"total_l8":int(round(total_l8/total_lines))},
                "l9":{"media_linha9":int(round(total_line9/total_lines)),"total_l9":int(round(total_l9/total_lines))},
                "l10":{"media_linha10":int(round(total_line10/total_lines)),"total_l10":int(round(total_l10/total_lines))},
                "c1":{"media_coluna1":int(round(total_colum1/total_lines)),"total_c1":int(round(total_c1/total_lines))},
                "c2":{"media_coluna2":int(round(total_colum2/total_lines)),"total_c2":int(round(total_c2/total_lines))},
                "c3":{"media_coluna3":int(round(total_colum3/total_lines)),"total_c3":int(round(total_c3/total_lines))},
                "c4":{"media_coluna4":int(round(total_colum4/total_lines)),"total_c4":int(round(total_c4/total_lines))},
                "c5":{"media_coluna5":int(round(total_colum5/total_lines)),"total_c5":int(round(total_c5/total_lines))},
                "c6":{"media_coluna6":int(round(total_colum6/total_lines)),"total_c6":int(round(total_c6/total_lines))},
                "c7":{"media_coluna7":int(round(total_colum7/total_lines)),"total_c7":int(round(total_c7/total_lines))},
                "c8":{"media_coluna8":int(round(total_colum8/total_lines)),"total_c8":int(round(total_c8/total_lines))},
                "c9":{"media_coluna9":int(round(total_colum9/total_lines)),"total_c9":int(round(total_c9/total_lines))},
                "c10":{"media_coluna10":int(round(total_colum10/total_lines)),"total_c10":int(round(total_c10/total_lines))},
                "idem":{"media_idem":int(round(total_idem/total_lines))}
                }

        Summary.objects.create(content_json=data)
        return HttpResponseRedirect(reverse_lazy("common:summary_detail"))