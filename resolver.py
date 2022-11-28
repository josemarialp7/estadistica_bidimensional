from prettytable import PrettyTable
from matplotlib import pyplot as plt
import math


data_nums = int(input('Introduce n --->   '))
txt_data_nums = str(data_nums)
data_x = []
data_y = []
data_x_2 = []
data_y_2 = []
total_data_x = 0
total_data_y = 0
total_data_x_2 = 0
total_data_y_2 = 0
mytable = PrettyTable(['Calc.Simples','n = ' + txt_data_nums,'Total'])
mytable1 = PrettyTable(['Calc.Complejos','Total'])
 
def nums_x():
    for i in range(data_nums):
        print('Introduce los datos de la x')
        data_x_input = float(input())
        data_x.append(data_x_input)

def nums_y():
    for i in range(data_nums):
        print('Introduce los datos de la y')
        data_y_input = float(input())
        data_y.append(data_y_input)

def nums_x_2():
    for i in data_x:
        data_x_2.append(math.pow(i,2))
        
        
def nums_y_2():
    for y in data_y:
        data_y_2.append(math.pow(y,2))
      

def num_total_data_x():
    for dx in data_x:
        global total_data_x
        total_data_x += dx 

def num_total_data_y():
    for dy in data_y:
        global total_data_y
        total_data_y += dy

def num_total_data_x_2():
    for dx2 in data_x_2:
        global total_data_x_2
        total_data_x_2 += dx2

def num_total_data_y_2():
    for dy2 in data_y_2:
        global total_data_y_2
        total_data_y_2 += dy2
   
nums_x()
nums_y()
nums_x_2()
nums_y_2()
num_total_data_x()
num_total_data_y()
num_total_data_x_2()
num_total_data_y_2()




data_multi_x_y = [x*y for x,y in zip(data_x,data_y)]
total_data_multi_x_y = 0
def num_total_data_multi_x_y():
    for dmxy in data_multi_x_y:
        global total_data_multi_x_y
        total_data_multi_x_y += dmxy       
num_total_data_multi_x_y()

mytable.add_row(['x',data_x , total_data_x])
mytable.add_row(['y',data_y , total_data_y])
mytable.add_row(['x2',data_x_2 , total_data_x_2])
mytable.add_row(['y2',data_y_2 , total_data_y_2])
mytable.add_row(['x*y',data_multi_x_y , total_data_multi_x_y])



print(mytable)


media_x = total_data_x / data_nums
media_y = total_data_y / data_nums
varianza_x = (total_data_x_2 / data_nums) - math.pow(media_x , 2)
varianza_y = (total_data_y_2 / data_nums) - math.pow(media_y , 2)
desviacion_tipica_x = math.sqrt(varianza_x)
desviacion_tipica_y = math.sqrt(varianza_y)
covarianza_x_y = (total_data_multi_x_y / data_nums) - (media_x * media_y)
coeficiente_de_correlacion = covarianza_x_y / (desviacion_tipica_x * desviacion_tipica_y)


mytable1.add_row(['x media', media_x])
mytable1.add_row(['y media', media_y])
mytable1.add_row(['varianza x', varianza_x])
mytable1.add_row(['varianza y', varianza_y])
mytable1.add_row(['desviacion tipica x', desviacion_tipica_x])
mytable1.add_row(['desviacion tipica y', desviacion_tipica_y])
mytable1.add_row(['covarianza x e y', covarianza_x_y])
mytable1.add_row(['coeficiente de correlacion', coeficiente_de_correlacion])



print(mytable1)


plt.scatter(data_x , data_y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grafica de puntos')
plt.show()


check = str(input('¿Tiene sentido hacer la recta de regresion de y sobre x? Escribe S si quieres hacerla o N si no --->   '))

if check == 'S':
    txt_media_y = str(media_y)
    txt_media_x = str(media_x)
    resultadoec = covarianza_x_y / varianza_x
    txt_resultadoec = str(resultadoec)
    print('y-' + txt_media_y + '=' + txt_resultadoec + '*' + '(x-' + txt_media_x + ')')
    
    check1 = str(input('¿Quiere sustituir la x o la y? S/N --->   '))
    if check1 == 'S':
        check2 = str(input('¿Que quiere sustituir, la x o la y? x/y --->   '))
        
        if check2 == 'x':
            checkX = int(input('¿Por cuanto quiere sustituir la X? --->   '))
            resultado_x = (checkX - media_x) * resultadoec + media_y
            txt_resultado_x = str(resultado_x)
            print('y=' + txt_resultado_x)
            
        elif check2 == 'y':
            checkY = int(input('¿Por cuanto quiere sustituir la Y? --->   '))
            multi_ec_x = resultadoec * 1
            resta_y = checkY - media_y
            resultado_y = resta_y + (resultadoec * media_x) / multi_ec_x
            txt_resultado_y = str(resultado_y)
            print('x=' + txt_resultado_y)
            
            
    else:
        print('Pos vale')
    

else:
    print('Pos vale')
