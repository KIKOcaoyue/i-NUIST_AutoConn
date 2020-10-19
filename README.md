# AutoConnCampusNetwork
自动连接NUIST的校园网的python脚本，无需打开浏览器输入用户名和密码。


使用方法：
在__main__中的函数gendata("usrname","domain","password")三个参数填入("手机号","中国移动、中国联通、中国电信"、"密码")，然后运行脚本即可、

**注意：由于网页采用了密码加密，故使用此脚本前需要抓包查看发送出去的密码是什么，然后填入gendata()函数中。此外，中国移动是CMCC，填入domain处，其他两家运营商的网络也需要抓包查看**
