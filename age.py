print ('Добрый день!')
print ('Введите ваш возраст')
age = int(input())

def WorkerAge (age):
    if 0 < age < 7: 
        return "Вы учитесь в детском саду"
    elif 7 < age < 16: 
        return 'Вы учитесь в школе'
    elif 16 < age < 22:
        return 'Вы учитесь в вузе'
    elif age > 22:
        return 'Вы должны работать'

a = WorkerAge(age)
print (a)