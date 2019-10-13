from django.contrib.auth.models import User as BaseUser
from django.db import models

MALE = 0
FEMALE = 1

GENDERS = (
    (MALE, 'Мужской'),
    (FEMALE, 'Женский'),
)

class Profile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, primary_key=True, blank=True,
                                related_name='user_profile', verbose_name='Пользователь')
    full_name = models.CharField('ФИО', max_length=500)
    email = models.EmailField('E-mail')
    phone = models.CharField('Телефон', max_length=100)
    age = models.PositiveIntegerField('Возраст')
    gender = models.IntegerField('Пол', choices=GENDERS)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    employment = models.ForeignKey('Employment', on_delete=models.CASCADE, verbose_name='Форма занятости')
    interests = models.ManyToManyField('Interest')

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'


class SocialProfile(models.Model):
    VK = 0
    OK = 1
    FB = 2

    SOCIAL_NETWORKS = (
        (VK, 'vkontakte'),
        (OK, 'odnoklassniki'),
        (FB, 'facebook'),
    )

    created_at = models.DateTimeField('Создано', auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Профиль')
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    social_id = models.BigIntegerField()
    first_name = models.CharField('Имя', max_length=200, blank=True)
    last_name = models.CharField('Фамилия', max_length=200, blank=True)
    avatar = models.CharField('Аватар', max_length=500, blank=True)
    token = models.CharField('Токен', max_length=800, blank=True)
    social_network = models.IntegerField('Социальная сеть', choices=SOCIAL_NETWORKS)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.social_id}: {self.full_name}'

    class Meta:
        verbose_name = 'Пользователь соц.сети'
        verbose_name_plural = 'Пользователи соц.сети'

class Project(models.Model):
    date_create = models.DateTimeField(auto_now_add=True)
    title = models.CharField('Заголовок', max_length=500)
    description = models.TextField('Текст')
    image = models.ImageField('Изображение', upload_to='project_images')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проект'


class Person(models.Model):
    avatar = models.ImageField('Аватар', upload_to='user_avatars', blank=True, null=True)
    full_name = models.CharField('ФИО', max_length=500)
    sort_order = models.PositiveIntegerField('Сортировка', default=0)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='persons')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Контактное лицо'
        verbose_name_plural = 'Контактное лицо'
        ordering = ['-sort_order']


class Attachment(models.Model):
    icon = models.ImageField('Иконка', upload_to='file_icons')
    file = models.FileField('Файл', upload_to='attachments')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='attachments')

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = 'Прикрепленный файл'
        verbose_name_plural = 'Прикрепленные файлы'

class City(models.Model):
    title = models.CharField('Название', max_length=500)
    sort_order = models.PositiveIntegerField('Сортировка', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['-sort_order']

class Interest(models.Model):
    title = models.CharField('Название', max_length=500)
    sort_order = models.PositiveIntegerField('Сортировка', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'
        ordering = ['-sort_order']


class Employment(models.Model):
    title = models.CharField('Название', max_length=500)
    sort_order = models.PositiveIntegerField('Сортировка', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Форма занятости'
        verbose_name_plural = 'Форма занятости'
        ordering = ['-sort_order']


class News(models.Model):
    title = models.CharField('Название', max_length=500)
    description = models.TextField('Текст')
    image = models.ImageField('Изображение', upload_to='news_images')
    is_interesting = models.BooleanField('Интересное')
    sort_order = models.PositiveIntegerField('Сортировка', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Интересы'
        ordering = ['-sort_order']
