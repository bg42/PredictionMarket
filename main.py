from market_classes import Market

if __name__ == "__main__":
    market = Market()


print("Welcome to Prediction Exchange! What would you like to do?")

menuFlag = True

while menuFlag:
    print("1. Log In")
    print("2. New Account")
    print("3. New Prediction")
    print("4. Resolve Existing Prediction")
    print("5. Account Standings")
    print("6. Quit")

    # TODO: Fix 1, 3, 4,

    choice = input()

    if choice == "1":
        account = input("Enter account name: ")
        player_account = None
        for player in market.players:
            if player.name == name:
                player_account = player
        print(player_account.capital)

    if choice == "2":
        print("What is your player's name?")
        name = input()
        if name in market.players:
            print("Error: Name already in use")
        else:
            market.add_player(name)
            print("Player " + str(name) + " added.")

    if choice == "3":
        flag = False
        name = input("What is the prediction name?")
        for prediction in market.predictions:
            if name == prediction.name:
                print("Error: Name already in use")
                flag = True
                break
        if not flag:
            market.add_prediction(name)

    if choice == "4":
        print("Available Predictions: ")
        for prediction in market.predictions:
            print(prediction.name)
        print("Enter the name of a prediction: ")
        name = input()
        bool = input("Was the prediction true or false?")
        market.resolve_prediction(name, bool)

    if choice == "5":
        for player in market.players:
            print(player.name + " " + str(player.capital))

    if choice == "6":
        menuFlag = False

    market.check_orders()
    #TODO: add protection for empty orders 


