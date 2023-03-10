# Generated by Django 4.1.4 on 2023-01-06 08:25

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.IntegerField(choices=[(1, 'ADMIN'), (2, 'VipClient'), (3, 'CLIENT')], verbose_name='Тип пользователя')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE')], verbose_name='Пол')),
                ('marital_status', models.IntegerField(choices=[(1, 'MARRIED'), (2, 'DIVORCED'), (3, 'WIDOWED'), (4, 'Never Married')], verbose_name='семейное положение')),
                ('salary', models.PositiveIntegerField()),
                ('race', models.IntegerField(choices=[(1, 'ELF'), (2, 'HUMAN'), (3, 'ORC'), (4, 'TROLL'), (5, 'GNOLL'), (6, 'UNICORN')], verbose_name='раса')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
