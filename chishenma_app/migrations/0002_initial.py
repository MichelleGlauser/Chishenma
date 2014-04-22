# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'chishenma_app_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category_label', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('category_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('category_tag', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'chishenma_app', ['Category'])

        # Adding model 'Dish'
        db.create_table(u'chishenma_app_dish', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dish_name_en', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dish_name_cn', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dish_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('dish_cuisine', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dish_course', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('dish_price', self.gf('django.db.models.fields.IntegerField')()),
            ('dish_last_reviewed', self.gf('django.db.models.fields.DateTimeField')()),
            ('dish_similar', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'chishenma_app', ['Dish'])

        # Adding M2M table for field menu on 'Dish'
        m2m_table_name = db.shorten_name(u'chishenma_app_dish_menu')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dish', models.ForeignKey(orm[u'chishenma_app.dish'], null=False)),
            ('menu', models.ForeignKey(orm[u'chishenma_app.menu'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dish_id', 'menu_id'])

        # Adding model 'Menu'
        db.create_table(u'chishenma_app_menu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('menu_price', self.gf('django.db.models.fields.IntegerField')()),
            ('menu_num_people', self.gf('django.db.models.fields.IntegerField')()),
            ('menu_tags', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('menu_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'chishenma_app', ['Menu'])

        # Adding model 'Review'
        db.create_table(u'chishenma_app_review', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('review_text', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('review_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chishenma_app.Restaurant'])),
        ))
        db.send_create_signal(u'chishenma_app', ['Review'])

        # Adding model 'Restaurant'
        db.create_table(u'chishenma_app_restaurant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rest_name_en', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rest_name_cn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rest_branch', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rest_other_branches', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('rest_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
            ('rest_desc', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rest_dianping_id', self.gf('django.db.models.fields.IntegerField')()),
            ('rest_latlong', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rest_address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rest_district', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rest_city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rest_phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('rest_hours', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rest_url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('rest_map_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chishenma_app.Category'])),
            ('dish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chishenma_app.Dish'])),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['chishenma_app.Menu'])),
            ('rest_bookmarked_users', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'chishenma_app', ['Restaurant'])

        # Adding model 'Foodie'
        db.create_table(u'chishenma_app_foodie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_wechat', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('user_city', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('user_waitlist_status', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user_waitlist_num', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('user_num_referrals', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal(u'chishenma_app', ['Foodie'])

        # Adding model 'Bookmark'
        db.create_table(u'chishenma_app_bookmark', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bookmark_rest_id', self.gf('django.db.models.fields.IntegerField')()),
            ('bookmark_tags', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bookmark_notes', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('bookmark_img', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal(u'chishenma_app', ['Bookmark'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'chishenma_app_category')

        # Deleting model 'Dish'
        db.delete_table(u'chishenma_app_dish')

        # Removing M2M table for field menu on 'Dish'
        db.delete_table(db.shorten_name(u'chishenma_app_dish_menu'))

        # Deleting model 'Menu'
        db.delete_table(u'chishenma_app_menu')

        # Deleting model 'Review'
        db.delete_table(u'chishenma_app_review')

        # Deleting model 'Restaurant'
        db.delete_table(u'chishenma_app_restaurant')

        # Deleting model 'Foodie'
        db.delete_table(u'chishenma_app_foodie')

        # Deleting model 'Bookmark'
        db.delete_table(u'chishenma_app_bookmark')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'chishenma_app.bookmark': {
            'Meta': {'object_name': 'Bookmark'},
            'bookmark_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'bookmark_notes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bookmark_rest_id': ('django.db.models.fields.IntegerField', [], {}),
            'bookmark_tags': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'chishenma_app.category': {
            'Meta': {'object_name': 'Category'},
            'category_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category_label': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'category_tag': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'chishenma_app.dish': {
            'Meta': {'object_name': 'Dish'},
            'dish_course': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dish_cuisine': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dish_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'dish_last_reviewed': ('django.db.models.fields.DateTimeField', [], {}),
            'dish_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dish_name_en': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dish_price': ('django.db.models.fields.IntegerField', [], {}),
            'dish_similar': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['chishenma_app.Menu']", 'symmetrical': 'False'})
        },
        u'chishenma_app.foodie': {
            'Meta': {'object_name': 'Foodie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_city': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_num_referrals': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'user_waitlist_num': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'user_waitlist_status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_wechat': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'chishenma_app.menu': {
            'Meta': {'object_name': 'Menu'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu_date': ('django.db.models.fields.DateTimeField', [], {}),
            'menu_num_people': ('django.db.models.fields.IntegerField', [], {}),
            'menu_price': ('django.db.models.fields.IntegerField', [], {}),
            'menu_tags': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'chishenma_app.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Category']"}),
            'dish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Dish']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Menu']"}),
            'rest_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rest_bookmarked_users': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'rest_branch': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rest_dianping_id': ('django.db.models.fields.IntegerField', [], {}),
            'rest_district': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_hours': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rest_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'rest_latlong': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rest_map_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'rest_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_other_branches': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'rest_phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rest_url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'chishenma_app.review': {
            'Meta': {'object_name': 'Review'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Restaurant']"}),
            'review_date': ('django.db.models.fields.DateTimeField', [], {}),
            'review_text': ('django.db.models.fields.CharField', [], {'max_length': '400'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['chishenma_app']