#! python2
# coding: utf-8
import time
from weibo import APIClient
import memo
from random import randint



def get_access_token(app_key, app_secret, callback_url):
    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    # 获取授权页面网址
    auth_url = client.get_authorize_url()
    print auth_url

    # 在浏览器中访问这个URL，会跳转到回调地址，回调地址后面跟着code，输入code
    code = raw_input("Input code:")
    r = client.request_access_token(code)
    access_token = r.access_token
    # token过期的UNIX时间
    expires_in = r.expires_in
    print 'access_token:',access_token
    print 'expires_in:', expires_in

    return access_token, expires_in

def init_login():
    app_key = '2769294092'
    app_secret = '8d6b0e602acb96f04cda158f998279a6'
    callback_url = 'https://api.weibo.com/oauth2/default.html'

    #access_token, expires_in = get_access_token(app_key, app_secret, callback_url)
    #上面的语句运行一次后，可保存得到的access token，不必每次都申请
    access_token = '2.00xXYulBktf6BD8de1312900i3je9E'
    expires_in = '1651792591'

    client = APIClient(app_key=app_key, app_secret=app_secret, redirect_uri=callback_url)
    client.set_access_token(access_token, expires_in)

    return client

def send_pic(client,pic_path,message):
    # send a weibo with img
    f = open(pic_path, 'rb')
    mes = message.decode('utf-8')
    client.statuses.upload.post(status=mes, pic=f)
    f.close()  # APIClient不会自动关闭文件，需要手动关闭
    print u"发送成功！"

def send_mes(client,message):
    utext = unicode(message,"UTF-8")
    client.post.statuses__update(status=utext)
    print u"发送成功！"

if __name__ == '__main__':
    name = ["三毛","韩寒","郭敬明","特斯拉","鲁迅","莎士比亚","牛顿","孔子",
    "蔡伦","谷登堡","哥伦布","爱因斯坦","巴斯德","伽利略","亚里士多德",
    "欧几里得","摩西","达尔文","秦始皇","奥古斯都","哥白尼","拉瓦锡",
    "君士坦丁大帝","瓦特","法拉第","麦克斯韦","路德","乔治华盛顿",
    "卡尔马克思","莱特兄弟","成吉思汗","亚当斯密","约翰道耳顿",
    "亚历山大大帝","拿破仑","爱迪生","列文虎克","威廉莫顿","马可尼",
    "希特勒","柏拉图","克伦威尔","弗莱明","洛克","贝多芬","海森堡",
    "达盖尔","玻利瓦尔","笛卡儿","米开朗琪罗","乌尔班二世","欧麦尔一世",
    "奥古斯丁","威廉·哈维","欧纳斯特·卢瑟福","约翰·加尔文",
    "孟德尔","马克思","利斯特","奥托","皮萨罗","科尔特斯","斯大林","恺撒",
    "威廉一世","弗洛伊德","伦琴","巴赫","老子","伏尔泰","开普勒","费密",
    "欧勒","卢梭","马基亚维里","马尔萨斯","平克斯","摩尼","隋文帝","达·伽马",
    "居鲁士大帝","彼得大帝","培根","福特","孟子","琐罗亚斯德","伊丽莎白一世",
    "戈尔巴乔夫","美尼斯","查理大帝","荷马",
    "查士丁尼一世","摩诃毗罗","C罗","赵本山","梅西","巴洛特利"]
    num = randint(0,len(name)-1)

    while True:
        client = init_login()

        t = time.localtime()
        a = memo.getmemo()
        print u"开始发送！"
        mes = '现在是北京时间'+str(t.tm_hour)+'时'+str(t.tm_min)+'分'+str(t.tm_sec)+'秒，早上好！' + name[num]+ "曾经说过：" + a.encode('utf8')
        send_mes(client,mes)
        print u"开始休眠！"
        time.sleep(21600)

        t = time.localtime()
        b = memo.getmemo()
        print u"开始发送！"
        num = randint(0,len(name)-1)
        mes = '现在是北京时间'+str(t.tm_hour)+'时'+str(t.tm_min)+'分'+str(t.tm_sec)+'秒，中午好！' + name[num]+ "曾经说过：" + b.encode('utf8')
        send_mes(client,mes)
        print u"开始休眠！"
        time.sleep(21600)

        print u"开始发送！"
        t = time.localtime()
        mes='现在是北京时间'+str(t.tm_hour)+'时'+str(t.tm_min)+'分'+str(t.tm_sec)+'秒，今天的你学习了吗？'
        mes = "今天的你学习了吗？"
        send_pic(client,'sendpic.jpg',mes)
        print u"开始休眠！"
        time.sleep(43200)
