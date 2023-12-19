lang = 'Python'
if lang == 'Python':
    print("Hello")
print('end')

def get_type_of_sentence(sentence):
    last = sentence[-1]

    if last =='?':
        sentence_type = 'question'
    else:
        sentence_type = 'normal'
    return "Sentence is " + sentence_type
print(get_type_of_sentence('Sentence'))
print(get_type_of_sentence('Sentence?'))

def user_number(user_data):
    permit_print = True

    if permit_print and user_data ==-6:
        print('Число = -6')
    elif permit_print and user_data > 0:
        print('Число положительное')
    elif not permit_print:
        print('Печать запрещена')

user_number(-6)
user_number(10)

def degree(courseNumber):
    if courseNumber > 0 and courseNumber <5:
        return "бакалавр"
    elif courseNumber > 4 and courseNumber < 7:
        return 'магистр'
    elif courseNumber > 6 and courseNumber < 10:
        return 'аспирант'
    else:
        return 'Введите корректный год обучения'

print(degree(5))
print(degree(-1))
print(degree((7.5)))


