import xadmin
from xadmin import views

from . import models


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)


class GlobalSettings(object):
    site_title = '股票资讯后台管理系统'
    site_footer = 'beta'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSettings)


class ColumnAdmin(object):
    model_icon = 'fa fa-gift'  # 图标
    list_display = ['id', 'name', 'intro']
    search_fields = ['id', 'name']
    list_editable = ['name', 'intro']


xadmin.site.register(models.Column, ColumnAdmin)


class ArticleAdmin(object):
    list_display = ['column', 'title', 'author', 'content', 'pub_date', 'poll_num']
    search_fields = ['id', 'title', 'author']
    list_editable = []


xadmin.site.register(models.Article, ArticleAdmin)


class CommentAdmin(object):
    list_display = ['user', 'article', 'content', 'pub_date', 'poll_num']
    search_fields = ['user', 'article']
    list_editable = []


xadmin.site.register(models.Comment, CommentAdmin)


class AuthorAdmin(object):
    list_display = ['name', 'profile', 'password', 'register_date']
    search_fields = ['name', 'register_date']
    list_editable = []


xadmin.site.register(models.Author, AuthorAdmin)


class PollAdmin(object):
    list_display = ['user', 'article', 'comment']
    search_fields = ['user', 'article', 'comment']
    list_editable = []


xadmin.site.register(models.Poll, PollAdmin)