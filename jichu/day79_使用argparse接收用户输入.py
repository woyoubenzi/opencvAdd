import cv2
import numpy as np
import argparse

"""
导入这个包(python内置,直接导入即可)
argpares :在命令行接收用户输入,通过 -a -b -c 这种方式接受参数的
"""
# 设置脚本参数
parse=argparse.ArgumentParser(description='传入一个数字')

# 定义参数名,required是否必须传入,help提示
parse.add_argument('-i','--image',required=True,help='you name')
parse.add_argument('-t','--template',required=True,help='you age')

# 接受传入的值
# vars 可以将对象的属性和属性值以字典的方式返回
args = vars(parse.parse_args())
print(args)