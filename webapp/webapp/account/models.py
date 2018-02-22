#coding:utf-8
# Last modified: 2017-02-04 09:09:52
from django.db import models
import hashlib
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
'''
用户系统
组->用户
1. 管理员
2. 代理商
3. 景区用户
'''

CHOICES_GROUP_TYPE = (
    (0, u'管理员'),
    (1, u'代理商'),
    (2, u'景区用户'),
)

class Group(models.Model):
    role = models.SmallIntegerField(u'角色',default=0)
    name = models.CharField(u'组名称', max_length=100)
    parent = models.ForeignKey('self', related_name='children', null=True)

class UserManager(BaseUserManager):
    def create_user(self, group, cellphone, username=None,password=None):
        user = self.model(
            group=group,
    		cellphone=cellphone,
    	)
    	user.save(using=self._db)
    	return user

    def create_superuser(self, cellphone, password=None):
        _groups = Group.objects.all()
        if _groups:
            group = _groups[0]
        else:
            group = Group(role=0, name=u'多倍通管理员').save()
        user = self.create_user(group, cellphone, password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    group = models.ForeignKey(Group)
    cellphone  = models.CharField(u'手机号', max_length=11, unique=True)
    # 验证码应该不需要，发短信时存在session里等待验证
    #captcha    = models.CharField(u'验证码', max_length=6)
    wechatUNID = models.CharField(u'微信ID', max_length=64)
    nickname   = models.CharField(u'昵称', max_length=50)

    username = models.CharField(max_length=64,null=True)
    headimgurl = models.CharField(max_length=200,null=True)

    created = models.DateTimeField(auto_now_add=True)
    
    is_delete = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = UserManager()

    USERNAME_FIELD = 'cellphone'
    REQUIRED_FIELDS = ()

    class Meta:
		ordering = ('-created',)

    def __unicode__(self):
		return self.cellphone

    def get_full_name(self):
		return self.nickname or self.cellphone

    def get_short_name(self):
		return self.cellphone

    def has_perm(self, perm, obj=None):
		return True

    def has_module_perms(self, app_label):
		return True

    def get_avatar_url(self):
		# 微信头像或默认图片
		return 'http://xxx.png'
  
    @property
    def is_staff(self):
		# 加上咱们的,写到settings里去
		if self.cellphone in ('15313177798',):
			return True
		return False

    @property
    def is_supperuser(self):
		# 加上咱们的
		if self.cellphone in ('15313177798',):
			return True
		return False
