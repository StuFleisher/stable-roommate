from matching.games import StableRoommates
from matching.exceptions import NoStableMatchingWarning
import warnings
warnings.filterwarnings("error")

from matching import Player

players = [
    Player("a"),
    Player("b"),
    Player("c"),
    Player("m"),
]

a, b, c, m = players

# jerry.set_prefs([george, elaine, kramer])
# george.set_prefs([jerry, kramer, elaine])
# elaine.set_prefs([jerry, kramer, george])
# kramer.set_prefs([elaine, george, jerry])

a.set_prefs([b, c, m])
b.set_prefs([c, a, m])
c.set_prefs([a, b, m])
m.set_prefs([a, b, c])

try:
    game = StableRoommates(players)
    print(game.solve())
except NoStableMatchingWarning as exc:
    print("exc")

# get initial preferences for each player
# implement pair tracking
# adjust preferences based on recent pairs
# try to solve
    #fail case
        #randomly select a player
        #randomly swap two preferences
        #repeat solve