# Основной источник

# https://www.w3schools.com/python

# Привет!
# Это простой набор заданий для выполнения.
# Выполнять можно в любой последовательности.
# Но я бы рекомендовал, чтобы все делалось по порядку и
# с внимательным изучением источника

# Как выполнять?
# На каждой строке есть вопрос. Ответь на этот вопрос в простой форме.
# Закоментируй вопрос.
# Если есть задание с кодом - напиши код.
# После выпосления - закоментируй код и приступай к выполнению следующего задания.
# -----------------------------------------------------------------------------------

# 1. Какие бывают переменные в питоне? Напиши пример в коде.
# 1. Обычные  выходные и глобальные
print('question1'.upper())
x = 20
y = 10
z = 23
print(x + y )
x , y,z=1,46,77
print(x)
print(y)
print(z)
name = ('Mark')
surname = ('Koval')
fullname = name + ' ' + surname
print(fullname)
print('_______________end------------')
# 2. Какие бывают типы данных в питоне? Напиши пример в коде.
# что такое метод? Что такое функция?
# 2. разные : str int range list и остальные
#
print('question2'.upper())
x= 1      #int
x_=2.1    #float
X=('htht')   #str
x_x=['jtj','elgeh','drhdrh']                #list
xx_ =('rhrrj','tjjtvnvbm','cvncncn')        #tuple
print(type(x))   #nex pin
print(type(x_))
print(type(X))
print(type(x_x))
print(type(xx_))
print('_______________end------------')
# 3. Покажи пример чисел. Как они объявляются?
print('question3'.upper())
x= 1 #number
x_=2.3  #number
x_x= 2e2
print(x)
print(x_)
print(x-x)
print('_______________end------------')
# 4. Есть такая штука как Casting. Еще её назыают преобразование типов. Покажи пример.
print('question4'.upper())
x=str('1tht')
x_= float(4)
x_x=int(3.9)
print(x)
print(x_)
print(x_x)
print('_______________end------------')
# 5. Что такое строки? Выведи мне строку.
print('question5'.upper())
a = "hello"
b = 'hello'  #а и b одно и тоже
print(a)
print(b)
print('_______________end------------')
# ВСЕ Я СПАТЬ (28.09.2021  0:30)
# 6. Нареж одну строку на две.
print('question6'.upper())
x='hell worl!'
print(x[:3])   #не до конца понял но вроде так
print(x[-5:])
print(x[0:4])
# Покажи пример Slicins #показал вроде
print('_______________end------------')
# Раскоментируй код ниже, допиши его, проверь и закоментируй вновь.
text = 'Hello, Mark!'  # переменная  text значит привет марк
print(text)
if 'Hello, Mark!' in text:     # если Саша говорит привет марк ,тогда марк говорит привет Саша
    print('hello to you, Sasha!!')
# 7. Сделай в строке все буквы заглавными.
print('question7'.upper())
# Upper Case
a = 'hello'
print(a.upper())
# Lower Case
b = 'Sasha!'
print(b.lower())
c = a + ' ' + b
print(c.title())
print('_______________end------------')
# 8. Раздели строку на две и помести в Lists.
print('question8'.upper())
text = 'Hello Sasha!'
a = text[0:4]
b = text[5:]
thislist = [a,b]
print(thislist)
# Split String
# 9. Собери строку в одну. Покажи пример
# Конкатенация
print('question9'.upper())
a = 'Мое имя'
b = 'Маpk'
c = a+' '+b
print(c)
print('_______________end------------')
# 10. Формат что строки это и как работает?
print('question10'.upper())
# это тип данных строки его можно менять и если ты сам не назначиш формат он выставиться автоматичеки
# Строка формата
# Покажи пример
a = 1
a =1.0
a ='one'
a = ['o','n','e']
#name = 'Марк'
#профессия = 'студент'
#mySpec = "Привет, меня зовут {}, меня зовут {}"
