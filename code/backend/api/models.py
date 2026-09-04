from django.db import models
from django.utils import timezone

class MediaCategory(models.Model): 
    name = models.CharField(
        verbose_name="Категория статьи",
        max_length=128
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Категория статьи"
        verbose_name_plural="Категории статей"

class MediaItem(models.Model): 
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        # auto_now_add=True
    )
    title = models.CharField(
        verbose_name="Заголовок",
        max_length=255
    )
    text = models.TextField(
        verbose_name="Основной текст"
    )
    photo = models.FileField(
        verbose_name="Файл изображения",
        upload_to='media_items/', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        MediaCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория"
    )
    
    @property
    def status(self):
        today = timezone.localdate()  # если DateField
        # today = timezone.now().date()  # тоже можно, но localdate предпочтительнее в большинстве случаев

        if self.created_at.date() < today:
            return 'Прошло'
        elif self.created_at.date() == today:
            return 'Идёт'
        else:
            return 'Будет'
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class BiographyItem(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]

    name = models.CharField(
        verbose_name="Имя",
        max_length=100
    )
    surname = models.CharField(
        verbose_name="Фамилия",
        max_length=100
    )
    partro = models.CharField(
        verbose_name="Отчество",
        max_length=100,
        blank=True,
        null=True
    )
    birth = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True
    )
    death = models.DateField(
        verbose_name="Дата смерти",
        blank=True,
        null=True
    )
    gender = models.CharField(
        verbose_name="Пол",
        max_length=1,
        choices=GENDER_CHOICES
    )
    photo = models.ImageField(
        verbose_name="Фотография",
        upload_to='biographies/photos/',
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )

    childrens = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='parents',
        blank=True,
        verbose_name="Дети"
    )

    class Meta:
        verbose_name = "Биография"
        verbose_name_plural = "Биографии"
        ordering = ['surname', 'name']

    def __str__(self):
        return f"{self.surname} {self.name} {self.partro or ''}".strip()



class ArtCategory(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=128
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Категория произведения"
        verbose_name_plural="Категории произведения"


class ArtSeries(models.Model):
    name = models.CharField(
        verbose_name="Название",
        max_length=128
    )
    
    class Meta:
        verbose_name="Серия картины"
        verbose_name_plural="Серии картин"

    def __str__(self):
        return self.name


class ArtItem(models.Model):
    title = models.CharField(
        verbose_name="Название произведения",
        max_length=255
    )
    year = models.IntegerField(
        verbose_name="Год создания",
        blank=True,
        null=True
    )
    photo = models.ImageField(
        verbose_name="Изображение",
        upload_to='art_items/',
        blank=True,
        null=True
    )
    desc = models.TextField(
        verbose_name="Полное описание",
        blank=True,
        null=True
    )
    start_writing_year = models.IntegerField(
        verbose_name="Начало написания",
        blank=True,
        null=True
    )
    end_writing_year = models.IntegerField(
        verbose_name="Окончание написания",
        blank=True,
        null=True
    )
    width = models.DecimalField(
        verbose_name="Ширина (см)",
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )
    height = models.DecimalField(
        verbose_name="Высота (см)",
        max_digits=6,
        decimal_places=2,
        blank=True,
        null=True
    )

    category = models.ForeignKey(
        ArtCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Категория"
    )
    series = models.ForeignKey(
        ArtSeries,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Серия"
    )

    class Meta:
        verbose_name = "Художественное произведение"
        verbose_name_plural = "Художественные произведения"
        ordering = ['title']

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(
        verbose_name="Название книги",
        max_length=255
    )
    author = models.CharField(
        verbose_name="Автор",
        max_length=255
    )
    year = models.IntegerField(
        verbose_name="Год издания",
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    photo = models.ImageField(
        verbose_name="Обложка",
        upload_to='books/covers/',
        blank=True,
        null=True
    )
    away_link = models.URLField(
        verbose_name="Ссылка на внешний ресурс",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ['title']

    def __str__(self):
        return f"{self.title} — {self.author}"

    
    