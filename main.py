# VALIDATE CPF :)

cpf = input('Hello my friend :) \nSend you cpf for validate: ')

cpfIsValid = True if cpf.find('-') and len(cpf.replace('.', '').replace('-', '')) == 11 else False
if cpfIsValid:
    cpfPart, *rest = cpf.replace('.', '').split('-')
    cpf = cpf.replace('.', '').replace('-', '')
    newCpf = cpfPart
    part1Cpf = list(cpfPart)
    part2Cpf = list(cpfPart)
    digitOne = 0
    digitTwo = 0
    firstColumn = 0
    secondColumn = 0
    for index, value in enumerate(range(10, 1, -1)):
        firstColumn += value * int(part1Cpf[index])
    else:
        result = 11 - (firstColumn % 11)
        digitOne = 0 if result >= 9 else result
        part2Cpf += str(digitOne)
    for index, value in enumerate(range(11, 1, -1)):
        secondColumn += value * int(part2Cpf[index])
    else:
        resultTwo = 11 - (secondColumn % 11)
        digitTwo = resultTwo if resultTwo <= 9 else 0

    newCpf += str(digitOne)
    newCpf += str(digitTwo)

    msg = 'Yesss!! :)\nYou cpf is valid' if newCpf == cpf else 'Ohh :( cpf invalid'
    print(msg)
else:
    print('Cpf invalid')
