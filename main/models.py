
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
import sys
from PIL import Image
from io import BytesIO
from django.core.files import File
from django import forms
# from django.contrib.auth.models import User


class Apartments(models.Model):
    apt_id = models.AutoField(primary_key=True)
    apt_name_eng = models.CharField(max_length=50, blank=True, null=True)
    apt_name_ua = models.CharField(max_length=50, blank=True, null=True)

    def __str__ (self):
        return self.apt_name_ua

    class Meta:
        managed = True
        db_table = 'apartments'
        verbose_name_plural = 'Квартири'
        verbose_name = 'Квартира'
        ordering = ['apt_id']


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Brands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=255)

    def __str__ (self):
        return self.brand_name

    class Meta:
        managed = False
        db_table = 'brands'
        verbose_name_plural = 'Бренди'
        verbose_name = 'Бренд'
        ordering = ['brand_name']


class Condition(models.Model):
    cond_id = models.SmallAutoField(primary_key=True)
    cond_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__ (self):
        return self.cond_name

    class Meta:
        managed = False
        db_table = 'condition'
        verbose_name_plural = 'Стан'
        verbose_name = 'Стан'
        ordering = ['-cond_name']


class Connection(models.Model):
    conn_id = models.IntegerField(primary_key=True)
    conn_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__ (self):
        return self.conn_name

    class Meta:
        managed = False
        db_table = 'connection'
        verbose_name_plural = "Під'єднання"
        verbose_name = "Під'єднання"
        ordering = ['-conn_name']


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Inventory(models.Model):
    name = models.ForeignKey('Names', models.DO_NOTHING, blank=True, null=True, verbose_name='Назва')
    brand = models.ForeignKey(Brands, models.DO_NOTHING, blank=True, null=True, verbose_name='Бренд')
    apt = models.ForeignKey(Apartments, models.DO_NOTHING, blank=True, null=True, verbose_name='Квартира №')
    loc = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True, verbose_name='Розташування')
    type = models.ForeignKey('Type', models.DO_NOTHING, blank=True, null=True, verbose_name='Категорія')
    conn = models.ForeignKey(Connection, models.DO_NOTHING, blank=True, null=True, verbose_name='Встановлення')
    cond = models.ForeignKey(Condition, models.DO_NOTHING, blank=True, null=True, verbose_name='Стан')
    input_date = models.DateField(verbose_name='Дата придбання')
    comments = models.CharField(max_length=255, blank=True, null=True, verbose_name='Коментар')
    invent_id = models.CharField(default=0, max_length=12)

# generating invent id according to certain template
    @property
    def generate_invent_id(self):
        return 'PHR-{0:07d}'.format(self.pk)

    @property
    def get_images(self):
        return self.images.all()

# selecting first pic for thumbnail in list of items
    @property
    def get_first_image(self):
        a = self.images.all()
        if len(a):
            return a[0]
        else:
            return ''

    def __str__ (self):
        return self.name

    class Meta:
        managed = True
        db_table = 'inventory'
        verbose_name_plural = 'Інвентаризація'
        verbose_name = 'Інвентаризація'
        ordering = ['invent_id']


class Pics(models.Model):
    id = models.AutoField(primary_key=True)
    pics_link = models.BinaryField(null=True)
    img = models.ImageField(upload_to='pics/')
    invent = models.ForeignKey(Inventory, models.DO_NOTHING, related_name='images', db_column='invent', verbose_name='Фото')

    def save(self, *args, **kwargs):
        if not self.id:
            self.img = self.compressImage(self.img)
        super(Pics, self).save(*args, **kwargs)

    def compressImage(self, img):
        image = Image.open(img).convert("RGB")
        im_io = BytesIO()

        if img.name.split('.')[1] == 'jpeg' or img.name.split('.')[1] == 'jpg':
            image.save(im_io, format='jpeg', optimize=True, quality=55)
            new_image = File(im_io, name="%s.jpeg" % img.name.split('.')[0], )
        else:
            image.save(im_io, format='png', optimize=True, quality=55)
            new_image = File(im_io, name="%s.png" % img.name.split('.')[0], )

        return new_image

    def __str__ (self):
        return self.img


    class Meta:
        managed = True
        db_table = 'pics'
        app_label = 'main'
        verbose_name_plural = 'Фотографії'
        verbose_name = 'Фотографії'
        ordering = ['invent']

class Location(models.Model):
    loc_id = models.IntegerField(primary_key=True)
    loc_name_eng = models.CharField(max_length=25, blank=True, null=True)
    loc_name_ua = models.CharField(max_length=35, blank=True, null=True)

    def __str__ (self):
        return self.loc_name_eng

    class Meta:
        managed = False
        db_table = 'location'
        verbose_name_plural = 'Де знаходиться'
        verbose_name = 'Де знаходиться'
        ordering = ['loc_name_eng']

class Names(models.Model):
    name_id = models.AutoField(primary_key=True)
    name_eng = models.CharField(max_length=255)
    name_ua = models.CharField(max_length=255)

    def __str__ (self):
        return self.name_ua

    class Meta:
        managed = False
        db_table = 'names'
        verbose_name_plural = 'Назва майна'
        verbose_name = 'Назва майна'
        ordering = ['name_ua']




class TestTable(models.Model):
    s_no = models.CharField(max_length=10)
    txt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_table'


class Type(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__ (self):
        return self.type_name

    class Meta:
        managed = False
        db_table = 'type'

