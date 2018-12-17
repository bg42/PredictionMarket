class Market:
    def __init__(self):
        self.predictions = []
        self.players = []
        self.bids = []
        self.asks = []

    def addPrediction(self, name):
        prediction = Prediction(name, 1000)
        self.predictions.append(self, prediction)

    def addPlayer(self, name):
            player = Player(self, name, 100)
            self.players.append(self, player)

    def checkOrders(self):
        for bid in self.bids:
            for ask in self.asks:
                if bid.price == ask.price:
                   bid.issuer.capital -= bid.price
                   ask.issuer.capital += ask.price
                   #  add code for share ownership swapping

class Player (Market):
    def __init__(self, name, startingCapital):
        self.name = name
        self.capital = startingCapital
        self.ownedShares = []

    def buyShare(self, name, bid):
        order = Order(self, True, name, bid)
        super.bids.append(order)

    def sellShare(self, name, ask):
        order = Order(self, False, name, ask)
        super.asks.append(order)

class Prediction:
    def __init__(self, name, total_shares):
        self.name = name;
        self.totalShares = total_shares
        self.yesShares = []
        self.noShares = []
        for i in range(total_shares / 2):
            yesShare = Share(self, True, 1.00, -1)
            noShare  = Share(self, False, 1.00, -1)
            self.yesShares.append(self, yesShare)
            self.noShares.append(self, noShare)
            # default of 1.00 for value, changes to 0.00 if option condition unmet
            # -1 is default for price paid, profit tracking feature may not be used right away

class Share:
    def __init__(self, status, value, pricePaid):
        self.status = status
        # boolean true for yes, false for no
        self.value = value
        self.pricePaid = pricePaid

    def setPricePaid(self, price):
        self.pricePaid = price

class Order:
    def __init__(self, player, buyOrSell, share, price):
        self.issuer = player
        self.buyOrSell = buyOrSell
        self.share = share
        self.price = price


market = Market()
market.addPlayer("p1")
market.addPlayer("p2")



