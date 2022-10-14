# ------ Bibliotecas --------
import math
from numpy import double
# ---------------------------


# ---- Cores no terminal ----
class Colors:

    def __init__(self):
        self.bold = '\033[1m'
        self.italic = '\033[3m'
        self.underlined = '\033[4m'
        self.normal = '\033[m'
        self.black = '\033[30m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.yellow = '\033[33m'
        self.blue = '\033[34m'
        self.magenta = '\033[35m'
        self.cyan = '\033[36m'
        self.gray = '\033[37m'

color = Colors()
# ---------------------------


# ---------- MENU -----------
print(f'''
\033[1m\033[36m• Autores:\033[m
  Carlos Massato Horibe Chinen   (R.A: 22.221.010-6)
  Gabriel Nunes Missima          (R.A: 22.221.040-3)
  Guilherme Quirino dos Santos   (R.A: 22.221.067-6)
  Gustavo das Flores Lima        (R.A: 22.221.041-1)

\033[1m\033[36m• Tópicos de Óptica de Física Moderna – CF3121\033[m
  NL 3A: Polarizadores

  ▶ A Polarização ocorre apenas em ondas transversais, característica das Ondas Eletromagnéticas. Um raio não polarizado passa por um filtro polarizador se torna um raio polarizado, este tem sua intensidade calculada pelo angulo no qual o raio atravessa tal filtro. Um raio polarizado pode passar por outros filtros, fazendo com que sua intensidade altere.

  ▶ O programa consiste em um menu com várias opções de entrada de valores referentes a Polarização de Ondas Eletromagnéticas que, por meio de contas que o programa realizará, retornarão outros valores, estes são, respectivamente:

{color.cyan}2 filtros:{color.normal}
 {color.green}✓{color.normal} Raio inicial: {color.italic}Intensidade da luz apos o primeiro filtro {color.normal}; {color.italic}Intensidade da luz apos o segundo filtro {color.normal}

 {color.green}✓{color.normal} Raio secundário: {color.italic}Intensidade da luz incidente {color.normal}; {color.italic}Intensidade da luz apos o segundo filtro {color.normal}

 {color.green}✓{color.normal} Raio final: {color.italic}Intensidade da luz incidente {color.normal}; {color.italic}Intensidade da luz apos o primeiro filtro {color.normal}

{color.cyan}3 filtros:{color.normal}
 {color.green}✓{color.normal} Raio inicial: {color.italic}Intensidade da luz apos o primeiro filtro {color.normal}; {color.italic}Intensidade da luz apos o segundo filtro {color.normal}; {color.italic}Intensidade da luz apos o terceiro filtro {color.normal}

 {color.green}✓{color.normal} Raio secundário: {color.italic}Intensidade da luz incidente {color.normal}; {color.italic}Intensidade da luz apos o segundo filtro {color.normal}; {color.italic}Intensidade da luz apos o terceiro filtro {color.normal}

 {color.green}✓{color.normal} Raio terciário: {color.italic}Intensidade da luz incidente {color.normal}; {color.italic}Intensidade da luz apos o primeiro filtro {color.normal}; {color.italic}Intensidade da luz apos o terceiro filtro {color.normal}

 {color.green}✓{color.normal} Raio final: {color.italic}Intensidade da luz incidente {color.normal}; {color.italic}Intensidade da luz apos o primeiro filtro {color.normal}; {color.italic}Intensidade da luz apos o terceiro filtro {color.normal}
''')   
# ---------------------------

#Enunciado com raio inicial não polarizado com o angulo do segundo filtro
def i0_nao_polarizado_2filtros():
    i0 = float(input("Raio incidente: \n"))
    ang1 = double(input("Angulo do primeiro filtro: \n"))
    ang2 = double(input("Angulo do segundo filtro: \n"))
    
    rad2 = math.radians(ang2)
    teta2 = math.cos(rad2)
    
    i1 = float(i0/2)
    i2 = float(i1*(teta2*teta2))
    
    print('Intensidade da luz apos o primeiro filtro: %.3f'% i1 +" W/c^2")
    print('Intensidade da luz apos o segundo filtro: %.3f'% i2 +" W/c^2")

#Enunciado com raio 1 polarizado com o angulo do segundo filtro   
def i1_polarizado_2filtros():
    i1 = float(input("Raio apos o primeiro filtro: \n"))
    ang1 = double(input("Angulo do primeiro filtro: \n"))
    ang2 = double(input("Angulo do segundo filtro: \n"))
    
    rad2 = math.radians(ang2)
    teta2 = math.cos(rad2)
    
    i0 = i1 * 2
    i2 = float(i1*(teta2*teta2))   
    
    print('Intensidade da luz incidente: %.3f'% i0 +" W/c^2")
    print('Intensidade da luz apos o segundo filtro: %.3f'% i2 +" W/c^2") 

#Enunciado com raio 2 polarizado com o angulo do segundo filtro    
def i2_polarizado_2filtros():
    i2 = float(input("Raio apos o segundo filtro: \n"))
    ang1 = double(input("Angulo do primeiro filtro: \n"))
    ang2 = double(input("Angulo do segundo filtro: \n"))
    
    rad2 = math.radians(ang2)
    teta2 = math.cos(rad2)
    
    i1 = i2/(teta2*teta2)
    i0 = i1 * 2  
    
    print('Intensidade da luz incidente: %.3f'% i0 +" W/c^2")
    print('Intensidade da luz apos o primeiro filtro: %.3f'% i1 +" W/c^2")
      
#Enunciado com raio inicial nao polarizado com o angulo do segundo filtro e terceiro filtro     
def i0_nao_polarizado_3filtros():
    i0 = float(input("Raio incidente: \n"))
    ang1 = double(input("Angulo do primeiro filtro: \n"))
    ang2 = double(input("Angulo do segundo filtro: \n"))
    ang3 = double(input("Angulo do terceiro filtro: \n"))
    
    rad2 = math.radians(ang2)
    teta2 = math.cos(rad2)
    
    ang3_2 = ang3-ang2
    rad3 = math.radians(ang3_2)
    teta3 = math.cos(rad3)
    
    i1 = i0/2
    i2 = i1*(teta2*teta2)
    i3 = i2*(teta3*teta3)
    
    print('Intensidade da luz apos o primeiro filtro: %.3f'% i1 +" W/c^2")
    print('Intensidade da luz apos o segundo filtro: %.3f'% i2 +" W/c^2")
    print('Intensidade da luz apos o terceiro filtro: %.3f'% i3 +" W/c^2")
    
#Enunciado com raio 1 polarizado com o angulo do segundo filtro e terceiro filtro
def i1_polarizado_3filtros():
    i1 = float(input("Raio apos o primeiro filtro: \n"))
    ang1 = float(input("Angulo do primeiro filtro: \n"))
    ang2 = float(input("Angulo do sengundo filtro: \n"))
    ang3 = float(input("Angulo do terceiro filtro: \n"))
    
    rad2 = math.radians(ang2)
    teta2 = math.cos(rad2)
    
    ang3_2 = ang3-ang2
    rad3 = math.radians(ang3_2)
    teta3 = math.cos(rad3)
        
    i0 = i1 * 2
    i2 = i1*(teta2*teta2)
    i3 = i2*(teta3*teta3)
    
    print('Intensidade da luz incidente: %.3f'% i0 +" W/c^2")
    print('Intensidade da luz apos o segundo filtro: %.3f'% i2 +" W/c^2")
    print('Intensidade da luz apos o terceiro filtro: %.3f'% i3 +" W/c^2")
         
#Enunciado com raio 2 polarizado com o angulo do primeiro filtro e terceiro filtro
def i2_polarizado_3filtros():
    i2 = float(input("Raio apos o segundo filtro: \n"))
    ang1 = float(input("Angulo do primeiro filtro: \n"))
    ang2 = float(input("Angulo do sengundo filtro: \n"))
    ang3 = float(input("Angulo do terceiro filtro: \n"))
    
    rad2 = math.radians(ang2)
    teta2 = math.cos(rad2)
    
    ang3_2 = ang3-ang2
    rad3 = math.radians(ang3_2)
    teta3 = math.cos(rad3)
     
    i1 = i2/(teta2*teta2)    
    i0 = i1 * 2
    i3 = i2*(teta3*teta3)
    
    print('Intensidade da luz incidente: %.3f'% i0 +" W/c^2")
    print('Intensidade da luz apos o primeiro filtro: %.3f'% i1 +" W/c^2")
    print('Intensidade da luz apos o terceiro filtro: %.3f'% i3 +" W/c^2")

#Enunciado com raio 3 polarizado com o angulo do segundo filtro e terceiro filtro
def i3_polarizado_3filtros():
    i3 = float(input("Raio apos o terceiro filtro: \n"))
    ang1 = float(input("Angulo do primeiro filtro: \n"))
    ang2 = float(input("Angulo do sengundo filtro: \n"))
    ang3 = float(input("Angulo do terceiro filtro: \n"))
    
    rad2 = math.radians(ang2)
    teta2 = math.cos(rad2)
    
    ang3_2 = ang3-ang2
    rad3 = math.radians(ang3_2)
    teta3 = math.cos(rad3)
    
    i2 = i3/(teta3*teta3) 
    i1 = i2/(teta2*teta2)    
    i0 = i1 * 2
    
    
    print('Intensidade da luz incidente: %.3f'% i0 +" W/c^2")
    print('Intensidade da luz apos o primeiro filtro: %.3f'% i1 +" W/c^2")
    print('Intensidade da luz apos o segundo filtro: %.3f'% i2 +" W/c^2")              


# ---- CÓDIGO PRINCIPAL -----
def main():
    while True:
        print('\n================ Menu ================\n')
        print('----- 2 Filtros -----\n')
        print('1 - Raio incidente e Angulo 1 e 2')
        print('2 - Raio 2 e Angulo 1 e 2')
        print('3 - Raio final e Angulo 1 e 2 \n')
        print('----- 3 Filtros -----\n')
        print('4 - Raio incidente e Angulo 1, 2 e 3')
        print('5 - Raio 1 e Angulo 1, 2 e 3')
        print('6 - Raio 2 e Angulo 1, 2 e 3')
        print('7 - Raio 3 e Angulo 1, 2 e 3')
        print('\n======================================\n')

        menu = int(input('Escolha uma das opções: \n'))

        if menu == 1:
            i0_nao_polarizado_2filtros()
        if menu == 2:
            i1_polarizado_2filtros()
        if menu == 3:
            i2_polarizado_2filtros()
        if menu == 4:
            i0_nao_polarizado_3filtros()
        if menu == 5:
            i1_polarizado_3filtros()
        if menu == 6:
            i2_polarizado_3filtros()
        if menu == 7:
            i3_polarizado_3filtros()
# ---------------------------
    
main()     