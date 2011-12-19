# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ProductPrice.product'
        db.alter_column('website_productprice', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Product']))


    def backwards(self, orm):
        
        # Changing field 'ProductPrice.product'
        db.alter_column('website_productprice', 'product_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Author']))


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.gallery': {
            'Meta': {'ordering': "('sort',)", 'object_name': 'Gallery'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'website.author': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'website.category': {
            'Meta': {'ordering': "('sort',)", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'website.news': {
            'Meta': {'ordering': "('-dt_mod', '-id')", 'object_name': 'News'},
            'content': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'dt_mod': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'preview': ('django.db.models.fields.TextField', [], {}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'website.product': {
            'Meta': {'ordering': "('sort',)", 'object_name': 'Product'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Author']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Category']"}),
            'content': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'website.productprice': {
            'Meta': {'object_name': 'ProductPrice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Product']"})
        },
        'website.settings': {
            'Meta': {'object_name': 'Settings'},
            'email': ('common.fields.MultiEmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['website']
