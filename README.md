# StartParser

`arg` -> `command` -> `application`

在窗口中输入关键字来快速启动应用

打造一个更加干净的桌面

在 config.yml 的`YML_PATH`中编辑 cmd.yml 的路径

在 cmd.yml 中编辑，创建自己的快速启动方式。

+ 对象的名字可以随便取

+ `keyword`表示输入的关键字
+ `cmd`表示执行的指令
+  这两个对象下必须 有 `- ` 表示数组

./dist/StartParser/StartParser.exe 是可执行文件，可以直接使用( 在config.yml, cmd.yml )格式，路径正确的情况下
