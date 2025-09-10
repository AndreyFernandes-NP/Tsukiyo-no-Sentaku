screen language_select:
    modal True
    tag menu
    
    add Solid("#00000080")

    frame:
        align (0.5, 0.5)
        padding (100, 100)

        vbox:
            spacing 35
            xalign 0.5

            text "Choose your Language":
                size 42
                xalign 0.5
                color "#FFFFFF"
                font "fonts/font_title.ttf"

            textbutton "Português (Brasil)":
                style "lang_button"
                action [SetVariable("persistent.choosen_language", "Portuguese"), Language('portuguese'), Return()]

            textbutton "English":
                style "lang_button"
                action [SetVariable("persistent.choosen_language", "English"), Language(None), Return()]

            textbutton "日本語":
                style "lang_button"
                text_font "fonts/VL-PGothic-Regular.ttf"
                action [SetVariable("persistent.choosen_language", "Japanese"), Language('japanese'), Return()]