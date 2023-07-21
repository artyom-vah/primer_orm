[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)



## Описание:
Для тренеровки написания запросов на Django ORM. Запросы буду написаны внизу этого файла



### **Стек:**
![python version](https://img.shields.io/badge/Python-3.11-brightgreen)   ![django version](https://img.shields.io/badge/Django-4.2.3-brightgreen)


### **Дополнительные библиотеки:**
[![django-extensions](https://img.shields.io/badge/django--extensions-3.2.3-blue)](https://pypi.org/project/django-extensions/3.2.3/)
[![ipython](https://img.shields.io/badge/ipython-8.14.0-blue)](https://pypi.org/project/ipython/8.14.0/)




### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
#### Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```bash
git clone https://github.com/artyom-vah/primer_orm.git
```

2. Установите и активируйте виртуальное окружение
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
или сразу так:
```bash
python -m venv venv && . venv/Scripts/activate
```
3. Обновите pip 
```bash
python -m pip install --upgrade pip
```
4. Установите зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
5. В папке с файлом manage.py создайте и выполните миграции:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
6. Создайте суперюзера 'укажите имя пользователя, адрес электронной почты (необязательно), и Password'
```bash
python manage.py createsuperuser
```

## Запросы на Django ORM (немного теории)

<details>
<summary>
<strong> 
Теория и примеры
</strong>
</summary>

### 1. Создание объектов:
#### 1.1 создание пользователя
```python
User.objects.create_user(username='Artyom', password='1234')
```

```python
user2 = User.objects.create_user(username='Николай', password='1234')
```
#### 1.2 создание категорий
```python
 Category.objects.create(title='программирование', slug='programming', description='Описание категории - программирование')
```

```python
Category.objects.create(title='аналитика', slug='analytics', description='Описание категории - аналитика')
```

```python
Category.objects.create(title='дизайн', slug='design', description='Описание категории - дизайн')
```

#### 1.3 создание поста

```python
 author = User.objects.get(username='adm')
```

```python
category = Category.objects.get(title='Программирование')
```

```python
post1 = Post.objects.create(title='Python', text='Python - интерпретируемый язык программирования высокого уровня с динамической типизацией. Он обладает простым и понятным синтаксисом.', author=author, categories=category)
```

* _либо так:_
```python
post2 = Post.objects.create(title='C#',text ='C# язык программирования, разработанный компанией Microsoft. Он является объектно-ориентированным языком с широкими возможностямиюю .', author=User.objects.get(username='Артемий'), categories=Category.objects.get(title='Программирование'))
```

## 2. Изменение объектов:
#### 2.1 изменение пользователя
```python
user1 = User.objects.get(pk=2)
```

```python
user1.username= 'Артемий'
```

```python
user1.first_name = 'Тема'
```

```python
user1.last_name = 'Пупкин'
```

```python
user1.save()
```

#### 1.2 изменение категорий
```python
c1 = Category.objects.get(title='программирование')
```

```python
c1.title = 'Программирование'
```

```python
c1.description = 'Описание группы программирование'
```

```python
c1.save()
```

## 3. Выборка разных объектов:
```python
Category.objects.all()
```

```python 
# будет выведено
<QuerySet [<Category: Программирование>, <Category: Аналитика>, <Category: Дизайн>]>
```

* _Вывод постов определенного пользователя_
```python
author = User.objects.get(username='adm')
```

```python
posts_adm = Post.objects.filter(author=author)
```

* _либо так:_
```python
 posts_adm = Post.objects.filter(author=User.objects.get(username='adm'))
```

```python
# будет выведено (то что указано в модели в методе __str__)
<QuerySet [<Post: Kotlin>, <Post: Ruby>, <Post: Java>, <Post: Python>]>
```

```python
посты_Николая = Post.objects.filter(author=User.objects.get(username='Николай'))
```

```python
# будет выведено (то что указано в модели в методе __str__)
<QuerySet [<Post: Go>, <Post: JavaScript>, <Post: C++>]>
```

* _Вывод постов по определенной категории ( тут вывод постов по дизайну)_
```python
category_disign =  Category.objects.get(title='Дизайн')
```

```python
category_disign =  Post.objects.filter(categories=category_disign)
```

* _либо так:_
```python
post_category_disign  = Post.objects.filter(categories=Category.objects.get(title='Дизайн'))
```

* _Вывод постов по определенному автору и по определенной категории_
```python
artemiy = User.objects.get(username='Артемий')
```

```python
programming = Category.objects.get(title='Программирование')
```

```python
posts_artemiy_programming = Post.objects.filter(author=artemiy, categories=programming)
```

* _либо так: (в данном слуе делает 2 запроса к бд, сначала выбирает user Артемий, потом выбирается категория Программирование)_
```python
posts_artemiy_programming = Post.objects.filter(author=User.objects.get(username='Артемий'), categories=Category.objects.get(title='Программирование'))
```

* _Выполнение запроса с использованием select_related предыдущего примера_ 
```python
artemiy = User.objects.get(username='Артемий')
```

```python
programming = Category.objects.get(title='Программирование')
```

```python
posts_artemiy_programming = Post.objects.select_related('author', 'categories').filter(author=artemiy, categories=programming)
```

```python
# будет такой результат
 [<Post: Стратегии тестирования>, <Post: Тестирование пользовательского интерфейса>, <Post: Автоматизация тестирования'>, <Post: Виды тестирования>, <Post: Введение в тестирование>, <Post: Принятие данных на основе аналитики>, <Post: Машинное обучение в аналитике>, <Post: Визуализация данных>, <Post: А
нализ данных и статистика>, <Post: Методы сбора данных для аналитики>, <Post: Введение в аналитику данных>, <Post: Тенденции в дизайне>, <Post: Эффективные пользовательские интерфейсы>, <Post: Типографика в дизайне>, <Post: Цветовая палитра в дизайне>, <Post: Основные принципы дизайна>, <Post: Тестирование>, <P
ost: Kotlin>, <Post: Go>, <Post: SQL>, '...(remaining elements truncated)
```

```python
for post in posts_artemiy_programming:
    print('Заголовок:', post.title)
    print('Текст:', post.text)
    print('Автор:', post.author.username)
    print('Категория:', post.categories.title)
    print('----------------------')
```

```python
# выводим все посты с авторами и категориями
posts = Post.objects.select_related('author', 'categories').all()
```

```python
# будет такой результат
<QuerySet [<Post: Стратегии тестирования>, <Post: Тестирование пользовательского интерфейса>, <Post: Автоматизация тестирования'>, <Post: Виды тестирования>, <Post: Введение в тестирование>, <Post: Принятие данных на основе аналитики>, <Post: Машинное обучение в аналитике>, <Post: Визуализация данных>, <Post: А
нализ данных и статистика>, <Post: Методы сбора данных для аналитики>, <Post: Введение в аналитику данных>, <Post: Тенденции в дизайне>, <Post: Эффективные пользовательские интерфейсы>, <Post: Типографика в дизайне>, <Post: Цветовая палитра в дизайне>, <Post: Основные принципы дизайна>, <Post: Тестирование>, <P
ost: Kotlin>, <Post: Go>, <Post: SQL>, '...(remaining elements truncated)...']>
```

```python
for post in posts:
    print('Заголовок:', post.title)
    print('Текст:', post.text)
    print('Автор:', post.author.username)
    print('Категория:', post.categories.title)
    print('----------------------')
```

* _Вывести автора который написал поста о "Python"_
```python
Post.objects.get(title="Python").author
```

</details>



## Задания:
[//]: # (--------------------------------------------------------------)
[//]: # (1. Создание любой объект моделей User, Category, Post.)
<details>
<summary>
<strong>
1. Создание(удаление) любого объекта моделей User, Category, Post.
</strong>
</summary>

```python
User.objects.create_user(username='Artyom', password='1234')
```
```python
Category.objects.create(title='программирование', slug='programming', description='Описание категории - программирование')
```

```python
Post.objects.create(title='Python', text='Python - интерпретируемый язык программирования высокого уровня с динамической типизацией. Он обладает простым и понятным синтаксисом.', author=author, categories=category)
```
* _удаление объектов:_
```python
User.objects.create_user(username="test", password="test")
```
```python
del_test_user = User.objects.get(pk=5).delete()
```
```python
User.objects.get(username="test").delete()
```
</details>

[//]: # (--------------------------------------------------------------)
[//]: # (2. Вывести все объекты моделей User, Category, Post и их  количество.)
<details>
<summary>
<strong> 
2. Вывести все объекты моделей User, Category, Post (и их количество).
</strong>
</summary>

```python
Post.objects.all()
```

```python
Category.objects.all()
```

```python
Category.objects.all().count()
```

```python
Post.objects.all().count()
```
</details>

[//]: # (--------------------------------------------------------------)
[//]: # (3. Вывести все посты определенного пользователя и их количество.)
<details>
<summary>
<strong> 
3. Вывести все посты определенного пользователя (и их количество).
</strong>
</summary>

```python
Post.objects.filter(author__username="adm")
```

```python
Post.objects.filter(author__username="adm").count()
```

* _также посты пользователя можно вызвать при помощи обратной модели related_name:_

```python
# вот моя модель:
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название поста')
    text = models.TextField(verbose_name='Текст поста')
    pub_date = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', verbose_name='Автор')
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='posts', blank=True, null=True, verbose_name='Категория')
```

```python
adm = User.objects.get(username='adm')
```

```python
posts_adm = adm.posts.all()
```

* _в случае если related_name не указан то можно использовать название самаой модели (+set) - post_set_
```python
adm = User.objects.get(pk=1)
```
```python
posts_adm = adm.post_set.all()
```

</details>

[//]: # (--------------------------------------------------------------)
[//]: # (4. Вывести все посты определенного пользователя и их количество.)
<details>
<summary>
<strong> 
4. Вывести все посты определенной категории (и их количество).
</strong>
</summary>

```python
Post.objects.filter(categories__title="Программирование")
```

```python
Post.objects.filter(categories__title="Программирование").count()
```
* _через related_name_
```python
programming = Category.objects.get(title='Программирование')
```
```python
programming.posts.all()
```
* _также считаем количество через related_name_
```python
programming.posts.all().count()
```

</details>

[//]: # (--------------------------------------------------------------)
[//]: # (5. Вывести все посты определенного пользователя и определенной категории.)
<details>
<summary>
<strong> 
5.Вывести все посты определенного пользователя и определенной категории.
</strong>
</summary>

```python
Post.objects.filter(author__username="adm", categories__title="Программирование")
```
* _либо так:_
```python
user = User.objects.get(username="adm")
```

```python
category = Category.objects.get(title='Программирование')
```

```python
Post.objects.filter(author=user, categories=category)
```
* _либо так:_
```python
Post.objects.filter(Q(author=user) & Q(categories=category)) 
```
</details>

[//]: # (--------------------------------------------------------------)
[//]: # (6. Вывести все посты пользователей adm, Николай, исключая категорию Аналитика, Дизайн.)
<details>
<summary>
<strong> 
6. Вывести все посты исключая категорию Аналитика, Дизайн, а также все посты исключая пользователей adm, Николай.
</strong>
</summary>

* _выводим все кроме аналитики или дизайна_
```python
Post.objects.all().exclude(categories__title = 'Аналитика')
```

```python
Post.objects.all().exclude(categories__title = 'Дизайн')
```
* _выводим все кроме аналитики и дизайна_

```python
programming = Category.objects.get(title='Программирование')
```
```python
testing = Category.objects.get(title='Тестирование')
```
```python
Post.objects.exclude(categories__in=[programming, testing])
```

* _выводим все посты кроме постов пользователя adm_
```python
Post.objects.all().exclude(author__username="adm")
```
* _выводим все посты кроме постов пользователя adm категории дизайн_
```python
Post.objects.all().exclude(author__username="adm", categories__title="Дизайн")
```
</details>


[//]: # (--------------------------------------------------------------)
[//]: # (7. Вывести все id постов и их сумму.)
<details>
<summary>
<strong> 
7. Вывести все id постов и их сумму
</strong>
</summary>

```python
post_ids = Post.objects.values_list('id', flat=True).count()
```
```python
total_sum = sum(post_ids)
```
```python
sum(Post.objects.values_list('id', flat=True))
```

</details>

[//]: # (--------------------------------------------------------------)
[//]: # (8. Написать несколько запросов с использованием select_related и prefetch_related.)
<details>
<summary>
<strong> 
8. Написать несколько запросов с использованием select_related и prefetch_related.
</strong>
</summary>

```python
Post.objects.select_related('author','categories').all()
```
```python
# вот пример select_related, таблицы: post, auth_user, category в одном запросе: 
 SELECT "app_primer_post"."id",
       "app_primer_post"."title",
       "app_primer_post"."text",
       "app_primer_post"."pub_date",
       "app_primer_post"."author_id",
       "app_primer_post"."categories_id",
       "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined",
       "app_primer_category"."id",
       "app_primer_category"."title",
       "app_primer_category"."slug",
       "app_primer_category"."description"
  FROM "app_primer_post"
 INNER JOIN "auth_user"
    ON ("app_primer_post"."author_id" = "auth_user"."id")
  LEFT OUTER JOIN "app_primer_category"
    ON ("app_primer_post"."categories_id" = "app_primer_category"."id")
 ORDER BY "app_primer_post"."pub_date" ASC
 LIMIT 21
```
```python
Post.objects.prefetch_related('author','categories').all()
```
```python
# вот пример prefetch_related, таблицы: post, auth_user, category в 3х запросах: 
SELECT "app_primer_post"."id",
       "app_primer_post"."title",
       "app_primer_post"."text",
       "app_primer_post"."pub_date",
       "app_primer_post"."author_id",
       "app_primer_post"."categories_id"
  FROM "app_primer_post"
 ORDER BY "app_primer_post"."pub_date" ASC
 LIMIT 21

Execution time: 0.000000s [Database: default]
SELECT "auth_user"."id",
       "auth_user"."password",
       "auth_user"."last_login",
       "auth_user"."is_superuser",
       "auth_user"."username",
       "auth_user"."first_name",
       "auth_user"."last_name",
       "auth_user"."email",
       "auth_user"."is_staff",
       "auth_user"."is_active",
       "auth_user"."date_joined"
  FROM "auth_user"
 WHERE "auth_user"."id" IN (1, 2, 3)

Execution time: 0.000000s [Database: default]
SELECT "app_primer_category"."id",
       "app_primer_category"."title",
       "app_primer_category"."slug",
       "app_primer_category"."description"
  FROM "app_primer_category"
 WHERE "app_primer_category"."id" IN (1, 2, 3, 4)
```
</details>


[//]: # (--------------------------------------------------------------)
[//]: # (9. Вывести посты в которых содержатся слова "других", "проце", "испол", "автом".)
<details>
<summary>
<strong> 
9. Вывести посты в которых содержатся слова "других", "проце", "испол", "автом"
</strong>
</summary>

```python
Post.objects.filter(text__contains="других")
```
</details>


[//]: # (--------------------------------------------------------------)
[//]: # (10. Вывести посты у которых значение id больше 5 и меньше 10.)
<details>
<summary>
<strong> 
10. Вывести посты у которых значение id больше 5 и меньше 10
</strong>
</summary>
```python
Post.objects.filter(pk__gt=5, pk__lt=10).count()
```
```python
Post.objects.filter(pk__gt=5).filter(pk__lt=10)
```
```python
from django.db.models import Q
```
```python
Post.objects.filter(Q(pk__gt=5) & Q(pk__lt=10))
```

</details>


[//]: # (--------------------------------------------------------------)
[//]: # (11. Вывести посты у которых значение id больше 5 и меньше 10.)
<details>
<summary>
<strong> 
11. Вывести посты у которых значение id больше 5 и меньше 10
</strong>
</summary>

```python
Post.objects.filter(pk__gt=5).filter(pk__lt=10)
```


</details>

```python

```

**Автор проекта: Артем Вахрушев.**
   