import time

def cronometro():
    input("Pressione Enter para iniciar o cronômetro...")
    inicio = time.time() # É uma variável que armazena o valor de time.time() no momento em que o cronômetro foi iniciado. Representa o ponto de partida do cronômetro.
    print("Cronômetro iniciado!")

    while True:
        tempo_decorrido = int(time.time() - inicio) #Esta subtração calcula a diferença entre o tempo atual (agora) e o tempo de início. Essa diferença representa o tempo decorrido desde o início do cronômetro em segundos.
        print("Tempo decorrido:", tempo_decorrido, "segundos")#inicialmente exibe 0 e a cada loop aumenta 1
        time.sleep(1)  # Aguarda 1 segundo

cronometro()
