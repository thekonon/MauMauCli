try:
    from src.card import Card
except ModuleNotFoundError:
    from card import Card



class WebSocket():
    def __init__(self):
        self.cards = [("S", "7"), ("C", "8"), ("C", "7"), 
                      ("C", "7"),
                      ("C", "9"),
                      ("C", "J"),
                      ("C", "Q")]

    def draw_card(self) -> Card:
        # This needs to be implemented
        import random
        return Card(*random.sample(self.cards, 1)[0])
    
    def play_card(self, card: Card) -> bool:
        # This needs to be implemented
        return True