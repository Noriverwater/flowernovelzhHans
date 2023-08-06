define config.language = "schinese"
        
screen infoscreen:
    modal True
    window:
        style "default_window"
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at windowtrans
        add "gui/staff/infobg.png"
        if _preferences.language == "schinese":
            imagebutton idle 'gui/staff/cn_idle.png' hover 'gui/staff/cn_hover.png' action ShowMenu("infocnscreen") xpos 440 ypos 289 xalign 0.0 yalign 0.0
        if renpy.android or renpy.ios:
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
                add 'gui/help/pc/bg_1.png'
                if renpy.macintosh:
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
                ypos 364
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
                ypos 440
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
                ypos 516
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
                ypos 597
                xmaximum 76
                ymaximum 76
                xminimum 76
                yminimum 76
                add 'gui/help/pc/icon_6.png' xalign 0.5 yalign 0.5 xpos 0.5 ypos 0.5 at btnzoomtr
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
        add "gui/staff/infocn.png"
        text "关于《夏末盛开的花》非官方中文化补丁 2.1" color "#ffffffc5" font "fonts/NanumSquareB.ttf" xpos 71 ypos 42 size 40
        text "您好，看到这意味着您已经启用了\"{font=fonts/NanumSquareacEB.ttf}여름의 끝에 피는 꽃(Flowers Blooming at the End of Summer){/font}\"的粉丝汉化补丁 2.1。\n请注意，最重要的事情是，这个补丁以完全免费的形式公开，译文也以 {a=https://creativecommons.org/licenses/by-nc-sa/4.0/deed.zh}CC-BY-NC-SA 4.0{/a} 的形式托管在Github上。实际上，游戏本体也是以完全免费的形式{a=https://store.steampowered.com/app/1173010}发行{/a}的，尽管也有赞助性质，价格6元，游戏本体内容与免费版一致的Steam Edition。因此，严禁将本补丁用于任何形式的商业用途，如果您花了钱才体验到这个补丁的内容，说明您被忽悠了。\n其次，这个补丁与 MidnightWorks 官方无关，仅供学习参考使用。补丁所提供的部分译文可能非常不靠谱，因此不能与原版游戏等同。如果您有能力建议游玩原版游戏以获得最好的游戏体验。\n这个补丁的公开发布已获得官方的许可，在已阅读并同意以上文字，且遵循发行商 PsychoFlux Entertainment 的{a=https://www.psychoflux.com/legal/video-policy/}规则{/a}，您被赋予在流媒体视频网站上直播或录播该补丁内容的权力。\n继续使用该补丁意味着您已知悉以上内容，且已确认游戏内容完全符合您所在地相关法律法规、宗教和风俗的要求。\n这个补丁首发于百度贴吧galgame吧（已不再更新）和Steam社区指南（已经被ban了），其余注意事项和疑问详见{a=https://github.com/Noriverwater/flowernovelzhHans/}github{/a}页。只要这个补丁能对您有帮助，我就已经很高兴了。" color "#ffffff90" font "fonts/NanumSquareB.ttf" xpos 71 ypos 118 xmaximum 1140 size 20 line_spacing 20
        imagebutton idle 'gui/staff/btnclose_idle.png' hover 'gui/staff/btnclose_hover.png' action Hide("infocnscreen") xpos 1108 ypos 553 xalign 0.0 yalign 0.0




screen licensescreen_1:
    modal True
    window:
        style "default_window"
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at windowtrans
        add "gui/license/licensedark2.png"
        if _preferences.language == "schinese":
            imagebutton idle 'gui/license/licenselink1.png' hover 'gui/license/licenselink1_.png' xpos 380 ypos 296 action OpenURL("https://www.renpy.org/doc/html/license.html")
        else:
            imagebutton idle 'gui/license/licenselink1.png' hover 'gui/license/licenselink1_.png' xpos 328 ypos 299 action OpenURL("https://www.renpy.org/doc/html/license.html")
        imagebutton idle 'gui/license/licenselink2.png' hover 'gui/license/licenselink2_.png' xpos 372 ypos 380 action OpenURL("https://www.renpy.org/doc/html/license.html")
        if renpy.windows or renpy.macintosh or renpy.linux:
            imagebutton idle 'gui/license/openfolder_idle.png' hover 'gui/license/openfolder_hover.png' action Function(folder_open, config.gamedir + "/License/Open Source License") xpos 70 ypos 206 xalign 0.0 yalign 0.0
        imagebutton idle 'gui/staff/btnclose_idle.png' hover 'gui/staff/btnclose_hover.png' action Hide("licensescreen_1") xpos 1108 ypos 553 xalign 0.0 yalign 0.0
        
        vbox:
            xalign 0.0
            yalign 0.0
            xpos 57
            ypos 454
            spacing 3
            hbox:
                xalign 0.0
                yalign 0.0
                spacing 2
                imagebutton idle 'gui/license/lc1.png' hover 'gui/license/lc1_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/GNU Lesser General Public License") ]
                imagebutton idle 'gui/license/lc2.png' hover 'gui/license/lc2_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Python License") ]
                imagebutton idle 'gui/license/lc3.png' hover 'gui/license/lc3_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Jpeg License") ]
            hbox:
                xalign 0.0
                yalign 0.0
                spacing 2
                imagebutton idle 'gui/license/lc4.png' hover 'gui/license/lc4_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/PNG License") ]
                imagebutton idle 'gui/license/lc5.png' hover 'gui/license/lc5_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Zlib License") ]
                imagebutton idle 'gui/license/lc6.png' hover 'gui/license/lc6_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Bzip2 License") ]
                imagebutton idle 'gui/license/lc7.png' hover 'gui/license/lc7_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Modified BSD License") ]
            hbox:
                xalign 0.0
                yalign 0.0
                spacing 2
                imagebutton idle 'gui/license/lc8.png' hover 'gui/license/lc8_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Artistic License") ]
                imagebutton idle 'gui/license/lc9.png' hover 'gui/license/lc9_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Apache License 2.0") ]
                imagebutton idle 'gui/license/lc10.png' hover 'gui/license/lc10_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Open Source License/Mozilla Public License 2.0") ]

screen licensescreen_2:
    modal True
    window:
        style "default_window"
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at windowtrans
        add "gui/license/licensedark.png"
        vbox:
            xpos 315
            ypos 275
            spacing -1
            imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Markazi Text") ]
            imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/M Plus Rounded 1c") ]
            imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Sarabun") ]
            imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Work Sans") ]
            imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Raleway") ]
            imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Gothic A1") ]
        vbox:
            xpos 670
            ypos 275
            spacing -1
            if _preferences.language == "schinese":
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/975maru") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Source Han") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Source Han") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Yozai Font") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/LxgwWenKai") ]
            else:
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Naver Nanum Fonts") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Naver Nanum Fonts") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Naver Nanum Fonts") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Naver Nanum Fonts") ]
                imagebutton idle 'gui/license/licensebtn.png' hover 'gui/license/licensebtn_.png' action [ ShowMenu("licensewindow"), SetVariable("load_license", "Fonts/Arita Fonts") ]
        
        if renpy.windows or renpy.macintosh or renpy.linux:
            imagebutton idle 'gui/license/openfolder_idle.png' hover 'gui/license/openfolder_hover.png' action Function(folder_open, config.gamedir + "/License/Fonts") xpos 71 ypos 624 xalign 0.0 yalign 0.0

        imagebutton idle 'gui/staff/btnclose_idle.png' hover 'gui/staff/btnclose_hover.png' action Hide("licensescreen_2") xpos 1108 ypos 553 xalign 0.0 yalign 0.0
