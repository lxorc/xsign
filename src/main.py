import requests
from bs4 import BeautifulSoup


config = {
     "BDUSS": "这里输入你的 BDUSS "
}

userAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWe" \
            "bKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"

headers = {
    "Cookie": "BDUSS=%s; " % (config["BDUSS"]),
    "User-Agent": userAgent,
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

if __name__ == "__main__":

    # TODO\(Mr.Kami\): 是否一定要个人主页? 还是有其他页面可以拿到? 这个页面元素太多获取性能差
    uri = "http://tieba.baidu.com/home/main?id=tb.1.8f71ec11.feoVuyJ1U8s8RA9tMu1a7g"

    r = requests.request('GET', uri, headers=headers)

    soup = BeautifulSoup(r.text,"html.parser")
    # TODO\(Mr.Kami\): 可能有 tbs 获取不到的情况
    tbs = ""
    for i in soup.body.children:
        if "Interaction" in str(i):
            tbs = str(i).split("'")[7]

    uri = "https://tieba.baidu.com/tbmall/onekeySignin1?tbs=%s" % (tbs)

    r = requests.request('POST', uri, headers=headers).json()

    no = r["no"]
    error = r["error"]
    data = r["data"]

    print(r)
    if 2500113 == no:
        print(
            """
            对不起, 你已经签到过了

            已经签到贴吧数: %s 个
            签到失败贴吧数: %s 个
            没有签到贴吧数: %s 个
            VIP签到贴吧数: %s 个
            """ % (
                data["signedForumAmount"],
                data["signedForumAmountFail"],
                data["unsignedForumAmount"],
                data["vipExtraSignedForumAmount"],
            )
        )
    else:
        # TODO\(Mr.Kami\): 格式化输出
        # {'no': 0, 'error': 'success', 'data': {'signedForumAmount': 3, 'signedForumAmountFail': 0, 'unsignedForumAmount': 6, 'vipExtraSignedForumAmount': 6, 'forum_list': [{'forum_id': 3287180, 'forum_name': '瓦奥', 'is_sign_in': 1, 'level_id': 9, 'cont_sign_num': 3, 'loyalty_score': {'normal_score': 4, 'high_score': 14}}, {'forum_id': 208889, 'forum_name': '手绘', 'is_sign_in': 1, 'level_id': 9, 'cont_sign_num': 3, 'loyalty_score': {'normal_score': 4, 'high_score': 14}}, {'forum_id': 2835769, 'forum_name': 'p站', 'is_sign_in': 1, 'level_id': 7, 'cont_sign_num': 3, 'loyalty_score': {'normal_score': 4, 'high_score': 14}}], 'gradeNoVip': 12, 'gradeVip': 126}}
        # {'signedForumAmount': 3, 'signedForumAmountFail': 0, 'unsignedForumAmount': 6, 'vipExtraSignedForumAmount': 6, 'forum_list': [{'forum_id': 3287180, 'forum_name': '瓦奥', 'is_sign_in': 1, 'level_id': 9, 'cont_sign_num': 3, 'loyalty_score': {'normal_score': 4, 'high_score': 14}}, {'forum_id': 208889, 'forum_name': '手绘', 'is_sign_in': 1, 'level_id': 9, 'cont_sign_num': 3, 'loyalty_score': {'normal_score': 4, 'high_score': 14}}, {'forum_id': 2835769, 'forum_name': 'p站', 'is_sign_in': 1, 'level_id': 7, 'cont_sign_num': 3, 'loyalty_score': {'normal_score': 4, 'high_score': 14}}], 'gradeNoVip': 12, 'gradeVip': 126}
        print(data)
    pass
