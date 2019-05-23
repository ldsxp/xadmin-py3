@ECHO OFF&PUSHD %~DP0 &TITLE ��վ������
mode con cols=150 lines=30

set scripts=D:\Envs\xadmin-py3\Scripts
set python=%scripts%\python.exe

if not exist %scripts% (
@ echo ���⻷����·�������ڣ������ļ�·����%scripts%�����½����⻷����
@ echo.
echo ���˳������й��ߣ�����
@ echo.
pause
exit

)

SetLocal EnableDelayedExpansion
:Menu
Cls


@ echo.
@ echo.   ѡ��   �� �� 
@ echo.
@ echo.   [r]    ����������
@ echo.
@ echo.   [s]    ����Ӧ�ó���
@ echo.
@ echo.   [1]    ��������Ա
@ echo.
@ echo.   [2]    ���Ǩ��
@ echo.
@ echo.   [3]    Ǩ������
@ echo. 
@ echo.   [e]    ���� requirements.txt
@ echo. 
@ echo.   [i]    ��װ requirements.txt
@ echo. 
@ echo.   �����������������˳�...
@ echo.
@ echo. 


set /p xj= ������ [] �ڵ�ѡ����س���
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
echo ѡ����Ч������������
pause
goto menu


:runserver
cls
@ echo.
ECHO �����������������ַ��127.0.0.1:8100/admin
%python% manage.py runserver 127.0.0.1:8100
goto menu

:create_app
cls
@ echo.
ECHO ����Ӧ�ó���
set /p in= ����Ӧ�ó�������ƣ�
%python% manage.py startapp %in%
@ echo.
pause
goto menu

:create_user
cls
@ echo.
ECHO ��������Ա
%python% manage.py migrate
ECHO ע����ֱ���������û��������䣬���������ʹ������ű����밴���޸ģ�
%python% manage.py createsuperuser --username=lds --email=85176878@qq.com
@ echo.
ECHO ��������Ա���
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
set /p in= ΪӦ�ó���Ǩ�ƣ�
%python% manage.py makemigrations %in%
%python% manage.py migrate
@ ECHO.
ECHO Ǩ���������
@ ECHO.
@ ECHO.
pause
goto menu

:export_requirements
%scripts%\pip freeze > requirements.txt
@ ECHO.
ECHO ���� requirements.txt ���
@ ECHO.
@ ECHO.
pause
cls
goto menu

:import_requirements
%scripts%\pip install -i https://pypi.douban.com/simple/ -r requirements.txt
@ ECHO.
ECHO ��װ requirements.txt ���
@ ECHO.
@ ECHO.
pause
cls
goto menu
