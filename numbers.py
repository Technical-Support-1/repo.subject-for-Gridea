import re




def number_check(x):
    if x.isnumeric():
        return True
    else:
        value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')       # 定义正则表达式
        result = value.match(x)
        if result:
            return True
        else:
            return False   # 以上是为了检验是否为整数或浮点数，下同

