import requests
import time
STATUS_OFFSET = 8
INFO_OFFSET   = 7
url = "http://a.nuist.edu.cn/index.php/index/login"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}
data = {
    "username": None,
    "domain": None,
    "password": None,
    "enablemacauth": "0"
}

def gendata(usrname, domain, pwd):
    data["username"] = usrname
    data["domain"] = domain
    data["password"] = pwd
    return data


def conn(newurl, newheaders, newdata):
    res = requests.post(url = newurl, headers = newheaders, data = newdata)
    return res.text


if __name__ == "__main__":
    nowdata = gendata("138xxxxx","CMCC","xxxxxx")
    res = conn(url, headers, nowdata)
    isok = True
    while res[res.find("status")+STATUS_OFFSET] != 1:
        if res[res.find("info")+INFO_OFFSET] == 'P':
            isok = False
            print('PassWord Error, Please Check!\n')
            break
        else:
            time.sleep(5)
            res = conn(url, headers, nowdata)
    if isok == True:
        print('Connect Success!\n')
    