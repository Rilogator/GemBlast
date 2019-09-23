#TODO Add dialogue busts

label chapter_2:
    scene bg house day

    "With last night's events behind you, the next couple days are actually pretty boring."

    if amyHangout == True:
        "Amethyst near drained the life out of you. Not that you'd complain if it happened again."
        jump Amy2
    else:
        "Pearl worked your over pretty good, nearly turning you into putty."
        jump Pearl2

    label Amy2:
        "She doesn't bring up the next day, a fact that doesn't bother you too much."
        "She seems her usual lazy self and doesn't bring up what happened."
        show amethyst
        "However, it does seem she's going out of her way to be around you."
        "Laughing a little more at your jokes, holding onto you and playfully shoving you a little more than usual."

        menu:
            "How do you respond?"

            "I don't like it.":
                "It's getting a little annoying."
            "I encourage it.":
                "You encourage her, giving a grope or two every now and again."

        "Its enough to make Pearl a little unnerved, and that's when you realize what Amethyst is up to."
        m "Are you trying to make Pearl jealous or something"
        a "Hey nooo."
        a "What makes you say that?"
        "Amethyst starts laughing in that way she does when she's up to no good."
        "Having a feeling of where this all leading up to, you wait for an oppurtunity when Pearl is out of the house."
        "When the coast is clear you call Amethyst over. She positively bounces over to you, knowing exactly whats in store."

        jump amethyst_2

        return

    label Pearl2:
        "It gets crazy enough around here without things getting weird between you two."
        "Some days later..."

        show pearl happy alt

        p "Hello [playerName]."

        m "Hey Pearl. What's happening?"

        show pearl embarrassed alt

        p "Oh not much is happening, which is what I'd like to talk to you about."

        "She looks kind of nervous. She glances around to see if Amethyst could be watching. Once she's sure, Pearl turns backs to you."

        show pearl neutral

        p "The monster attacks have ceased as of late."
        p "Which is a good thing to be sure!"
        p "However, it makes me wonder..."
        p "If that's why you left in the first place?"

        show pearl embarrassed

        p "Is there not enough excitement for you here?"
        p "If that is the case, I completely understand of course."

        menu:
            "No of course not! I love Beach City.":
                show pearl happy
                p "I am so glad to hear that!"
                "Pearl pulls you into a big hug."
                p "It makes me so happy having you home again, [playerName]!"

            "Honestly, a little. Beach City is all I've ever known.":
                p "Oh..."

        show pearl flirty alt

        p "Well I am determined to make things a little more exciting around here!"

        jump pearl_2

        return

return
