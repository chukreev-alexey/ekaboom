# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table('website_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('common.fields.MultiEmailField')(max_length=255)),
        ))
        db.send_create_signal('website', ['Settings'])

        # Adding model 'News'
        db.create_table('website_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255, null=True, blank=True)),
            ('dt_mod', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('preview', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('website', ['News'])

        # Adding model 'Author'
        db.create_table('website_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('website', ['Author'])

        # Adding model 'Category'
        db.create_table('website_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('website', ['Category'])

        # Adding model 'Product'
        db.create_table('website_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Author'])),
            ('materials', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('content', self.gf('tinymce.models.HTMLField')(null=True, blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
        ))
        db.send_create_signal('website', ['Product'])

        # Adding model 'ProductPrice'
        db.create_table('website_productprice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['website.Author'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('website', ['ProductPrice'])


    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table('website_settings')

        # Deleting model 'News'
        db.delete_table('website_news')

        # Deleting model 'Author'
        db.delete_table('website_author')

        # Deleting model 'Category'
        db.delete_table('website_category')

        # Deleting model 'Product'
        db.delete_table('website_product')

        # Deleting model 'ProductPrice'
        db.delete_table('website_productprice')


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
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'website.news': {
            'Meta': {'ordering': "('-dt_mod', '-id')", 'object_name': 'News'},
            'content': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'dt_mod': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'preview': ('django.db.models.fields.TextField', [], {}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'website.product': {
            'Meta': {'ordering': "('sort',)", 'object_name': 'Product'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Author']"}),
            'content': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'materials': ('tinymce.models.HTMLField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'})
        },
        'website.productprice': {
            'Meta': {'object_name': 'ProductPrice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['website.Author']"})
        },
        'website.settings': {
            'Meta': {'object_name': 'Settings'},
            'email': ('common.fields.MultiEmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['website']
