# GUI - DEFAULT

define config.font_name_map = {"975SCHans": FontGroup().add("tl/schinese/fonts/975maru.ttf", 0x0020, 0x007f).add("tl/schinese/fonts/Lxgw975HazyGoSC-500W.ttf", 0x0000, 0xffff)}

translate schinese style default: #sans-serif
    font "tl/schinese/fonts/ChillDuanSans_Medium.otf"
    language "japanese-loose"

translate schinese style default_bold is default: #sans-serif
    font "tl/schinese/fonts/ChillDuanSans_Bold.otf"


# GUI - LICENSE

translate schinese style license_font: #Noto Sans
    font "fonts/NotoSansMonoCJKsc-Regular.otf"

translate schinese style license_description_1 is default: #sans-serif
    size 27.49
    line_spacing 15.2
    color "#ffffff99"

translate schinese style license_description_2 is default: #sans-serif
    size 16.35
    line_spacing 4.2
    color "#ffffff99"


# GUI - HISTORY

translate schinese style history_text: #rounded sans-serif
    # font "tl/schinese/fonts/ChillRoundFBold.otf"
    font "975SCHans"
    language "japanese-loose"

translate schinese style history_name_text: #serif
    font "tl/schinese/fonts/LxgwWenKai.ttf"

translate schinese style choice_pick_text is default #sans-serif


# GUI - OTHERS

translate schinese style navi_music_name_text is default_bold: #bold sans-serif
    kerning -0.5


# DIALOGUE - SCRIPT

translate schinese style dialogue_text_base: #rounded sans-serif
    # font "tl/schinese/fonts/ChillRoundFBold.otf"
    font "975SCHans"
    size 24
    color "#ffffff"
    language "japanese-loose"
    line_spacing 10.5
    line_overlap_split -2

translate schinese style dialogue_text is dialogue_text_base:
    pos (202, 557)
    xsize 760

translate schinese style dialogue_text_letterbox is dialogue_text_base:
    pos (154, 631)
    xsize 900

translate schinese style say_dialogue is dialogue_text:
    line_spacing 10.5


# DIALOGUE - NAME

translate schinese style dialogue_name_text:
    font "tl/schinese/fonts/LxgwWenKai.ttf"
    size 33
    color "#ffffff"
    anchor (0.5, 0.5)
    pos (119, 603)

translate schinese style dialogue_name_text_letterbox is dialogue_name_text:
    size 31
    anchor (1.0, 0.5)
    pos (115, 648)


# DIALOGUE - NVL

translate schinese style dialogue_nvl_text:
    font "tl/schinese/fonts/LxgwWenKai.ttf"
    size 37
    language "korean-with-spaces"
    color "#ffffff"
    align (0.5, 0.5)
    line_spacing 8
    xsize 1000
    textalign 0.5
"""
translate schinese style glossary_tooltiptext: #rounded sans-serif
    language "unicode"
    size 20
    line_leading 5
    line_spacing 5
"""

# OTHERS

translate schinese style default_frame_staff:
    background None
    xpos 20
    align (0,0)
    padding (0,0,0,0)
    margin (0,0,0,0)

translate schinese style language_labs_onoff_button is default:
    color "#ffffffB3"
    line_leading 1
    size 19.54

translate schinese style dlc_button_title:
    first_indent -10
    size 18.44
    color '#ffffffa8'

# SYSTEM

translate schinese python:
    gui.system_font = u'tl/schinese/fonts/ChillDuanSans_Medium.otf'
    gui.font = u'tl/schinese/fonts/ChillDuanSans_Medium.otf'

