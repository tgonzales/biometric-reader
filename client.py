from biometriclib import *

_time = 0.3
init()
time.sleep(_time)
print(stream())
time.sleep(_time)
run(3, 'MyTemplate')
for i in range(5):
    time.sleep(_time)
    print(stream())

run(2)
print('Run 2 - break proccess 3 and start 5')
time.sleep(3)

run(5)
print('Run 5')
time.sleep(_time + 1)
for i in range(5):
    time.sleep(_time)
    print(stream())

run(2)
print('Run 2 - break proccess 5 and start 4')
time.sleep(3)

run(4, [1,2,3])
for i in range(5):
    time.sleep(_time)
    print(stream())

run(0)
print('FINISH ...')
