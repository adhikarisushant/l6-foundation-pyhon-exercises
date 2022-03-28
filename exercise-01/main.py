list1 =['ram', 'laxman', 'bharat', 1992]
print(list1[0])
print(list1[-1])
print(list1[1:3])
print(list1)
list1[-1]='dasarath'
print(list1)

#         print stars for representing numbers
# list1 = [6, 2, 6, 2, 6, 5]

# for i in list1:
#     stri = ''
#     for j in range(i):
#         stri = stri + 'x'
#         print(stri)

#         calculate the cordinate of a square
# for x in range(2):
#     for y in range(2):
#         i=int(input('enter x cordinate: '))
#         j=int(input('enter y cordinate: '))
#         print(i, j)





#         calculate sum of array using for loop
# sum = 0
# for i in [1000, 2000, 3000, 2500]:
#     sum = sum + i;    
# print(f'sum: {sum}')




#             Car Start Stop Program using while loop
# command = ''
# start_status = False
# stop_status = False
# while True:
#     command = input('enter the command: ')
#     if command == 'start':
#         if start_status == True:
#             print('car has been already started!!!')
#         else:
#             print('car started!!!')
#             start_status = True

#     elif command == 'stop':
#         if not start_status:
#             print('car has already stopped!!!')
#         else:
#             print('car has stopped!!!')
#             start_status = False

#     elif command == 'help':
#         print('''
#             start - car started
#             stop - car stopped
#             quit - terminate the program
#         ''')
#     elif command == 'quit':
#         print('terminate the program')
#         break
#     else:
#         print('Invalid command!!!')