import requests
import time
import json




HEADERS = {
  
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
    'cookie': 'csrtoken=iE5Hh8imrBbYKANqzE8ONMQUA4EEE2N9;ds_user_id=5582187629;fbm_124024574287414=base_domain=.instagram.com;fbm_124024574287414,fbsr_124024574287414=q4efflY3DqBw2WkhJ5vA7p0zCNapB81kp9zVR02nzxI.eyJ1c2VyX2lkIjoiMTAwMDE3MzIwNjY2NTkzIiwiY29kZSI6IkFRQ3hUTHFUR2RLemYtRlBQLWZsTXF2ZlpfQXY5aU9pX1VxaHFHZGNMc0JwajlJRW0yWmJxYjc2QTI3OWVUWnVIbHZsR0Vzam5Ha1NoZU56MGdmWlRUdUlndEtvUUllU3VucUJtdmNjR0RIU2hySk9Kd0d5QUhWUTRzOEU1ZHY4ZWhaajdBdEMxaTdZYlVkeks3M0RWeTdJQ05BRU1FV3VSd3UtVGJuY1dYNDlrOVdSSEVmY3Z5OGdvNUhoaFU1M2JneDJjMzUzc0FicmNLS2hick9IV21VUy1Mc1pvQUp3WmZ0YkZLcHBDcnVzMVhDMjhfd2FaS3hZTUxZeVVFUlNxbWxObjFJbWJ2bjFvR2RoeV9GUnplNmtnMFhNakxsWkQ3YTBxMnNpdTdkYV9GSy1RZkZFa2Npb3hZc3hCdFdjeVJHcDFUSnNPaGp4T2tIQ2h4Q2tkeERnIiwib2F1dGhfdG9rZW4iOiJFQUFCd3pMaXhuallCQUdwZHdrNldEdTRQb3h5Y2hvV005YWNBNVhjRHJaQXRxUHJrVHhNdFl6UFpBd3dsMzRSRHdCdnRlNzl3a0luMVpDbU4zTUV3WkJZSnVZYWZOU1dQbmRSQkdzY1NlcFBERXRwcndnalNHUmFHYlVLWG95SVRiS0psWkNGcWJjSFg1c05aQWY5RVMxWkJPZGs2QjV3amoxajJNZ2U5U3l0RlNsazRsc251WkFDbyIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNjEyMDQ3MjU1fQ;ig_did=920E09FD-BD11-4578-941C-5F1064DD1061;ig_nrcb=1;mid = X8yVbwALAAGX89Lxu1wnY87BpLLp;rur=ATN;sessionid=5582187629%3Ak341NgT3pq79eO%3A21;shbid=14817;shbts=1612041158.5688953;ig_cb=2;ig_gdpr_signup=%7B%22count%22%3A2%2C%22timestamp%22%3A1611848828988%7D'
    }
URL = 'https://www.instagram.com'

username = str(input("Username: "))

def statistic():




    g = open('edge_followed.txt','r')
    g1 = int(g.read(10))



    s = open('edge_followed_by.txt')
    s1 = int(s.read(10))

    
    r = requests.get(f'{URL}/{username}/?__a=1', headers = HEADERS)

    data = json.loads(r.content)


    


    edge_followed2 =  int(data['graphql']['user']['edge_follow']['count'])
    edge_followed_by_write3 = int(data['graphql']['user']['edge_followed_by']['count'])


    if  edge_followed2 > g1:
            b4 = str(edge_followed2 - g1)
            c = (",пользователь подписался " + b4)
            file_edge_followed = open('edge_followed.txt', 'w')
            file_edge_followed.write(str(edge_followed2 - g1))
            file_edge_followed.close()

    elif edge_followed2 == g1:
        c = (",количество подписок не изменилось")

    elif g1 > edge_followed2:
         res = str(g1 - edge_followed2)
         c = (",пользователь отписался " + res)

        

    if edge_followed_by_write3 > s1:
        edge_followed_by_write3 - s1
        file_edge_followed_by = open('edge_followed_by.txt', 'w')
        file_edge_followed_by.write(str(edge_followed_by_write3 - s1))
        file_edge_followed_by.close()
        resultate = ("кол-во подписчиков увеличилось "+ edge_followed_by_write3 - s1)

    elif edge_followed_by_write3 == s1:
        resultate = ("кол-во подписчиков не изменилось")
    elif s1 > edge_followed_by_write3:
         file_edge_followed_by = open('edge_followed_by.txt', 'w')
         file_edge_followed_by.write(str(s1 - edge_followed_by_write3))
         file_edge_followed_by.close()
         resultate = ("от пользователя отписались " + str(s1 - edge_followed_by_write3))
    print("За последний час " + resultate,c )

def statistic_function():
    r = requests.get(f'{URL}/{username}/?__a=1', headers = HEADERS)
    data = json.loads(r.content)


    print("ID:" + str(data['graphql']['user']['id']))
    edge_followed_by = print("Edge followed by:" + str(data['graphql']['user']['edge_followed_by']['count']))
    edge_followed = print("Edge followed:" + str(data['graphql']['user']['edge_follow']['count']))
    edge_followed_by_write = str(data['graphql']['user']['edge_followed_by']['count'])
    edge_followed_write =  str(data['graphql']['user']['edge_follow']['count'])




    file_followed_by = open('edge_followed_by.txt', 'w')
    print("Статистика была собрана")

    file_followed_by.write(edge_followed_by_write)

    file_followed_by.close()

    file_edge_followed = open('edge_followed.txt', 'w')

    file_edge_followed.write(edge_followed_write)

    file_edge_followed.close()
    
    usr = open('usr.txt', 'w')

    usr.write(username)

    usr.close()

    timeround = int(input("Введите интервал между проверкой(в секундах):  "))
    time.sleep(timeround)
    statistic()

statistic_function()
