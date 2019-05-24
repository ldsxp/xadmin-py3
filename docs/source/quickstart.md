# 快速入门指南

要使用Xadmin，需要安装[Django 2.2](http://www.djangoproject.com/)并且必须激活[管理站点](http://docs.djangoproject.com/en/dev/ref/contrib/admin/)。

## 安装

```
pip install xadmin-py3
```

## 运行演示

如果已下载Xadmin的源tarball，则可以`demo_app`在项目层次结构中找到目录。可以发出以下命令以快速创建Xadmin的演示实例：

```
cd demo_app
python manage.py runserver
```

指向浏览器以`http://127.0.0.1:8000`查看结果。

## 使用现有项目

首先，编辑你的`settings.py`Xadmin添加到你的`INSTALLED_APPS`。

```python
INSTALLED_APPS = (
    ...

    'xadmin',
    'crispy_forms',
    # 'reversion',

    ...
)
```

然后添加URL模式并执行`autodiscover`：

```python
# -*- coding: utf-8 -*-
import xadmin
xadmin.autodiscover()

# version 模块自动注册需要版本控制的 Model
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    url(r'xadmin/', include(xadmin.site.urls)),
)
```

收集静态资源（假设到服务器才需要）：

```
python manage.py collectstatic
```

