# Generated by Django 3.2.9 on 2021-12-10 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_alter_ocrmodel_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='ocrmodelcoord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left', models.IntegerField()),
                ('top', models.IntegerField()),
                ('word', models.CharField(max_length=100)),
                ('ocrmodel1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ocr.ocrmodel')),
            ],
        ),
    ]
