label pearl_1:
 # Variables
    $ sweep = False
    $ mop = False

    scene bg house day

    "You set in to cleaning up around the house, which mainly means cleaning up after yourself."

    menu house_cleaning:
        "Pick a spot to clean."

        "Pick up trash and sweep." if sweep == False:
            $ sweep = True
            "You start out by picking up paper plates and plastic cups."
            "You guys really made a mess all over the house."
            "Amethyst didn't bother using plates, instead just eating fistfulls of cake and getting crumbs everywhere."
            "It kind of feels good to do something productive and help out."
            "They did go through the trouble of organizing a welcome home party after all."

            "Once the garbage is collected, you get a trash bag to put it all in."
            "The sweeping goes by without any major calamity."
            "All the dirt and crumbs slowly vanish as you diligently clean the house."
            "Satisfied with your work, you take out the very full bag and toss it in a dumpster outside."
            jump house_cleaning

        "Mop the floors." if mop == False:
            $ mop = True
            "The bucket and mop are in the same place you remember before you left."
            "Pearl likes to keep things organized."
            "You do your best to clean up around the mess and furniture."
            "A bit of sweat drips off your brow with all the hard work you're doing."
            "With the floors sparkling, you arrange the couch and the rest of the decor back to its proper place."

            "As the floors dry you take a moment to rest."
            "The house does look a bit smaller now."
            "An ottoman that you liked to use while drawing seems too small to sit on comfortably."
            "The stark lemon-y smell of floor cleaner dissapates as you contemplate how one can never truly go back home."
            "There's more work to do."
            jump house_cleaning

        "Finish unpacking." if sweep and mop:
            "With the house itself looking spick and span, it's time to actually get yourself settled proper."

    "You only came with a duffle bag, so it doesn't take long for you to put away your clothes and knick knacks."

    scene bg house night with dissolve

    "As you're close to finishing, Pearl comes in from her patrol."

    show pearl embarrassed night

    p "[playerName]!"
    p "Did you clean up the whole house?"

    "She looks rather surprised more than grateful."

    m "Ah well I had nothing to do today and wanted to return the favor for the awesome party you guys threw."

    show pearl embarrassed alt night

    "You can see that she's struggling to say 'thank you'."

    "It occurs to you she probably has nothing to do today now that you've finished the chores."

    show pearl embarrassed night

    p "Oh well um, thank you [playerName]."

    "That was very nice of you."

    hide pearl with dissolve

    "You go off and relax a bit after running errands all day."

    scene bg house night

    "That night..."
    "Since you were busy all day and its been ages since you had any private time, you decide its high time to fap."
    "Right as you're getting familiar with yourself, you hear a creak at the door."

    play music "music/lewd_pearl.ogg" loop fadeout 1.0 fadein 1.0

    show pearl happy alt night with dissolve

    p "Oh I read about this. Since I'm free tonight, I can help you out with that."

    show pearl flirty alt night

    p "Actually..."

    show pearl1 1 with dissolve

    p "I have these for just this occasion!"
    "…"
    "You're kind of taken aback but you're not going to complain."
    "Why was she keeping those around, anyway?"
    "Before you know it, you're sitting on your bed."
    "Pearl's slender fingers do what can be called a physical examination of your dick."
    "She's delicate but insistent as she caresses and squeezes different parts of you."
    "You almost wonder if she's taking measurements."
    "As you're stroked to full hardness, Pearl seems satisfied with her progress."
    "She then lathers her hands with with oil and lotion, making her hands glisten in the moonlight."

    show pearl1 2 with dissolve

    "Okay"
    "Here we go"
    "Time to be a good host"
    "You have to suppress a laugh hearing Pearl psych herself up for handjob."
    "Deciding not to put her off, you keep your composure."
    "She hesitates for a moment as her hands hover around your proud member."

    show pearl1 3 with dissolve

    "One of her hands circles around the base of your dick."
    "The other focuses on spreading lubricant around the top of your head."
    "Her hands meet in the middle and vary their pressure as they glide around your prick."
    "Has she practiced this before?"
    "She looks pretty cute, the way she's focused solely on your satisfaction."
    "Its like watching a dance, the way her fingers glide and rub everywhere they can, like graceful spiders."
    "She stops for a moment to rub the underside of your shaft with her thumb."
    "One moment she's rubbing in little circles."
    "The next, she's making a cage with her fingers and sliding them up and down."
    "Each sensation never lasts too long, as she teases you with different motions."

    show pearl1 4 with dissolve

    "You begin to notice that you're letting out little gasps of pleasure."
    "Your hands grab at the bed sheets."
    "Pearl seems not to notice, her concentration never letting up."
    "Instead, she just strokes faster, probably sensing that you're getting close."
    "The unsubtle “shlicking” sounds of a dick being whipped to climax hit your ears."
    "Good thing Amethyst's room is in a different dimension."
    "Your head leans back on its own"
    m "Pearl, I'm... I'm close..."

    show pearl1 5 with dissolve

    "Oh yeah, {i}that{/i} part."
    "I would appreciate if you waited until I was out of the way [playerName]."
    "I don't appreciate being covered in those fluids you humans are so fond of"

    show pearl1 6 with dissolve

    "Pearl's indifference about the whole situation is just the trigger to set you off."
    "You shoot a long rope of cum in her direction."
    "Her surprise at being caught mid-sentence foils any chance at it missing her."
    "Before she has a chance to recover, you're already letting loose multiple smaller spurts."

    show pearl1 7 with dissolve

    "Her hands are absolutely covered in your semen, and a long trail of it hangs down from her porcelain face."
    p "Uck, it's everywhere"
    m "Eh sorry, Pearl."
    m "I guess you did too good of a job, huh?"
    "You laugh nervously as Pearl gets up to leave."

    scene bg house night with dissolve
    "She walks out of your room to clean herself up, but not before you spot a warm smile."



    jump living_room

return
