# 特别说明
在使用autobuild.py时，请先进入rvm环境，请先在终端中输入:rvm system

## 对于autobuild.py的说明 ##
- 使用这个python文件之前，请先进入到当前python文件所在文件目录下面
即通常情况下，python文件地址和工程name.xcodeproj或者name.xcworkspace同一个目录

###### 使用前说明 ######
- 如果你的python环境中没有包含requests库，需要先去包涵此库 pip install requests(如果出现问题请以sudo根用户权限输入命令)
在包含此库的时候需要pip
- 个人证书相关的信息请在exportOptions.plist里面进行修改
- 还需要修改你需要上传到蒲公英的地址，如果不进行将会传到我的地址里面

###### 文件目录说明 ######
- name.xcarchive文件在auto_build文件夹下
- exportOptions.plist文件在auto_build文件夹下
- name.ipa文件也在auto_build文件夹下
- UploadToPgy的python文件放在auto_build目录下

## 对于uploadToPgy.py 的说明##
- 由于python源代码也是一个文本文件，所以，当你源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为utf-8编码。

- 当python读取源代码的时候，为了让它按utf-8编码读取。我们通常在文件开头写上上面两行代码




&copy;第一版
