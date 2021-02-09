# VSCode中运行虚拟 Python 环境及其建立基础的应用项目结构

1. `python -m venv venv[虚拟环境配置文件所在的文件夹名]` (pyVenvTest 根据自己的命名修改）
   
2. `call venv/Scripts/activate.bat` 跳转到虚拟环境执行命令
   
3. `call ./venv/Scripts/deactivate` 退出虚拟环境
   
4. `pip freeze > requirements.txt` 生成依赖包列表文件
   
5. `pip install -r requirements.txt` 安装依赖包
   
6. `python -m tests --package=xxx --module=xxx --clsname=xxx` 单元测试执行
   
7. `python -m app --package=xxx --module=xxx --method=xxx` 应用执行
   
## 项目结构说明
   + app 是整个应用程序的执行文件目录, `__main__.py`启动入口
   + tests 是整个应用程序的测试文件目录
   + docs 项目帮助文档
   + requirement.txt 用于存放整个应用依赖的外部Python包列表
   + ReadMe.md 项目说明文档

## 项目目录
1. [x] [测试](./docs/demo.md)
