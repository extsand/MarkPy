# Обработка файла и поиск данных

f = open('resources/names.db', 'r')
names = []
names.append(f.read().split("\n"))
# print(names[0][4])
find = 'Ruby'

def foundMatch(search, lists):
    for item in lists:
        part_of = item.split(' ')
        # print(len(partOf))
        if len(part_of) > 1:
            # print(partOf)
            if item == search or part_of[0] == search or part_of[1] == search:
                print(f'We have match {item}')

foundMatch(find, names[0])

