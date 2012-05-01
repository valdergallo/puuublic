# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PublicationPermission'
        db.delete_table('publication_publicationpermission')

        # Adding model 'Moderator'
        db.create_table('publication_moderator', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='moderator_owner', to=orm['auth.User'])),
            ('moderator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='moderator_user', to=orm['auth.User'])),
            ('publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='publication_moderator', to=orm['publication.Publication'])),
            ('can_publish', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('can_exclude', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('publication', ['Moderator'])

        # Deleting field 'Comment.Publication'
        db.delete_column('publication_comment', 'Publication_id')

        # Adding field 'Comment.publication'
        db.add_column('publication_comment', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='comments', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'PublicationImage.Publication'
        db.delete_column('publication_publicationimage', 'Publication_id')

        # Adding field 'PublicationImage.publication'
        db.add_column('publication_publicationimage', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_images', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Foward.Publication'
        db.delete_column('publication_foward', 'Publication_id')

        # Adding field 'Foward.publication'
        db.add_column('publication_foward', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_foward', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Liked.Publication'
        db.delete_column('publication_liked', 'Publication_id')

        # Adding field 'Liked.publication'
        db.add_column('publication_liked', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_liked', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Rated.Publication'
        db.delete_column('publication_rated', 'Publication_id')

        # Adding field 'Rated.publication'
        db.add_column('publication_rated', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_rated', to=orm['publication.Publication']),
                      keep_default=False)

        # Adding field 'Publication.published'
        db.add_column('publication_publication', 'published',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'Watched.Publication'
        db.delete_column('publication_watched', 'Publication_id')

        # Adding field 'Watched.publication'
        db.add_column('publication_watched', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_watched', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'PublicationTag.Publication'
        db.delete_column('publication_publicationtag', 'Publication_id')

        # Adding field 'PublicationTag.publication'
        db.add_column('publication_publicationtag', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='tags', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Alert.Publication'
        db.delete_column('publication_alert', 'Publication_id')

        # Adding field 'Alert.publication'
        db.add_column('publication_alert', 'publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_alert', to=orm['publication.Publication']),
                      keep_default=False)

    def backwards(self, orm):
        # Adding model 'PublicationPermission'
        db.create_table('publication_publicationpermission', (
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('Publication', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_Publication', to=orm['publication.Publication'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_user', to=orm['auth.User'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('friend', self.gf('django.db.models.fields.related.ForeignKey')(related_name='permission_friend', to=orm['auth.User'])),
        ))
        db.send_create_signal('publication', ['PublicationPermission'])

        # Deleting model 'Moderator'
        db.delete_table('publication_moderator')


        # User chose to not deal with backwards NULL issues for 'Comment.Publication'
        raise RuntimeError("Cannot reverse this migration. 'Comment.Publication' and its values cannot be restored.")
        # Deleting field 'Comment.publication'
        db.delete_column('publication_comment', 'publication_id')

        # Adding field 'PublicationImage.Publication'
        db.add_column('publication_publicationimage', 'Publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_images', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'PublicationImage.publication'
        db.delete_column('publication_publicationimage', 'publication_id')

        # Adding field 'Foward.Publication'
        db.add_column('publication_foward', 'Publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_foward', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Foward.publication'
        db.delete_column('publication_foward', 'publication_id')

        # Adding field 'Liked.Publication'
        db.add_column('publication_liked', 'Publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_liked', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Liked.publication'
        db.delete_column('publication_liked', 'publication_id')

        # Adding field 'Rated.Publication'
        db.add_column('publication_rated', 'Publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_rated', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Rated.publication'
        db.delete_column('publication_rated', 'publication_id')

        # Deleting field 'Publication.published'
        db.delete_column('publication_publication', 'published')

        # Adding field 'Watched.Publication'
        db.add_column('publication_watched', 'Publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_watched', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Watched.publication'
        db.delete_column('publication_watched', 'publication_id')

        # Adding field 'PublicationTag.Publication'
        db.add_column('publication_publicationtag', 'Publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='tags', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'PublicationTag.publication'
        db.delete_column('publication_publicationtag', 'publication_id')

        # Adding field 'Alert.Publication'
        db.add_column('publication_alert', 'Publication',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, related_name='publication_alert', to=orm['publication.Publication']),
                      keep_default=False)

        # Deleting field 'Alert.publication'
        db.delete_column('publication_alert', 'publication_id')

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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_alert'", 'to': "orm['publication.Publication']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_alert'", 'to': "orm['auth.User']"})
        },
        'publication.comment': {
            'Meta': {'object_name': 'Comment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': "orm['publication.Publication']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'publication.foward': {
            'Meta': {'object_name': 'Foward'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_foward'", 'to': "orm['publication.Publication']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_foward'", 'to': "orm['auth.User']"})
        },
        'publication.liked': {
            'Meta': {'object_name': 'Liked'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_liked'", 'to': "orm['publication.Publication']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_liked'", 'to': "orm['auth.User']"})
        },
        'publication.moderator': {
            'Meta': {'object_name': 'Moderator'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'can_exclude': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'can_publish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moderator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moderator_user'", 'to': "orm['auth.User']"}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'moderator_owner'", 'to': "orm['auth.User']"}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_moderator'", 'to': "orm['publication.Publication']"})
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
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rated_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publications'", 'to': "orm['auth.User']"}),
            'watched_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'publication.publicationimage': {
            'Meta': {'object_name': 'PublicationImage'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_images'", 'to': "orm['publication.Publication']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['auth.User']"})
        },
        'publication.publicationtag': {
            'Meta': {'object_name': 'PublicationTag'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tags'", 'to': "orm['publication.Publication']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publication.Tag']"})
        },
        'publication.rated': {
            'Meta': {'object_name': 'Rated'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_rated'", 'to': "orm['publication.Publication']"}),
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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'publication_watched'", 'to': "orm['publication.Publication']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_watched'", 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['publication']