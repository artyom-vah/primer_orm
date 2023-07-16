from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.title}'


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название поста')
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='related_author', verbose_name='Автор')
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='related_categories', blank=True, null=True, verbose_name='Категория')


    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f"{self.title} {self.text}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Комментарий поста')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Автор комментария')
    text = models.TextField(verbose_name='Текст комментария')

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return self.text


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower', verbose_name='Подписчик')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', verbose_name='Подписка на этого автора')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique follow'
            ),
        ]
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    def __str__(self):
        return f"Подписчик: {self.user}, Автор : {self.author}"
