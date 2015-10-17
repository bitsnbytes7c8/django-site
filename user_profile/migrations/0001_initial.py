# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullName', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(b'^[0-9]*$', b'Only 0-9 allowed', b'Invalid Number')])),
                ('website', models.URLField(verbose_name=b'Website', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
