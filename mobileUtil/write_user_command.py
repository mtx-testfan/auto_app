import yaml
class WriteUserCommand:
    def read_data(self):
        '''
        读取数据
        :return: data
        '''
        with open('../data/userconfig.yml') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        return data
    def get_value(self,section,key):
        '''
        获取value的值
        :param section: user_info_0
        :param key: bp
        :return: 4930
        '''
        data = self.read_data()
        try:
            value = data.get(section)
            value = value.get(key)
            return value
        except:
            print('没有可用设备')
            return None

    def write_data(self,i,device,bp,port):
        '''
        data和获取到data
        {'user_info_0': {'bp': '4930', 'deviceName': '127.0.0.1:62025', 'port': '4702'}, 'user_info_1': {'bp': '4931', 'deviceName': '127.0.0.1:62001', 'port': '4703'}}
        :return:
        '''
        data = self.join_data(i,device,bp,port)
        with open('../data/userconfig.yml','a') as f:
            yaml.dump(data,f)

    def join_data(self,i,device,bp,port):
        '''

        :param i:
        :param device:
        :param bp:
        :param port:
        :return:
        '''
        data = {
            'user_info_'+str(i):{
                'devicename':device,
                'bp':bp,
                'port':port
            }

        }
        return data

    def get_file_lines(self):
        '''
        获取有几个设备
        :return:
        '''
        data = self.read_data()
        return len(data)

    def clear_data(self):
        '''
        清除yaml数据
        :return:
        '''
        with open('../data/userconfig.yml','a') as f:
            f.truncate()


if __name__ == '__main__':
    print(WriteUserCommand().read_data())
    print(WriteUserCommand().get_file_lines())
