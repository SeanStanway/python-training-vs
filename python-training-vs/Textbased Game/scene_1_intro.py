def introduction(player):
    name = input("Hey hey, I'm a super unreliable narrator. What is your name, young squire?\n\n")

    print("{} eh? Well, that doesn't sound terrible at all... anyway. Let's give you some stats shall we?\n\n".format(name))

    player.set_name(name)

    print("\nHere is your base stats:\n")
    player.printStatus()

    print("\nNot bad, y'know, a little poor, but we'll fix that.\nI couldn't have done better myself (even though I technically did do that)\n")
    print("Hey, I got a great idea, let's kick off this thing with a fight, whaddya say, friend? Here, this guy is easy...\n\n")