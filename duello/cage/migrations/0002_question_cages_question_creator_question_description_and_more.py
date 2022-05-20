# Generated by Django 4.0.3 on 2022-05-19 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_users_role_id'),
        ('cage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='cages',
            field=models.ManyToManyField(to='cage.cage'),
        ),
        migrations.AddField(
            model_name='question',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='custom_auth.users'),
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='Unamed', max_length=30),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(default='', max_length=500)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cage.question')),
            ],
        ),
    ]
