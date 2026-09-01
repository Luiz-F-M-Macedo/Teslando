def read(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite apenas números inteiros!")

initial = read("Digite o número inicial: ")
end = read("Digite o número final: ")

while True:
    increment = read("Digite o incremento (não pode ser 0): ")
    if increment != 0:
        break
    print("O incremento não pode ser zero!")

if initial > end and increment > 0:
    print("O início não pode ser maior que o final se o incremento for maior que zero")
if initial < end and increment < 0:
    print("O início não pode ser menor que o final se o incremento for menor que zero")

""" if initial > end and increment > 0:
    print("Como o início é maior que o fim e o incremento positivo, o incremento foi invertido para negativo.")
    increment = -increment

if initial < end and increment < 0:
    print("Como o início é menor que o fim e o incremento é negativo, o incremento foi invertido para positivo.")
    increment = -increment """

corrected_end = end + 1 if increment > 0 else end - 1

for i in range(initial, corrected_end, increment):
    print(i)