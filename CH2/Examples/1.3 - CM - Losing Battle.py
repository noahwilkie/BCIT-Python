# Troll Battle
# Watch your hero battle the forces of evil

from random import randint

print("    Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword and begins the last fight of his life.\n")

health = 25
trolls = 0


while health > 0:
    trolls = trolls + 1
    damage = randint(1, 10)
    health = health - damage

    print("Your hero swings and defeats an evil troll. " \
          "but takes", damage, "damage points.")

print()
print("Your hero fought valiantly and defeated", trolls, "trolls")
print("But, alas, your hero is no more!")
input() #Leave this line at end of code




# The result will look something like this:

###########################################################################
#    Your lone hero is surrounded by a massive army of trolls.
# Their decaying green bodies stretch out, melting into the horizon.
# Your hero unsheathes his sword and begins the last fight of his life.
#
# Your hero swings and defeats an evil troll. but takes 8 damage points.
# Your hero swings and defeats an evil troll. but takes 3 damage points.
# Your hero swings and defeats an evil troll. but takes 10 damage points.
# Your hero swings and defeats an evil troll. but takes 9 damage points.
#
# Your hero fought valiantly and defeated 4 trolls
# But, alas, your hero is no more!
###########################################################################

# Code Magnets
# Cut & Paste the following code fragments in place of the empty "#" markers


