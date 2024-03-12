import json
import requests

# 创建类
class WxTools():
    def __init__(self,app_id,app_secret): # 这个魔术方法可以直接实例化
        self.app_id=app_id
        self.app_secret=app_secret

    def get_access_token(self):
        app_http = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={self.app_id}&secret={self.app_secret}"
        # 发送get请求
        resp = requests.get(app_http).json()  # 得到一个json字符串
        # 截取到token字符串值
        access_token = resp.get('access_token')
        return access_token

    def send_wx_customer_msg(self, open_id, msg="有人闯入了摄像区"):
        # https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=ACCESS_TOKEN
        url = f"https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token={self.get_access_token()}"
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
    # 公众号ID，公众号密钥，用户ID
    app_id = "wx6c83f1dba496bfbb"
    app_secret = "f8817f4987903dab5e4b33a9fd7dea75"
    user_id="oYMly6SiLaR2TedvAKJ7D3GoxoZQ"

    wx_tools = WxTools(app_id, app_secret)
    wx_tools.send_wx_customer_msg(user_id)
