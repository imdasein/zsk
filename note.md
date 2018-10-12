# 类的基本实现
 - 类的命名
    - 大驼峰（首字母大写，单词相连）
    - 尽量避开和系统命名相似的命名
 - 声明一个类
    - 用class关键字
    - 类由属性和方法构成，其它不存在、
    - 成员属性定义可以直接使用变量赋值，如果没有值可以用None
    - 可以通过默认内置变量检查类和对象的所有成员
        -对象所有成员检查
            #dict前后各有两个下划线
            obj.__dict__
        -类的所有成员
            class_name.__dict__
            
    
# anaconda基本使用
    -是一个虚拟环境管理器，还是一个安装包管理器
    - conda list:显示anaconda安装的包
    - conda env list:显示anaconda的虚拟环境列表
    - conda create -n xxx python=3.6:创建python版本为3.6的虚拟环境，名为XXX

