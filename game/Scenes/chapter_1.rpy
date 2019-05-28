label chapter_1:
    scene bg house
    "This is chapter 1's dialouge"
    
    menu pearl_chores:
        "Would you like to help Pearl with chores?"
        "Nah man, she's annoying":
            $ amyRoute = True
            "You hang out with Amethyst instead."
        "Yeah I'd love to!":
            "She is very grateful for your help"
            return
        
    "Some more dialogue."    


return