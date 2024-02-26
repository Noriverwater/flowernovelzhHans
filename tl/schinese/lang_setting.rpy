init -1:
    $ languagelist.append(("简体中文{size=*0.6}fan-made{/size}", "schinese", "Simplified Chinese", "tl/schinese/fonts/DreamHanSans.ttf", "tl/schinese/fonts/975maru.ttf", "japanese-loose", "zh", "hans", ("cn", "sg"), "reboot-1.0"))

    $ fontlist.append(("975 圆体", "tl/schinese/fonts/DreamHanSans.ttf", "License/Fonts/975maru.txt"))
    $ fontlist.append(("思源黑体", "tl/schinese/fonts/DreamHanSans.ttf", "License/Fonts/Source Han.txt"))
    $ fontlist.append(("思源宋体", "tl/schinese/fonts/DreamHanSans.ttf", "License/Fonts/Source Han.txt"))
    $ fontlist.append(("悠哉字体", "tl/schinese/fonts/DreamHanSans.ttf", "License/Fonts/Yozai Font.txt"))
    $ fontlist.append(("霞鹜文楷", "tl/schinese/fonts/DreamHanSans.ttf", "License/Fonts/LxgwWenKai.txt"))


screen infoscreen:
    modal True
    window:
        style "default_window"
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at windowtrans
        if renpy.android or renpy.ios:
            add "gui/staff/infobg.png"
            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 290
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/btn1.png' xalign 0.5 yalign 0.5 xpos 0.5 ypos 0.5 at btnzoomtr
            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 364
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/btn2.png' xalign 0.5 yalign 0.5 xpos 0.5 ypos 0.5 at btnzoomtr
            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 440
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/bar1.png'
                add 'gui/help/one.png' at one1
            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 516
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/bar3.png'
                add 'gui/help/one.png' at one3
            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 597
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/bar4.png'
                add 'gui/help/one.png' at one4
        else:
            add "gui/staff/infobg_pc.png"
            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 216
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/pc/bg_1.png'
                if renpy.macintosh == True:
                    add 'gui/help/pc/icon_1_1_mac.png' at icon11tr
                else:
                    add 'gui/help/pc/icon_1_1.png' at icon11tr
                add 'gui/help/pc/icon_1_2.png' at icon12tr
                add 'gui/help/pc/icon_1_3.png' at icon13tr

            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 292
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/pc/icon_2.png' xalign 0.5 yalign 0.5 xpos 0.5 ypos 0.5 at btnzoomtr

            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 366
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/pc/bg_3.png'
                add 'gui/help/pc/icon_3.png' at icon3tr

            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 442
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/pc/bg_5.png'
                add 'gui/help/pc/icon_5_1.png' at icon51tr
                add 'gui/help/pc/icon_5_2.png' at icon52tr

            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 520 #451
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/pc/icon_6.png' xalign 0.5 yalign 0.5 xpos 0.5 ypos 0.5 at btnzoomtr

            window:
                style "default_window"
                xalign 0
                yalign 0
                xpos 54
                ypos 597
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/pc/icon_7.png' xalign 0.5 yalign 0.5 xpos 0.5 ypos 0.5 at btnzoomtr
        if _preferences.language == "schinese":
            imagebutton idle 'tl/schinese/gui/staff/cn_idle.png' hover 'tl/schinese/gui/staff/cn_hover.png' action ShowMenu("infocnscreen") xpos 440 ypos 289 xalign 0.0 yalign 0.0
        imagebutton idle 'gui/staff/btnclose_idle.png' hover 'gui/staff/btnclose_hover.png' action Hide("infoscreen") xpos 1108 ypos 553 xalign 0.0 yalign 0.0


screen infocnscreen:
    modal True
    window:
        style "default_window"
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at windowtrans
        add Solid("#000000F0")
        text "关于《夏末盛开的花》非官方中文化补丁" color "#ffffffc5" xpos 71 ypos 42 size 40
        text "看到这里意味着您已经启用了\"{font=fonts/NanumSquareacEB.ttf}여름의 끝에 피는 꽃(Flowers Blooming at the End of Summer){/font}\"的粉丝汉化补丁。\n这个补丁的译文是自由使用的，您拿去做什么都可以。但是图片不行，对它们二次创作前需要征求MidnightWorks的意见。\n补丁的绝大部分内容是我们在《夏花》刚发售不久后，实力不足的时候制作的，本质上还是一个机器翻译补丁。\n这些译文可能不太靠谱，所以如果您认为《夏花》的剧情或文笔有问题，那大概率是这些破烂译文的问题，而不是《夏花》本身的问题。\n如果您有能力的话，希望您还是啃生肉。\n\n但是，我很难有时间和精力去更正这些问题。如果您打算帮助我们改一改的话，我会非常感激的……为了让我知道您的联系方式，您可以前往这个补丁在{a=https://github.com/Noriverwater/flowernovelzhHans/blob/main/}Github上的发布页{/a}提交Issues。\n\n最后，希望这个补丁能对您有帮助。" color "#ffffff90" xpos 71 ypos 118 xmaximum 1140 size 20 line_spacing 20
        imagebutton idle 'gui/staff/btnclose_idle.png' hover 'gui/staff/btnclose_hover.png' action Hide("infocnscreen") xpos 1108 ypos 553 xalign 0.0 yalign 0.0
