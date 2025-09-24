label splashscreen:
    scene black
    show splash with Dissolve(2)
    #play music pressing
    $ renpy.pause(2.0, hard=True)
    hide splash with Dissolve(2)
    #stop music
    #queue sound chaptercard
    #scene splash2
    #$ renpy.pause(0.5, hard=True)
    return