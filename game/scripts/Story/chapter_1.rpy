label chapter_1:
    $ pearlHelped = False
    $ amyHangout = False

    scene bg house night
    "The next morning..."
    show pearl embarrassed night
    p "Um..."
    hide pearl
    m "What was that?"
    m "Was she... watching me sleep?"
    "Probably."
    scene bg house day
    "Anyway, the rest of the day is rather uneventful, as is the next week."
    "You spend your catching up with your old friends, asking about their adventures since you've been away."
    "They similarly ask how you've been on your break from Beach City."

    label daily_reset:
    "At the start of a new day, you decide to do something productive."
    "But what?"

    menu daytime_activities:
        m "Today I will..."

        "Help Pearl clean up around the house.":
            $ pearlHelped = True
            "While Pearl is out trying to clean the beach front, you decide to be a good boy and keep things inside tidy for her."
            jump afternoon

        "Watch some television.":
            $ amyHangout = True
            jump amyTv

    return

    label amyTv:
        "You missed out on a lot of TV while you were gone, and it's time to catch up on your shows."
        "As if summoned by this bout of laziness, Amethyst shows up."
        show amethyst neutral
        a "Hey [playerName], whats up!"
        "You're a bit startled by her sudden appearance."
        m "Oh hey."
        m "I was just about to watch something."
        show amethyst flirty
        a "Yeah?"
        hide amethyst with dissolve
        "She sits her big bottom down on the couch next to you, and you notice she's kind of close."
        "Amethyst has always been a bit wide at the hips, not that you're complaining."
        "You're gently squeezed between the arm rest of the couch and Amethyst's soft body."
        a "What are we watching then?"

        menu tv_channel:
            #"You have the remote after all. What will you watch?"

                "Something with action.":
                    "You want to see how your favorite dark fantasy show ended."
                    "Amethyst rolls her eyes which puts you off. This used to be your favorite show to watch together."
                    "As it turns out, the final season was horrendous."
                    "The writing really went downhill after it got passed the story of the books."
                    "All your favorite characters are saying the dumbest things."
                    "Amethyst is extremely bored the whole way through."

                "Family Comedy":
                    a "Oh man I love this show!"
                    "That little dude sure is funny."
                    "You and Amethyst have a good time watching TV."

                "Boring documentary.":
                    "Something about this program catches your eye. It's a nature doc about the mating habits of certain beetles."
                    "Out of politeness, Amethyst tries to pay attention, but the effort takes too much out of her."
                    "She was already leaning on you a bit, and now she's dozed off."
                    "Her thick thighs spread out onto the rest of the couch as she rests most her weight onto your arm."
                    "Even something as a captivating a documentary can't keep you from looking downward at her sizable cleavage."
                    "Well more than sizable, massive really."
                    "You can't help but get more than a little turned on, trapped as you are."

        "You watch the program well past noon. Amethyst gets up to stretch and wonders off to find something else to sleep on."
        jump afternoon
    return

    label afternoon:
        "After grabbing some lunch, you think about what to do in the latter half of the day."
        menu afternoon_activities:
            "You decide that you're going to..."

            "Do some more hard work":
                if pearlHelped == True:
                    jump pearl_1
                elif amyHangout == True:
                    jump amethyst_1
                return

            "Play some gamestation":
                "You play your Gamestation."
                "Playing a VN just to pretend to play videogames is kinda sad."
                "You end up putting the controller down and contemplate how you wasted your day."
                jump daily_reset
    return
return
