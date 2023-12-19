number =  0

while number <10:
    print(f'number = {number}')
    number += 1
print("app close")

string = ''
while len(string) >0:
    print('Строка существует - ' + string)
    string = string[0:len(string) - 1]
else:
    print('пустая строка')

def cycle_for(items):
    for item in items:
        print(item)

cycle_for('string')
cycle_for([0, 1, 2])
cycle_for(('a', 'b', 'c'))


def summ(list):
    return sum(list)
print(summ([1, 2, 3]))
print(max('abcd'))

numb_break = 0
while numb_break < 5:
    numb_break+=1
    if numb_break ==3:
        break
    print(f"number = {numb_break}")

numb_continue = 0
while numb_continue < 5:
    if numb_continue == 3:
        continue
    print(f"number = {numb_continue}")

