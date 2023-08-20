define config.language = "japanese"

init python:
    def font_arguments_callback(char, *args, **kwargs):
        if _preferences.language == "japanese":
            kwargs["what_font"] = 'fonts/NotoSansMonoCJKkr-Regular.otf'
            kwargs["font"] = 'fonts/NotoSansMonoCJKkr-Regular.otf'
            kwargs["what_language"] = "japanese-normal"
            kwargs["what_line_spacing"] = 5
        return args, kwargs

define config.say_arguments_callback = font_arguments_callback
