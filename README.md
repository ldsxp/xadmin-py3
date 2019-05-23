# Xadmin-py3



使用 Xadmin 您只需定义您数据的字段等信息，即可即刻获得一个功能全面的管理系统。不仅如此，您还可以方便的扩展更多的定制功能和系统界面。



## 在线演示

- 待更新...



## 功能

- 更好的过滤器，日期范围，数量范围等。

- 基于Bootstrap3，支持在多种屏幕上无缝浏览，并支持Bootstrap主题模板

- 内置丰富的插件功能。包括数据导出、书签、图表、数据添加向导及图片相册等多种扩展功能

- 插件开发简单，安装方便。

  

## 截图

- 待更新...



## 入门



### 安装

通过PyPI安装，请运行：

```
pip install xadmin
```

或从GitHub源安装：

```
pip install git+git://github.com/sshwsfc/xadmin.git
```



## 安装需要

- [django](http://djangoproject.com/) >=1.9
- [django-crispy-forms](http://django-crispy-forms.rtfd.org/) >=1.6.0 (For xadmin crispy forms)
- [django-reversion](https://github.com/etianen/django-reversion) ([OPTION] For object history and reversion feature, please select right version by your django, see [changelog](https://github.com/etianen/django-reversion/blob/master/CHANGELOG.rst) )
- [django-formtools](https://github.com/django/django-formtools) ([OPTION] For wizward form)
- [xlwt](http://www.python-excel.org/) ([OPTION] For export xls files)
- [xlsxwriter](https://github.com/jmcnamara/XlsxWriter) ([OPTION] For export xlsx files)



## 文档

- [Chinese](https://xadmin.readthedocs.org/en/latest/index.html)



## 更改日志



## 在本地运行Demo

```
cd demo_app
./manage.py migrate
./manage.py runserver
```

http://127.0.0.1:8000

在浏览器中打开 [http://127.0.0.1:8000](http://127.0.0.1:8000/) ，管理员用户密码为admin。
