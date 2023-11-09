
import random
nome = input("Coloque seu nome: ")
hp = 10
ataque = 3
exp = 1.0
defesa = 2.3
inventario = ["pocao"]
monstros = {
    "goblin": 10,
    "slime": 4
}
itens = ["espada", "pocao", "escudo"]

def item_drop():
    if monstros[escolha] > 0:
        inventario.append(random.choice(itens))

print("Bem-vindo ao meu RPG!")
print("Comandos:")
print("batalhar, inventario, status, comandos, sair")

while True:
    comando = input("Comando: ")

    if comando == "batalhar":
        escolha = random.choice(list(monstros.keys()))
        print("Um", escolha, "selvagem apareceu!")
        print("HP:", monstros[escolha])
        
        while True:
            comando = input("Comando (ataque/defesa/fujir): ")
            
            if comando == "ataque":
                monstros[escolha] -= ataque
                print("Inimigo com", monstros[escolha], "HP.")
                if monstros[escolha] <= 0:
                    print("Você derrotou o", escolha)
                    exp += 0.5  # Ganha experiência
                    print("Seu status!")
                    print("Nome:", nome)
                    print("HP:", hp)
                    print("Ataque:", ataque)
                    print("Experiência:", exp)
                    print("Defesa:", defesa)
                    item_drop()
                    break
                hp -= monstros[escolha]
                print("Seu HP:", hp)

            elif comando == "defesa":
                hp += defesa
                print("Seu HP:", hp)

            elif comando == "fujir":
                print("Você fugiu da batalha.")
                break

    elif comando == "inventario":
        while True:
            print("Inventário:", inventario)
            comando = input("Comando: ")
            if comando == "usar":
                item = input("Item: ")
                print(inventario)

                if item == "pocao":
                    hp += 5
                elif item == "escudo":
                    defesa += 4
                elif item == "espada":
                    ataque += 3

            elif comando == "sair":
                break

    elif comando == "status":
        print("Nome:", nome)
        print("HP:", hp)
        print("Ataque:", ataque)
        print("Experiência:", exp)
        print("Defesa:", defesa)

    elif comando == "comandos":
        print("cancela, batalhar, inventario, status, comandos, sair")

    elif comando == "sair":
        break
