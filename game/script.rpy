# Characters
define p = Character("Pearl", who_color="#c8ffc8", what_prefix='"', what_suffix='"')
define g = Character("Garnet", who_color="#CD3081", what_prefix='"', what_suffix='"')
define a = Character("Amethyst", who_color="#B898CA", what_prefix='"', what_suffix='"')

# Background

# The game starts here.

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

    p "What if Steven's penis..."

    p "gets in the way!?"

    menu:
        "What if Steven's Penis (tm) gets in the way?"

        "It won't":
            show garnet determined

            g "It won't"
            
        "Who?":
            show amethyst baked

            a "Who?"

        "Stop":
            "Guys... stop..."
            jump home

label home:
    p "Steven's."
    return
