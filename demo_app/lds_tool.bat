@ECHO OFF&PUSHD %~DP0 &TITLE 网站管理工具
mode con cols=150 lines=30

set scripts=D:\Envs\xadmin-py3\Scripts
set python=%scripts%\python.exe

if not exist %scripts% (
@ echo 虚拟环境的路径不存在，修正文件路径（%scripts%）或新建虚拟环境。
@ echo.
echo 将退出命令行工具！！！
@ echo.
pause
exit

)

SetLocal EnableDelayedExpansion
:Menu
Cls


@ echo.
@ echo.   选项   菜 单 
@ echo.
@ echo.   [r]    启动服务器
@ echo.
@ echo.   [s]    创建应用程序
@ echo.
@ echo.   [1]    创建管理员
@ echo.
@ echo.   [2]    检查迁移
@ echo.
@ echo.   [3]    迁移数据
@ echo. 
@ echo.   [e]    导出 requirements.txt
@ echo. 
@ echo.   [i]    安装 requirements.txt
@ echo. 
@ echo.   输入其他任意内容退出...
@ echo.
@ echo. 


set /p xj= 请输入 [] 内的选项，按回车：
if /i "%xj%"=="r" Goto runserver
if /i "%xj%"=="s" Goto create_app
if /i "%xj%"=="1" Goto create_user
if /i "%xj%"=="2" Goto check_db
if /i "%xj%"=="3" Goto create_db
if /i "%xj%"=="e" Goto export_requirements
if /i "%xj%"=="i" Goto import_requirements
@ echo.
cls
exit
echo 选择无效，请重新输入
pause
goto menu


:runserver
cls
@ echo.
ECHO 启动服务器，管理地址：127.0.0.1:8100/admin
%python% manage.py runserver 127.0.0.1:8100
goto menu

:create_app
cls
@ echo.
ECHO 创建应用程序
set /p in= 输入应用程序的名称：
%python% manage.py startapp %in%
@ echo.
pause
goto menu

:create_user
cls
@ echo.
ECHO 创建管理员
%python% manage.py migrate
ECHO 注：我直接输入了用户名和邮箱，如果您正在使用这个脚本，请按需修改！
%python% manage.py createsuperuser --username=lds --email=85176878@qq.com
@ echo.
ECHO 创建管理员完成
pause
goto menu

:check_db
cls
@ echo.
%python% manage.py check
pause
goto menu

:create_db
cls
@ echo.
set /p in= 为应用程序迁移：
%python% manage.py makemigrations %in%
%python% manage.py migrate
@ ECHO.
ECHO 迁移数据完成
@ ECHO.
@ ECHO.
pause
goto menu

:export_requirements
%scripts%\pip freeze > requirements.txt
@ ECHO.
ECHO 导出 requirements.txt 完成
@ ECHO.
@ ECHO.
pause
cls
goto menu

:import_requirements
%scripts%\pip install -i https://pypi.douban.com/simple/ -r requirements.txt
@ ECHO.
ECHO 安装 requirements.txt 完成
@ ECHO.
@ ECHO.
pause
cls
goto menu
