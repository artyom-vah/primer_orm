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

## 1. Создание объектов:
#### 1.1 создание пользователя
```bash
User.objects.create_user(username='Artyom', password='1234')
```
```bash
user2 = User.objects.create_user(username='Николай', password='1234')
```
#### 1.2 создание категорий
```bash
 Category.objects.create(title='программирование', slug='programming', description='Описание категории - программирование')
```
```bash
Category.objects.create(title='аналитика', slug='analytics', description='Описание категории - аналитика')
```
```bash
Category.objects.create(title='дизайн', slug='design', description='Описание категории - дизайн')
```
#### 1.3 создание поста
```bash
 author = User.objects.get(username='adm')
```
```bash
category = Category.objects.get(title='Программирование')
```
```bash
post1 = Post.objects.create(title='Python', text='Python - интерпретируемый язык программирования высокого уровня с динамической типизацией. Он обладает простым и понятным синтаксисом.', author=author, categories=category)
```
либо так:
```bash
post2 = Post.objects.create(title='C#',text ='C# язык программирования, разработанный компанией Microsoft. Он является объектно-ориентированным языком с широкими возможностямиюю .', author=User.objects.get(username='Артемий'), categories=Category.objects.get(title='Программирование'))
```

```bash

```
## 2. Изменение объектов:
#### 1.1 изменение пользователя
```bash
user1 = User.objects.get(pk=2)
```
```bash
user1.username= 'Артемий'
```
```bash
user1.first_name = 'Тема'
```
```bash
 user1.last_name = 'Пупкин'
```
```bash
user1.save()
```

#### 1.2 изменение категорий
```bash
 c1 = Category.objects.get(title='программирование')
```
```bash
 c1.title = 'Программирование'
```
```bash
 c1.description = 'Описание группы программирование'
```
```bash
 c1.save()
```


## 3. Выборка разных объектов:
```bash
Category.objects.all()
```
```bash 
# будет выведено
<QuerySet [<Category: Программирование>, <Category: Аналитика>, <Category: Дизайн>]>
```

Вывод постов определенного пользователя
```bash
author = User.objects.get(username='adm')
```
```bash
posts_adm = Post.objects.filter(author=author)
```
либо так:
```bash
 posts_adm = Post.objects.filter(author=User.objects.get(username='adm'))
```
```bash
# будет выведено (то что указано в модели в методе __str__)
<QuerySet [<Post: Kotlin>, <Post: Ruby>, <Post: Java>, <Post: Python>]>
```
```bash
посты_Николая = Post.objects.filter(author=User.objects.get(username='Николай'))
```
```bash
# будет выведено (то что указано в модели в методе __str__)
<QuerySet [<Post: Go>, <Post: JavaScript>, <Post: C++>]>
```
Вывод постов по определенной категории ( тут вывод постов по дизайну)
```bash
category_disign =  Category.objects.get(title='Дизайн')
```
```bash
category_disign =  Post.objects.filter(categories=category_disign)
```
либо так:
```bash
post_category_disign  = Post.objects.filter(categories=Category.objects.get(title='Дизайн'))
```

Вывод постов по определенному автору и по определенной категории  
```bash
artemiy = User.objects.get(username='Артемий')
```
```bash
programming = Category.objects.get(title='Программирование')
```
```bash
posts_artemiy_programming = Post.objects.filter(author=artemiy, categories=programming)
```
либо так: (в данном слуе делает 2 запроса к бд, сначала выбирает user Артемий, потом выбирается категория Программирование)
```bash
posts_artemiy_programming = Post.objects.filter(author=User.objects.get(username='Артемий'), categories=Category.objects.get(title='Программирование'))
```

```bash

```
 programming = Category.objects.get(title='Программирование')
**Автор проекта: Артем Вахрушев.**
