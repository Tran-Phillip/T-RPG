'''
TBS (turn-based-system) is the main
function that controls our battle system.
It'll initialize a battle....in some ways!
'''
from queue import Queue
class BattleInstance:

    def __init__(self, party_members:list, enemies:list):
        self.party_members = party_members
        self.enemies = enemies
        self.turn_queue = (party_members + enemies)
        self.turn_queue.sort(key=self.sort_by_agi,reverse=True)
    def log(self):
        for member in self.party_members:
            print(member.name)
        for enemy in self.enemies:
            print(enemy.name)

    def sort_by_agi(self, object):
        return object.agi
