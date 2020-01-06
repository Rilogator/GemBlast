label chapter_1:
    scene bg house day
    play music "music/main_theme.ogg" loop fadeout 1.0 fadein 1.0

    "Inside, you find a huge banner hang from the ceiling, reading “Welcum Home [playerName]!”"

    menu:
        "Do you point out 'Welcome' is spelled wrong?"

        "Of course I do.":

            show pearl embarrassed at right with dissolve

            p "Oh bother."
            p "Amethyst the sign was your job!"

            show amethyst neutral at left with dissolve

            a "Pearl, I literally can't read."
            a "So I think I did a pretty good job."

        "I like it the way it is.":

            m "I think it's great, guys."
            m "Really."
            "You hold back a laugh, wondering how Pearl will react when she finds out."

    "The celebration is short lived, as you are reminded of Garnet's early departure by the sound of the teleport pad energizing."

    show garnet with dissolve

    g "I'm all ready to go now."
    g "Take care everyone."
    g "We really missed you, [playerName]."
    g "Make sure to behave yourself when you're gone."

    show garnet alt with dissolve

    g "You get me?"

    show garnet with dissolve

    "You give, not really sure what Garnet is talking about."
    "As Amethsyt and Pearl start putting your stuff away-"
    "Well putting them somewhere in Amethyst's case."
    "Garnet stands on the teleport pad with her back facing you."

    menu:
        "An opportunity presents itself."

        "Jump onto the teleport pad.":
            "At the last second you leap onto the pad."
            "Just before the energy beam wisks you away to parts unknown, Garnet gives you a knowing smile."
            jump garnet_1

        "Decide to keep Pearl and Amethyst company.":
            "Instead of letting compulsion get the better of you, you stay put and wave goodbye."
            "Perhaps by coincidence, Garnet gives a small backwards wave of her own."

    hide garnet with flash

    "..."
    "The tower of light dissipates and Garnet's gone."
    "Wth a heavy sigh you get to tracking down the rest of your things and put them in their proper place."

    show pearl happy alt with dissolve

    "Before you get too down, Pearl presents you with a slice of cake!"

    p "Cheer up [playerName]. I have made you a cake!"

    show pearl neutral

    p "Well actually I made several cakes but Amethyst ate most of them."

    show pearl at right with move

    show amethyst neutral at left
    a "They were good cakes P."

    p "Yes, quite."

    "You laugh and take a bite, a little spoon already neatly embedded in the slice."
    "The rest of the homecoming party goes by rather merrily."
    "Stories are swapped and laughter is had, until all too soon, night falls."

    scene bg house night with dissolve

    "Today was a big day, and the bus ride home was rather long."
    "A nice comfortable bed is a good sight to finally see."
    "You drift off to sleep, glad that things are back to normal."

    scene bg house day with dissolve

    "The next morning..."

    show pearl embarrassed

    p "Um..."

    show pearl at right with move

    hide pearl with dissolve

    "Was she watching you sleep?"
    "Probably."

    jump living_room

return
