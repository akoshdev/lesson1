i = int(input('Vvedite chislo uchastnikov: '))
members = []

# if i.isdiggit():
while i > 0:
    result = input('Kto zanyal {}: '.format(i))
    members.append(result)
    i -= 1
# else:
#     print('Vvedite chislo')

members.reverse()
resultt = members[:3]

for n in resultt:
    print('Pobiditel {} mesto poluchil:  {} Pozdravlaym!'.format(i,n))
