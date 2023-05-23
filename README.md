# 简介

视觉小说[여름의 끝에 피는 꽃（Flowers blooming at the end of summer）](https://store.steampowered.com/app/1173010/)，译名《夏末盛开的花》的非官方，粉丝制作的简体中文化补丁。

“夏末花开”是旧译名。虽然“夏末盛开的花”更加贴合原始标题，但您可以根据自己的喜好随意使用两个译名来称呼这部作品。官方认可的简称是“夏花（여름꽃）”

[한국어](https://github.com/Noriverwater/flowernovelzhHans/blob/main/README_ko.md) [English](https://github.com/Noriverwater/flowernovelzhHans/blob/main/README_en.md) [日本語](https://github.com/Noriverwater/flowernovelzhHans/blob/main/README_jp.md) 版说明以后再写。

## 下载

[Releases](https://github.com/Noriverwater/flowernovelzhHans/releases/tag/2.0)

## 构建补丁

**准备**

- Python 3
- Ren'Py 8.03

**从源代码构建**

1. `git clone https://github.com/Noriverwater/flowernovelzhHans.git`

2. 添加以下内容：
    ```
    init python:
        build.archive("zh-hans", "all")

        build.classify("game/screens_zh.rpy", "zh-hans")
        build.classify("game/tl/chinese/**", "zh-hans")
    ```

3. 构建发行版
## 贡献翻译或代码

`tl/chinese`下是 Ren'py 的翻译文件，您可以直接修改其中的译文。screens_zh.rpy 在启动游戏后加载这些文件，以提供非官方的多语言支持，因此，这个项目不会替换原游戏的任何内容。要想贡献翻译，只需要提交 [pull request](https://github.com/Noriverwater/flowernovelzhHans/pulls).

最初的时候，这只是一个在机器翻译基础上润色的项目。后来，虽然大多数多翻译错误已经被更正，但仍然有很多不尽人意的地方没来得及改。欢迎您更正错误。或者增加新的功能，我会非常感激的。目前第二章、第三章、和第四章后半部分有较多错误并需要润色。如果有可能，请优先更正它们。

## 译文许可证

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]



[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/

[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png

[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg

## Q&A

**Q：我买不到这个游戏的DLC *When the Lying Petals Scatter Into the Wind*。你玩过它吗？**

<p align="center"><img src= "https://cdn.cloudflare.steamstatic.com/steam/apps/1521480/header.jpg?t=1625836179" alt="가짜 꽃잎이 바람에 흩날릴 때" width="230" height="107" /></a></p>

A：我没玩过。这个DLC是开发早期赞助了94,900韩元以上众筹者的奖励之一，属于非卖品。见
[여름날의 감동을 담은 비주얼노벨, '여름의 끝에 피는 꽃'.](https://tumblbug.com/flowernovel/)

不过，根据网上的公开信息，我知道它是有关两名女配角的故事，与“过去”和“未来”密切相关。它属于游戏本篇的外传，而不是本篇的后续。

**Q：为什么游戏里的背景没有正常加载，只有文字能显示？**

A：可能是因为您的音频服务不能正常工作，比如您没有可用的声音输出设备（音响，耳机）。

**Q：我可以直播或录播这个补丁的内容吗？**

A：可以。注意遵守发行商 PsychoFlux Entertainment 的规定[스트리밍 및 영상화 규정
](http://www.psychoflux.com/video-policy/)，即制作该游戏的介绍视频时不得完全剧透故事内容。

**Q：为什么我在steam社区找不到这个补丁了？**

A：因为不符合[《Steam 规则及指引：讨论、评测以及用户生成内容》](https://help.steampowered.com/zh-cn/faqs/view/6862-8119-C23E-EA7B)的要求。

**Q：这是制作组的第一部作品吗？**

A：严格来说，这不是制作人的第一部作品。

**Q：有DLC的替代品吗？好想知道两名女孩的故事啊，没有她们的线路真是太可惜了……**

A：您大概率已经发现了，这里有一个同样是非官方的粉丝制作模组["다시, 기억의 끝자락에서 피는 꽃"](https://cafe.naver.com/midnightworks/2238)（再次，在记忆的末尾盛开的花）。
它添加了优美和贤智的个人线路，**但您务必要在完全达成游戏本篇的结局后安装这个模组，因为这些是在游戏本篇结局后发生的故事**。作为一个非官方的作品，其中的设定应该只是模组团队剧本的想法，应该吧。

好消息是，云恭雀正在翻译这个模组：[夏末盛开的花 同人if线 chapter1选项前剧情](https://www.bilibili.com/video/BV17g4y1W7Er/)。在这项工作完成之前，你可以采用[LunaTranslator](https://github.com/HIllya51/LunaTranslator)、[MisakaTranslator](
https://github.com/hanmin0822/MisakaTranslator)等工具帮助你体验模组。在游戏中按下`Shift+C` 可以将当前台词复制到剪贴板。

### 关于 "여름의 끝에 피는 꽃"

**在观看完最终结局后（这很重要）**，这些内容非常值得一看：

- 这是官方的后继故事：https://www.youtube.com/watch?v=sODHt1C2xPg

    有人制作了中文字幕：https://www.bilibili.com/video/BV11B4y1e7Xz/


- 这是粉丝记录的，가스마스크선생与制作人的访谈摘要，可惜没有录播。

    https://cafe.naver.com/midnightworks/1970

    https://gall.dcinside.com/mgallery/board/view/?id=talesshop&no=65311


- 要想了解这部作品的前世与今生，可以看看制作人写的这篇文章：

    https://cafe.naver.com/midnightworks/2175


- 要想了解有关这部作品的更多信息，[namuwiki](https://namu.wiki/w/%EC%97%AC%EB%A6%84%EC%9D%98%20%EB%81%9D%EC%97%90%20%ED%94%BC%EB%8A%94%20%EA%BD%83) 和 [VNDB](https://vndb.org/v30340) 上有更加详细的记载。










