# len, []  

# a = 'salam'
# print(len(a), a[4])

# ---------------------
# loop string

# 1 a ='salam khobi'
# tool =len(a)
# for i in range(0, tool):
#     print(i, a[i])

# ---------------------
# 2 loop string

# a = 'salam chetori'
# for i in range(0, len(a)):
#     print(a[i])
    
# ----------------------
# 3 loop string
# for letter in 'salam chetori?':
#     print(letter)
    
# -----------------------
# 4 loop string
# string = 'salam chetori'
# count =0
# for letter in string:
#     if letter == 'm':
#         count += 1
# print(count)

# -----------------------
# string  slice and Methood class s

# s = 'salam Abbas chetor? Faezeh khobe?     a    '
# # print(len(s))
# # for i in range(0, len(s)):
# #     print(i, s[i])
# print(s[20:33])
# print(s[20:])
# print(s[:20])
# print(s.upper(),'upper')
# print(s.lower(),'lower')
# print(s.count('a'),'count')
# print(s.startswith('a'),'startswhite')
# print(s.startswith('s'),'startswhite')
# print(s.split(),'split')
# print(s.strip(),'strip')
# print('Helpe=====>>>',dir(s))


# ----------------------

# %s and % print

# name = 'abbas'
# sen = 31
# print('salam %s chetori to %s salete' % (name, sen))
# print('salam %s %i sale'%(name,sen))

# ----------------------
# list methood

# l = [1, 3, 4,]
# #print(dir(l))
# print(l)

# l.append(100)
# print(l)

# l.extend([1, 88, 7])
# print(l)

# del l [3]
# print(l)

# ---------------------
# convert list to string and string to list

# srting = 'abbas salam halet chetore'

# l = srting.split()
# print(l, 'type l',type(l))

# s = ' '.join(l)
# print(s)



# -------------------------
# miyangin ba estefade az sum va len

# l = [100, 23, 4, 50]
# print(sum(l))
# print(sum(l) / len(l))


# ---------------------
# Dictionary
# dic 1

# f2e = dict()
# print(type(f2e))

# f2e['yek'] = 'one'
# f2e['do'] = 'tow'
# f2e['se'] = 'three'
# print(f2e)


# ---------------------
# Dictionary len methood
# dic 2

# f2e = {'yek': 'one', 'do': 'tow', 'se':'tree', 'char' : 'four'}
# print(type(f2e))
# print(f2e)
# print(len(f2e))
# print(f2e.keys())
# print(f2e.values())
# print(list(f2e.keys()))
# print(list(f2e.values()))

# --------------------
# bar nameye peyda kardane alef ba Esey

# string = 'salam abbas halet chetore?'
# counter = dict()
# for letter in string:
#     # print(letter)
#     if letter in counter:
#         counter[letter] += 1
#     else:
#         counter[letter] = 1
#     #print(letter, counter)
    
# for this_one in list(counter.keys()):
#     print('%s ,appeared %s time '%(this_one, counter[this_one]))
    
# --------------------
#bar nameye peyda kardane alef ba Hard

# string = 'salam abbas halet chetore?'
# counter = dict()
# for letter in string:
#     counter[letter] = counter.get(letter, 0) + 1
    
    
# for this_one in list(counter.keys()):
#     print('%s ,appeared %s time '%(this_one, counter[this_one]))






# --------------------
# Tupel

# --------------------

# s = 'salam jafar haley chetore'
# count = 0
# for i in s:
#     if i == 'a':
#         count = count + 1
    
# print(count)

# -------------------
#tamrine fogholade az zehne khodam

# num = input('what is your number ??')
# num = int(num)
# l = []
# count = 0
# while num != -1:
#     l.append(num)
#     num = input('what is your number ??')
#     num = int(num)
    
# jam = sum(l)
# tedad =len(l)
# print('jame adade vared shode %s adade vared shode %s ' % (jam,tedad))
# miyangin = jam / tedad
# print(miyangin)

#--------------------------
#book python for evry body

# fruit = 'banana'

# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index = index + 1


# for i in fruit:
#     print(i)
#--------------------------
#tamrine ketab 

# total = 0
# count = 0
# while (True):
#     inp = input('Enter a number: ')
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1
# average = total / count
# print('Average:', average)






























































