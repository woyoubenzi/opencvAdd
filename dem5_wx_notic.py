import json
import requests

# 1 获取access_token
# https请求方式: GET
# https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET

def get_access_token(app_id, app_secret):
    app_http = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={app_id}&secret={app_secret}"
    # 发送get请求
    resp = requests.get(app_http).json()  # 得到一个json字符串
    # 截取到token字符串值
    access_token = resp.get('access_token')
    return access_token


# # 2 利用access_token发送微信的通知
# # http请求方式: POST
def send_wx_customer_msg(access_token,open_id,msg="你好"):
    # https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN
    url = f"https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={access_token}"
    req_data = {
        "touser": open_id,  # 要发送给的用户
        "msgtype": "text",
        "text":
            {
                "content": msg
            }
    }
    # 转换成json格式，并使用utf-8格式发送
    date = json.dumps(req_data, ensure_ascii=False).encode("utf-8")
    requests.post(url, data=date)

if __name__ == "__main__":
    app_id = "wx6c83f1dba496bfbb"
    app_secret = "f8817f4987903dab5e4b33a9fd7dea75"
    token=get_access_token(app_id,app_secret)
    open_id="oYMly6SiLaR2TedvAKJ7D3GoxoZQ"
    send_wx_customer_msg(token,open_id,"有物体闯入")
