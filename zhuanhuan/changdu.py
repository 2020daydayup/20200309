import re

class  LengthConversion:
    "长度转换"
    value = 0

    def __init__(self,value):
        self.__rate__ = 0.9144
        self.value = value

    def m2yd(self, value):
        "米转换成码"
        result = round(value / self.__rate__, 4)
        print(f"{self.value} == {str(result)}码(yd)")

    def yd2m(self,value):
        "码转换成米"
        result = round(value * self.__rate__, 4)
        print(f"{self.value} == {str(result)}米(m)")

    def main_exption(self):
        "异常数据处理"
        re_data = r'^(\d+|\d+\.\d+)(yd|m)'
        re_num = r'\d+\.?\d*'
        if re.match(re_data, self.value):
            value = float((re.findall(re_num,self.value))[0])
            self.judge(value)
        else:
            print("输入数据错误："+self.value)

    def judge(self, value):
        "判断输入长度单位"
        if "yd" in self.value:
            self.yd2m(value)
        else:
            self.m2yd(value)

if __name__ == '__main__':
    LengthConversion("2yd").main_exption()