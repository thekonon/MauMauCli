try:
    from src.card import Card
except ModuleNotFoundError:
    from card import Card

class WebSocket():
    def __init__(self):
        # idk how to implement this but whatever
        ...

    def draw_card(self) -> Card:
        return Card("S", "7")
    
    def play_card(self, card: Card) -> bool:
        return True