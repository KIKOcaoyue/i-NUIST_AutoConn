# AutoConnCampusNetwork
自动连接NUIST的校园网的python脚本，无需打开浏览器输入用户名和密码。
关键词：南京信息工程大学校园网、南信大校园网


使用方法：
在__main__中的函数gendata("usrname","domain","password")三个参数填入("手机号","中国移动、中国联通、中国电信"、"密码")，然后运行脚本即可、

**注意：由于网页采用了密码加密，故使用此脚本前需要抓包查看发送出去的密码是什么，然后填入gendata()函数中。此外，中国移动是CMCC，填入domain处，其他两家运营商的网络也需要抓包查看**
**注意2：run.bat是因为我的电脑没有把python加入环境变量，所以才需要run.bat这个东西，如果你也是conda，并且没有把它加入环境变量，把run.bat内的setcondaRoot换成自己的anaconda3目录即可**
