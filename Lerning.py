import random

PlayerOne = "Анна"
PlayerTwo = "Алекс"

AnnaScore = 0
AlexScore = 0

# У каждого кубика шесть возможных значений
diceOne = [1, 2, 3, 4, 5, 6]
diceTwo = [1, 2, 3, 4, 5, 6]


def playDiceGame():
    """Оба участника, Анна и Алекс, бросают кубик, используя метод shuffle"""

    for i in range(5):
        # оба кубика встряхиваются 5 раз
        random.shuffle(diceOne)
        random.shuffle(diceTwo)
    firstNumber = random.choice(diceOne)  # использование метода choice для выбора случайного значения
    SecondNumber = random.choice(diceTwo)
    return firstNumber + SecondNumber


print("Игра в кости использует модуль random\n")

# Давайте сыграем в кости три раза
for i in range(3):
    # определим, кто будет бросать кости первым
    AlexTossNumber = random.randint(1, 100)  # генерация случайного числа от 1 до 100, включая 100
    AnnaTossNumber = random.randrange(1, 101, 1)  # генерация случайного числа от 1 до 100, не включая 101

    if (AlexTossNumber > AnnaTossNumber):
        print("Алекс выиграл жеребьевку.")
        AlexScore = playDiceGame()
        AnnaScore = playDiceGame()
    else:
        print("Анна выиграла жеребьевку.")
        AnnaScore = playDiceGame()
        AlexScore = playDiceGame()

    if (AlexScore > AnnaScore):
        print("Алекс выиграл игру в кости. Финальный счет Алекса:", AlexScore, "Финальный счет Анны:", AnnaScore, "\n")
    else:
        print("Анна выиграла игру в кости. Финальный счет Анны:", AnnaScore, "Финальный счет Алекса:", AlexScore, "\n")