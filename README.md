# python3-flask-cli
一个flask的框架
## 创建虚拟环境
1. 创建一个叫env的虚拟环境
    ```cmd
    python -m venv env
    ```
2. 激活虚拟环境
    ```cmd
    cd env/Scripts   //进入虚拟环境的Scripts目录
    activate         //激活虚拟环境
    cd ..            //回到上一级路径
    cd ..            //回到上一级路径（项目的根目录）
    ```
3. 安装第三方的包
    ```cmd
    pip install -r requirements.txt
    ```
## 设计框架
框架结构
```
├── app
│   ├── __init__.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── tools.py
│   └── routes
│       ├── __init__.py
│       └── user.py
├── manager.py
├── requirements.txt
├── README.md
├── logs
├── docs
├── env
├── config.py
└── tests

```

## 已完成功能
- 基本的登录注册的demo实现
- MySQL的方法类的封装
- redis的方法类的封装
- 日志的封装
- token的生成和校验
- 正则表达式的参数校验的类的封装
