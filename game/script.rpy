# Variables
$ playerName= ""
$ amyRoute = False

# Characters
define m = Character("[playerName]", what_prefix="{i}", what_suffix="{/i}")
define p = Character("Pearl", who_color="#c8ffc8", what_prefix='"', what_suffix='"')
define g = Character("Garnet", who_color="#CD3081", what_prefix='"', what_suffix='"')
define a = Character("Amethyst", who_color="#B898CA", what_prefix='"', what_suffix='"')

# Background
## A list of backgrounds should go here

#bepis

label start:

    scene bg outside night

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

    call chapter_2 from _call_chapter_2

    # call chapter_3 from _call_chapter_3

    # call chapter_4 from _call_chapter_4

    # call epilogue from _call_epilogue

    "That's all the content for now!"
    "But maybe you can get a different ending."
    "Make sure to check out the Patreon link in the main menu."
    "We look forward to seeing you next time!"

return
