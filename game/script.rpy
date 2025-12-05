# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mi = Character("Miya", color="#ffd700")
define mc = Character("Ren", color="#546bab")

init python:
    ambience_sfx_cycle = SfxCycler(items=corridor_ambience_sfx, interval=(20.0, 50.0), channel="ambfx", fadein=0.05, fadeout=0.05, auto_rotation_mode="all")

label splashscreen:

    scene black with fade
    with Pause(1)

    if not persistent.choosen_language:
        call screen language_select with fade
    
    window hide
    scene black with fade
    $ from_splash = True

    return

label main_menu:

    python:
        if from_splash:
            renpy.transition(Dissolve(1.0))
            from_splash = False
        menu_init()
    jump main_menu_screen

label start:
    stop music fadeout 1.0

    $ renpy.scene()
    $ renpy.block_rollback()
    nvl clear

    call future_prologue() from _calling_scene1
    jump corridors

    return

label iscene(target):
    $ scene_register(target)
    call expression target from _call_expression
    
    return

# Maybe create one for menus too? Depends if I really need it.

label future_prologue:
    scene black
    window hide
    
    $ qc_menu('hide')

    pause(2.0)

    
    play music music_peaceful fadein 2.0
    
    $ qc_menu('show')
    
    show text _("I used to think that some nights lingered in our memories by accident...") with fade
    pause
    show text _("As if certain moments only mattered because we kept circling back to them.") with fade
    pause
    show text _("People like to say life is all about choices. And they're not wrong.") with fade
    pause
    show text _("But looking back now, I feel like so many things happened simply because I never found a reason to stop them.") with fade
    pause
    show text _("Maybe that's why I stopped wondering how things could have turned out differently.") with fade
    pause
    show text _("By the time, I got used to the idea that nothing really needed to matter that much.") with fade
    pause
    show text _("Even so, some memories kept coming back.") with fade
    pause
    show text _("Not because they were special, but because somehow, they never really left.") with fade
    pause
    show text _("It was on a day like that when everything felt a little different, though I couldn't have explained why.") with fade
    pause
    show text _("It was the final week of high school. By then, I was showing up more out of routine than anything else.") with fade
    pause
    show text _("Soon, it would all be over. I'd start college and stop seeing all the people I'd known for years.") with fade
    pause
    show text _("Even if that sounded sad, I didn't feel much of anything. It bothered me, but somehow, it didn't seem to matter either.") with fade
    pause
    show text _("That afternoon, she'd sent me a message, telling me to come by the school later that night.") with fade
    pause
    show text _("We'd been talking less and less lately, so it caught me off guard.") with fade
    pause
    show text _("It was the sort of thing she did sometimes, just to see how far I'd go to play along.") with fade
    pause
    show text _("I didn't really believe it meant anything. Maybe that's exactly why I decided to go on.") with fade
    pause
    show text _("There was no one else left at school. It was already close to eleven when I climbed over the wall and walked into the main hall.") with fade
    pause
    show text _("I made my way up the stairs slowly and stopped in front of a door.") with fade
    pause
    show text _("Just an ordinary door, like any other classroom. But it was the door to our room.") with fade
    pause
    show text _("I didn't have any expectations, no certainty that anyone would be waiting.") with fade
    pause
    show text _("For a moment, I even thought turning back. Pretending I'd fallen for her last end-of-year prank and that it had been a good one.") with fade
    pause
    show text _("But part of me wanted to believe it was something more, that there was some reason I was standing there.") with fade
    pause
    show text _("Maybe, I just needed to prove to myself that nothing had changed between us. Or that there was still something left to say.") with fade
    pause
    show text _("At that time, everything seemed a little less real. Like I had the feeling that any answer wouldn't really matter.") with fade
    pause
    show text _("In the end, all I knew I could do was open the door.") with fade
    pause

    hide text
    with contextchange

    stop music fadeout 1.0
    with Pause(1.5)

    return

label end_of_build:
    scene black with scenechange
    window hide

    $ qc_menu('hide')

    pause(2.0)

    $ qc_menu('show')

    show text "Tsukiyo no Sentaku - Fim da Build v[config.version]" with fade
    pause

    return