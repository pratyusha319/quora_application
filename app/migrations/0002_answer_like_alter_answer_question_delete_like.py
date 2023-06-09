# Generated by Django 4.1.7 on 2023-05-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='like',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='app.question'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
