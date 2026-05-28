# list and list operations 

# indexing in list

task = ['eat', 'sleep', 'code', 'repeat']
print("Before append:", task)

task.append('fun')
print("After append:", task)

for i in task:
    print(i)
    if i == 'eat':
        print("sleep well")
    elif i == 'code':
        print("code well")
    elif i == 'fun':
        print("have fun")
    else:
        print("repeat well")

#task:

task.clear()
print("After clear:", task)

task.copy()
print("After copy:", task)

task.count('eat')
print("After count:", task.count('eat'))

task.extend(['eat', 'sleep', 'code', 'repeat'])
print("After extend:", task)

task.index('code')
print("After index:", task.index('code'))

task.insert(2, 'think well before you code')
print("After insert:", task)

task.pop()
print("After pop:", task)

task.remove('eat')
print("After remove:", task)

task.reverse()
print("After reverse:", task)

task.sort()
print("After sort:", task)

