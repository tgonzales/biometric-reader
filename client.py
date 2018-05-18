from createdb import createDatabase, removeDatabase
from biometriclib import *
# methods run(),  init(), stream()

createDatabase()
_time = 0.3
init()
time.sleep(_time)
print(stream())
time.sleep(_time)

# ify - 1:N
run(3)
for i in range(15):
    time.sleep(_time)
    print(stream())

# break
run(2)
print('Run 2 - break proccess 3 and start 5')
time.sleep(3)

# enr grava template
run(5)
print('Run 5')
time.sleep(_time + 1)
for i in range(5):
    time.sleep(_time)
    print(stream())

# break
run(2)
print('Run 2 - break proccess 5 and start 4')
time.sleep(3)

# vfy 1:1
run(4, 'MyTemplate')
for i in range(5):
    time.sleep(_time)
    print(stream())

removeDatabase()

# Close
run(0)
print('FINISH ...')
