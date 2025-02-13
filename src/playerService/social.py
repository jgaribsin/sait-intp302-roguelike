import random

class SocialManager:
    def __init__(self):
        self.friends = {}

    def interact(self, npc_name, action):
        if npc_name not in self.friends:
            self.friends[npc_name] = {"friendship_level": 50, "trust": 30}
        
        if action == "compliment":
            self.friends[npc_name]["friendship_level"] += 10
        elif action == "argue":
            self.friends[npc_name]["friendship_level"] -= 15
            
        return self.friends[npc_name]["friendship_level"]

    def get_clue(self, npc_name):
        if self.friends.get(npc_name, {}).get("trust", 0) > 50:
            return random.choice([
                "The werewolf was recently at the library",
                "The victim was a top student"
            ])
        return None