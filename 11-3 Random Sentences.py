#-------------------------------------------------------------------------------
# Name:        Joshua Khooba
# Purpose:     random sentences
#
# Filename:     11-3
# Date:  11/3/2021
#-------------------------------------------------------------------------------

from random import randint

nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily", "dutifully", "foolishly", "merrily", "occasionally")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")

print(nouns[randint(0, len(nouns)-1)]+ " "+ verbs[randint(0, len(verbs)-1)]+" "+ adv[randint(0, len(adv)-1)]+" "+ adj[randint(0, len(adj)-1)],end = ".")

