define config.language = "chinese"
#define config.has_autosave = True
#define config.autosave_on_choice = True
#define config.autosave_on_quit = True

screen say:

    # side_image 와 two_window 의 기본값
    default side_image = None
    default two_window = False

    # 창을 1개 사용할지, 2개 사용할지 결정합니다.
    if not two_window:

        # 창을 1개 쓰는 대사창
        window:
            id "window"
            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # 이름과 대사, 창을 2개 쓰는 대사창
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # 사이드 이미지가 있다면 텍스트 위에 표시한다.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu
    key "mousedown_4" action ShowMenu('text_history')
    key "mousedown_5" action RollForward


screen file_picker:
    key "s" action NullAction()
    #key "n" action NullAction()
    if mainwindow == True:
        if persistent.gameend == 1:
            if persistent.giveher == 1:
                if renpy.android == True or renpy.ios == True:
                    add 'gui/blur/0/android/menu.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0 at mainblur
                else:
                    add 'gui/blur/0/steam/menu.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0 at mainblur
            else:
                if renpy.android == True or renpy.ios == True:
                    add 'gui/blur/1/android/menu.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0 at mainblur
                else:
                    add 'gui/blur/1/steam/menu.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0 at mainblur
        else:
            if renpy.android == True or renpy.ios == True:
                add 'gui/blur/0/android/menu.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0 at mainblur
            else:
                add 'gui/blur/0/steam/menu.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0 at mainblur


    window:
        top_margin 0
        bottom_margin 0
        left_margin 0
        right_margin 0
        top_padding 0
        bottom_padding 0
        left_padding 0
        right_padding 0
        background None
        foreground None
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at windowtrans
        if save:
            add 'gui/saveload/bg1.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0
        else:
            add 'gui/saveload/bg2.png' xalign 0.0 yalign 0.0 xpos 0 ypos 0
        default page_name_value = FilePageNameInputValue(pattern=_("{}페이지"), auto=_("자동저장"), quick=_("퀵세이브 목록"))
        default page_name_value_eng = FilePageNameInputValue(pattern=_("PAGE{}"), auto=_("AUTOSAVE"), quick=_("QUICKSAVE"))
        default setpg = FilePageName(auto='a', quick='q')
        
        if save:
            imagebutton idle 'gui/settings/btnclose_idle.png' hover 'gui/settings/btnclose_hover.png' action Hide("save") xpos 1130 ypos 360 xalign 0.5 yalign 0.5
        else:
            imagebutton idle 'gui/settings/btnclose_idle.png' hover 'gui/settings/btnclose_hover.png' action Hide("load") xpos 1130 ypos 360 xalign 0.5 yalign 0.5
        


        if setpg == 'a' or setpg == 'q':
            imagebutton idle 'gui/saveload/alpha.png' hover 'gui/saveload/alpha.png' action FilePage("1")
            vbox:
                xalign 0.0
                yalign 0.5
                xpos 866
                ypos 360
                spacing 9
                imagebutton idle 'gui/saveload/btnprevious_hover.png' hover 'gui/saveload/btnprevious_hover.png'
                imagebutton idle 'gui/saveload/btnnext_hover.png' hover 'gui/saveload/btnnext_hover.png'    
        else:
            vbox:
                xalign 0.0
                yalign 0.5
                xpos 866
                ypos 360
                spacing 9
                if setpg == '1':
                    imagebutton idle 'gui/saveload/btnprevious_hover.png' hover 'gui/saveload/btnprevious_hover.png'
                else:
                    imagebutton idle 'gui/saveload/btnprevious_idle.png' hover 'gui/saveload/btnprevious_hover.png' action FilePagePrevious()                 
                imagebutton idle 'gui/saveload/btnnext_idle.png' hover 'gui/saveload/btnnext_hover.png' action FilePageNext()    
        

        input:
            #style "page_label_text"
            color "#e3e3e3"
            size 31.75
            xalign 0.0
            yalign 0.0
            xpos 65
            ypos 595
            font 'fonts/NanumSquareB.ttf'
            value page_name_value 
        input:
            #style "page_label_text"
            color "#e3e3e3"
            size 11.5
            xalign 0.0
            yalign 0.0
            xpos 67
            ypos 633
            kerning 17
            font 'fonts/NanumSquareB.ttf'
            value page_name_value_eng

        
        for slotpage in range(0, 3):
            for slot in range(0, 2):
                window:
                    top_margin 0
                    bottom_margin 0
                    left_margin 0
                    right_margin 0
                    top_padding 0
                    bottom_padding 0
                    left_padding 0
                    right_padding 0
                    background None
                    foreground None
                    xalign 0
                    yalign 0
                    xpos 315 + slot * 265
                    ypos 69 + slotpage * 204
                    xminimum 258
                    yminimum 186
                    xmaximum 258
                    ymaximum 186
                    if save:
                        if setpg == 'q':
                            imagebutton idle 'gui/saveload/slot_idle.png' hover 'gui/saveload/slot_hover.png'
                        else:
                            imagebutton idle 'gui/saveload/slot_idle.png' hover 'gui/saveload/slot_hover.png' action FileSave(slotpage*2+slot+1)
                    else:
                        imagebutton idle 'gui/saveload/slot_idle.png' hover 'gui/saveload/slot_hover.png' action FileLoad(slotpage*2+slot+1)
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        xpos 0.5
                        ypos 0.56
                        spacing 5
                        add FileScreenshot(slotpage*2+slot+1) xzoom 0.5 yzoom 0.5
                        $ description = "%s \n%s" % (
                            FileTime(slotpage*2+slot+1, empty="空存档位"),
                            FileSaveName(slotpage*2+slot+1))
                        text description size 19 align (0.5, 0.5)
 
        if save:
            if setpg == 'a':
                imagebutton idle 'gui/saveload/wblank.png' hover 'gui/saveload/wblank.png' action ShowMenu("autoslot") xpos 315 ypos 69 xalign 0.0 yalign 0.0
            if setpg == 'q':
                imagebutton idle 'gui/saveload/wblank.png' hover 'gui/saveload/wblank.png' action ShowMenu("qsaveslot") xpos 315 ypos 69 xalign 0.0 yalign 0.0


        vbox:
            xalign 0.0
            yalign 1.0
            xpos 866
            ypos 655
            spacing 9
            if setpg == 'a':
                imagebutton idle 'gui/saveload/btnq_hover.png' hover 'gui/saveload/btnq_hover.png' action FilePage("quick")
                add 'gui/saveload/btna_idle.png'
            else:
                if setpg == 'q':
                    add 'gui/saveload/btnq_hover.png'
                    #imagebutton idle 'gui/saveload/btna_hover.png' hover 'gui/saveload/btna_hover.png' action FilePage("auto")
                else:
                    imagebutton idle 'gui/saveload/btnq_idle.png' hover 'gui/saveload/btnq_hover.png' action FilePage("quick")
                    #imagebutton idle 'gui/saveload/btna_hover.png' hover 'gui/saveload/btna_idle.png' action FilePage("auto")

screen licensescreen_1:
    modal True
    window:
        top_margin 0
        bottom_margin 0
        left_margin 0
        right_margin 0
        top_padding 0
        bottom_padding 0
        left_padding 0
        right_padding 0
        background None
        foreground None
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at windowtrans
        add "gui/license/licensedark2.png"
        imagebutton idle 'gui/license/licenselink1.png' hover 'gui/license/licenselink1_.png' xpos 328 ypos 299 action OpenURL("https://www.renpy.org/doc/html/license.html")
        imagebutton idle 'gui/license/licenselink1.png' hover 'gui/license/licenselink1_.png' xpos 347 ypos 160 action OpenURL("https://www.renpy.org/doc/html/license.html")
        imagebutton idle 'gui/license/licenselink2.png' hover 'gui/license/licenselink2_.png' xpos 372 ypos 380 action OpenURL("https://www.renpy.org/doc/html/license.html")
        imagebutton idle 'gui/license/lcwtf.png' hover 'gui/license/lcwtf_.png' xpos 57 ypos 59 action ShowMenu("lcwtf")
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
                imagebutton idle 'gui/license/lc1.png' hover 'gui/license/lc1_.png' action ShowMenu("lca")
                imagebutton idle 'gui/license/lc2.png' hover 'gui/license/lc2_.png' action ShowMenu("lcb")
                imagebutton idle 'gui/license/lc3.png' hover 'gui/license/lc3_.png' action ShowMenu("lcc")
            hbox:
                xalign 0.0
                yalign 0.0
                spacing 2
                imagebutton idle 'gui/license/lc4.png' hover 'gui/license/lc4_.png' action ShowMenu("lcd")
                imagebutton idle 'gui/license/lc5.png' hover 'gui/license/lc5_.png' action ShowMenu("lce")
                imagebutton idle 'gui/license/lc6.png' hover 'gui/license/lc6_.png' action ShowMenu("lcf")
                imagebutton idle 'gui/license/lc7.png' hover 'gui/license/lc7_.png' action ShowMenu("lcg")
            hbox:
                xalign 0.0
                yalign 0.0
                spacing 2
                imagebutton idle 'gui/license/lc8.png' hover 'gui/license/lc8_.png' action ShowMenu("lch")
                imagebutton idle 'gui/license/lc9.png' hover 'gui/license/lc9_.png' action ShowMenu("lci")
                imagebutton idle 'gui/license/lc10.png' hover 'gui/license/lc10_.png' action ShowMenu("lcj")

screen lcwtf:
    modal True
    window:
        top_margin 0
        bottom_margin 0
        left_margin 0
        right_margin 0
        top_padding 0
        bottom_padding 0
        left_padding 0
        right_padding 0
        background None
        foreground None
        xalign 0
        yalign 0
        xpos 0
        ypos 0
        at helptrans
        add "gui/license/licensewhite.png"
        viewport id "support_scroll":
            area (280,0,720,720)
            draggable True
            mousewheel True
            vbox:
                #spacing 20
                add 'gui/license/lczwtf.png' zoom 0.6
        vbar value YScrollValue("support_scroll"):
            xalign 0.0 yalign 0.0
            xpos 1010 ypos 20
            xminimum 30
            ymaximum 680
            base_bar None
            thumb "gui/license/licensescroll.png" #1458
        $lc1 = '                  DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE\n                       Version 2, December 2004\n\n Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>\n\n        Everyone is permitted to copy and distribute verbatim or modified\n copies of this license document, and changing it is allowed as long\n as the name is changed.\n\n            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE\n   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION\n\n  0. You just DO WHAT THE FUCK YOU WANT TO. '
        imagebutton idle 'gui/license/licensembtn.png' hover 'gui/license/licensembtn_.png' xpos 1155 ypos 590 xalign 0.5 yalign 0.5 action Function(copytext, t=lc1)
        imagebutton idle 'gui/license/licensembtn.png' hover 'gui/license/licensembtn_.png' xpos 1155 ypos 660 xalign 0.5 yalign 0.5  action Hide("lcwtf")
        text "복사 (Copy)" color "#ffffff" font "fonts/NanumSquareB.ttf"  xpos 1155 ypos 590 xalign 0.5 yalign 0.5 size 18.7
        text "이전으로 (Back)" color "#ffffff" font "fonts/NanumSquareB.ttf"  xpos 1155 ypos 660 xalign 0.5 yalign 0.5 size 18.7
    
    key "game_menu" action Hide("lcwtf")