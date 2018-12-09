# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-08 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import dynamic_validator.field_validation.validator


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fixed_price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=(dynamic_validator.field_validation.validator.ModelFieldRequiredMixin, models.Model),
        ),
    ]
