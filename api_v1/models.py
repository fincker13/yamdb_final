from django.db import models
from django.contrib.auth import get_user_model
from .validators import date_validator
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Genres(models.Model):
    name = models.CharField(verbose_name='Название жанра', max_length=200)
    slug = models.SlugField(verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(verbose_name='Имя категории', max_length=200)
    slug = models.SlugField(verbose_name='Слаг', unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название произведения',
        max_length=300
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год выхода произведения',
        null=True,
        blank=True,
        validators=[date_validator]
    )

    description = models.CharField(
        verbose_name='Описание',
        max_length=1000,
        blank=True
    )

    category = models.ForeignKey(
        Categories,
        verbose_name='Категория произведения',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(Genres, verbose_name='Жанр произведения')

    def __str__(self):
        return self.name


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        verbose_name='ID произведения',
        on_delete=models.CASCADE,
        related_name='review'
    )
    text = models.TextField(verbose_name='Текст отзыва', max_length=1000)
    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        on_delete=models.CASCADE,
        related_name='review'
    )
    score = models.IntegerField(
        default=None,
        verbose_name='Рейтинг от 1 до 10',
        validators=[MaxValueValidator(10),
                    MinValueValidator(1)])
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True
    )

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    author = models.ForeignKey(
        User, verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(verbose_name='Дата добавления',
                                    auto_now_add=True,
                                    db_index=True
                                    )

    class Meta:
        ordering = ['-pub_date']
