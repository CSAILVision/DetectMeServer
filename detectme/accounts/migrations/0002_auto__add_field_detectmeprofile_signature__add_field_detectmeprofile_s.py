# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DetectMeProfile.signature'
        db.add_column(u'accounts_detectmeprofile', 'signature',
                      self.gf('django.db.models.fields.TextField')(default='tbd.', max_length=1024, blank=True),
                      keep_default=False)

        # Adding field 'DetectMeProfile.signature_html'
        db.add_column(u'accounts_detectmeprofile', 'signature_html',
                      self.gf('django.db.models.fields.TextField')(default='tbd.', max_length=1054, blank=True),
                      keep_default=False)

        # Adding field 'DetectMeProfile.time_zone'
        db.add_column(u'accounts_detectmeprofile', 'time_zone',
                      self.gf('django.db.models.fields.FloatField')(default=3.0),
                      keep_default=False)

        # Adding field 'DetectMeProfile.language'
        db.add_column(u'accounts_detectmeprofile', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en-us', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'DetectMeProfile.show_signatures'
        db.add_column(u'accounts_detectmeprofile', 'show_signatures',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Adding field 'DetectMeProfile.post_count'
        db.add_column(u'accounts_detectmeprofile', 'post_count',
                      self.gf('django.db.models.fields.IntegerField')(default=0, blank=True),
                      keep_default=False)

        # Adding field 'DetectMeProfile.avatar'
        db.add_column(u'accounts_detectmeprofile', 'avatar',
                      self.gf('sorl.thumbnail.fields.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'DetectMeProfile.autosubscribe'
        db.add_column(u'accounts_detectmeprofile', 'autosubscribe',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DetectMeProfile.signature'
        db.delete_column(u'accounts_detectmeprofile', 'signature')

        # Deleting field 'DetectMeProfile.signature_html'
        db.delete_column(u'accounts_detectmeprofile', 'signature_html')

        # Deleting field 'DetectMeProfile.time_zone'
        db.delete_column(u'accounts_detectmeprofile', 'time_zone')

        # Deleting field 'DetectMeProfile.language'
        db.delete_column(u'accounts_detectmeprofile', 'language')

        # Deleting field 'DetectMeProfile.show_signatures'
        db.delete_column(u'accounts_detectmeprofile', 'show_signatures')

        # Deleting field 'DetectMeProfile.post_count'
        db.delete_column(u'accounts_detectmeprofile', 'post_count')

        # Deleting field 'DetectMeProfile.avatar'
        db.delete_column(u'accounts_detectmeprofile', 'avatar')

        # Deleting field 'DetectMeProfile.autosubscribe'
        db.delete_column(u'accounts_detectmeprofile', 'autosubscribe')


    models = {
        u'accounts.detectmeprofile': {
            'Meta': {'object_name': 'DetectMeProfile'},
            'autosubscribe': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'favourite_snack': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en-us'", 'max_length': '10', 'blank': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'show_signatures': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'signature': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'signature_html': ('django.db.models.fields.TextField', [], {'max_length': '1054', 'blank': 'True'}),
            'time_zone': ('django.db.models.fields.FloatField', [], {'default': '3.0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'detectme_profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']