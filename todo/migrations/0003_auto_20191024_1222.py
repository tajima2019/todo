# Generated by Django 2.2 on 2019-10-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='done',
            field=models.BooleanField(choices=[('done', 'DONE'), ('not done', 'NOT DONE')], default=True),
        ),
    ]
