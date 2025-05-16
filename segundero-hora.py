def calc_segundos():
    A=input('\nIngrese la hora en el formato HH:MM:SS: ')
    Hr=int(A[0:2:1])
    Min=int((A[3:5:1]))
    Seg=int((A[6::1]))
    
    while (Hr>23 or Hr<0) or (Min>59 or Min<0) or (Seg>59 or Seg<0):
        A=input('El tiempo no puede excederse\nIngrese la hora en el formato HH:MM:SS: ')
        Hr=int(A[0:2:1])
        Min=int((A[3:5:1]))
        Seg=int((A[6::1]))
    segundos=(Hr*3600)+(Min*60)+(Seg)
    
    print('\nLa hora ingresada da un total de ' + str(segundos) + ' segundos')

def calc_hora():
    A=int(input('\nIngrese la cantidad de segundos (debe ser mayor o igual a 3600): '))
    
    while A<3600:
        A=int(input('Debe ser mayor o igual a 3600\nIngrese la cantidad de segundos (debe ser mayor o igual a 3600): '))
    Hr=int(A/3600)
    Min=int((A%3600)/60)
    Seg=(A%3600)%60
    
    print('\nLos segundos ingresados dan como hora ' + str(Hr) + ':' + str(Min) + ':' + str(Seg))
    
R=3
while R==3:
    print('\nCalcular segundos -> Presionar 0')
    print('Calcular horas, minutos y segundo -> Presionar 1')
    print('Salir -> 2')
    R=int(input('Respuesta: '))
    
    while R==0:
        calc_segundos()
        R=int(input('\n¿Intentar otra vez?\nSi -> Presionar 0\nNo -> Presionar 3\nRespuesta: '))
        
    while R==1:
        calc_hora()
        R=int(input('\n¿Intentar otra vez?\nSi -> Presionar 1\nNo -> Presionar 3\nRespuesta: '))