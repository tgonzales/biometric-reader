#!/usr/bin/python3

'''
Program Reader PalmSecure

cmd
0 = close
1 = init
2 = break process
3 = ify # Identification
4 = vfy # Verification
5 = enr # Enrollment

O programa tem 2 threads

a thread principal, executa os seguintes metodos
init() iniciar a comunicaÃ§Ã£o com o driver
close() fechar a comunicaÃ§Ã£o com o driver
run() manda comandos para o driver que sao armazenados na variavel global CMD
stream() pega a ultima mensagem do driver.

Em paralelo Ã© executado a segunda thread
run_thread_process()
esse metodo fica checando a variavel CMD
para ele o importante sao os CMD 3,4 e 5
ify - identification (1 para 1 - compara a mao que esta no sensor se eh valida com a que esta em um array unico)
vfy - verification (1 para N - compara a mao que esta no sensor se eh valida com as maos que estao em um array multiplo)
enr - grava o template da mao

A necessidade de ter 2 threads eh pela necessidade de termos que interromper um processo e iniciar outro.
ex. uma vez que estamos rodando vfy e queremos mudar para ify. nesse caso, o programa cliente deve
iniciar o vfy, encerrar e iniciar o ify,
run(4) inicia vfy
run(2) encerra vfy
run(3) inicia ify

isso acontece porque ify, vfy, enr rodam em um while entao precisamos dar um break para entrar em outro CMD

dentro de __main__ esta um teste que ao executar o arquivo diretamente roda um fluxo basico de operacao
'''
import threading
import time

CMD = 0
STREAM = 'STOPED'
TMPL = None
TMPLS = []

def run_thread_process():
    global CMD
    while True:
        if CMD == 3:
            ify()
        if CMD == 4:
            vfy()
        if CMD == 5:
            enr()

t = threading.Thread(target=run_thread_process)
t.daemon = True
threads = []

def init():
    global t
    threads.append(t)
    t.start()

def close():
    t._stop()

def run(cmd, data=False):
    global CMD
    if cmd == 3:
        TMPL = data
    if cmd == 4:
        TMPLS = data
    CMD = cmd

def stream():
    return STREAM

def ify():
    global CMD, TMPL, STREAM
    while True:
        time.sleep(0.2)
        if CMD == 2:
            break

        STREAM = 'IFY: Coloque a mao no sensor'
        # compare TMPL

def vfy():
    global CMD, TMPLS, STREAM
    while True:
        time.sleep(0.2)
        if CMD == 2:
            break
    
        STREAM = 'VFY: Coloque a mao no sensor'
        # compare palm in TMPLS

def enr():
    global CMD, STREAM
    while True:
        time.sleep(0.2)
        if CMD == 2:
            break
        STREAM = 'ENR: Coloque a mao no sensor'
