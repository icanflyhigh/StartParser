# StartParser

自定义的命令行脚本启动工具

## 安装

无需安装，直接解压压缩包

## 使用

压缩包中包括: `StartParser.exe`, `config.yml`, `resource/cmd.yml`。

* 打开`StartParser.exe`，在窗口中输入关键字来快速启动应用。
* `resource/cmd.yml`用于存放关键字以及对应所需执行的指令。
* `resource/links` 文件夹下用于存放快捷方式，可使用快捷方式的名字作为关键字来打开快捷方式。

* `config.yml`用来指定的文件`resource/cmd.yml`和文件夹`resource/links`的位置。`YML_PATH`定义 `cmd.yml`的路径，`LINK_PATH`定义`resource/links`的路径。




### 使用例子

在`cmd.yml`中定义了如下：

```yaml
Test:
  keyword:
    - 'test'
  cmd:
    - 'start explorer "C:\"'
    
```



如果在`StartParser.exe`中输入关键字 `test`, 则`StartParser.exe`执行`start explorer "C:\"`，打开一个文件夹。

如果`resource/links`中存在 `a.lnk`且在在`StartParser.exe`中输入关键字`a`，则直接启动`a.lnk`。



## TODO

* [ ] GUI
