# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c_s = Character("Cadence", what_prefix="\"", what_suffix="\"")   #cadence speaking
define c_t = Character("Cadence")                                       #cadence thinking
define h = Character("Harvey")                                          #harvey
define b = Character("Bobby")                                           #bobby (hookup)
define q = Character("Quinten")                                         #quinten (roommate)

transform Speaker_Body(frame1, frame2, frame3):
    frame1
    0.15
    frame2
    0.15
    frame3
    0.15
    repeat

transform Speaker_FaceFeature(frame1, frame2, frame3, frame4, frame5):
    frame1
    0.15
    frame2
    0.15
    frame3
    0.15
    frame4
    0.15
    frame5
    0.15
    repeat

transform portrait:
    xpos 1144
    ypos 0
    xsize 776
    ysize 1080

layeredimage speaker c:
    group body:
        attribute body default:
            Speaker_Body("c_body_1", "c_body_2", "c_body_3")
    group eyes:
        attribute neutral default:
            Speaker_FaceFeature("c_eyes_neutral_1","c_eyes_neutral_2","c_eyes_neutral_3","c_eyes_neutral_4","c_eyes_neutral_5")
    group eyebrows:
        attribute neutral default:
            Speaker_FaceFeature("c_eyebrows_neutral_1","c_eyebrows_neutral_2","c_eyebrows_neutral_3","c_eyebrows_neutral_4","c_eyebrows_neutral_5")
    group mouth:
        attribute revd default:
            Speaker_FaceFeature("mouth_3_1","mouth_3_2","mouth_3_3","mouth_3_4","mouth_3_5")

label start:
    scene black

    #show cubes 53
    
    show speaker c at portrait

    c_s "I gotta stick my dick in the record hole."

    return
