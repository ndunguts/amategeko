# Generated by Django 5.1.2 on 2024-10-30 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mys', '0011_rename_idq_answer_concluson_rename_true_a_answer_noq_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='F',
        ),
    ]