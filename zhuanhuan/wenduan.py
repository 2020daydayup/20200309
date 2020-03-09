import re

class  TemperatureConverter:
    "温度转换"
    value = 0

    def __init__(self,value):
        self.__rate__ = 1.8
        self.value = value

    def centigrade2f(self, value):
        "摄氏度转换为华氏度"
        result = round(value * (9 / 5)+ 32, 4)
        print(f"{self.value} == {str(result)}华氏度(°F)")

    def f2centigrade(self,value):
        "华氏度转换为摄氏度"
        result = round((value - 32) * (5/9) + 273, 4)
        print(f"{self.value} == {str(result)}摄氏度(°C)")

    def main_exption(self):
        "异常数据处理及转换入口"
        re_data = r'^(\d+|\d+\.\d+)(f|c)'
        re_num = r'\d+\.?\d*'
        if re.match(re_data, self.value):
            value = float((re.findall(re_num,self.value))[0])
            self.judge(value)
        else:
            print("输入数据错误："+self.value)

    def judge(self, value):
        "判断输入温度单位，调用不同的温度转换方法"
        if "f" in self.value:
            self.f2centigrade(value)
        else:
            self.centigrade2f(value)
