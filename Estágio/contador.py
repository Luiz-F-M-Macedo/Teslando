def read(msg):
    """Garante que o usuário digite apenas números inteiros"""
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Erro: Digite apenas números inteiros!")

initial = read("Digite o número inicial: ")
end = read("Digite o número final: ")

while True:
    increment = read("Digite o incremento (não pode ser 0): ")
    if increment != 0:
        break
    print("O passo não pode ser zero!")


if initial > end and increment > 0:
    print("Aviso: Como o início é maior que o fim, o passo foi invertido para negativo.")
    increment = -increment

corrected_end = end + 1 if increment > 0 else end - 1

for i in range(initial, corrected_end, increment):
    print(i)
