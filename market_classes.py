class Market:
    # class representing the market as a whole. Stores player objects, active predictions, and market orders.
    def __init__(self):
        self.predictions = []
        self.players = []
        self.bids = []
        self.asks = []

    def add_prediction(self, name):
        self.predictions.append(Prediction(name, 100))

    def add_player(self, name):
        self.players.append(Player(name, 20))

    def check_orders(self):

        # TODO: refactor to faster complexity ?

        if len(self.asks) == 0 and len(self.bids) == 0:
            return

        for bid, ask in self.bids, self.asks:
            if bid.price >= ask.price:
                bid.issuer.capital -= bid.price
                ask.issuer.capital += bid.price
                for share in ask.issuer.ownedShares:
                        if share.name == ask.shareName:
                            bid.issuer.ownedShares.append(share)
                            ask.issuer.ownedShares.remove(share)
                            break
                            # break so only first matching share is transferred

    def resolve_prediction(self, name, boolean):
        if boolean:
            value = 1
        else:
            value = 0
        for player in self.players:
            for share in player.ownedShares:
                if share.name == name:
                    share.value = value
                    player.capital += share.value
                    player.ownedShares.remove(share)


class Player (Market):

    # Controls the actions available to a single player in the market: buying and selling shares.
    def __init__(self, name, starting_capital):
        self.name = name
        self.capital = starting_capital
        self.ownedShares = []

    def buy_bundle(self, name):
        for prediction in super.predictions:
            if prediction.name == name:
                self.ownedShares.append(prediction.noShares.pop())
                self.ownedShares.append(prediction.yesShares.pop())
                self.capital -= 1

    def buy_share(self, name, bid):
        order = Order(self, True, name, bid)
        super.bids.append(order)

    def sell_share(self, name, ask):
        # TODO: add checks for share existence
        order = Order(self, False, name, ask)
        self.asks.append(order)


class Prediction:
    # TODO: rewrite the handling of prediction shares

    # Stores the status of predictions within the Market object
    def __init__(self, name, total_shares):
        self.name = name
        self.totalShares = total_shares
        self.yesShares = []
        self.noShares = []
        for i in range(total_shares // 2):
            yes_share = Share(self, True, 1.00, -1)
            no_share  = Share(self, False, 1.00, -1)
            self.yesShares.append(yes_share)
            self.noShares.append(no_share)
            # default of 1.00 for value, changes to 0.00 if option condition unmet
            # -1 is default for price paid, profit tracking feature may not be used right away


class Share:

    # Represents a single share belonging to a certain prediction
    def __init__(self, status, value, price_paid):
        self.status = status
        # boolean true for yes, false for no
        self.value = value
        self.pricePaid = price_paid

    def set_price_paid(self, price):
        self.pricePaid = price


class Order:

    # Stores an order (buy or sell) made by a player
    def __init__(self, player, buy_or_sell, share, price):
        self.issuer = player
        self.buyOrSell = buy_or_sell
        self.shareName = share
        self.price = price
