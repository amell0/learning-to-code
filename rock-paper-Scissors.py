print("You only get to choose rock, paper or scissors")
choices = ["rock", "paper", "scissors"]
p1score, p2score = 0, 0
j = int(input("Enter the number of rounds you wanna play: "))
i = 1

while i <= j:
    p1 = input("Player 1: Enter rock/paper/scissors or quit: ").lower()
    p2 = input("Player 2: Enter rock/paper/scissors or quit: ").lower()

    if p1 == "quit" or p2 == "quit":
        break
    if p1 not in choices or p2 not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue
    
    match(p1, p2):
        case("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            print("Player one wins!")
            p1score += 1
        case("scissors", "rock") | ("rock", "paper") | ("paper", "scissors"):
            print("Player two wins!")
            p2score += 1
        case _: 
            print("tie!")
    i += 1

print(f"The first player's score is {p1score} and the second player's score is {p2score}")
 
