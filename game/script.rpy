# Variables
$ playerName= ""
$ amyRoute = False

# Characters
    #This is the narrator
define n = Character("")
define m = Character("Player")
define p = Character("Pearl", who_color="#c8ffc8", what_prefix='"', what_suffix='"')
define g = Character("Garnet", who_color="#CD3081", what_prefix='"', what_suffix='"')
define a = Character("Amethyst", who_color="#B898CA", what_prefix='"', what_suffix='"')

# Background
## A list of backgrounds should go here

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg character creation

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    n "Welcome to our digital adventure!"
    n "We're sure you'll have a wonderful time, but first we need to ask some questions."
    n "Firstly, we'll need your name!"

    label nameEntry:
    $ playerName = renpy.input("")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "John"

    menu:
        n "Are you sure your name is [playerName]?"
        "Let me change it.":
            jump nameEntry
        "Yes! Let's get on with it already!":
            n "Suit yourself! Here we go..."
            
    call prologue

    call chapter_1

    call chapter_2

    call chapter_3

    call chapter_4

    call epilogue

return