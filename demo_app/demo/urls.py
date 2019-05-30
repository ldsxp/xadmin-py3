# -*- coding: utf-8 -*-
# from django.conf.urls import include, url
from django.urls import include, path
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
