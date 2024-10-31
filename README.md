# Linux shell Tutorial

这个一个关于如何更好的使用linux shell的教程。主要关注`shell`的通用概念，具体介绍的则是最经典的`bash`。这个文档面向计算机专业的新同学和那些想要从其他的专业转到计算机方向的同学，因此我致力于让文档内容从零基础开始也能很容易读懂。

## 如何在本地构建本文档

### 配置构建环境

本文档使用[mkdocs](https://python-poetry.org/)构建，并使用[poetry](https://python-poetry.org/)管理`python`环境。因此首先请配置好python环境并根据poetry官方网站的指导安装好poetry。

如果你懒得去看那些东西并且你恰好使用的是`Debian`/`Ubuntu`，那么也可以尝试直接使用下面的命令

```bash
sudo apt update
sudo apt install pip --update
pip install poetry
```

### 使用peotry安装依赖

使用下面的命令，让poetry根据配置文件`pyproject.toml`安装合适的依赖。然后进入本项目的python环境。

```bash
poetry install
poetry shell
```

### 使用mkdocs构建

使用下面的命令直接构建并启动一个本地的服务器

```bash
mkdocs serve
```

命令最后会输出一个构建出的网址，大概率会是[http://127.0.0.1:8000/Linux-shell-Tutorial/](http://127.0.0.1:8000/Linux-shell-Tutorial/)，进入这个网址即可看到本地构建结果。

使用下面的命令可以在当前文件夹下的`./site`文件夹下构建一个静态站点的全部内容。(`--clean`会清除上一次构建的结果)

```bash
mkdocs build --clean
```

## 如何贡献

目前为本项目的贡献方式包括在github仓库issue中提出意见，或者给我发[电子邮件](mailto:2200012909@stu.pku.edu.cn)。之后可能会在页面下方开放评论区。

暂不支持为本项目直接贡献内容。

## TODO list

初级篇

* [x] 3. echo, printf, 命令行参数, terminal和shell操作相关的知识
* [x] 4. ls, cd, mkdir, touch, find
* [x] 5. pwd,
* [ ] 6. cp, mv, cat, view, rm, shred, rmdir, tee
* [ ] 7. 输入输出重定向，管道, mkfifo, &&
* [ ] 8. ip, ifconfig, curl, telnet, wget, ssh, scp, netcat
* [ ] 9. 进程，信号, ctrl-C, ctrl-D
* [ ] 10. top, htop, kill, pkill, ps, nohup, &
* [ ] 11. tar, zip, unzip
* [ ] 12. sleep. timeout, date
* [ ] 13. man, pr, tldr
* [ ] 14. history, alias, su, sudo, install, yes

中级篇

* [ ] 13. 硬链接，软连接，readlink, readpath, link, ln, mount, unmount, /mnt, pwd
* [ ] 14. 万物皆文件，文件类型，mknod, mktemp
* [ ] 15. less, more
* [ ] 16. vim, vi
* [ ] 17. head, tail, tr, wc, nl
* [ ] 18. grep, awk, sed
* [ ] 19. bc, numfmt, od, xxd, hexdump
* [ ] 20. 展开
* [ ] 21. tmux
* [ ] 22. 环境变量, printenv，path
* [ ] 23. .bashrc, fish-config
* [ ] 24. strace

高级篇

* [ ] 25. 脚本基础
* [ ] 26. To be continue

这一篇可能包括的内容：脚本, shabang, 脚本命令行参数，if语句，for语句，
loop语句，变量，数组, seq, xargs, test

整活篇

* [ ] xx. To be continue

这一篇可能包括的内容：还不知道
