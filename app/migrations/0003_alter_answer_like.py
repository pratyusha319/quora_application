# Generated by Django 4.1.7 on 2023-05-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_answer_like_alter_answer_question_delete_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='like',
            field=models.CharField(max_length=100, null=True),
        ),
    ]