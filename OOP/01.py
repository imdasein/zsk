'''
定义一个学生类
'''
# 定义一个空的类
class Student():
    # 一个空类，pass必须有，表示跳过，否则会报错
    pass
# 定义一个对象
mingyue = Student()
# 定义一个学Python的学生
class PythonStudent():
    name = None
    age = 8
    course = "python"
    #def的缩进层级和系统变量一样，二是默认有一个self参数
    def doHomework(self):
        print("I am doing my homework.")
        #推荐在函数末尾使用return语句
        return None
# 实例化
yueyue = PythonStudent()
#用点号操作符
print(yueyue.age)
print(yueyue.name)
#注意成员函数的调用没有传递参数
yueyue.doHomework()

# 类和对象的成员分析
    -类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
    -类存储成员时使用的是和类关联的一个对象

