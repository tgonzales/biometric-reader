## Program Biometric Reader

### cmd
- 0 = close
- 1 = init
- 2 = break process
- 3 = ify # Identification
- 4 = vfy # Verification
- 5 = enr # Enrollment

### O programa tem 2 threads
- a thread principal, executa os seguintes metodos
	> init() iniciar a comunicao com o driver
	
	> close() fechar a comunicao com o driver
	
	> run() manda comandos para o driver que sao armazenados na variavel global CMD
	
	> stream() retorna a ultima mensagem (string) do driver.

- Em paralelo eh executado a segunda thread
	> run_thread_process()

- esse metodo fica checando a variavel CMD
para ele o importante sao os CMD 3, 4 e 5
	> 3 - ify - identification (1 para N - compara a mao que esta no sensor com algum template de mao que estao em um array)
	
	> 4 - vfy - verification (1 para 1 - compara a mao que esta no sensor com o template da mao informado previamente)
enr - grava o template da mao e retorna o template

A necessidade de ter 2 threads eh pela necessidade de termos que interromper um processo e iniciar outro.
ex. 
- uma vez que estamos rodando vfy e queremos mudar para ify. nesse caso, o programa cliente deveria
iniciar o vfy, encerrar e iniciar o ify,
	> run(4) # inicia vfy
	
	> run(2) # encerra vfy
	
	> run(3) # inicia ify

isso acontece porque ify, vfy, enr rodam em um while entao precisamos dar um break para entrar em outro CMD

### como testar o programa:
```
from createdb import createDatabase, removeDatabase
from biometriclib import *

>>> createDatabase()
>>> init()
>>> print(stream())
AWAYT
>>> run(3)
>>> print(stream())
IFY: Coloque a mao no sensor >
>>> run(2)
>>> print(stream())
AWAYT
>>> run(4, 'meuTemplateBiometrico')
>>> print(stream())
VFY: Coloque a mao no sensor >
>>> run(2)
>>> print(stream())
AWAYT
>>> run(5)
>>> print(stream())
ENR: Coloque a mao no sensor >
>>> run(2) # break process
>>> run(0) # close program
```

ou execute o programa demo client.py
```
$ python3 client.py
```
