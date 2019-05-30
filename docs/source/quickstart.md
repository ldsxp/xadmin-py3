# 快速入门指南

要使用Xadmin，需要安装[Django 2.2](http://www.djangoproject.com/)并且必须激活[管理站点](http://docs.djangoproject.com/en/dev/ref/contrib/admin/)。

## 安装

```
pip install xadmin-py3
```

## 运行演示

如果已下载或克隆[xadmin-py3](https://github.com/ldsxp/xadmin-py3)源码，则可以进入`demo_app`目录，运行演示实例：

```
cd demo_app
python manage.py runserver
```

指向浏览器以`http://127.0.0.1:8000`查看结果。

## 使用现有项目

首先，编辑`settings.py`，添加 Xadmin 到`INSTALLED_APPS`。

```python
INSTALLED_APPS = [
    ...

    'xadmin',
    # django-crispy-forms DRY表单
    'crispy_forms',
    # django-reversion 版本控制
    'reversion',

    ...
]
```

然后添加URL模式并执行`autodiscover`：

```python
from django.urls import path
from django.contrib import admin

# 取消注释接下来的两行以启用管理员：
import xadmin
xadmin.autodiscover()

# version模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()


urlpatterns = [
    path(r'admin', admin.site.urls),
]

urlpatterns += [
    path(r'', xadmin.site.urls),
]
```

收集静态资源（安装在服务器才需要）：

```
python manage.py collectstatic
```

