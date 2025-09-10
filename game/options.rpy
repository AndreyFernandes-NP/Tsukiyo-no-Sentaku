define config.name = _("Tsukiyo no Sentaku")
define build.name = "TsukiyonoSentaku"

init -999:
    define config.developer = True
    define config.defer_tl_scripts = True
    define config.version = "0.1"
    define config.transparent_tile = False

    define config.autosave_slots = 4
    define config.quicksave_slots = 4
    define config.log = "development_log.txt"

    define config.narrator_menu = True
    define choice_delay = 0.5

init python:
    def _amb_sync_with_state():
        ch = "ambfx"

        try:
            inst = ambience_sfx_cycle
        except NameError:
            inst = None

        if inst and inst.running:
            return

        renpy.music.set_queue_empty_callback(None, channel=ch)
        if renpy.music.is_playing(channel=ch):
            renpy.music.stop(channel=ch, fadeout=0.05)

    config.start_interact_callbacks.append(_amb_sync_with_state)
    config.after_load_callbacks.append(_amb_sync_with_state)


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.
define gui.about = _p("""
""")


## Sounds and music ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "audio/music/Wiosna.ogg"


## Transitions #################################################################

## Entering or exiting the game menu.
define config.enter_transition = dissolve
define config.exit_transition = dissolve

## Between screens of the game menu.
define config.intra_transition = dissolve

## A transition that is used after a game has been loaded.
define config.after_load_transition = dissolve

## Used when entering the main menu after the game has ended.
define config.end_game_transition = None


## Window management ###########################################################
define config.window = "auto"
define config.gl_resize = False


## Transitions used to show and hide the dialogue window
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.
default preferences.text_cps = 60

## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.
default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "TsukiyonoSentaku-1750652344"



## The icon displayed on the taskbar or dock.
define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.archive('script','all')
    build.archive('gui','all')
    build.archive('audio','all')
    build.archive('sprites','all')
    build.archive('bgs','all')
    build.archive('fonts','all')

    build.classify('game/script/**','script')

    build.classify('game/bgs/**','bgs')

    build.classify('game/sprites/**','sprites')

    build.classify('game/gui/**','gui')

    build.classify('game/audio/**','audio')

    build.classify('game/**.ttf','fonts')
    build.classify('game/fonts/**.ttf','fonts')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
