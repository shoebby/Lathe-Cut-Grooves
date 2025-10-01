label saline:
    scene black
    play music "headsounds.ogg" fadein 10
    play sound "doorclose.ogg"

    show cadence wedge angry incl at portrait
    c_s "What a fucking asshole."

    show cadence revd angry incl at portrait
    c_s "And a PERV!"

    show cadence revd squint incl at portrait
    c_s "GOD."

    show cadence revv sad incl at portrait
    c_s "..."

    show cadence revd angry incl at portrait
    c_s "GOD!"

    show cadence wedge angry incl at portrait
    "She's mad."
    "She's really really -really- mad."
    "Mostly because she is really really -really- sad."
    
    show cadence revv sad incl at portrait
    "She grabs her medicine box to disinfect and dress some of her wounds."
    "She thinks she doesn't deserve to treat all of them."

    show cadence o sad decl at portrait
    c_s "Ow..."

    show cadence revv sad decl at portrait
    "After a few moments most of them are addressed."
    "Her split lip."
    "Her split knuckles."
    "Her swollen cheeks."
    show cadence smirk sad decl at portrait
    "(both sets)"
    show cadence revv sad decl at portrait
    "Dinner can wait."
    "She needs to submerge herself in her ritual."

    show cadence o halfopen confused at portrait
    c_t "Let's start with..."

    show cadence revv halfopen confused at portrait
    c_t "Hmmm..."

    show cadence three open straight at portrait
    c_s "Jelly Tones."

    hide cadence
    show a_sigil at bg with Dissolve(2.0)
    show cadence three open straight at portrait
    "She rolls up a musty rug, revealing an intricate magic circle carved into the linoleum floor."

    show cadence d open straight at portrait
    c_s "An album by Ken Ishii."

    show cadence neutral open straight at portrait
    "She places objects on the outer ring of the circle, in 45 degree increments."

    show cadence o open confused at portrait
    c_s "Techno, illbient, futuristic."

    show cadence neutral open confused at portrait
    "The record cover, a record player, a preamp, speakers..."

    show cadence d halfopen straight at portrait
    c_s "Released in 1995, a sound arguably ahead of its time."

    show cadence neutral halfopen straight at portrait
    "A plush rabbit, a can of beer, a box cutter, a sheet of stickers."

    show cadence d open straight at portrait
    c_s "The album cover might lead you to think it's an anime OST, but it's not."
    show cadence d halfopen straight at portrait
    c_s "The track 'Extra' does have an animated music videos directed by Koji Morimoto, though."

    show cadence naked neutral halfopen straight at portrait
    "She undresses, down to her socks and undies and sits down in the middle of the circle, with her laptop in her lap."

    stop music fadeout 2.0
    show cadence o halfopen straight at portrait
    c_s "Let's begin."

    show cadence smirk open straight at portrait
    "She turns on the record player and presses record in Audacity."
    play music "jellytones.wav" fadein 2.0 volume 0.5
    "First nothing but crackle, then, waves of music wash over her."
    show cadence smirk tired decl at portrait
    "Her head is finally quiet."
    "Nothing going on, nothing to worry about."
    "Worries washed away for a time, she can sit and do nothing."
    "She doesn't even feel guilty for it."
    "This is her peace, this is her-{nw}"

    show cadence revv open straight at portrait
    play sound "crackle6.ogg"
    $ renpy.pause(1.0, hard=True)

    show cadence scar1 revv squint incl at portrait
    play sound "slice.mp3"
    "She swipes for the box cutter and runs a cut across her shoulder."
    show cadence revv halfopen confused at portrait
    "She was probably careless, made it dirty, damaged, this is punishment."
    "Blood starts to trickle down her ar-{nw}"

    play sound "crackle1.ogg"
    $ renpy.pause(1.0, hard=True)

    show cadence scar2 wedge squint incl at portrait
    play sound "slice.mp3"
    "Another slash, this time across the side of her wrist."
    show cadence wedge sad decl at portrait
    "Blood starts to drip and seep into the reddish scars of the floor."
    show cadence three sad decl at portrait
    "Tears are welling up and her stupid dumb cunt face is flush."
    show cadence perv sad decl at portrait
    "She also has a bo-{nw}"

    play sound "crackle2.ogg"
    $ renpy.pause(1.0, hard=True)

    show cadence scar3 perv squint incl at portrait
    play sound "slice.mp3"
    "Inner thigh, every third failure deserves a special kind of pain."
    show cadence perv sad decl at portrait
    "Shoulder, wrist, thigh."
    "These are her landlines, keeping her from drifting off."
    show cadence three sad decl at portrait
    "Keeping her in check."

    play sound "crackle3.ogg"
    $ renpy.pause(1.0, hard=True)

    show cadence scar4 revv squint incl at portrait
    play sound "slice.mp3"
    "Shoulder."

    play sound "crackle4.ogg"
    $ renpy.pause(1.0, hard=True)

    show cadence scar5 wedge squint incl at portrait
    play sound "slice.mp3"
    "Wrist."

    
    play sound "crackle5.ogg"
    $ renpy.pause(1.0, hard=True)

    show cadence scar6 perv squint incl at portrait
    play sound "slice.mp3"
    "Thigh."

    show cadence perv sad decl at portrait
    c_s "Hff... H-hahhh..."

    show cadence perv sad confused at portrait
    "She reaches for the beer and cracks it open, taking multiple big swigs in succession."
    show cadence perv tired decl at portrait
    "With a hollow thud she slumps into a deep sleep, seeping herself into her floorboards."
    "Her new record crackling on into the night."

    hide harvey
    stop music fadeout 3.0
    hide a_sigil with Dissolve(1.0)
    $ renpy.pause(1.0, hard=True)
    hide cadence with Dissolve(2.0)
    $ renpy.pause(2.0, hard=True)

    nvl clear
    jump incense