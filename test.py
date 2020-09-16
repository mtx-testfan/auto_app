import configparser
config = configparser.ConfigParser()
config.read(r'D:\company\auto\20200606\lesson10\lesson10_1\pageObject\doubanPage.ini',encoding='utf-8')
print(config.get('TextInput', '用户名'))