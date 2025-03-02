init -2 python:

    register_language(name="简体中文", id="schinese", subtitle_text="Simplified Chinese", uifont_path="tl/schinese/fonts/ChillDuanSans_Medium.otf",
                      dialoguefont_path="975SCHans", breaking_method="japanese-loose", locale="zh", script="hans", 
                      region=("cn", "sg"), version="official-1.0")

    register_font(name="975朦胧黑体", font_path="tl/schinese/fonts/ChillDuanSans_Medium.otf", license_path="License/Fonts/SourceHan.txt")
    register_font(name="寒蝉端黑体", font_path="tl/schinese/fonts/ChillDuanSans_Medium.otf", license_path="License/Fonts/SourceHan.txt")
    register_font(name="梦源宋体", font_path="tl/schinese/fonts/ChillDuanSans_Medium.otf", license_path="License/Fonts/SourceHan.txt")
    register_font(name="霞鹜文楷", font_path="tl/schinese/fonts/ChillDuanSans_Medium.otf", license_path="License/Fonts/LxgwWenKai.txt")
    register_font(name="851手書き雑フォント", font_path="tl/schinese/fonts/ChillDuanSans_Medium.otf", license_path="License/Fonts/851tegakizatsu.txt")

    #preferences.voice_after_game_menu = True - it has minor issues.


init python:
    TooltipComment("schinese_b102a617", "译注：每年的上半年是第一个学期。")
    TooltipComment("schinese_31d98d55", "译注：{font=fonts/NanumSquareRoundB.ttf}편의주의{/font}（便宜主義）是指一种不寻找原因而临时敷衍的方法，或指一种总是出于自己的方便和利益为标准的思维方式。")
    TooltipComment("schinese_c035fedb", "译注：“你”在这里作为宾语前置。")
    TooltipComment("schinese_75f48953", "译注：指的是勾陈一，也就是我们目前的北极星。")
    TooltipComment("schinese_71798e1b", "译注：指的是少卫增八，在第30世纪，它将成为那个时代的北极星。")
