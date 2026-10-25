# OpenEixworldMC

废物。

# EixworldMC 启动器 V1.7.0

一个 Python 写的 Minecraft 启动器。界面是 PyQt6，文案和 QSS 是那种一眼能看出来的 AI 味，打包用的 PyInstaller。V1.7.0，更新日志日期 2026-10-25。上一版是 10 月 24 日的 1.6.0。

作者自己的宣传语还在主页上：「一款为黑客和 PVP 玩家打造的 MC 启动器」。主页能填兑换码。1.7 新增了游戏列表、Modrinth 模组/整合包，下载不用再跳浏览器。

说了几句不好听的，对方气急败坏，直接踢人。1.7 的包还是留下来了。

启动器自己写着「请到群里下载最新版」。群文件里到 10 月 25 日还只有 `EixworldMC启动器-V1.6.0.zip`，260.5 MB，来自 Eixfun，47 次下载，14 天过期。

![群文件里还是 1.6.0](screenshots/group-files.png)

## 实际怎么包的

和 1.6 一样，两层：

1. 入口 `main.py` 还是普通 Python 3.13 字节码，躺在 PyInstaller 归档里。1.7 这份和 1.6 **是同一个脚本**：同样的 import、同样的 `vip.guard()`、同样的 `Microsoft YaHei UI` 9pt、60ms 建窗口、4 秒兜底。
2. `_internal` 里 37 个业务模块被 **Cython 3.2.8** 编成 `*.cp313-win_amd64.pyd`。比 1.6 多了 `instances_page`、`mods_page`、`version_panel`。函数体是 x64 机器码，没有逐行源码。

`1.7.0/src/*.py` 里能确定的是模块、类、函数的名字和顺序，以及字符串表里的文案、QSS、URL。函数体写成 `...`。`1.7.0/symbols/*.json` 是原始表。1.6 的还原挪到 `1.6.0/`。

## 启动时干什么

`1.7.0/main.py`：

1. `_verify_env()` 调 `vip.guard()`。不过就弹「环境校验失败 / 程序文件不完整或已被修改」。
2. 读 `load_settings()["ui_scale"]`，写进 `QT_SCALE_FACTOR`。字体写死 `Microsoft YaHei UI` 9pt。
3. 图标：`<base>/Eix/eixfun/Eixfun.png`。
4. `welcome.needed()` 为真就弹欢迎窗。
5. 先出 `Splash`，60ms 后建 `MainWindow`，4 秒兜底强制显示。
6. 没接住的异常写到 `<base>/crash.log`。

侧边栏还是五个页：主页、启动、下载、设置、关于。左下角版本号 `v1.7.0`。

1.7 的更新日志（字符串表和界面一致）：

- 下载页新增「模组整合包」标签，接入 Modrinth
- 模组可在启动器内选版本直接安装，不跳浏览器
- 新增游戏列表，支持导入整合包、删除、查看详情
- 版本详情页显示模组列表，可从电脑选 jar 导入
- 按当前游戏自动锁定模组加载器
- 窗口不再默认全屏，尺寸受控
- 修复 Forge 启动时未校验 srg/extra/client jar 导致启动失败
- 修复下载卡死、皮肤导入闪退、正版账号误判离线

![1.7.0 更新日志](screenshots/changelog-1.7.0.png)

## 笑点

### 字体粗细很诡异

QSS 里的 `font-weight` 只有四档，而且全是粗的：600 出现 50 次，700 出现 93 次，800 出现 65 次，900 出现 3 次。正常的 400 一次都没有。入口再把全局字体钉成微软雅黑 9pt。标题、说明、按钮各胖一档，看着发飘。

### Emoji 一会有圆角一会没圆角

欢迎语是 Unicode：`你好，欢迎回来 👋`。启动页空状态另有一个 `📦`。版本卡片上那个箱子又是一张位图，圆角和彩色表情不是一套。

![未选择版本](screenshots/no-version.png)

Qt 在 Windows 上彩色 emoji 走 DirectWrite，缺字就退回雅黑，圆角就没了。入口 `_qt_message` 看见 `qt.qpa.fonts` 和 `DirectWrite` 直接 `return`，字体烂了连日志都不打。

### 傻逼指定 Java

设置里 Java 8、17、21、25 各填一个 `java.exe`。这张图上写进去的是精确到小版本的路径：

- Java 8：`C:\Program Files\Java\jdk1.8.0_202\bin\java.exe`
- Java 17：空的，占位「适配 1.17 ~ 1.20.4」
- Java 21：`C:\Program Files\Java\jdk-21.0.12\bin\java.exe`
- Java 25：空的，「可选，最新版本」

![Java 路径](screenshots/java-paths.png)

扫描器自己也只翻写死的那几棵目录：`C:\Program Files\Java`、`C:\Program Files (x86)\Java`，再猜一个 `D:\Java`、`D:\Program Files\Java`，外加 Corretto / Adoptium / Zulu / Microsoft。找不到就让你去「设置 → 其他设置」手动指。

### 诡异模糊

背景图 `Eix/picture/hub2.png` 是 1445×811、2.4MB。画到窗口上走 `background._blur`，缩放用 Qt 的 `SmoothTransformation`。铺法三选一：「铺满 · 左上对齐」「铺满 · 居中裁剪」「拉伸铺满」（最后这个是 `IgnoreAspectRatio`，直接拉变形）。

高清图先被糊成一块，再拉回窗口大小，抗锯齿是死的，看起来像先压成老爷画质再低清放大。滑条上「模糊度」可以是 0，背景照样是一坨。

![模糊度](screenshots/blur-slider.png)

## 模块

| 模块 | 干什么 |
|---|---|
| eix_config | `accounts.json` / `settings.json` / `selected.json`，外加 `java_path` |
| ui, launch, home, sidebar, titlebar, theme, splash, welcome, dialog, toast, fx, skin, background | PyQt6 界面。背景的模糊和铺满在 `background` |
| instances_page | 1.7 新增。游戏列表，导入整合包、删除实例 |
| mods_page | 1.7 新增。Modrinth 搜索模组 / 整合包 |
| version_panel | 1.7 新增。按项目拉 Modrinth 版本 |
| launcher | 补版本、BMCLAPI / 官方源、库和资源 |
| download_page, download_worker, downloader, forge_install | 下载，Forge / NeoForge，「模组整合包」标签 |
| launch | 选版本，缺 Java 时打开下载页，多实例退出提示 |
| java_finder | 扫写死的那几棵目录，按版本挑 `java.exe` |
| runner | 拉起 Java，写启动日志 |
| msa_auth | 微软设备码登录，Xbox Live → XSTS → Minecraft profile |
| account, vip, vip_card, key | 账号、赞助兑换码、更新检查（版本字符串 `1.7.0`） |
| settings_page, runpage, version_detail, about, prompts, media_tools, loader_icons, client_dev_catalog | 设置、运行日志、版本详情里的模组列表、图标 |

字符串表里的更新地址还是原来那三个：

- `https://eixworldupdateserver.pages.dev/update.txt`
- `https://eixworldupdateserver.pages.dev/config.json`
- `https://eixworldupdateserver.pages.dev/keys.json`

Modrinth 用的是公开 API：`https://api.modrinth.com/v2/search` 和 `https://api.modrinth.com/v2/project/%s/version`。微软登录的 client id 在 `1.7.0/src/msa_auth.py` 的 `_STRINGS` 里。
