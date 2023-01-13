import requests


def scrapnprint(url, headers, data):
    response = requests.post(url=url, headers=headers, data=data).json()  # 对目标url发起post请求
    for key in response['data'][0]:
        print(key, response['data'][0][key])


def main():
    url = 'https://fanyi.baidu.com/sug'  # 需要请求的url
    headers = {  # 进行UA伪装，本人的User-Agent
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/108.0.0.0 Safari/537.36 '
    }
    while True:  # 使程序进入死循环，输入非字母即视为结束
        keyw = input("输入需要查询的单词：")
        if not keyw.isalpha():
            break
        data = {  # post请求携带的参数
            'kw': keyw
        }
        scrapnprint(url=url, headers=headers, data=data)


if __name__ == '__main__':
    main()
