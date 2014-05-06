# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Restaurant.rest_dianping_id'
        db.alter_column(u'chishenma_app_restaurant', 'rest_dianping_id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Restaurant.rest_position'
        db.alter_column(u'chishenma_app_restaurant', 'rest_position', self.gf('geoposition.fields.GeopositionField')(max_length=42, null=True))

    def backwards(self, orm):

        # Changing field 'Restaurant.rest_dianping_id'
        db.alter_column(u'chishenma_app_restaurant', 'rest_dianping_id', self.gf('django.db.models.fields.IntegerField')(default=1))

        # Changing field 'Restaurant.rest_position'
        db.alter_column(u'chishenma_app_restaurant', 'rest_position', self.gf('geoposition.fields.GeopositionField')(max_length=42))

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
            'bookmark_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bookmark_notes': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'bookmark_rest_id': ('django.db.models.fields.IntegerField', [], {}),
            'bookmark_tags': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'bookmarker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
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
            'dish_course': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'dish_cuisine': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dish_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dish_last_reviewed': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'dish_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'dish_name_en': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'dish_price': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'dish_similar': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
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
            'bookmarked_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rest_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rest_branch': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rest_city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_desc': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'rest_dianping_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rest_dishes': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Dish']", 'null': 'True', 'blank': 'True'}),
            'rest_district': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_hours': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rest_img': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rest_map_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'rest_menu': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Menu']", 'null': 'True', 'blank': 'True'}),
            'rest_name_cn': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rest_name_en': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rest_other_branches': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'rest_phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'rest_position': ('geoposition.fields.GeopositionField', [], {'default': "'0,0'", 'max_length': '42', 'null': 'True'}),
            'rest_url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'chishenma_app.review': {
            'Meta': {'object_name': 'Review'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['chishenma_app.Restaurant']"}),
            'review_date': ('django.db.models.fields.DateTimeField', [], {}),
            'review_text': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'reviewer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
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