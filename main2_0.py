# ------ Bibliotecas --------
from math import *
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
  Carlos Massato Horibe Chinen (R.A: 22.221.010-6)
  Gabriel Nunes Missima  (R.A: 22.221.040-3)
  Guilherme Quirino dos Santos (R.A: 22.221.067-6)
  Gustavo das Flores Lima (R.A: 22.221.041-1)

\033[1m\033[36m• Tópicos de Óptica de Física Moderna – CF3121\033[m
  NL 2A: Átomo de Bohr e quantização com Python   

  ▶ O modelo atômico de Bohr define que os elétrons de um átomo tem um nivél mínimo de energia e que ao sofrer qualquer pertubação em seu nível atual afeta diretamente sua energia potêncial, processo denominado quantização, fazendo com que ocorra a o salto quântico, onde esses passariam para outro nível de energia.

  ▶ O programa consiste em um menu com várias opções de entrada de valores referentes a Quantização que, por meio de contas que o programa realizará, retornarão outros valores, estes são, respectivamente:

{color.yellow}!{color.normal} Numero Quantico (n): {color.italic}Rn ; Vn ; Kn ; Un ; En ; Yn{color.normal} 
   {color.yellow}--> Problema com o comprimento de onda de De Broglie{color.normal}
{color.green}✓{color.normal} Energia do foton (Ef): {color.italic}Ef ; Y ; F{color.normal}
{color.green}✓{color.normal} Frequencia do foton (F) absorvido/emitido: {color.italic}ni ; nf{color.normal}
{color.green}✓{color.normal} Comprimento de onda do foton (Y) absorvido/emitido: {color.italic}ni ; nf{color.normal}

Variáveis: (apagar no final)
  Raio da órbita (Rn):
  Velocidade (Vn):
  Energia Cinética (Kn):
  Energia Potencial (Un):
  Energia total(En):
  Comprimento de onda do eletron (Yn):
  Numero Quantico inicial e final (ni - nf) = Ef ; Ff ; Yf
  Numero quantico inicial ou final (ni ou nf) + (Ff ou Yf absorvido)
''')   
# ---------------------------


# ---- Variaveis Globais ----
c = 3e8
h = 4.136e-15
m = 9.11e-31
R = 1.097e7
nm = 1e9 # nanometro
thz = 1e12 # Terahertz
# ---------------------------


# --------- FUNÇOES ---------
def numeroQuantico():
    '''
    Recebe:
        - Estado n do atomo (n)

    Retorna:
        - Raio da órbita(Rn)
        - Velocidade do elétron(Vn)
        - Energia cinética do elétron(Kn)
        - Energia potencial do elétron(Un)
        - Energia total do elétron(En)
        - Comprimento da onda de De Broglie(Yn)
    '''
    h = 6.626e-34

    n = float(input('\nEstado n do atomo: \n'))

    Rn = ((n ** 2) * 5.29e-11) * nm
    Vn = 2.187e6 / n
    Kn = 13.6 / (n ** 2)
    Un = -27.2 / (n ** 2)
    En = -13.6 / (n ** 2)
    Yn = (h / (m * Vn)) * nm

    print(f'raio da órbita[m]: {color.italic}{Rn:.3f} nm{color.normal}\n')
    print(f'velocidade[m/s]: {color.italic}{Vn:.3f} m/s{color.normal}\n')
    print(f'energia cinética[eV]: {color.italic}{Kn:.3f} eV{color.normal}\n')
    print(f'energia potencial[eV]: {color.italic}{Un:.3f} ev{color.normal}\n')
    print(f'energia total[eV]: {color.italic}{En:.3f} eV{color.normal}\n')
    print(f'comprimento de onda de De Broglie do elétron [nm]: {color.italic}{Yn:.3f} m{color.normal}\n')


def energiaFoton():
    '''
    Recebe:
        - n_inicial
        - n_final
    
    Retorna:
        - Energia do Fóton
        - Comprimento de onda do Fóton
        - Frequência do Fóton
    '''
    ni = float(input(f'\nn inicial:{color.blue} \n'))
    nf = float(input(f'{color.normal}n final:{color.blue} \n'))
    print(f'{color.normal}')

    Yf = abs(1 / (R * ((1 / (nf ** 2)) - (1 / (ni ** 2)))))
    Ff = (c / Yf)
    Ef = (h * c) / Yf

    print(f'Energia do Fóton[eV]: {color.italic}{Ef:.2f} eV{color.normal}\n')
    print(f'Comprimento de onda do Fóton[m]: {color.italic}{Yf} m{color.normal}\n')
    print(f'Frequência do Fóton absorvido[Hz]: {color.italic}{Ff:.2f} Hz{color.normal}\n')


def frequenciaFoton():
    '''
    Recebe:
        - n_inicial
        - n_final
        - Frequencia
    
    Retorna:
        - n_inicial
        - n_final
    '''
    ni = int(input('n inicial:\n'))
    nf = int(input('n final:\n'))
    F = float(input('Frequencia do Foton[Hz]:\n'))

    Ef = h * F

    # n inicial
    n_inicial = nf - int(Ef)

    # n final
    n_final = ni + int(Ef)

    print(f'\n{color.magenta}ABSORÇÃO{color.normal}')
    print(f'Número quântico inicial(ni): {color.italic}{n_inicial:.1f}{color.normal}')
    print(f'Número quântico final(nf): {color.italic}{n_final:.1f}{color.normal}')

    # n inicial
    n_inicial = nf + int(Ef)

    # n final
    n_final = ni - int(Ef)

    print(f'\n{color.magenta}EMISSÃO{color.normal}')
    print(f'Número quântico inicial(ni): {color.italic}{n_inicial:.1f}{color.normal}')
    print(f'Número quântico final(nf): {color.italic}{n_final:.1f}{color.normal}')


def comprimentoOndaFoton():
    '''
    Recebe:
        - n_inicial
        - n_final
        - Comprimento de onda
    
    Retorna:
        - n_inicial
        - n_final
    '''
    ni = float(input('n inicial:\n'))
    nf = int(input('n final:\n'))
    Y = float(input('Comprimento de onda do Fóton:\n'))

    # Dicionário opcional
    n = {
        1 : -13.6,
        2 : -3.4,
        3 : -1.51,
        4 : -0.85,
        5 : -0.54,
        6 : -0.38,
        7 : -0.28
    }
 
    energia_foton = (h * c) / Y

    # n_final
    energia_inicial = (-13.6 / (ni ** 2))
    energia_final = energia_inicial + energia_foton
    n_final = sqrt(13.6 / abs(energia_final))

    # n_inicial
    energia_final = (-13.6 / (nf ** 2))
    energia_inicial = energia_final + energia_foton
    n_inicial = sqrt(13.6 / abs(energia_inicial))

    print(f'\n{color.magenta}ABSORÇÃO{color.normal}')
    print(f'Número quântico inicial(ni): {n_inicial:.0f}')
    print(f'Número quântico final(nf): {n_final:.0f}')

    # n inicial
    energia_final = (-13.6 / (nf ** 2))
    energia_inicial = energia_final + energia_foton
    n_inicial = sqrt(13.6 / abs(energia_inicial)) 

    # n final
    energia_inicial = -13.6 / (ni ** 2)
    energia_final = energia_inicial - energia_foton
    n_final = sqrt(13.6 / abs(energia_final))

    print(f'\n{color.magenta}EMISSÃO{color.normal}')
    print(f'Número quântico inicial(ni): {n_inicial:.0f}')
    print(f'Número quântico final(nf): {n_final:.0f}')
# ---------------------------
    

# ---- CÓDIGO PRINCIPAL -----
def main():
    while True:
        print()
        print('Menu'.center(36, '='))
        print('[ 1 ] Número Quântico\n')
        print('[ 2 ] Estados do atomo de hidrogenio\n')
        print('[ 3 ] Frequência do Fóton\n')
        print('[ 4 ] Comprimento de onda do Fóton')
        print('=' * 36)

        choice = int(input(f'{color.underlined}Escolha uma das opções:{color.normal}\n'))

        if choice == 1:
            numeroQuantico()
        
        elif choice == 2:
            energiaFoton()
        
        elif choice == 3:
            frequenciaFoton()
        
        elif choice == 4:
            comprimentoOndaFoton()
        else:
            continue


if __name__ == '__main__':
    main()
# ---------------------------