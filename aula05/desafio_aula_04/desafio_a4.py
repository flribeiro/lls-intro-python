from pessoa import Pessoa

pessoa_1 = Pessoa('Frederico Trajano', 42, 75.5, 1.74)
pessoa_2 = Pessoa('Josiane da Silva', 18, 62.2, 1.68)

pessoa_2.envelhecer()
pessoa_1.engordar(0.5)
pessoa_2.emagrecer(1)
pessoa_2.envelhecer()

print(pessoa_1)
print(pessoa_2)