# Effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

label prologue:

    scene bg sky
    play music "music/coming_home.mp3" loop fadeout 1.0 fadein 1.0

    "Long hours spent on a bus have almost soured the trip, but then you peer through the window, out toward the horizon."
    "The coastline shimmers with a familiar beauty, reinvigorating your mood."
    "The ocean waves crash on your home town, {b}Beach City{/b}."
    "Four years away at university,  you return with newfound insight."
    "All you can think about right now though is how good coming back home feels."
    "You think about all the denizens that are sure to be happy at your return."
    "Of all your old friends, the ones you can’t wait to see most are, of course, the Crystal Gems."

    "Eventually you pull into the bus station, and hike your bag on your shoulder and make your way to the house."

    scene bg town

    "As much as you’d like for your family to greet you as soon as you set foot down in the city, their presence always causes a ruckus with the townies."
    "A laugh escapes you as you think about all the antics the heroes of Beach City get up to."
    "They mean well, but things can still get out of hand."
    "You wonder what they’ve been up to while you’ve been away, smiling and waving at passersby."

    "Those that recognize you call out and ask small questions."

    menu:
        "How do you respond?"

        "Hurry home.":
            "They sound dissapointed but understand your eagerness to get back home."

        "Give a polite nod and make small talk.":
            "You take your time saying 'hello' to apparent strangers."
            "It never occured to you that you were ever this popular but the proof lies in the many small commotions your appearance causes."

    scene bg outside day

    "The sun still hangs high in the air when you make it to your beachside abode."
    "Memories flood your mind as you stare affectionately at the little shack nestled under the gigantic statue built into the mountainside."
    "Lost in reminiscence, you almost fail to notice:"

    show garnet at center
    "{b}Garnet{/b}"

    show amethyst happy at left
    "{b}Amethyst{/b}"

    show pearl happy at right
    "and {b}Pearl{/b}!"

    p "[playerName]! Oh it is so good to see you!"

    a "Hey [playerName]!"
    a "Who said you could get so tall, dude?"

    show amethyst neutral
    show pearl neutral

    "Garnet just pulls the three of you into a great big bear hug, making use of her impressive size and strength."

    g "It is good to see you, [playerName]."
    g "The girls were worried sick about you the whole time."

    a "Nah I wasn't too worried."

    show pearl happy

    p "I was very worried!"

    show pearl neutral

    "Right before you ask her to let you breath, Garnet lets everyone loose from her embrace."

    g "I'm glad I got to see you before I headed out on the mission."

    "You give a look of dissapointment and Garnet nods solemnly."

    g "I know, but this is something that can’t be put off."
    g "I hope you'll understand."

    show pearl neutral alt

    p "She loves you just as much as we do, [playerName]."

    menu:
        "I understand... ":
            m "Yeah... I know how it is."

        "That's not fair!":
            m "I just got here and everything!"

    g "Monsters don't take a break, you know that."

    a "He’s a big guy P, stop being all mushy."

    g "Come. We have something to show you before I leave."

    show pearl happy alt

    p "Oh yes! We simply cannot wait to show you."

    "Without further ado, Pearl helps you bring your things inside."
    "Home at last."
return
