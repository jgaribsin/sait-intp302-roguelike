# Werewolf game event class
import random

class GameEvent:
    @staticmethod
    def survive_night(player):
        if player.suspicion >= 70:
            if random.randint(1, 100) > 50:
                return "Game Over!"
            player.attributes.mood -= 20
            return "Escaped attack"
        return "Normal night"