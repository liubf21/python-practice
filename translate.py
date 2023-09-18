import re
import requests
import hashlib
from random import randint

def generate_sign(appid, q, salt, secret_key):
    # 拼接字符串1
    string1 = appid + q + salt + secret_key
    
    # 对字符串1进行MD5加密
    sign = hashlib.md5(string1.encode('utf-8')).hexdigest()
    
    return sign


def translate_chinese_to_english(text):
    appid = '20230915001818452'
    q = text
    salt = str(randint(32768, 65536))
    secret_key = 'ArP8EyCqhjHdAljtNyhL'

    sign = generate_sign(appid, q, salt, secret_key)
    # print(sign)
    url = f'http://api.fanyi.baidu.com/api/trans/vip/translate?q={q}&from=zh&to=en&appid={appid}&salt={salt}&sign={sign}'
    response = requests.get(url)
    translation = response.json()['trans_result'][0]['dst']
    print(q, "->", translation)
    return translation



def translate_code_file(code_file):
    with open(code_file, 'r', encoding='utf-8') as file:
        code_content = file.read()

    chinese_characters = re.findall(r'[\u4e00-\u9fff]+\w*[\u4e00-\u9fff]+', code_content)

    for chinese_char in chinese_characters:
        english_translation = translate_chinese_to_english(chinese_char)
        code_content = code_content.replace(chinese_char, english_translation, 1) # only replace the first occurence

    with open(code_file, 'w', encoding='utf-8') as file:
        file.write(code_content)

    print("Operation complete.")


# print(translate_chinese_to_english('你好'))
translate_code_file('/Users/bytedance/GolandProjects/data_weekly_report/src/data_weekly_report/weekly_report_generator.go')