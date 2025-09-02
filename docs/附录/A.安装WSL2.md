# 安装WSL2

> WSL是最好的Linux发行版。
>                   ————匿名

## 什么是WSL

WSL(**W**indows **S**ubsystem for **L**inux), 也就是Windows的Linux子系统。WSL是微软提供的一个功能允许你在不安装虚拟机或双系统的情况下，直接在 Windows 上运行 Linux 环境。而且这个系统可以提供几乎所有的Linux内核的功能，也就是说，它给我们提供了一种方式，不必安装虚拟机或者双系统，就可以使用Linux。

!!! info "info"
    ### 什么不是虚拟机

    虚拟机是一种软件，借助硬件的帮助在你的计算机上实现虚拟一个计算机，不仅虚拟一个完整的操作系统，也会虚拟一些必要的硬件。
    相比于WSL，虚拟机需要安装一个完整的新系统。因此虚拟机的启动比较慢，对计算机资源的消耗比较大，并且性能损失也比较高。另外，虚拟机的文件系统和你的本机是完全隔离的，因此和虚拟机之间的传递文件是一件比较麻烦的事。

    ### 为什么不是双系统

    双系统则是指在你的物理机器上安装两个操作系统。这需要在你的硬盘上安装两个系统引导，同时需要在每次开机的从Bios选择你要使用哪个系统启动。因此，如果你想要在两个系统中互相切换就必须重启启动电脑并且在启动的进入bios。并且在更新你的操作系统的时候，会有概率损坏磁盘上的系统引导，导致你的双系统中某个系统无法正常启动。并且对于双系统来说，两个系统之间的隔离程度最高，传递文件也会一样非常困难。

因此，对于使用Windows的同学，如果你日常想要使用Linux，例如探索Linux操作系统的命令，或者使用Linux作为实验换环境等，选择WSL都是最好的选择。WSL拥有的优势包括但不限于：
1. 提供了一个相对完整的Linux功能。
2. 启动迅速。
3. 对系统资源占用少。
4. 和Windows系统之间的文件共享简单。

## 如何安装WSL2

实际上，微软提供了WSL和WSL2，但是我们只推荐使用WSL2，因为WSL2是最新的版本，更加稳定并且性能更好。实际上，微软的官方文档中已经详细说明了如何安装WSL2，所以这里我就不做过多介绍了，请你直接阅读微软提供[文档](https://learn.microsoft.com/zh-cn/windows/wsl/install)来进行安装。


## 如何更丝滑地使用WSL2

微软同样也提供了一个详细的[文档](https://learn.microsoft.com/zh-cn/windows/wsl/setup/environment#set-up-windows-terminal)仔细介绍了如何更加丝滑的使用WSL2，包括在Windows Terminal中设置WSL2，在VSCode中连接WSL2，在WSL2中使用docker，git等等。

!!! info "info"

    另外一个很常用功能是在你的Windows和WSL2中传递文件。可以在WSL中的`/mnt/*/`目录下查看你的Windows中的文件，其中`*`是你的Windows中的盘符(通常是c/d/e...，请使用小写)。在WSL2中如何操作文件具体请看[初级篇第4章](../初级篇/d-4.操作文件系统的shell命令.md)。

    即使你通过VSCode也可以在Windows和WSL2中传递文件，我仍然推荐你使用上述方法。因为VSCode中是通过[ssh](../初级篇/i-9.网络应用相关的shell命令.md#ssh)来建立你的Windows和WSL2之间的连接的，所以文件的传递过程会比上述方法慢很多。

## WSL2的高级配置

如果你开始更加大量地使用WSL2用于你的开发，你可能需要关心一些WSL2的高级配置，例如如何配置WSL可以使用的内存用量，CPU用量，网络模式等。这个方面微软也提供了详细的[文档](https://learn.microsoft.com/zh-cn/windows/wsl/wsl-config)进行说明，你可以在需要的时候阅读这个文档进行操作。

## 通过Windows terminal来使用WSL

我们推荐你通过Windows terminal来使用WSL，你可以通过微软的[文档](https://learn.microsoft.com/zh-cn/windows/terminal/install)来了解如何安装和使用它。

<script src="https://giscus.app/client.js"
        data-repo="OshinoShinobu-Chan/Linux-shell-Tutorial"
        data-repo-id="R_kgDONEc4yg"
        data-category="Announcements"
        data-category-id="DIC_kwDONEc4ys4Cj5Fk"
        data-mapping="title"
        data-strict="0"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>