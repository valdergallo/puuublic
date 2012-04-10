# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Liked'
        db.create_table('public_liked', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_liked', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='public_liked', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['Liked'])

        # Adding model 'Foward'
        db.create_table('public_foward', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_foward', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='public_foward', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['Foward'])

        # Adding model 'Watched'
        db.create_table('public_watched', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_watched', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='public_watched', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['Watched'])

        # Adding model 'Rated'
        db.create_table('public_rated', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_rated', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='public_rated', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['Rated'])

        # Adding model 'Alert'
        db.create_table('public_alert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_alert', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='public_alert', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['Alert'])

        # Adding model 'Tag'
        db.create_table('public_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('public', ['Tag'])

        # Adding model 'PublicTag'
        db.create_table('public_publictag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['public.Tag'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tags', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['PublicTag'])

        # Adding model 'Public'
        db.create_table('public_public', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('lon', self.gf('django.db.models.fields.FloatField')(db_index=True, null=True, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publics', to=orm['auth.User'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='parents', null=True, to=orm['public.Public'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('rated_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('watched_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('liked_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('public', ['Public'])

        # Adding model 'DefaultImage'
        db.create_table('public_defaultimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('public', ['DefaultImage'])

        # Adding model 'PublicImage'
        db.create_table('public_publicimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='public_images', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['PublicImage'])

        # Adding model 'PublicPermission'
        db.create_table('public_publicpermission', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_user', to=orm['auth.User'])),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_friend', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_public', to=orm['public.Public'])),
        ))
        db.send_create_signal('public', ['PublicPermission'])

    def backwards(self, orm):
        # Deleting model 'Liked'
        db.delete_table('public_liked')

        # Deleting model 'Foward'
        db.delete_table('public_foward')

        # Deleting model 'Watched'
        db.delete_table('public_watched')

        # Deleting model 'Rated'
        db.delete_table('public_rated')

        # Deleting model 'Alert'
        db.delete_table('public_alert')

        # Deleting model 'Tag'
        db.delete_table('public_tag')

        # Deleting model 'PublicTag'
        db.delete_table('public_publictag')

        # Deleting model 'Public'
        db.delete_table('public_public')

        # Deleting model 'DefaultImage'
        db.delete_table('public_defaultimage')

        # Deleting model 'PublicImage'
        db.delete_table('public_publicimage')

        # Deleting model 'PublicPermission'
        db.delete_table('public_publicpermission')

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
        'public.alert': {
            'Meta': {'object_name': 'Alert'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'public_alert'", 'to': "orm['public.Public']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_alert'", 'to': "orm['auth.User']"})
        },
        'public.defaultimage': {
            'Meta': {'object_name': 'DefaultImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'public.foward': {
            'Meta': {'object_name': 'Foward'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'public_foward'", 'to': "orm['public.Public']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_foward'", 'to': "orm['auth.User']"})
        },
        'public.liked': {
            'Meta': {'object_name': 'Liked'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'public_liked'", 'to': "orm['public.Public']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_liked'", 'to': "orm['auth.User']"})
        },
        'public.public': {
            'Meta': {'object_name': 'Public'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'liked_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'parents'", 'null': 'True', 'to': "orm['public.Public']"}),
            'rated_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publics'", 'to': "orm['auth.User']"}),
            'watched_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'public.publicimage': {
            'Meta': {'object_name': 'PublicImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'public_images'", 'to': "orm['public.Public']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['auth.User']"})
        },
        'public.publicpermission': {
            'Meta': {'object_name': 'PublicPermission'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'friend': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permission_friend'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permission_user'", 'to': "orm['auth.User']"}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'permission_public'", 'to': "orm['public.Public']"})
        },
        'public.publictag': {
            'Meta': {'object_name': 'PublicTag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': "orm['public.Public']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['public.Tag']"})
        },
        'public.rated': {
            'Meta': {'object_name': 'Rated'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'public_rated'", 'to': "orm['public.Public']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_rated'", 'to': "orm['auth.User']"})
        },
        'public.tag': {
            'Meta': {'object_name': 'Tag'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'public.watched': {
            'Meta': {'object_name': 'Watched'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'public_watched'", 'to': "orm['public.Public']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_watched'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['public']