
from random import seed
from random import randint

start = input("Deseja jogar uma partida de blackjack? y/n : ")

if(start == "y"):
    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

    def deal_card():

        value = randint(0,12)
        card = cards[value]
        return card

    user_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    cartas_usuario = 2

    computer_cards = []
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    cartas_computador = 2

    print("User: [" + str(user_cards[0]) + ", " + str(user_cards[1]) + "]")
    print("Computer: [" + str(computer_cards[0]) + ", " + "?" + "]")

    def calculate_score(isUser, qtde):

        result = 0

        if(isUser == 1):
            for i in range(qtde):
                if(user_cards[i] == 'A'):
                    if(result + 11 > 21):
                        result += 1
                    else:
                        result += 11
                elif(user_cards[i] == 'J'):
                    result += 10
                elif(user_cards[i] == 'Q'):
                    result += 10
                elif(user_cards[i] == 'K'):
                    result += 10
                else:
                    result += user_cards[i]

        else:
            for i in range(qtde):
                if(computer_cards[i] == 'A'):
                    result += 11
                elif(computer_cards[i] == 'J'):
                    result += 10
                elif(computer_cards[i] == 'Q'):
                    result += 10
                elif(computer_cards[i] == 'K'):
                    result += 10
                else:
                    result += computer_cards[i]

        if(qtde == 2 and result == 21):
            return 0
        else:
            return result

outra = "y"
pontos_usuario = calculate_score(1, cartas_usuario)
if(pontos_usuario == 0):
    print("Blackjack! user wins")
    exit()
pontos_computador = calculate_score(0, cartas_computador)
if(pontos_computador == 0):
    print("Blackjack! Dealer wins")
    exit()
while(calculate_score(1, cartas_usuario) < 21 and outra != "n"):

    outra = input("deseja tirar outra carta? y/n : ")

    if(outra == "y"):
        user_cards.append(deal_card())
        cartas_usuario += 1
        index = cartas_usuario - 1
        print(user_cards[index])
        calculate_score(1, cartas_usuario)
    else:
        pontos_usuario = calculate_score(1, cartas_usuario)
        pontos_computador = calculate_score(0, cartas_computador)

        if(pontos_usuario <= 21 and pontos_usuario > pontos_computador):
            print("User: " + str(pontos_usuario) + " points")
            print("Dealer: " + str(pontos_computador) + " points")
            print("user wins")
        elif(pontos_usuario > 21):
            print("User: " + str(pontos_usuario) + " points")
            print("Dealer: " + str(pontos_computador) + " points")
            print("dealer wins")
        elif(pontos_usuario == pontos_computador):
            print("User: " + str(pontos_usuario) + " points")
            print("Dealer: " + str(pontos_computador) + " points")
            print("Draw")

if(calculate_score(1, cartas_usuario) > 21):
    print("User: " + str(pontos_usuario) + " points")
    print("Dealer: " + str(pontos_computador) + " points")
    print("Dealer wins")

