

class BattleObject():
    def __init__(self, hp, mp, str, dex, int,agi, wis, luk):
        self.name = None
        self.job = None
        self.hp = hp
        self.mp = mp
        self.str = str
        self.dex = dex
        self.int = int
        self.agi = agi
        self.wis = wis
        self.luk = luk
    def __str__(self):
        return self.name
