class Market:
    # class representing the market as a whole. Stores player objects, active predictions, and market orders.
    def __init__(self):
        self.predictions = []
        self.players = []
        self.bids = []
        self.asks = []

    def addPrediction(self, name):
        self.predictions.append(Prediction(name, 1.00))

    def addPlayer(self, name):
        self.players.append(Player(name, 20))

    def checkOrders(self):
        for bid in self.bids:
            for ask in self.asks:
                if bid.price == ask.price:
                   bid.issuer.capital -= bid.price
                   ask.issuer.capital += ask.price
                   #  TODO: add code for share ownership swapping

class Player (Market):
    # Controls the actions available to a single player in the market: buying and selling shares.
    def __init__(self, name, startingCapital):
        self.name = name
        self.capital = startingCapital
        self.ownedShares = []

    def buyBundle(self, name):
        for prediction in super.predictions:
            if prediction.name == name:
                self.ownedShares.append(prediction.noShares.pop())
                self.ownedShares.append(prediction.yesShares.pop())
                self.capital -= 1

    def buyShare(self, name, bid):
        order = Order(self, True, name, bid)
        super.bids.append(order)

    def sellShare(self, name, ask):
        order = Order(self, False, name, ask)
        super.asks.append(order)

class Prediction:
    # Stores the status of predictions within the Market object
    def __init__(self, name, total_shares):
        self.name = name
        self.totalShares = total_shares
        self.yesShares = []
        self.noShares = []
        for i in range(total_shares // 2):
            yesShare = Share(self, True, 1.00, -1)
            noShare  = Share(self, False, 1.00, -1)
            self.yesShares.append(yesShare)
            self.noShares.append(noShare)
            # default of 1.00 for value, changes to 0.00 if option condition unmet
            # -1 is default for price paid, profit tracking feature may not be used right away

class Share:
    # Represents a single share belonging to a certain prediction
    def __init__(self, status, value, pricePaid):
        self.status = status
        # boolean true for yes, false for no
        self.value = value
        self.pricePaid = pricePaid

    def setPricePaid(self, price):
        self.pricePaid = price

class Order:
    # Stores an order (buy or sell) made by a player
    def __init__(self, player, buyOrSell, share, price):
        self.issuer = player
        self.buyOrSell = buyOrSell
        self.share = share
        self.price = price
