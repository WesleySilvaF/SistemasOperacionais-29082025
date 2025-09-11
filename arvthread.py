#importação de biblioteca
import threading #Importa Demódulos de threading
import time #Importa Demódulos de tempo para calculos 
import math #Importa Demódulos matemáticos
#Estrutura da Thread
def estruturaThread(nome, incio, fim):
    for i in range(incio, fim +1):
        print(f'{nome} -> {i}')
        time.sleep(1) #Tempo de Resposta para cada contagem (EX: time.sleep(2) usado para definir 2 segundos de tempo de resposta)

thread1 = threading.Thread(target=estruturaThread, args=("thread1", 1, 10)) #É a função usada definir a estrutura de contagem
thread2 = threading.Thread(target=estruturaThread, args=("thread2", 50, 60)) #É a função usada definir a estrutura de contagem

thread1.start() #Comando usado para iniciar os funções
thread2.start() #Comando usado para iniciar as funções

