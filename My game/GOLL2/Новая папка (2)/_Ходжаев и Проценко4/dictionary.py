# В программе используется структура данных Словарь (Dictionary)
# Словарь отличается от обычного массива тем, что его элементы
# обозначаются не номером, а словом (ключом).
# Словари можно заполнять двумя способами:

schooler = {}
schooler['name']  	     = 'Sasha'
schooler['age']   	     = 16
schooler['average_mark'] = 4.4

print(schooler)

game = {'genre'      : 'platformer',
  		  'name'   	   : 'PacMan',
  		  'best_score' : 255}

print(game)

# game.keys() возвращает список всех ключей

for key in game.keys():
    print(key)