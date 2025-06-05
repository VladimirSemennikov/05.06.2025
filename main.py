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

class Person:
    name = 'Вася'
    age = 14
person_1 = Person()
print(getattr(person_1, 'name', False))