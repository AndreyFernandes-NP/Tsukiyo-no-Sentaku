label classroom:
    $ qc_menu('hide')

    pause(2.5)

    $ qc_menu('show')

    mc "…"
    mc "Miya?"

    $ qc_menu('hide')

    play sound sfx_cg_woosh
    scene cg miya_classroom_moonlight:
        truecenter
        zoom 1.2 rotate -5 subpixel True
        easein 7.0 zoom 1.0 rotate 0
    with flash
        
    play music music_happy_girl fadein 0.1

    with Pause(7.0)

    $ qc_menu('show')

    "…"

    jump end_of_build
    return