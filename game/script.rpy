# Characters
define p = Character("Pearl", who_color="#c8ffc8", what_prefix='"', what_suffix='"')
define g = Character("Garnet", who_color="#CD3081", what_prefix='"', what_suffix='"')
define a = Character("Amethyst", who_color="#B898CA", what_prefix='"', what_suffix='"')

# Background
## A list of backgrounds should go here

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show pearl concerned

    call prologue

    call chapter_1

    menu:
        "Do you like birds or do you like trash?"

        "Gimme da Poil":
            show pearl happy

            p "Penis? I mean- Steven?"
            call pearl_1

        "I want that purple marshmallow":
            show amethyst devious

            a "Get in these guts"
            call amethyst_1

    call chapter_2

    call chapter_3

    call chapter_4

    call opal_1

return