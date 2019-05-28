label prologue:

    scene bg house exterior

    n "It's been a while, but after being away for too long you decide to visit your old friends."
    n "You find yourself in your home town of Beach City, a shining shoreline town."
    n "As you ponder the memories you've made, three colorful figures you approach you."
    n "It can only be, of course..."

    show garnet happy
    show per neutral at right
    show amy neutralF at left

    n "The Crystal Gems!"
    a "[playerName]! Welcome back buddy, we totally missed you!"
    p "Yes! Even though we know you probably don't need us worrying about you, we're still happy to see you return home safe."
    g "I wasn't worried at all."
    show per concerned
    p "Garnet!"
    a "Relax P, you know she's got the whole future thing covered."
    p "..."
    show per neutral
    p "I suppose you are right. [playerName] is capable of handling himself."
    g "You know he is. Welcome back, [playerName]."
    p "Welcome back indeed!"

    n "You let out a joyful laugh, and the gems join in as well."
    n "It is good to see them after such a long time, and they haven't changed one bit."
    n "Garnet shows off her massive strength by lifting all your things above her head with one hand."

    g "Come on then. No time to waste."

    n "The strongest of the gems takes your things into the house, and the rest of you follow suit."

    scene bg house interior

    n "You get settled in quickly with four you helping along."
    show per neutral
    p "Oh good we're right on schedule."
    show per upset
    p "No thanks to Amethyst..."
    show amy neutral at right
    a "Hey, I put away all the food."
    n "Pearl rolls her eyes before putting on a smile as she turns to you."
    hide amy neutral
    p "Now then, if everything is in the right place, we do have something to tell you."
    show gar at right
    show per neutralF at left
    g "That's right."
    g "I have to leave now. I know you just arrived but its an important mission. You know how it is."

    menu:        
        "Can't you postpone it?":
            n "She laughs warmly."
            g "If only."
        "Yeah I guess I do.":
            g "Don't worry [playerName]"
            
    g "I'll be back before you know it."
    g "Pearl, can I have a moment with [playerName]?"
    p "Of course." 
    hide per neutralF    
    p "Come on Amethyst, we need to go find food for [playerName] to eat while he's here."
    a "Oh right I forgot he needs to do that..."
    show gar at center
    g "..."
    g "I'm glad you're home safe."
    g "But this really is an important mission. Before I go I just wanted to tell you."
    g "Behave yourself."
    n "You're taken slightly aback by Garnet's directness."
    n "Hardly out of character when it comes to her, yet you're still a bit uneased."
    n "Sensing this, Garnet pulls you close into a powerful hug."
    g "And don't be too serious. You're here to have fun too, remember?"
    n "You smile back as the tension diffuses, and return her embrace."
    g "And that goes for the rest of you."
    show per neutralF at left
    show amy neutral at right
    g "I want to see [playerName] in one piece when I get back, is that clear?"
    a "You got it, boss."
    p "I will make sure of it, no doubt about that."
    a "Excellent. Goodbye everyone."
    n "Garnet makes a salute gesture with two fingers before stepping onto the warp pad."
    n "Without hesitation she looks up and..."
    # Flash effect
    n "She's gone! To parts unknown, leaving you with the other two Crystal Gems."

return

return