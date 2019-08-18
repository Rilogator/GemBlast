# Effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

label prologue:

    scene bg outside day

    "It's been a while, but after being away for too long you decide to visit your old friends."
    "You find yourself in your home town of Beach City, a shining shoreline town."
    "As you ponder the memories you've made, three colorful figures you approach you."
    "It can only be, of course..."

    show garnet at center
    show pearl neutral at right
    show amethyst neutral at left

    "The Crystal Gems!"
    show amethyst happy
    a "[playerName]! Welcome back buddy, we totally missed you!"
    show amethyst neutral
    show pearl happy
    p "Yes! Even though we know you probably don't need us worrying about you, we're still happy to see you return home safe."
    g "I wasn't worried."
    show pearl embarrassed
    p "Garnet!"
    a "Relax P, you know she's got the whole future thing covered."
    p "..."
    show pearl embarrassed alt
    p "I suppose you are right. [playerName] is capable of handling himself."
    g "You know he is. Welcome back, [playerName]."
    show pearl happy
    p "Welcome back indeed!"

    "You let out a joyful laugh, and the gems join in as well."
    show amethyst happy
    "It is good to see them after such a long time, and they haven't changed one bit."
    "Garnet shows off her massive strength by lifting all your things above her head with one hand."

    g "Come on then. No time to waste."

    "The strongest of the gems takes your things into the house, and the rest of you follow suit."

    scene bg house day

    "You get settled in quickly with four you helping along."
    show pearl neutral
    p "Oh good we're right on schedule."
    show pearl embarrassed alt
    p "No thanks to Amethyst..."
    show amethyst neutral at right
    a "Hey, I put away all the food."
    "Pearl rolls her eyes before putting on a smile as she turns to you."
    hide amethyst
    show pearl neutral
    p "Now then, before you settle in, we do have something to tell you."
    show garnet at center
    show pearl neutral at right
    g "[playerName]"
    g "I have to leave now. I know you just arrived but its an important mission. You know how it is."

    menu:        
        "Can't you postpone it?":
            "She laughs warmly."
            g "If only."
        "Yeah I guess I do.":
            g "Don't worry [playerName]"
            
    g "I'll be back before you know it."
    g "Pearl, can I have a moment with [playerName]?"
    p "Of course." 
    hide pearl
    p "Come on Amethyst, we need to go find food for [playerName] to eat while he's here."
    a "Oh right I forgot he needs to do that..."
    show garnet at center
    g "..."
    g "I'm glad you're home safe."
    g "But this really is an important mission. Before I go I just wanted to tell you."
    show garnet alt
    g "Behave yourself."
    show garnet
    "You're taken slightly aback by Garnet's directness."
    "Hardly out of character when it comes to her, yet you're still a bit uneased."
    "Sensing this, Garnet pulls you close into a powerful hug."
    g "And don't be too serious. You're here to have fun too, remember?"
    "You smile back as the tension diffuses, and return her embrace."
    g "And that goes for the rest of you."
    show pearl neutral at right
    show amethyst neutral at left
    g "I want to see [playerName] in one piece when I get back, is that clear?"
    a "You got it, boss."
    p "I will make sure of it, no doubt about that."
    g "Excellent. Goodbye everyone."
    "Garnet makes a salute gesture with two fingers before stepping onto the warp pad."
    "Without hesitation she looks up and..."
    scene bg house day
    with flash

    show pearl neutral at right
    show amethyst neutral at left
    
    "She's gone! To parts unknown, leaving you with the other two Crystal Gems."
    "They help you get settled in and reacquainted with the old beach house."
    "It definitely feels good to be back home."

return