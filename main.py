import math


print('• Autores:' + '\n'+'\n'+ 
'Carlos Massato Horibe Chinen (R.A: 22.221.010-6)\n' '' 
'Gabriel Nunes Missima  (R.A: 22.221.040-3)\n'
'Guilherme Quirino dos Santos (R.A: 22.221.067-6)\n'
'Gustavo das Flores Lima (R.A: 22.221.041-1)'+'\n \n')

print('Tó(math.pi)cos de Óptica de Física Moderna – CF3121\n'
'NL1 – A1 : Ondas Eletromagnéticas com Python\n\n'
'• As OEM ou Ondas Eletromagnéticas são a energia elétrica e magnética liberadas em conjunto que, por se movimentarem na velocidade da luz, tomam a forma de uma onda.\n Para que tal efeito ocorra o campo eletromagnético oscila em uma direção enquanto o campo magnético oscila em outra, fazendo com que a onda se propague em uma só direção.\n\n'
'• O programa consiste em um menu com várias opções de entrada de valores referentes a Ondas Eletromagnéticas que, por meio de contas que o programa realizará,\n retornarão outros valores, estes são, respectivamente:\n\n'

'Amplitude do Campo Elétrico (Em) = Bm ; I\n'
'Amplitude do Campo Eletromagnético (Bm) = Em ; I\n'
'Intensidade da Onda (I) = Em ; Bm\n'
'Frequência (F) = Y ; K ; W\n'
'Comprimento de Onda (Y) = F ; K ; W\n'
'Número de Onda (K) = F ; Y ; W\n'
'Frequência Angular (W) = F ; Y ; K\n\n')

V = 3*10**8
pi4 = 4*math.pi
u = pi4*(10**-7)

def frequencia ():
    F = float(input('Digite o valor da frequencia(F) em Hz: ' + '\n'))

    W = (F*(2*(math.pi)))
    K = W/V
    Y = 2*(math.pi)/K

    W = str(W)
    K = str(K)
    Y = str(Y)

    frequencia_angular = print('O valor da frequencia angular é ' + W + ' rad/s\n')
    numero_de_onda = print('O valor do numero de onda da onda é ' + K + ' rad/m\n') 
    comprimento_de_onda = print('O valor da comprimento de onda é ' + Y +' m\n')

    return comprimento_de_onda, numero_de_onda, frequencia_angular

def comprimentoDaOnda():
    Y = float(input('Digite o valor do comprimento da onda(Y) em metros: '))

    K = 2*(math.pi)/Y
    W = K*V
    F = W/(2*(math.pi))

    K = str(K)
    W = str(W)
    F = str(F)

    frequencia  = print('O valor da frequencia é igual a ' + F + ' Hz\n')
    numero_de_onda = print('O valor do numero de onda da onda é igual a ' + K + ' rad/m\n')
    frequencia_angular = print('O valor da frequencia angular é igual a ' + W + ' rad/s\n')

    return frequencia, numero_de_onda, frequencia_angular

def numeroDeOnda():
    K = float(input('Digite o valor do numero de onda(K) em rad/m: '))
    
    Y = 2*(math.pi)/K
    W = K*V
    F = W/(2*(math.pi))

    Y = str(Y)
    W = str(W)
    F = str(F)

    frequencia = print('O valor da frequencia é igual a ' + F + ' Hz\n')
    comprimento_de_onda = print('O valor do comprimento de onda é igual a ' + Y + ' m\n')
    frequencia_angular = print('O valor da frequencia angular é igual a ' + W + ' rad/s\n')

    return frequencia, comprimento_de_onda, frequencia_angular

def frequenciaAngular():
    W = float(input('Digite o valor da frequencia angular(W) em rad/s: '))

    F = W/(2*(math.pi))
    K = W/V
    Y = 2*(math.pi)/K

    F = str(F)
    K = str(K)
    Y = str(Y)

    frequencia = print('O valor da frequencia é igual a ' + F + ' Hz\n')
    comprimento_de_onda = print('O valor do comprimento de onda é igual a ' + Y + ' m\n')
    numero_de_onda = print('O valor do numero de onda da onda é ' + K + ' rad/m\n')

    return frequencia, comprimento_de_onda, numero_de_onda

def amplitudeCampoEletrico():
    Em = float(input('Digite o valor da amplitude do campo eletrico(Em) em V/m: ' + '\n'))

    Bm = Em/V

    I = ((Em**2)/(2*((u)*(V))))

    Bm = str(Bm)
    I = str(I)

    amplitude_do_campo_eletromagnetico = print('O valor da amplitude do campo eletromagnetico é igual a ' + Bm + ' T\n')
    intensidade_do_campo_eletromagnetico = print('O valor da intensidade da onda é igual a ' + I + ' W/m^2\n')

    return amplitude_do_campo_eletromagnetico, intensidade_do_campo_eletromagnetico

def amplitudeCampoEletromagnetico():
    Bm = float(input('Digite o valor da amplitude do campo magnetico(Bm) em T: ' + '\n'))

    Em = Bm*V

    I = ((Em**2)/(2*(u)*(V)))

    Em = str(Em)
    I = str(I)

    amplitude_do_campo_eletrico = print('O valor da amplitude do campo eletrico é igual a ' + Em + ' V/m\n')
    intensidade_do_campo_eletromagnetico = print('O valor da intensidade da onda é igual a ' + I + ' W/m^2\n')

    return amplitude_do_campo_eletrico, intensidade_do_campo_eletromagnetico

def intensidade():
    I = float(input('Digite o valor da intensidade(I) em W/m^2: ' + '\n'))

    Em = (math.sqrt(I * (2 * (u)* (V))))

    Bm = Em/V

    Em = str(Em)
    Bm = str(Bm)

    amplitude_do_campo_eletrico = print('O valor da amplitude do campo eletrico é igual a ' + Em + ' V/m\n')
    amplitude_do_campo_eletromagnetico = print('O valor da amplitude do campo eletromagnetico é igual a ' + Bm + ' T\n')

    return amplitude_do_campo_eletrico, amplitude_do_campo_eletromagnetico

def main():
    while True:
        print('Escolha a váriavel já obtida através do enunciado')
        print('-------- Menu --------')
        print('1 - Frequencia')
        print('2 - Comprimento de onda')
        print('3 - Numero de onda')
        print('4 - Frequencia angular')
        print('5 - Amplitude do campo Eletrico')
        print('6 - Amplitude do campo Eletromagnetico')
        print('7 - Intensidade da onda')


        choice = int(input('Escolha uma das opções: \n'))

        if choice == 1:
            frequencia()
        if choice == 2:
            comprimentoDaOnda()
        if choice == 3:
            numeroDeOnda()
        if choice == 4:
            frequenciaAngular()
        if choice == 5:
            amplitudeCampoEletrico()  
        if choice == 6:
            amplitudeCampoEletromagnetico()                                            
        if choice == 7:
            intensidade()                

main()