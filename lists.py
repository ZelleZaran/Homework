#Удалить из списка №1 элементы, встречающиеся в списке №2



listik1 = [7,7,8,9,5,4,3,6,7]
listik2 = [7,2,1,3,11]

new_listik = [i for i in listik1 if i not in listik2]
print(new_listik)
