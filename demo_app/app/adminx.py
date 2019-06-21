from __future__ import absolute_import
import xadmin
from xadmin import views
from xadmin.models import UserWidget
from .models import IDC, Host, MaintainLog, HostGroup, AccessRecord
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction
from xadmin.filters import MultiSelectFieldListFilter
from xadmin.plugins.actions import BaseActionView

from django.http import HttpResponse


@xadmin.sites.register(views.website.IndexView)
class MainDashboard(object):
    """ 主页面 """
    widgets = [
        [
            # 定义 html 内容
            {"type": "html", "title": "主页 Widget",
             "content": "<h3> Welcome to Xadmin! </h3><p>Github: https://github.com/ldsxp/xadmin-py3</p>"},
            # 定义图表
            {"type": "chart", "model": "app.accessrecord", "chart": "user_count",
             "params": {"_p_date__gte": "2013-01-08", "p": 1, "_p_date__lt": "2013-01-29"}},
            # 显示模型内容
            {"type": "list", "model": "app.host", "params": {"o": "-guarantee_date", "_p_name__contains": "显示"}},
        ],
        [
            # 定义按钮
            {"type": "qbutton", "title": "快速开始",
             "btns": [{"model": UserWidget}, {"model": Host}, {"model": IDC},
                      {"title": "Google", "url": "http://www.google.com"}]},
            # 定义 添加内容表单
            {"type": "addform", "model": MaintainLog},
        ]
    ]


@xadmin.sites.register(views.BaseAdminView)
class BaseSetting(object):
    # 开启主题选择
    enable_themes = True
    use_bootswatch = True


@xadmin.sites.register(views.CommAdminView)
class GlobalSetting(object):
    """
    主要是一些 xadmin 页面通用的内容设置
    """
    # 网站标题
    site_title = '我们的网站标题'
    # 网站的下角标文字
    site_footer = '20190530 by xadmin'
    # 全局搜索
    global_search_models = [Host, IDC]
    # 全局的 Model 图标
    global_models_icon = {
        Host: 'fa fa-laptop', IDC: 'fa fa-cloud'
    }
    # 默认 Model 图标
    # default_model_icon = None
    # View模板继承的基础模板
    # base_template = 'xadmin/base_site.html'
    # 网站菜单
    menu_style = 'default'  # 'accordion'  左侧导航条修改可折叠


class MaintainInline(object):
    model = MaintainLog
    extra = 1
    style = 'accordion'


class MyAction(BaseActionView):
    """ 自定义 Action """

    # 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    action_name = 'my_action'
    #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.
    description = '测试选择 %(verbose_name_plural)s'

    # Action 需要的权限
    model_perm = 'change'

    # 实现 do_action 方法
    def do_action(self, queryset):
        # queryset 是包含了已经选择的数据的 queryset
        for obj in queryset:
            # obj 的操作
            ...
        # 返回 HttpResponse
        return HttpResponse('修改成功！')


@xadmin.sites.register(IDC)
class IDCAdmin(object):

    # 自定义显示列
    def open_web(self, instance):
        return """<a href="http://%s" target="_blank">Open</a>""" % instance.name

    open_web.short_description = "Acts"
    open_web.allow_tags = True
    open_web.is_column = True

    # 插件 list
    # 列表显示的字段 默认 ('__str__',)
    list_display = ('name', 'description', 'create_time', 'contact', 'telphone', 'address', 'customer_id', 'open_web')
    # 显示修改或查看数据详情连接的列
    list_display_links = ('name',)
    # 点击列表连接后是否转到详情页面
    list_display_links_details = False
    # 是否提前加载关联数据, 使用 ``select_related``
    list_select_related = None
    # 每页显示数据的条数
    list_per_page = 50
    # 每页最大显示数据的条数
    list_max_show_all = 200
    # 排除显示的列, 在显示列的设置中不会出现这些被排除的列
    list_exclude = ()
    # 搜索的字段, 使用模糊搜索
    search_fields = ['name', 'description', 'contact', 'telphone', 'address']
    # 是否可以自由搜索. 如果开启自由搜索, 用户可以通过 url 参数来进行特定的搜索, 例如:name__contains=我，默认为 True
    # 这个会影响到过滤，因为他也规范化了过滤查询内容
    # free_query_filter = False
    # 排序（加‘-’表示降序）
    # ordering = None

    # 添加数据时候，一步一步填写数据
    wizard_form_list = [
        ('第一步', ('name', 'description')),
        ('第二步', ('contact', 'telphone', 'address')),
        ('第三步', ('customer_id',))
    ]

    # 过滤器, 系统会自动生成搜索器
    list_filter = ['name', ]
    # list_quick_filter 必须是 list_filter 的一个子集才能工作
    list_quick_filter = [{'field': 'name', 'limit': 10}]
    # 添加过滤（这里是过滤日期）
    # date_hierarchy = ['date']
    # filter_horizontal 从‘多选框’的形式改变为‘过滤器’的方式，水平排列过滤器，
    # 必须是一个 ManyToManyField类型，且不能用于 ForeignKey字段，
    # 默认地，管理工具使用``下拉框`` 来展现`` 外键`` 字段
    # filter_horizontal = ('authors',)
    # 同上 filter_horizontal，垂直排列过滤器
    # filter_vertical = ['authors', ]

    # 开启书签功能，默认为 True
    # show_bookmarks = False
    # 设置默认书签
    # 用户可以在列表页面添加自己的书签, 我们可以设定好一些默认书签
    list_bookmarks = [{
        'title': '我是默认书签',  # 书签的名称, 显示在书签菜单中
        'query': {'name__exact': '123'},  # 过滤参数, 是标准的 queryset 过滤
        'order': ('-name',),  # 排序参数
        'cols': ('name', 'contact'),  # 显示的列
        'search': 'name'  # 搜索参数, 指定搜索的内容
    },
    ]

    # 定义数据导出功能，可以导出 Excel, CSV, XML, json 格式('xls', 'csv', 'xml', 'json')
    list_export = ('xls', 'csv', 'xml', 'json')

    # 列表定时刷新
    # 定义自动刷新列表, 用户可以选择3秒或5秒刷新一次页面
    refresh_times = (3, 5)

    # 显示数据详情 details
    # 设置哪些字段要显示详细信息的按钮
    show_detail_fields = ['name', ]
    # 自动显示所有关联字段的详细信息, 该属性默认为 True
    # show_all_rel_details = False

    # 数据即时编辑
    # 使用 Ajax , 无需提交或刷新页面即可完成数据的修改
    list_editable = ['name']

    # 将ForeignKey字段从‘下拉框’改变为‘文本框’显示
    raw_id_fields = ("groups",)

    # 当 Model 是其他 Model 的 ref model 时，其他 Model 在显示本 Model 的字段时使用的 Field Style
    # fk-ajax 涉及到外键下拉的时候使用ajax搜索的方式而不是全部列出的方式，比如在分类下拉很多的情况下，这个功能就很好用
    relfield_style = 'fk-select'

    # 图标样式
    model_icon = 'fa fa-user-secret'

    reversion_enable = True

    # 插件 edit
    # 是否显示 ``另存为`` 按钮，默认为 False
    save_as = True
    # 是否在页面上面显示按钮组，默认为 False，这个测试无效
    # save_on_top = True
    # 字段显示样式
    # style_fields = {
    #     "name": "radio-inline",
    #     "contact": "checkbox-inline",
    # }

    # 页面 Form 的 Layout 对象，是一个标准的 Crispy Form Layout 对象。
    # 使用 Layout 可以方便的定义整个 Form 页面的结构。
    form_layout = (
        # 主区域
        Main(
            TabHolder(
                Tab(
                    'TAB 名字',
                    Fieldset(
                        '名字',
                        # 单行显示字段内容
                        Row('telphone', 'address'),
                        'description',
                        # Inline(MaintainLog),  # 无效
                        description='一些说明文字',
                    ),
                ),
                Tab(
                    'TAB 名字 2',
                    Fieldset(
                        '一些名字',
                        Row('telphone', 'address'),
                        Row(
                            AppendedText('customer_id', '描述'),
                        ),
                        # 'create_time'    # 无效
                    ),
                ),
            ),
        ),
        # 侧边区域
        Side(
            Fieldset('Status data', 'telphone', 'address'),
        )
    )

    # 插件 aggregation
    # 列聚合，在list表格下面会增加一行统计的数据，可用的值： count min max avg sum
    # aggregate_fields = {'user_count': 'sum', }

    # 插件 layout
    # 列表的布局方式，是以表格一行一条的方式还是类似于缩略图的方式展示的
    # grid_layouts = ("table", "thumbnails")

    # actions 属性是一个列表, 包含启用的 Action 的类. 系统已经默认内置了删除数据的 Action,
    # 可以制作 Action 来实现特定的功能, 例如 MyAction
    actions = [BatchChangeAction, MyAction, ]
    # 批处理的字段
    batch_fields = ('contact', 'description', 'address', 'customer_id')

    # def queryset(self):
    #     """函数作用：使当前登录的用户只能看到自己内容"""
    #     qs = self.super().queryset()
    #     if self.request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=self.request.user)


@xadmin.sites.register(Host)
class HostAdmin(object):

    def open_web(self, instance):
        return """<a href="http://%s" target="_blank">Open</a>""" % instance.ip

    open_web.short_description = "Acts"
    open_web.allow_tags = True
    open_web.is_column = True

    list_display = (
        "name", "idc", "guarantee_date", "service_type", "status", "open_web",
        "description", "ip",
    )
    list_display_links = ("name",)

    raw_id_fields = ("idc",)
    style_fields = {"system": "radio-inline"}

    search_fields = ["name", "ip", "description", "idc__name"]
    list_filter = [
        "idc", "guarantee_date", "status", "brand", "model", "cpu", "core_num",
        "hard_disk", "memory", (
            "service_type",
            MultiSelectFieldListFilter,
        ),
    ]

    list_quick_filter = ["service_type", {"field": "idc__name", "limit": 10}]
    # list_quick_filter = ["idc_id"]
    list_bookmarks = [{
        "title": "Need Guarantee",
        "query": {"status__exact": 2},
        "order": ("-guarantee_date",),
        "cols": ("brand", "guarantee_date", "service_type"),
    }]

    show_detail_fields = ("idc",)
    list_editable = (
        "name", "idc", "guarantee_date", "service_type", "description", "ip"
    )
    save_as = True

    aggregate_fields = {"guarantee_date": "min"}
    grid_layouts = ("table", "thumbnails")

    form_layout = (
        Main(
            TabHolder(
                Tab(
                    "Comm Fields",
                    Fieldset(
                        "Company data", "name", "idc",
                        description="some comm fields, required",
                    ),
                    Inline(MaintainLog),
                ),
                Tab(
                    "Extend Fields",
                    Fieldset(
                        "Contact details",
                        "service_type",
                        Row("brand", "model"),
                        Row("cpu", "core_num"),
                        Row(
                            AppendedText("hard_disk", "G"),
                            AppendedText("memory", "G")
                        ),
                        "guarantee_date"
                    ),
                ),
            ),
        ),
        Side(
            Fieldset("Status data", "status", "ssh_port", "ip"),
        )
    )
    inlines = [MaintainInline]
    reversion_enable = True

    # 定义图表
    # title : 图表的显示名称
    # x-field : 图表的 X 轴数据列, 一般是日期, 时间等
    # y-field : 图表的 Y 轴数据列, 该项是一个 list, 可以同时设定多个列, 这样多个列的数据会在同一个图表中显示
    # order : 排序信息, 如果不写则使用数据列表的排序
    data_charts = {
        "host_service_type_counts": {'title': "Host service type count", "x-field": "service_type",
                                     "y-field": ("service_type",),
                                     "option": {
                                         "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
                                         "xaxis": {"aggregate": "count", "mode": "categories"},
                                     },
                                     },
    }


@xadmin.sites.register(HostGroup)
class HostGroupAdmin(object):
    list_display = ("name", "description")
    list_display_links = ("name",)

    list_filter = ["hosts"]
    search_fields = ["name"]
    style_fields = {"hosts": "checkbox-inline"}


@xadmin.sites.register(MaintainLog)
class MaintainLogAdmin(object):
    list_display = (
        "host", "maintain_type", "hard_type", "time", "operator", "note")
    list_display_links = ("host",)

    list_filter = ["host", "maintain_type", "hard_type", "time", "operator"]
    search_fields = ["note"]

    form_layout = (
        Col("col2",
            Fieldset("Record data",
                     "time", "note",
                     css_class="unsort short_label no_title"
                     ),
            span=9, horizontal=True
            ),
        Col("col1",
            Fieldset("Comm data",
                     "host", "maintain_type"
                     ),
            Fieldset("Maintain details",
                     "hard_type", "operator"
                     ),
            span=3
            )
    )
    reversion_enable = True


@xadmin.sites.register(AccessRecord)
class AccessRecordAdmin(object):

    def avg_count(self, instance):
        return int(instance.view_count / instance.user_count)

    avg_count.short_description = "Avg Count"
    avg_count.allow_tags = True
    avg_count.is_column = True

    list_display = ("date", "user_count", "view_count", "avg_count")
    list_display_links = ("date",)

    list_filter = ["date", "user_count", "view_count"]
    actions = None
    aggregate_fields = {"user_count": "sum", "view_count": "sum"}

    refresh_times = (3, 5, 10)
    data_charts = {
        "user_count": {'title': "User Report", "x-field": "date", "y-field": ("user_count", "view_count"),
                       "order": ('date',)},
        "avg_count": {'title': "Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)},
        "per_month": {'title': "Monthly Users", "x-field": "_chart_month", "y-field": ("user_count",),
                      "option": {
                          "series": {"bars": {"align": "center", "barWidth": 0.8, 'show': True}},
                          "xaxis": {"aggregate": "sum", "mode": "categories"},
                      },
                      },
    }

    def _chart_month(self, obj):
        return obj.date.strftime("%B")

# xadmin.sites.site.register(HostGroup, HostGroupAdmin)
# xadmin.sites.site.register(MaintainLog, MaintainLogAdmin)
# xadmin.sites.site.register(IDC, IDCAdmin)
# xadmin.sites.site.register(AccessRecord, AccessRecordAdmin)

# from xadmin.models import Log
# from django.contrib.auth.models import Group
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Permission

# # 取消日志管理
# xadmin.sites.site.unregister(Log)
# # 取消 认证和授权 - 组
# xadmin.sites.site.unregister(Group)
# # 取消 认证和授权 - 用户
# xadmin.sites.site.unregister(User)
# # 取消 认证和授权 - 权限
# xadmin.sites.site.unregister(Permission)
