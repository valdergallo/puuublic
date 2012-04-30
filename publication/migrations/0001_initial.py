# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Liked'
        db.create_table('publication_liked', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_liked', to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publication_liked', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['Liked'])

        # Adding model 'Foward'
        db.create_table('publication_foward', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_foward', to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publication_foward', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['Foward'])

        # Adding model 'Watched'
        db.create_table('publication_watched', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_watched', to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publication_watched', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['Watched'])

        # Adding model 'Rated'
        db.create_table('publication_rated', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_rated', to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publication_rated', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['Rated'])

        # Adding model 'Alert'
        db.create_table('publication_alert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_alert', to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publication_alert', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['Alert'])

        # Adding model 'Tag'
        db.create_table('publication_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('publication', ['Tag'])

        # Adding model 'PublicationTag'
        db.create_table('publication_publicationtag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publication.Tag'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['PublicationTag'])

        # Adding model 'Publication'
        db.create_table('publication_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publications', to=orm['auth.User'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parents', null=True, to=orm['publication.Publication'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=30, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('rated_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('watched_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('liked_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('publication', ['Publication'])

        # Adding model 'PublicationImage'
        db.create_table('publication_publicationimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publication_images', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['PublicationImage'])

        # Adding model 'Comment'
        db.create_table('publication_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['Comment'])

        # Adding model 'PublicationPermission'
        db.create_table('publication_publicationpermission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_user', to=orm['auth.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_friend', to=orm['auth.User'])),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_Publication', to=orm['publication.Publication'])),
        ))
        db.send_create_signal('publication', ['PublicationPermission'])

    def backwards(self, orm):
        # Deleting model 'Liked'
        db.delete_table('publication_liked')

        # Deleting model 'Foward'
        db.delete_table('publication_foward')

        # Deleting model 'Watched'
        db.delete_table('publication_watched')

        # Deleting model 'Rated'
        db.delete_table('publication_rated')

        # Deleting model 'Alert'
        db.delete_table('publication_alert')

        # Deleting model 'Tag'
        db.delete_table('publication_tag')

        # Deleting model 'PublicationTag'
        db.delete_table('publication_publicationtag')

        # Deleting model 'Publication'
        db.delete_table('publication_publication')

        # Deleting model 'PublicationImage'
        db.delete_table('publication_publicationimage')

        # Deleting model 'Comment'
        db.delete_table('publication_comment')

        # Deleting model 'PublicationPermission'
        db.delete_table('publication_publicationpermission')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'publication.alert': {
            'Meta': {'object_name': 'Alert'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_alert'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_alert'", 'to': "orm['auth.User']"})
        },
        'publication.comment': {
            'Meta': {'object_name': 'Comment'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'publication.foward': {
            'Meta': {'object_name': 'Foward'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_foward'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_foward'", 'to': "orm['auth.User']"})
        },
        'publication.liked': {
            'Meta': {'object_name': 'Liked'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_liked'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_liked'", 'to': "orm['auth.User']"})
        },
        'publication.publication': {
            'Meta': {'object_name': 'Publication'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'liked_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parents'", 'null': 'True', 'to': "orm['publication.Publication']"}),
            'rated_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publications'", 'to': "orm['auth.User']"}),
            'watched_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'publication.publicationimage': {
            'Meta': {'object_name': 'PublicationImage'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_images'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['auth.User']"})
        },
        'publication.publicationpermission': {
            'Meta': {'object_name': 'PublicationPermission'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permission_Publication'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permission_friend'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permission_user'", 'to': "orm['auth.User']"})
        },
        'publication.publicationtag': {
            'Meta': {'object_name': 'PublicationTag'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publication.Tag']"})
        },
        'publication.rated': {
            'Meta': {'object_name': 'Rated'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_rated'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_rated'", 'to': "orm['auth.User']"})
        },
        'publication.tag': {
            'Meta': {'object_name': 'Tag'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'publication.watched': {
            'Meta': {'object_name': 'Watched'},
            'Publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_watched'", 'to': "orm['publication.Publication']"}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_watched'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['publication']