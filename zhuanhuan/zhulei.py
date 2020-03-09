import changdu
import huilv
import wenduan

class Transfer:
    "转换器主类，输入及判断"

    # def __init__(self,value):
    #     self.value = value

    # def input_data(self):
    #     value = input("请输入要转换的数值：")

    def mian_input(self, value):
        "程序入口"


        keep = True
        while (keep):
            print("'t'代表温度：'1t'表示1摄氏度，'1f'表示1华氏温度")
            print("'len'代表长度：'1m'表示1米，'1yd'表示1英码")
            print("'e'代表汇率：'￥1'表示1人民币，'$1'表示1美元")
            select = input("请选择单位类型（t/len/e）：")




            if select.lower() == 't':
                value = input("请输入要转换的数值：")
                wenduan.TemperatureConverter(value).main_exption()
                keep = input("是否继续（y/n）：") == 'y'

            elif select.lower() == 'len':
                value = input("请输入要转换的数值：")
                changdu.LengthConversion(value).main_exption()
                keep = input("是否继续（y/n）：") == 'y'

            elif select.lower() == 'e':
                value = input("请输入要转换的数值：")
                huilv.ExchangeRate(value).main_exption()
                keep = input("是否继续（y/n）：") == 'y'

            else:
                print("数据格式错误")
                keep = input("是否继续（y/n）：") == 'y'

if __name__ == '__main__':
    Transfer().mian_input('')