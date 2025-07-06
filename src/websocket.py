try:
    from src.card import Card
except ModuleNotFoundError:
    from card import Card



class WebSocket():
    def __init__(self):
        self.types = ["S", "C", "D", "H"]
        self.values = ["7", "8", "9","J", "Q","K","A"]

    def draw_card(self) -> Card:
        # This needs to be implemented
        # Send a draw card command to server
        # Response is drawn card
        import random
        type = random.sample(self.types, 1)[0]
        value = random.sample(self.values, 1)[0]
        return Card(type, value)
    
    def play_card(self, card: Card) -> bool:
        # This needs to be implemented
        # Send to server which card is to be played
        # Return True if its valid card
        # Return False if its not
        return True