import requests

if __name__ == '__main__':
    r = requests.get('http://baidu.com/')
    print r

    # url params
    # http://unionimage.baidu.com:7891/get_list.do?site=cnqiang.com&count=10&callback=__imageplus_recommend_callback__abzb1t_8
    myParams = {
        'site': 'cnqiang.com',
        'count': 10,
        'callback': 'test'
    }
    r_params = requests.get("http://unionimage.baidu.com:7891/get_list.do", params=myParams)

    # print r_params.url
    print r_params.content