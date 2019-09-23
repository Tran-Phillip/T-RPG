
# Internal
from tools.text import Text
from game_systems.battle_ui import PlayerTurnUI
from game_objects.party_members import BattleObject
from game_systems.TBS import BattleInstance

phill = BattleObject(hp=10, mp=10,str=5,dex=5,int=5,agi=5,wis=5,luk=5)
slime = BattleObject(hp=4, mp=10,str=1,dex=3,int=5,agi=2,wis=1,luk=5)
phill.name = 'Phillip'
slime.name = 'slime'
instance = BattleInstance([phill],[slime])
instance.log()
