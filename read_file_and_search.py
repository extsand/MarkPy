#Обработка файла и поиск данных в нем
from os import read


f = open('names.txt', 'r')
names = []
names.append(f.read().split("\n"))
# print(names[0][4])
find = 'Ruby'

def foundMatch(search, list):
	for item in list:
		partOf = item.split(' ')
		# print(len(partOf))
		if len(partOf) > 1:
			# print(partOf)
			if item == search or partOf[0] == search or partOf[1] == search:
				print(f'We have match {item}')



foundMatch(find, names[0])




