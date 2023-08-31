from django.shortcuts import render
from django.views.generic import View, ListView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
import pandas as pd
from common.models import File, Lines, Summary, Games
from common.process import ProcessLine
from common.parameters import DEFAULT_LIST
from common.processes_game import PlayGame
import itertools
import random

class CommonIndexView(ListView):
    model = Games
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

class GetGameView(View):
    model = Games

    def get(self, request, *args, **kwargs):
        play = self.model.objects.get(id=kwargs.get('pk'))
        numbers = play.content_json['jogo']
        quantidade_adicionar = 50
        numeros_adicionais = random.sample(range(1, 101), quantidade_adicionar)
        numbers.extend(numeros_adicionais)
        play.content_json['jogo'] = numbers
        play.save()
        return HttpResponseRedirect(reverse_lazy("common:index"), "Processado")

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
        status = PlayGame(df).main()
        if status:
            return HttpResponseRedirect(reverse_lazy("common:index"), "Processado")
        return HttpResponseRedirect(reverse_lazy("common:index"))

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