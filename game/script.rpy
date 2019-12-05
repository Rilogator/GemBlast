# Variables
default pearlRoute = 0
default amyRoute = 0

# Characters
define m = Character("[playerName]", what_prefix="{i}", what_suffix="{/i}")
define p = Character("Pearl", who_color="#c8ffc8", what_prefix='"', what_suffix='"')
define g = Character("Garnet", who_color="#CD3081", what_prefix='"', what_suffix='"')
define a = Character("Amethyst", who_color="#B898CA", what_prefix='"', what_suffix='"')

# Background
## A list of backgrounds should go here

#Effects
$ flash = Fade(.25, 0, .75, color="#fff")

label start:

<<<<<<< HEAD
    scene bg sky
=======
    call screen livingRoom

    scene bg outside night
>>>>>>> f8838e79e8b22b31925180e0dd0ca39daac3fbcd

    "Welcome to our digital adventure!"
    "We're sure you'll have a wonderful time, but first we need to ask some questions."
    "Firstly, we'll need your name!"

    label nameEntry:
    $ playerName = renpy.input("")
    $ playerName = playerName.strip()
    if playerName == "":
        $ playerName = "John"

    menu:
        "Are you sure your name is [playerName]?"
        "Let me change it.":
            jump nameEntry
        "Yes! Let's get on with it already!":
            "Suit yourself! Here we go..."

    call prologue from _call_prologue

    call chapter_1 from _call_chapter_1


    label epilogue:

        "That's all the content for now!"
        "But maybe you can get a different ending."
        "Make sure to check out the Patreon link in the main menu for future updates."
        "We look forward to seeing you next time!"

return
<<<<<<< HEAD
=======

screen livingRoom():

    imagemap:

        auto "mapTest/mapTest_%s.png"

        hotspot (649, 474, 141, 141) action Jump('amethyst_1')
        hotspot (43, 552, 170, 161) action Jump('pearl_1')



##############################################################
#############################################################












return
>>>>>>> f8838e79e8b22b31925180e0dd0ca39daac3fbcd
