salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Salário anterior R${:.2f} Salário reajustado R${:.2f}'.format(salario, novo))