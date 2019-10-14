label living_room:

    if renpy.music.get_playing() != "<loop 2.8>music/main_theme.ogg" or "<from 2.8>music/main_theme.ogg":
        play music "<from 2.8>music/main_theme.ogg" loop fadeout 1.0 fadein 1.0

    scene bg house day with dissolve

    if amyRoute == 2 and pearlRoute == 2:
        return

    "With yesterday behind you and a clean schedule for the day, what do you do?"

    menu:
        # Pearl Options
        "Clean up the mess from the party." if pearlRoute == 0:
            $ pearlRoute += 1
            jump pearl_1

        "Pearl looks like she has something she wants to talk about." if pearlRoute == 1:
            $ pearlRoute += 1
            jump pearl_2



        # Amethyst Options
        "Watch some TV." if amyRoute == 0:
            $ amyRoute += 1
            jump amethyst_1

        "Amethyst sure is close lately." if amyRoute == 1:
            $ amyRoute += 1
            jump amethyst_2


        # Other stuff
        "That's the end for now!" if amyRoute == 2 and pearlRoute == 2:
            return

return
