# -*- coding: utf-8 -*-
"""forge_install — recovered from EixworldMC启动器 V1.7.0

Compiled with Cython 3.2.8 to a native .pyd (Python 3.13, win_amd64).
There is no bytecode. Names, nesting and string literals below are exact
recoveries from the binary. Function bodies were machine code and are
shown as ``...``.
"""

# string-table recovery: rdata
# unicode strings: 566   interned-from: 134

_STRINGS = (
    '1.',
    '.1f',
    '%2B',
    '403',
    '404',
    '[信息] Forge ',
    '[信息] 已解出 Forge 主 jar：',
    '无法解析 Forge 主 jar 的 maven 路径',
    '%H:%M:%S',
    '本机没有 Java ',
    '[信息] 处理器使用 Java ',
    ' MB/s',
    'META-INF/MANIFEST.MF',
    ' 没有 Main-Class',
    'Minecraft-Dists',
    '[信息] 已注入 Minecraft-Dists 属性',
    '[警告] 注入 Minecraft-Dists 失败: ',
    '\nMinecraft-Dists: client\n\n',
    'Mozilla/5.0 EixWorld/0.1.0',
    'None',
    '{ROOT}',
    'User-Agent',
    ' ',
    '\\[([^\\[\\]]+)\\]',
    '] ',
    ' 安装器 ',
    '[信息] 复用已缓存的安装器',
    '[信息] 下载 ',
    '[信息] 安装器地址候选 ',
    ' 个',
    '[',
    '//',
    '[警告] ',
    ' 失败：',
    '下载 ',
    ' 安装器失败：',
    '）',
    '[下载中] ',
    '  ',
    '  速度 ',
    ']',
    '[信息] ',
    ' 分块下载未完成（',
    '），改用普通下载',
    ': ',
    '[下载] ',
    '原版 ',
    '[信息] 待下载 ',
    ' 个文件，',
    '@',
    ' 线程并发下载',
    '[失败] ',
    ' 个依赖下载失败',
    '[信息] 准备原版 ',
    '官方清单里没有原版 ',
    '[信息] 写入原版 ',
    '，请先在「设置」里配置',
    '（',
    "'",
    '{',
    ':',
    '    ',
    '    ... 省略 ',
    ' 行 ...',
    '处理器 ',
    '}',
    '[处理] ',
    '处理器超时：',
    '处理器运行异常：',
    '处理器失败（退出码 ',
    '）：',
    '.',
    '[完成] 写出 ',
    '\\',
    '[信息] 开始安装 ',
    '[完成] ',
    ' 安装完成，耗时 ',
    ' 秒',
    ' 安装完成',
    '[错误] ',
    '/',
    '-',
    '+',
    'binarypatcher 没有产出 client jar',
    ':client',
    '-cp',
    'forge-',
    'https://bmclapi2.bangbang93.com/forge/minecraft/',
    'https://bmclapi2.bangbang93.com/mc/game/version_manifest_v2.json',
    'https://cmcc.mirrors.ustc.edu.cn/bmclapi/',
    'https://files.minecraftforge.net/maven/',
    'https://maven.minecraftforge.net/',
    'https://maven.neoforged.net/releases/',
    'https://neoforged.forgecdn.net/releases/',
    'https://piston-meta.mojang.com/mc/game/version_manifest_v2.json',
    '旧版安装器里缺少 install.filePath',
    'install_profile 里没有客户端处理器',
    'install_profile.json',
    '安装器里没有 install_profile.json',
    '.installer-',
    '-installer.jar',
    '（installer spec ',
    '.jar',
    '（旧版安装器，直接释放主 jar）',
    ' jar',
    '缺少原版 jar：',
    '缺少处理器 jar：',
    '[信息] 游戏 jar：',
    '找不到 java：',
    '.json',
    '.json（旧版安装器）',
    'main-class:',
    'neoforge-',
    'neoforge-metadata.xml',
    'net/minecraftforge/forge/',
    'net.minecraftforge:forge:',
    'net.neoforged',
    'net.neoforged:minecraft-client-patched:',
    'net/neoforged/neoforge/',
    'net.neoforged:neoforge:',
    'net/neoforged/neoforge/maven-metadata.xml',
    '.tmpjar',
    ':universal',
    'utf-8',
    'version.json',
    '安装器里的 version.json 不完整',
    '\\{(\w+)\\}',
)


def _dl_workers(*args, **kwargs):
    ...

def sha1_file(*args, **kwargs):
    ...

def fetch_json(*args, **kwargs):
    ...

def fetch_manifest(*args, **kwargs):
    ...

def maven_path(*args, **kwargs):
    ...

def maven_urls(*args, **kwargs):
    ...

def download_from(*args, **kwargs):
    ...

def forge_builds(*args, **kwargs):
    ...

def neo_builds(*args, **kwargs):
    def key(*args, **kwargs):
        ...

def _processor_is_client(*args, **kwargs):
    ...

def _jar_main_class(*args, **kwargs):
    ...

def _extract_maven_refs(*args, **kwargs):
    ...

class _Installer:
    def __init__(*args, **kwargs):
        ...

    def log(*args, **kwargs):
        ...

    def prog(*args, **kwargs):
        ...

    def cancelled(*args, **kwargs):
        ...

    def fetch_installer(*args, **kwargs):
        def cb(*args, **kwargs):
            ...

    def read_profile(*args, **kwargs):
        ...

    def collect_needed(*args, **kwargs):
        def add(*args, **kwargs):
            ...

    def download_libs(*args, **kwargs):
        def on_prog(*args, **kwargs):
            ...

        def work(*args, **kwargs):
            ...

    def prepare_vanilla(*args, **kwargs):
        ...

    def check_vanilla_jar(*args, **kwargs):
        ...

    def resolve_java(*args, **kwargs):
        ...

    def _extract_from_installer(*args, **kwargs):
        ...

    def resolve_data(*args, **kwargs):
        ...

    def _log_proc_output(*args, **kwargs):
        ...

    def extract_universal(*args, **kwargs):
        ...

    def run_processors(*args, **kwargs):
        def _wait(*args, **kwargs):
            ...

    def inject_manifest_dists(*args, **kwargs):
        ...

    def write_version_json(*args, **kwargs):
        ...

    def cleanup(*args, **kwargs):
        ...

def install(*args, **kwargs):
    ...
