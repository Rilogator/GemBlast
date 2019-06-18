label chapter_1:
    scene bg bedroom
    "The next morning..."
    show per surprised
    p "Um..."
    hide per
    m "What was that?" 
    m "Was she... watching me sleep?"
    "Probably."
    "Anyway, you get your day started with some breakfast."
    "Eggs and toast to be precise."
    "You know that Pearl is probably busy cleaning up the beach front at this time."
    "Amethyst is probably in her room pretending to sleep to get out of work."
    "So nows the matter of how to spend the next couple of hours"

    menu pearl_chores:
        "Would you like to help Pearl by cleaing inside the house?"
        "Nah man, she's annoying":
            $ amyRoute = True
            "You're a guest after all, why should you have to put in work?"
        "Yeah I'd love to!":
            "She is very grateful for your help"
            return
        
    "Some more dialogue."    

    #label Amy hangout



return