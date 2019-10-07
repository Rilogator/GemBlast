label garnet_1:

    scene bg mission day with flash

    show garnet with dissolve

    "Teleporting isn't exactly new to you but it has been a while."

    g "You all right [playerName]?"

    "She doesn't seem the least bit surprised, probably because of her future sight."

    m "Yeah, I'm okay."
    m "I bet you saw this coming, huh?"

    "You're a little embarassed by your own impulsiveness but Garnet doesn't seem to mind."
    "In fact she seems even a little excited."

    g "I never said you couldn't come along for the mission."
    g "But we do have to be quick."
    g "Come along then."

    m "Aren't they gonna come along?"

    g "Nah I told them not to."

    "Being her mysterious stoic self, she's already a good distance down the path leading from the teleport pad."
    "You just shrug your shoulders and do as you're told."

    hide garnet with dissolve

    "Admittedly this is a pretty exciting way to kick off your return home."
    "Almost feels like nothing's changed at all, being back on another mission."
    "Along the way Garnet explains something unusual entered the atmosphere."
    "You're here to scout it out and see if there's any danger."

    scene bg mission night with dissolve

    "A day's worth of searching and there doesn't seem to be any luck."
    "You start to think hopping along for a mission after traveling most of the morning wasn't a good idea."
    "Fortunately Garnet has set up a makeshift shelter in a cave nearby."
    "Soon, the two of you are resting by a small campfire."

    "The two of you catch up as the embers crackle."
    "Most of it is you talking about what you've been up to."
    "Garnet doesn't talk much but you get the idea that things home have been business as usual."
    "She seems pleased to hear you enjoyed yourself and gotten plenty of good experiences out of your time away."

    play music "music/lewd_garnet.ogg" loop fadeout 1.0 fadein 1.0

    "After a bit of silence there's a subtle shift in the air."

    g "You know, [playerName]."
    g "I was worried about you too."

    "Her voice is a bit lower, so you lean in to hear better."

    g "Not that anything would happen to you while you were out there."
    g "You can handle it."
    g "It's more about how things would be when you came back."
    g "As strong as I am, I can't stop change."
    g "Just do my best to guide all of you to a better future."

    "She places an arm around you, holding you tight."
    "Garnet is surprisingly warm."

    g "[playerName], you're special to me."
    g "So I wanna show you how special."

    "You're left a little confused as she gets up and takes a few steps around the fire."

    g "This is a future I want to happen."
    g "The only thing I have to ask is..."

    show garnet1 1a with dissolve

    menu:
        g "Visor on or off?"

        "On, I think.":
            $ visor = True
            "I still don't get-"

        "Take it off, I guess?":
            $ visor = False
            show garnet1 1b with dissolve
            "What are you trying to-"

    if visor:
        show garnet1 2a with dissolve
    else:
        show garnet1 2b with dissolve

        g "This is what's happening."
        g "Don't talk."


    if visor:
        show garnet1 4a with dissolve
    else:
        show garnet1 4b with dissolve

    if visor:
        show garnet1 6a with dissolve
    else:
        show garnet1 6b with dissolve

    "fi"


    if visor:
        show garnet1 7a with dissolve
    else:
        show garnet1 7b with dissolve


    "fo"

    if visor:
        show garnet1 8a with dissolve
    else:
        show garnet1 8b with dissolve

    "fum"

    if visor:
        show garnet1 9a with dissolve
    else:
        show garnet1 9b with dissolve

    "I smell"

return
