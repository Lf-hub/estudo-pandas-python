import random
import pandas as pd

from common.parameters import DEFAULT_LIST
from common.models import Lines, Games


class PlayGame:
    def __init__(self, df):
        self.par = 10
        self.impar = 10
        self.total_numbers = 20
        self.sorteados = []

        self.media_quad1 = df.at[0,'quadrante_quad1']['media_quad1']
        self.media_quad2 = df.at[0,'quadrante_quad2']['media_quad2']
        self.media_quad3 = df.at[0,'quadrante_quad3']['media_quad3']
        self.media_quad4 = df.at[0,'quadrante_quad4']['media_quad4']
        
        self.col1_len = df.at[0,'c1_media_coluna1']
        self.col2_len = df.at[0,'c2_media_coluna2']
        self.col3_len = df.at[0,'c3_media_coluna3']
        self.col4_len = df.at[0,'c4_media_coluna4']
        self.col5_len = df.at[0,'c5_media_coluna5']
        self.col6_len = df.at[0,'c6_media_coluna6']
        self.col7_len = df.at[0,'c7_media_coluna7']
        self.col8_len = df.at[0,'c8_media_coluna8']
        self.col9_len = df.at[0,'c9_media_coluna9']
        self.col10_len = df.at[0,'c10_media_coluna10']

        self.line1_len = df.at[0,'l1_media_linha1']
        self.line2_len = df.at[0,'l2_media_linha2']
        self.line3_len = df.at[0,'l3_media_linha3']
        self.line4_len = df.at[0,'l4_media_linha4']
        self.line5_len = df.at[0,'l5_media_linha5']
        self.line6_len = df.at[0,'l6_media_linha6']
        self.line7_len = df.at[0,'l7_media_linha7']
        self.line8_len = df.at[0,'l8_media_linha8']
        self.line9_len = df.at[0,'l9_media_linha9']
        self.line10_len = df.at[0,'l10_media_linha10']

    def main(self):
        last_game = Lines.objects.all().last().content_json.get('numeros')
        mestre = DEFAULT_LIST.get('mestres')
        remove_list = [last_game, mestre]
        numeros = list(range(1, 101))
        for lista in remove_list:
            list_numbers = [numero for numero in numeros if numero not in lista]
        
        while self.total_numbers > 0:
            status_step1 = False
            status_quadrant = False
            status_col = False
            status_line = False
            number = random.choice(list_numbers)
            # step1
            status_step1 = self.get_par_or_impar(number)
            # step2
            if status_step1:
                status_quadrant = self.get_quadrante(number)
            # step3
            if status_quadrant:
                status_col = self.get_colum(number)
            # step4
            if status_col:
                status_line = self.get_line(number)    
            if status_line:
                self.sorteados.append(number)
                self.total_numbers -= 1
                
        else:
            data = {"jogo":self.sorteados}
            Games.objects.create(content_json=data)

    def get_par_or_impar(self, number):
        status = False
        if number % 2 == 0:
            if self.par > 0:
                self.par -= 1
            else:
                self.par += 1
            status = True
        else:
            if self.impar > 0:
                self.impar -= 1
            else:
                self.impar += 1
            status = True
        return status
    
    def get_quadrante(self,number):
        if self.media_quad1 != 0:
            n = number if number in DEFAULT_LIST.get('first_quadrant') else False
            if n:
                self.media_quad1 -= 1
                return True
        else:
            self.media_quad1 += 1
            return True
        
        if self.media_quad2 != 0:
            n = number if number in DEFAULT_LIST.get('second_quadrant') else False
            if n:
                self.media_quad2 -= 1
                return True
        else:
            self.media_quad2 += 1
            return True
        
        if self.media_quad3 != 0:
            n = number if number in DEFAULT_LIST.get('third_quadrant') else False
            if n:
                self.media_quad3 -= 1
                return True
        else:
            self.media_quad3 += 1
            return True
        
        if self.media_quad4 != 0:
            n = number if number in DEFAULT_LIST.get('fourth_quadrant') else False
            if n:
                self.media_quad4 -= 1
                return True
        else:
            self.media_quad4 += 1
            return True

    
    def get_colum(self, number):
        if self.col1_len != 0:
            n = number if number in DEFAULT_LIST.get('first_colum') else False
            if n:
                self.col1_len -= 1
                return True
        else:
            self.col1_len += 1
            return True
        
        if self.col2_len != 0:
            n = number if number in DEFAULT_LIST.get('second_colum') else False
            if n:
                self.col2_len -= 1
                return True
        else:
            self.col2_len += 1
            return True

        if self.col3_len != 0:
            n = number if number in DEFAULT_LIST.get('third_colum') else False
            if n:
                self.col3_len -= 1
                return True
        else:
            self.col3_len += 1
            return True

        if self.col4_len != 0:
            n = number if number in DEFAULT_LIST.get('fourth_colum') else False
            if n:
                self.col4_len -= 1
                return True
        else:
            self.col4_len += 1
            return True
        
        if self.col5_len != 0:
            n = number if number in DEFAULT_LIST.get('fifth_colum') else False
            if n:
                self.col5_len -= 1
                return True
        else:
            self.col5_len += 1
            return True
        
        if self.col6_len != 0:
            n = number if number in DEFAULT_LIST.get('sixth_colum') else False
            if n:
                self.col6_len -= 1
                return True
        else:
            self.col6_len += 1
            return True

        if self.col7_len != 0:
            n = number if number in DEFAULT_LIST.get('seventh_colum') else False
            if n:
                self.col7_len -= 1
                return True
        else:
            self.col7_len += 1
            return True
        
        if self.col8_len != 0:
            n = number if number in DEFAULT_LIST.get('octave_colum') else False
            if n:
                self.col8_len -= 1
                return True
        else:
            self.col8_len += 1
            return True

        if self.col9_len != 0:
            n = number if number in DEFAULT_LIST.get('ninth_colum') else False
            if n:
                self.col9_len -= 1
                return True
        else:
            self.col9_len += 1
            return True
            
        if self.col10_len != 0:
            n = number if number in DEFAULT_LIST.get('tenth_colum') else False
            if n:
                self.col10_len -= 1
                return True
        else:
            self.col10_len += 1
            return True    


    def get_line(self,number):
        if self.line1_len != 0:
            n = number if number in list(range(1, 11)) else False
            if n:
                self.line1_len -= 1
                return True
        else:
            self.line1_len += 1
            return True
        
        if self.line2_len != 0:
            n = number if number in list(range(11, 21)) else False
            if n:
                self.line2_len -= 1
                return True
        else:
            self.line2_len += 1
            return True
        
        if self.line3_len != 0:
            n = number if number in list(range(21, 31)) else False
            if n:
                self.line3_len -= 1
                return True
        else:
            self.line3_len += 1
            return True

        if self.line4_len != 0:
            n = number if number in list(range(31, 41)) else False
            if n:
                self.line4_len -= 1
                return True
        else:
            self.line4_len += 1
            return True
        
        if self.line5_len != 0:
            n = number if number in list(range(41, 51)) else False
            if n:
                self.line5_len -= 1
                return True
        else:
            self.line5_len += 1
            return True
        
        if self.line6_len != 0:
            n = number if number in list(range(51, 61)) else False
            if n:
                self.line6_len -= 1
                return True
        
        if self.line7_len != 0:
            n = number if number in list(range(61, 71)) else False
            if n:
                self.line7_len -= 1
                return True
        if self.line8_len != 0:
            n = number if number in list(range(71, 81)) else False
            if n:
                self.line8_len -= 1
                return True
        if self.line9_len != 0:
            n = number if number in list(range(81, 91)) else False
            if n:
                self.line9_len -= 1
                return True
        if self.line10_len != 0:
            n = number if number in list(range(91, 101)) else False
            if n:
                self.line10_len -= 1
                return True    
        return False
