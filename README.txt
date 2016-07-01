1、pycli是什么？
python实现的命令工具集，可以安装到系统目录，像使用系统命令一样使用pycli的命令。
初始化版本仅搭建了项目框架，实现了一个演示用的log命令。

2、安装pycli

方法一：
第一次安装pycli
sudo pip install git+https://github.com/changong/pycli.git

pycli发布新版本后更新安装
sudo pip install git+https://github.com/changong/pycli.git --upgrade

方法二：
下载pycli项目
git clone https://github.com/changong/pycli.git

在pycli的上级目录执行安装命令
第一次安装pycli
sudo pip ./pycli

pycli发布新版本后更新安装
sudo pip ./pycli --upgrade

3、pycli的安装位置
终端执行 which pycli
会显示pycli的安装位置 /usr/local/bin/pycli

4、使用pycli命令行工具集
 终端执行 pycli
 会列出pycli帮助信息及提供的命令列表
 例如：
 localhost:pycli zhangyg$ pycli
Usage: pycli [OPTIONS] COMMAND [ARGS]...

Options:
  -h, --help  Show this message and exit.

Commands:
  log

使用pycli命令集中的log命令，示例如下：
pycli log -m "pycli log cmd"


