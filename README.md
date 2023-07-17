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

## Запросы на Django ORM

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

### 4. Задания:
[//]: # (--------------------------------------------------------------)
[//]: # (4.1 Создание любой объект моделей User, Category, Post.)
<details>
<summary>
<strong>
4.1 Создание(удаление) любого объекта моделей User, Category, Post.
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
[//]: # (4.2 Вывести все объекты моделей User, Category, Post.)
<details>
<summary>
<strong> 
4.2 Вывести все объекты моделей User, Category, Post.
</strong>
</summary>

```python
Post.objects.all()
```

```python
Category.objects.all()
```
</details>

[//]: # (--------------------------------------------------------------)
[//]: # (4.3 Вывести количество всех Пользователей, Постов, Категорий.)
<details>
<summary>
<strong> 
4.3 Вывести количество всех Пользователей, Постов, Категорий.
</strong>
</summary>

```python
Category.objects.count()
```

```python
Post.objects.count()
```
</details>

[//]: # (--------------------------------------------------------------)
[//]: # (4.4 Вывести все посты определенного пользователя и их количество.)
<details>
<summary>
<strong> 
4.4 Вывести все посты определенного пользователя и их количество.
</strong>
</summary>

```python
Post.objects.filter(author__username="adm")
```

```python
Post.objects.filter(author__username="adm").count()
```
</details>

[//]: # (--------------------------------------------------------------)
[//]: # (4.5 Вывести все посты определенного пользователя и их количество.)
<details>
<summary>
<strong> 
4.5 Вывести все посты определенной категории и их количество.
</strong>
</summary>

```python
Post.objects.filter(categories__title="Программирование")
```

```python
Post.objects.filter(categories__title="Программирование").count()
```
</details>

[//]: # (--------------------------------------------------------------)
[//]: # (4.6 Вывести все посты определенного пользователя и определенной категории.)
<details>
<summary>
<strong> 
4.6 Вывести все посты определенного пользователя и определенной категории.
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

```bash

```


**Автор проекта: Артем Вахрушев.**
   