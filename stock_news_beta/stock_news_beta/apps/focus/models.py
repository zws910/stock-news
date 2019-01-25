import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class NewUser(AbstractUser):
    """普通用户"""
    profile = models.CharField('profile', default='', max_length=256)

    def __str__(self):
        return self.username


class Column(models.Model):
    """类别"""
    name = models.CharField('column_name', max_length=256)
    intro = models.TextField('introduction', default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name
        ordering = ['name']


class Article(models.Model):
    """文章"""
    column = models.ForeignKey(Column, blank=True, null=True, verbose_name='belong to')  # 所属类别
    title = models.CharField(max_length=256)
    author = models.ForeignKey('Author')
    user = models.ManyToManyField('NewUser', blank=True)
    content = models.TextField('content')
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    published = models.BooleanField('notDraft', default=True)
    poll_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    keep_num = models.IntegerField(default=0)
    wechat_status = models.BooleanField(default=False)  # 微信采集状态

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name


class Comment(models.Model):
    """评论"""
    user = models.ForeignKey('NewUser', null=True)
    article = models.ForeignKey(Article, null=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    poll_num = models.IntegerField(default=0)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name


class Author(models.Model):
    """作者"""
    name = models.CharField(max_length=256)
    profile = models.CharField('profile', default='', max_length=256)
    password = models.CharField('password', max_length=256)
    register_date = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class Poll(models.Model):
    """点赞"""
    user = models.ForeignKey('NewUser', null=True)
    article = models.ForeignKey(Article, null=True)
    comment = models.ForeignKey(Comment, null=True)

    class Meta:
        verbose_name = '点赞'
        verbose_name_plural = verbose_name
