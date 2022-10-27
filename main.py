# comando input(), permitir que o usuario digite algo

nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

print (f"Seu nome é {nome} e sua idade é {idade} anos")
#comando de saida..exibir na tela
print(f"Boa noite, seu nome é {nome}")
#exiba ¨sua idade é ...¨

print("sua idade é {}".format (idade))
#se eu quisesse mostrar o DOBRO da idade informada?
dobro = idade * 2
print("O dobro da idade informada é {}".format(dobro))
#Estrutura condicional - o famoso "SE" (if)
#Se a pessoa for maior de idade, ótimo! ja pode beber ou dirigir"
if idade >= 18:
  print("vc é maior de idade, ótimo! ja pode beber ou dirigir")