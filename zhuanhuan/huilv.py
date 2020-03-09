import re

class ExchangeRate:
    "汇率转换类"

    value = 0

    def __init__(self,value):
        self.__exchange_rate__ = 6.9298
        self.value = value

    def cny2usd(self, value):
        "人民币转换成美元"
        result = round(value / self.__exchange_rate__, 4)
        print(f"{self.value} == ${str(result)}")

    def usd2cny(self,value):
        "美元转换成人民币"
        result = round(value * self.__exchange_rate__, 4)
        print(f"{self.value} == ￥{str(result)}")

    def main_exption(self):
        "异常数据处理"
        re_data = r'^\$|￥(\d+|\d+\.\d+)'
        if re.match(re_data, self.value):
            value = float((self.value)[1:])
            self.judge(value)
        else:
            print("输入数据错误："+self.value)
    def judge(self, value):
        "判断输入币种"
        if "￥" in self.value:
            self.cny2usd(value)
        else:
            self.usd2cny(value)
