# TODO: Translation updated at 2023-07-21 14:01

translate japanese strings:

    # game/screens.rpy:1199
    old "Start Game"
    new "スタート"

    # game/screens.rpy:1200
    old "Load Game"
    new "ロード"

    # game/screens.rpy:1201
    old "추가요소"
    new "追加要素"

    # game/screens.rpy:1202
    old "제작진"
    new "スタッフ"

    # game/screens.rpy:1203
    old "Preferences"
    new "環境設定"

    # game/screens.rpy:1204
    old "기존메뉴"
    new "既存のメニュー"

    # game/screens.rpy:1205
    old "Quit"
    new "終了"

    # game/screens.rpy:1558
    old "풀스크린"
    new "フルスクリーン"

    # game/screens.rpy:1559
    old "일반"
    new "ウィンドウ"

    # game/screens.rpy:1775
    old "{}페이지"
    new "ページ {}"

    # game/screens.rpy:1775
    old "자동저장"
    new "オートセーブ"

    # game/screens.rpy:1775
    old "퀵세이브 목록"
    new "クイックセーブ"

    # game/screens.rpy:1776
    old "PAGE{}"
    new "PAGE{}"

    # game/screens.rpy:1776
    old "AUTOSAVE"
    new "AUTOSAVE"

    # game/screens.rpy:1776
    old "QUICKSAVE"
    new "QUICKSAVE"

    # game/screens.rpy:1954
    old "빈 슬롯"
    new "空のスロット"

    old "해당 장면으로 바로 이동할까요?"
    new "そのシーンに直接移動しますか？"

    old "이전으로 (Back)"
    new "前に戻る (Back)"

    old "복사 (Copy)"
    new "コピー (Copy)"
    
    old "{alpha=0.34}하단의 LOG에서도 지나간 대사를 볼 수 있어요.{/alpha}"
    new "{alpha=0.34}下部のLOGでも過ぎ去った台詞を見ることができます。{/alpha}"

    old "{alpha=0.5}소녀{/alpha}"
    new "{alpha=0.5}少女{/alpha}"

    old "{alpha=0.5}기타 등장인물{/alpha}"
    new "{alpha=0.5}その他の登場人物{/alpha}"

    old "{alpha=0.5}현지{/alpha}"
    new "{alpha=0.5}ヒョンジ{/alpha}"

    old "{alpha=0.5}유미{/alpha}"
    new "{alpha=0.5}ユミ{/alpha}"

    old "{alpha=0.5}명령어를 입력하세요.{/alpha}"
    new "{alpha=0.5}コマンドを入力してください。{/alpha}"

    old "이 대사의 장면으로 돌아갈까요?"
    new "そのセリフのシーンに戻りましょうか？"

translate japanese python:
    gui.system_font = u'fonts/NotoSansMonoCJKkr-Regular.otf'
    gui.font = u'fonts/NotoSansMonoCJKkr-Regular.otf'

translate japanese style default:
    font u'fonts/NotoSansMonoCJKkr-Regular.otf'

translate japanese style history_text:
    font u'fonts/NotoSansMonoCJKkr-Regular.otf'
    language "japanese-normal"

translate japanese style choice_pick_text:
    font u'fonts/NotoSansMonoCJKkr-Regular.otf'
    language "japanese-normal"
