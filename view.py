# Консоль для выбора чисел 1- Комплексные, 2 - рациональные числа .
#  Затем ввод 1 первого числа , ввод 2 числа,  ввод знака +-*/
# ( затем можно сделать кнопки)

#def view_data(data, title): # посчитанные данные с блоков
#    print(f'{title} = {data}')

def input_data():
    type = input('С какими числами будем работать? 1 -комплексные числа, 2 - рациональные числа')
    if type == '1':
        a = input('Введите первое число (используйте формат: "5 + 3j"):')
        b = input('Введите второе число (используйте формат: "5 + 3j"):')
        operand = input('Выберите операцию:')

    elif type == '2':
        a = input('Введите первое число (используйте формат: "5/11"):')
        b = input('Введите второе число (используйте формат: "5/11"):')
        operand = input('Выберите операцию:')

    return (type, a, operand, b) # данные передаются в блок расчёта чисел