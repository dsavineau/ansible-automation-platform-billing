# Generated by Django 3.2.9 on 2022-02-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobHostSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField()),
                ('job_id', models.PositiveIntegerField()),
                ('host_id', models.PositiveIntegerField()),
                ('host_name', models.CharField(max_length=1024)),
                ('changed', models.PositiveIntegerField(default=0, editable=False)),
                ('dark', models.PositiveIntegerField(default=0, editable=False)),
                ('failures', models.PositiveIntegerField(default=0, editable=False)),
                ('ignored', models.PositiveIntegerField(default=0, editable=False)),
                ('ok', models.PositiveIntegerField(default=0, editable=False)),
                ('processed', models.PositiveIntegerField(default=0, editable=False)),
                ('rescued', models.PositiveIntegerField(default=0, editable=False)),
                ('skipped', models.PositiveIntegerField(default=0, editable=False)),
                ('failed', models.BooleanField(db_index=True, default=False, editable=False)),
            ],
            options={
                'verbose_name_plural': 'job host summaries',
                'ordering': ('-pk',),
                'managed': False,
            },
        ),
    ]
