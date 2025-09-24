define narrator = Character(None, kind=nvl, what_color="#c9c9c9")
define c_s = Character("Cadence", color="#ff6600", kind=nvl, what_prefix="\"", what_suffix="\"")   #cadence speaking
define c_t = Character("Cadence", color="#ff6600", kind=nvl)                                       #cadence thinking
define h = Character("Harvey", color="#ffffff", what_prefix="\"", what_suffix="\"")      #harvey
define b = Character("Bobby", color="#ffffff", what_prefix="\"", what_suffix="\"")       #bobby (hookup)
define q = Character("Quinten", color="#ffffff", what_prefix="\"", what_suffix="\"")     #quinten (roommate)

transform bg:
    xpos 240
    ypos 0
    ysize 1080
    xsize 1440

transform BodyAnim(frame1, frame2, frame3):
    frame1
    0.15
    frame2
    0.15
    frame3
    0.15
    repeat

transform NakedAnim(frame1, frame2, frame3, frame4):
    frame1
    0.15
    frame2
    0.15
    frame3
    0.15
    frame4
    0.15
    repeat

transform FacialFeatureAnim(frame1, frame2, frame3, frame4, frame5):
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

image cadence_showcase_eyes:
    "eyes_neutral_1"
    0.15
    "eyes_angry_1"
    0.15
    "eyes_open_1"
    0.15
    "eyes_sad_1"
    0.15
    "eyes_squint_1"
    0.15
    "eyes_tired_1"
    0.15
    repeat

image cadence_showcase_eyebrows:
    "eyebrows_neutral_1"
    0.15
    "eyebrows_angry_1"
    0.15
    "eyebrows_sad_1"
    0.15
    "eyebrows_confused_1"
    0.15
    repeat

image cadence_showcase_mouth:
    "mouth_neutral_1"
    0.15
    "mouth_3_1"
    0.15
    "mouth_d_1"
    0.15
    "mouth_o_1"
    0.15
    "mouth_perv_1"
    0.15
    "mouth_revd_1"
    0.15
    "mouth_revv_1"
    0.15
    "mouth_smirk_1"
    0.15
    "mouth_wedge_1"
    0.15
    repeat

image bobby:
    "bobby1"
    0.15
    "bobby2"
    0.15
    "bobby3"
    0.15
    "bobby4"
    0.15
    repeat

image nvl_anim:
    "nvl1"
    .15
    "nvl2"
    .15
    "nvl3"
    .15
    "nvl4"
    .15
    repeat

#region BGs

image a_station:
    "station1"
    0.05
    "station2"
    0.05
    "station3"
    0.05
    repeat

image a_cubes:
    "cubes1"
    0.05
    "cubes2"
    0.05
    "cubes3"
    0.05
    repeat

image a_pillars:
    "pillars1"
    0.05
    "pillars2"
    0.05
    "pillars3"
    0.05
    repeat

image a_racks:
    "racks1"
    0.05
    "racks2"
    0.05
    "racks3"
    0.05
    repeat

image a_records:
    "records1"
    0.05
    "records2"
    0.05
    "records3"
    0.05
    repeat

image a_cds:
    "cds1"
    0.05
    "cds2"
    0.05
    "cds3"
    0.05
    repeat

image a_home:
    "home1"
    0.05
    "home2"
    0.05
    "home3"
    0.05
    repeat

#endregion

transform portrait:
    xpos 1144
    ypos 0
    xsize 776
    ysize 1080

transform person:
    xpos 425
    ypos 0
    xsize 540
    ysize 820

layeredimage cadence:
    group body:
        attribute body default:
            BodyAnim("body_1", "body_2", "body_3")
        attribute naked:
            NakedAnim("naked_1", "naked_2", "naked_3", "naked_4")
    group eyes:
        attribute halfopen default:
            FacialFeatureAnim("eyes_neutral_1","eyes_neutral_2","eyes_neutral_3","eyes_neutral_4","eyes_neutral_5")
        attribute angry:
            FacialFeatureAnim("eyes_angry_1","eyes_angry_2","eyes_angry_3","eyes_angry_4","eyes_angry_5")
        attribute open:
            FacialFeatureAnim("eyes_open_1","eyes_open_2","eyes_open_3","eyes_open_4","eyes_open_5")
        attribute sad:
            FacialFeatureAnim("eyes_sad_1","eyes_sad_2","eyes_sad_3","eyes_sad_4","eyes_sad_5")
        attribute squint:
            FacialFeatureAnim("eyes_squint_1","eyes_squint_2","eyes_squint_3","eyes_squint_4","eyes_squint_5")
        attribute tired:
            FacialFeatureAnim("eyes_tired_1","eyes_tired_2","eyes_tired_3","eyes_tired_4","eyes_tired_5")
        attribute showcase:
            "cadence_showcase_eyes"
    group eyebrows:
        attribute straight default:
            FacialFeatureAnim("eyebrows_neutral_1","eyebrows_neutral_2","eyebrows_neutral_3","eyebrows_neutral_4","eyebrows_neutral_5")
        attribute incl:
            FacialFeatureAnim("eyebrows_angry_1","eyebrows_angry_2","eyebrows_angry_3","eyebrows_angry_4","eyebrows_angry_5")
        attribute decl:
            FacialFeatureAnim("eyebrows_sad_1","eyebrows_sad_2","eyebrows_sad_3","eyebrows_sad_4","eyebrows_sad_5")
        attribute confused:
            FacialFeatureAnim("eyebrows_confused_1","eyebrows_confused_2","eyebrows_confused_3","eyebrows_confused_4","eyebrows_confused_5")
        attribute showcase:
            "cadence_showcase_eyebrows"
    group mouth:
        attribute line default:
            FacialFeatureAnim("mouth_neutral_1","mouth_neutral_2","mouth_neutral_3","mouth_neutral_4","mouth_neutral_5")
        attribute three:
            FacialFeatureAnim("mouth_3_1","mouth_3_2","mouth_3_3","mouth_3_4","mouth_3_5")
        attribute d:
            FacialFeatureAnim("mouth_d_1","mouth_d_2","mouth_d_3","mouth_d_4","mouth_d_5")
        attribute o:
            FacialFeatureAnim("mouth_o_1","mouth_o_2","mouth_o_3","mouth_o_4","mouth_o_5")
        attribute perv:
            FacialFeatureAnim("mouth_perv_1","mouth_perv_2","mouth_perv_3","mouth_perv_4","mouth_perv_5")
        attribute revd:
            FacialFeatureAnim("mouth_revd_1","mouth_revd_2","mouth_revd_3","mouth_revd_4","mouth_revd_5")
        attribute revv:
            FacialFeatureAnim("mouth_revv_1","mouth_revv_2","mouth_revv_3","mouth_revv_4","mouth_revv_5")
        attribute smirk:
            FacialFeatureAnim("mouth_smirk_1","mouth_smirk_2","mouth_smirk_3","mouth_smirk_4","mouth_smirk_5")
        attribute wedge:
            FacialFeatureAnim("mouth_wedge_1","mouth_wedge_2","mouth_wedge_3","mouth_wedge_4","mouth_wedge_5")
        attribute showcase:
            "cadence_showcase_mouth"