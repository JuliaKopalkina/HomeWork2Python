# Реализуйте алгоритм перемешивания списка.
import random

MixList = [1,2,3,4]
print('Начальный список:'+str(MixList))
for i in range (len(MixList)-1,0,-1):
    j = random.randint(0,i+1)
    MixList[i],MixList[j] = MixList[j],MixList[i]
print('Перемешаный список:'+str(MixList)) 
