# class Person:
#     def __init__(self, name, gender, age, study, work):
#         self.name = name
#         self.gender = gender
#         self.age = age
#         self.study = study
#         self.work = work
# id_1 = Person('Вася','муж.', 18, 'колледж', 'доставка')
# id_2 = Person('Ярослав','муж.', 28, 'универ', 'сварщик')
# id_3 = Person('Мажа','жен.', 23, 'колледж', 'кассир')
#
# print(id_1.__dict__)                    #на выходе словарь


# class Person:
#     def __init__(self, music, film, what, ufo, ID):
#         self.music = music
#         self.film = film
#         self.what = what
#         self.ufo = ufo
#         self.ID = ID
# id_1 = Person('Rock','OdinDoma','file','Yes',15234451)
# id_2 = Person('Pop','GarryPotter','game','Yes',23414451)
# id_3 = Person('Shanson','Simson','text','No',15323212)
#
# print(id_1.__dict__)
# print(id_2.__dict__)
# print(id_3.__dict__)
#
# print(f"Музыка 1 персоны --- {id_1.music}")
# print(f"Что кодим? -- {id_2.what}")
# print(f"Ваш ID -- {id_3.ID} и ты веришь в НЛО ? -- {id_3.ufo}")


"""
Функции для работы с атрибутами
setattr - создание атрибута или изменение его
getattr - получение значения атрибута
hasattr - проверка наличие атрибута
delattr - удаление атрибута
"""

#setattr

# class Person:
#     pass
#
# id_1 = Person()
# setattr(id_1, "name", "Кирилл")                     #создали атрибут
# setattr(id_1, "name", "Женя")                       #изменили атрибут
# id_1.name = "Артем"                                 #изменили значение атрибут 2 вариант
#
# print(id_1.__dict__)

# file = {'name':'Alex', 'age':18, 'hobby':'films'}
# class Person:
#     pass
# id_1 = Person()
# for key, value in file.items():             #через цикл записали все ключ+значение
#     setattr(id_1, key, value)
# print(id_1.hobby)
# print(id_1.__dict__)
# print(id_1.name)                        #обращаемся к ключу и получаем значение


# class Person:
#     pass
# id_1 = Person()                             #создали экземпляр
# setattr(id_1,"name", "Vasya")
# setattr(id_1,"name", "Masha")
# print(id_1.name)
# print(id_1.__dict__)

# class Person:
#     setup = ['set_name', 'set_age', 'set_work', 'set_study']
# id_1 = Person()
# for i in Person.setup:
#     setattr(id_1,i,input())
# print(id_1.__dict__)
#
# #2 способ
# for attribute in id_1.setup:
#     value = input()
#     setattr(id_1, attribute, value)
# print(id_1.__dict__)
#
# #получение значения(проверка)
# for value in id_1.setup:
#     print(getattr(id_1,value))              #получаем значение атрибута

#getattr

# class Person:
#     name = 'Вася'
#     age = 14
# person_1 = Person()
# print(getattr(person_1, 'name', False))
# print(getattr(person_1, 'birth', 'Нет атрибута'))
# print(getattr(person_1, 'birth'))               #нету 3 значения и будет ошибка


# file = ['name', 'age', 'hobby', 'lolo']
# class Person:
#     hobby = 'films'
#
# for value in file:
#     if getattr(Person, value, False):
#         print(value)

# Masha Prosto Kvasha Мы любим тебя --- проверяем правильно ли
# class Person:
#     name1= 'Masha'
#     name2= 'Prosto'
#     name3= 'Kvasha'
# list_person = []
# file = ['name1','name2','name3','name4']
# for value in file:
#     list_person.append(getattr(Person, value, 'Мы любим тебя'))
# print(list_person)

# class Person:
#     dance = ['nnn', 'mmm', 'ccc']
#
# id_1 = Person()
# for value in id_1.dance:
#     if getattr(Person, value, True):
#         print(value)
#
#
# list_person = ['hobby', 'work', 'study']
# class Person:
#     hobby = 'dance'
#     work = 'design'
#     study = 'collage'
# id_1 = Person()
#
# print(getattr(id_1,'hobby'))
# print(getattr(id_1,'work'))
# print(getattr(id_1,'study'))

# from random import sample
# magic_ing = ['вино', 'вода', 'масло', 'вишня', 'творог', 'колбаса']
# class Magic:
#     ingredients = sample(magic_ing,3)
# my_cocktail = Magic()
# for value in my_cocktail.ingredients:
#     getattr(my_cocktail, 'ingredients')
#     print(value)
# print('Спасибо, Машенька')


#hasattr

# class Person:
#     name = 'Vasya'
# id_1 = Person()
# print(hasattr(Person, 'name'))                      #True
# print(hasattr(id_1, 'name'))                        #True
# print(hasattr(id_1, 'age'))                         #False

class Pokemon:
    pass
pokemons = Pokemon()
setattr(pokemons,"pikachu", "")
setattr(pokemons,"scyther", "")
setattr(pokemons,"gyarados", "")
setattr(pokemons,"gengar", "")

print(hasattr(pokemons,'lapras'))
print(hasattr(pokemons,'pikachu'))
print(hasattr(pokemons,'alakazam'))