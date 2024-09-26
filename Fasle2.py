#import math
#import math
# print(math.sin(0.6))

#-----------------------------
#import random
# import random
# print(random.randint(1, 10))
#----------------------------
#random in the list
# import random
# t = [10, 11, 54, 88, 9]
# print(random.choice(t))
#----------------------------
#function
# pre_hour = input('meghdar daryafti dar saaat ra vared konid : ')
# pre_hour = int(pre_hour)
# hour = input('saat karee khod ra vared konid : ')
# hour = int(hour)
# def daryafti(pre_hour, hour):
#     if hour > 8 and pre_hour > 100:
#         return 'oh Erroor'
#     else:
#         daryaft = pre_hour * hour
#         return daryaft
# print(daryafti(pre_hour, hour))

#-----------------------------
#function

# def Hi():
#     print('salam chetori???')

# Hi()

#----------------------------
#function

# def hi(name):
#     print('salam',name ,'chetori?',)
    
# hi('Abbas')

#-----------------------------
#function

# def jam(a, b):
#     javab = a + b
#     return javab
# print(jam(5, 3))

#-----------------------------
#function

# def jam(a, b):
#     javab = a + b
#     return javab
# adade_aval = 10
# adade_dovom = 15
# jam_2_adad =jam(adade_aval, adade_dovom)
# print(jam_2_adad)

#-----------------------------
#function

# def salary(h, w):
#     pre = h * w
#     return pre
# hours = input('How many hours did you work per month?')
# hours = int(hours)
# wege = input('How much is the hourly wage?')
# wege = int(wege)
# daryaft = salary(hours, wege)
# print(daryaft)

#-----------------------------
#function

# def salary(hours, wega):
#     if hours <= 8:
#         return 'Error going to office'
#     elif hours >=10:
#         return 'Error hour > 10 repet'
#     else:
#         daryaft = hours * wega
#         return daryaft
# h = input('saate kareto vared kon:')
# h = int(h)
# w = input('dast mozdeto vared kon:')
# w =int(w)
# per = salary(h, w)
# print(per, 'meghdar daryafti')

#------------------------------
#itraction while

# n = 15 
# while n > 5 :
#     print(n)
#     n -= 1

#------------------------------
#itraction while

# name = input('what is your name ?')
# while name != 'end':
#     print('salam',name,'chetori??')
#     name = input('what is your name ?')
    
#-----------------------------
#itraction and break while

# n = 3 
# while n >=0:
#     print(n)
#     n += 1
#     if n == 100:
#         print('resid be 100')
#         break
# print('end loop')

#-----------------------------
#intraction while continue

# i = 0
# while i < 6:
#     print(i)
#     i +=1
#     if i == 3:
#         print('resid be 3')
#         continue
# print(i)

#-----------------------------
#itration for 

# for i in range(1, 10):
#     print(i , i * 2)

#----------------------------
#itration for

# for i in range(1, 20):
#     print(i , i *i)
#     if i == 11:
#         print('resid be 11')
#         break
    
#---------------------------
#itration for

# ferends =['abbas', 'faezeh', 'mahoor']
# count = 0
# for i in ferends:
#     print('salam', i)
#     count +=1
# print(count)
#---------------------------
# intration for
    
# count = 0
# for itervar in [3, 41, 12, 9, 74, 15]:
#     count = count + 1
#     print('Count: ', count)
    
#---------------------------
#practice

# count =0
# sum = 0
# num = input('Enter your number :')
# num = int(num)
# while num != -1: 
#     count += 1
#     sum += num  #===>> sum = sum + num
#     num = input('Enter your number :')
#     num = int(num)
# print('tedade adade vared shode',count)
# print('jame adadi ke vared Kardeim',sum)
# print('miyangin:', sum / count)
#--------------------------

# num = input('what is your number ? ')
# num = int(num)
# tedad = 0
# jam = 0
# while num != -1:
#     num = input('what is your number ? ')
#     num = int(num)
#     tedad += 1
#     jam += num
    
# miyangin = jam / tedad
# if miyangin % 2 == 0:
#     print('adad zoj hastesh',miyangin)
# else:
#     print('adad fard hastesh',miyangin)

# print(tedad,'adad vared shode',jam,'jame adad','miyangin',miyangin )

#---------------------------
#Hads number

# import random
# javab = random.randint(1, 100)
# name = input('what is your name ? \n')
# print(name,'welcom to Game Hads(beyne 0, 100):')
# hads = input('what is your hads : ')
# hads= int(hads)
# count = 0
# while hads != javab:
#     if hads > javab:
#         print('hads bozorg tar az javab hastesh')
#     else:
#         print('hads kochik tar az javab hastesh')
#     count += 1
#     hads = input('what is your hads : ')
#     hads= int(hads)
    
# print('you did it', name)
# print(count,'bar natonestin javab ra bedahin')

#----------------------------
#bar akse hads Eshtebah vali nazdik

# import random

# hads = random.randint(0, 100)
# print(hads)
# keys = input('Enter User ID : \n 1 = adadet kochik tare \n 2 = adadet bozorg tare \n 3 = you did it \n :')
# keys = int(keys)

# while keys == 3:
#     if keys == 1:
#         print('adadet kochik tare boro bala')    
#     elif keys == 2:
#         print('aadet bozorg tare boro pain')
#     else:
#         print('Error')
    
     
#----------------------------
#tamrine bar aks kardane tamrin hads Chat GPT


# def guess_number():

#     low = 0

#     high = 100

#     feedback = ''
    
    

#     print("لطفا یک عدد بین ۰ تا ۱۰۰ در ذهن خود داشته باشید و به من بگویید که آیا عددی که من حدس میزنم بزرگتر، کوچکتر یا درست است.")



#     while feedback != 'd':

#         guess = (low + high) // 2

#         feedback = input(f"آیا عدد {guess} درست است (d)، بزرگتر است (b)، یا کوچکتر است (k)؟ ").lower()

        

#         if feedback == 'b':

#             low = guess + 1

#         elif feedback == 'k':

#             high = guess - 1

#         elif feedback != 'd':

#             print("لطفا فقط 'd'، 'b' یا 'k' را وارد کنید.")



#     print(f"آفرین! عدد شما {guess} بود.")



# if __name__ == "__main__":

#     guess_number()


#------------------------------
#intraction continue

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     print('resid  be 3')
#     continue
#   print(i)

#-----------------------------
#intraction breack

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     print('resid  be 3')
#     break
#   print(i)
#------------------------------
#intraction else

# i = 10
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

#---------------------------------
#practic fanction


# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
#-----------------------------------






































































