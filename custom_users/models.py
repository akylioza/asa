from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ADMIN = 1
VipClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VipClient, 'VipClient'),
    (CLIENT, 'CLIENT')
)

MALE = 1
FEMALE = 2

GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)
# married; divorced, separated, or widowed; and never married
MARRIED = 1
DIVORCED = 2
WIDOWED = 3
Never_Married = 4

MARITAL = (
    (MARRIED, 'MARRIED'),
    (DIVORCED, 'DIVORCED'),
    (WIDOWED, 'WIDOWED'),
    (Never_Married, 'Never Married')
)

ELF = 1
HUMAN = 2
ORC = 3
TROLL = 4
GNOLL = 5
UNICORN = 6

RACES = (
    (ELF, 'ELF'),
    (HUMAN, 'HUMAN'),
    (ORC, 'ORC'),
    (TROLL, 'TROLL'),
    (GNOLL, 'GNOLL'),
    (UNICORN, 'UNICORN')
)


class Custom_User(User):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя')
    phone_number = models.CharField('Номер телефона', max_length=100)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER, verbose_name='Пол')
    marital_status = models.IntegerField(choices=MARITAL, verbose_name='семейное положение')
    salary = models.PositiveIntegerField()
    race = models.IntegerField(choices=RACES, verbose_name='раса')
