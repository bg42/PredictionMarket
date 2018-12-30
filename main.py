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

    # TODO: Fix 1, 4
    # TODO: prediction creation causes errors with number of shares, refactor to reflect bundle creation

    choice = input()

    if choice == "1":
        account = input("Enter account name: ")
        player_account = None
        for player in market.players:
            if player.name == account:
                success_flag = False
                player_account = player
                print("What would you like to do?")
                print("1. Buy Bundle")
                print("2. Make Bid")
                print("3. Make Ask")
                selection = input()
                if selection == "1":
                    prediction_name = input("What prediction would you like to buy a bundle of? ")
                    for prediction in market.predictions:
                        if prediction.name == prediction_name:
                            player_account.buy_bundle(prediction.name)
                            print("Success")
                            success_flag = True
                    if not success_flag:
                        print("Error: No Prediction Found")
                if selection == "2":
                    prediction_name = input("What prediction shares would you like to make a bid for? ")
                    for prediction in market.predictions:
                        if prediction.name == prediction_name:
                            # print("Success")
                            # success_flag = True
                            # continue
                    # if not success_flag:
                        # print("Error: No Prediction Found")


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
        name = input("What is the prediction name? ")
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


