from matching.games import StableRoommates
from matching.exceptions import NoStableMatchingWarning
from random import choice, choices
import warnings
warnings.filterwarnings("error")

from matching import Player




def handle_no_match():
    player = choice(players)
    prefs_list = player.prefs
    random_prefs = choices(prefs_list, k=2)

    # indexes = []
    # for pref in random_prefs:
    #     indexes.append(prefs_list.index(pref))

    a, b = prefs_list.index(random_prefs[0]), prefs_list.index(random_prefs[1])

    prefs_list[a], prefs_list[b] = prefs_list[b], prefs_list[a]

    player.set_prefs(prefs_list)


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

pairs = None

while not pairs:
    try:
        game = StableRoommates(players)
        pairs = game.solve()
    except NoStableMatchingWarning as exc:
        handle_no_match()


print(pairs)

# get initial preferences for each player
# implement pair tracking
# adjust preferences based on recent pairs
# try to solve
    #fail case
        #randomly select a player
        #randomly swap two preferences
        #repeat solve


# prioritize bumping down frequent pairs (think about recency if pattern develops)
# user can select "choose for me" button to opt out of preference ranking (will randomize their pref list)

# DB setup
# project sesssion & exercise session ==> pairs ==> students
    # form for project/exercise session will contain area for pairs
    # on submit, will populate Pairs table with foreign keys to session id & student ids

