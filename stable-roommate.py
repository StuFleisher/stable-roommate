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

#for each student1
    #query pairs for student1
    #get id for top 3 student2's
    #adjustfrequencies(student1)


#get frequencies
    #for each student that isn't a



frequencies = {
    "a":[(b,2),(c,1),(d,0)]
    "b":{
        "a":2,
        "c":1,
        "m":0,
       }
}

frequencies.b.values()
frequencies.a.sorted(val=>val[1])
a, b, c, m = players


a.set_prefs([b, c, m])
b.set_prefs([c, a, m])
c.set_prefs([a, b, m])
m.set_prefs([a, b, c])


def adjust_preferences(student, top_three):
    #find top_three[2]
        #bump -1
    #find top_three[1]
        #bump -2
    #find top_three[0] (first place)
        #bump them down 3 spaces


def get_pairs():
    pairs = None

    while not pairs:
        try:
            game = StableRoommates(players)
            pairs = game.solve()
        except NoStableMatchingWarning as exc:
            handle_no_match()
    return pairs


print(get_pairs())

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

