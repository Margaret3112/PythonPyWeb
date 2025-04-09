import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    obj = Entry.objects.filter(author__name__contains='author')
    print(obj)
    """<QuerySet [<Entry: Оазисы Сахары: красота и опасность>, 
    <Entry: Новые гаджеты и устройства: обзор рынка>]>"""

    obj = Entry.objects.filter(author__authorprofile__city=None)
    print(obj)
    """<QuerySet [<Entry: Знакомство с Парижем>, 
    <Entry: Инновации в области виртуальной реальности>]>"""

    print(Entry.objects.get(id__exact=4))
    print(Entry.objects.get(id=4))  # Аналогично exact
    print(Blog.objects.get(name__iexact="Путешествия по миру"))

    print(Entry.objects.filter(headline__contains='мод'))
    # <QuerySet [
    # <Entry: Тенденции моды на текущий сезон>,
    # <Entry: История моды: от ретро до современности>,
    # <Entry: Интервью с известными модельерами и дизайнерами>
    # ]>

    print(Entry.objects.filter(id__in=[1, 3, 4]))
    # <QuerySet [<Entry: Изучение красот Мачу-Пикчу>, <Entry: Знакомство с Парижем>, <Entry: Открывая тайны Колизея>]>

    print(Entry.objects.filter(number_of_comments__in='123'))  # число комментариев 1 или 2 или 3
    """
    <QuerySet [
    <Entry: Изучение красот Мачу-Пикчу>, 
    <Entry: Открывая тайны Колизея>, 
    <Entry: Экзотические специи и их использование>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: История моды: от ретро до современности>
    ]>
    """

    # Вывести все записи, у которых число комментарием больше 10
    print(Entry.objects.filter(number_of_comments__gt=10))
    """
    <QuerySet [
    <Entry: Приключения в Амазонке>, 
    <Entry: Новые гаджеты и устройства: обзор рынка>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>, 
    <Entry: Инновации в области виртуальной реальности>
    ]>
    """
    # Вывести все записи, которые опубликованы (поле pub_date) позже и равное 01.06.2023
    import datetime

    print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    """
    <QuerySet [
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Десерты для настоящих сладкоежек>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: Как правильно заниматься йогой>, 
    <Entry: Последние тренды в мире искусственного интеллекта>, 
    <Entry: Как создать стильный образ на каждый день>, 
    <Entry: История моды: от ретро до современности>
    ]>
    """
    # Вывести все записи, у которых число комментарием больше 10 и рейтинг < 4
    print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    """
    <QuerySet [
    <Entry: Новые гаджеты и устройства: обзор рынка>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>
    ]>
    """
    # Вывести все записи, у которых заголовок статьи лексиграфически <= "Зя"
    print(Entry.objects.filter(headline__lte="Зя"))
    """
    <QuerySet [
    <Entry: Знакомство с Парижем>, 
    <Entry: Десерты для настоящих сладкоежек>, 
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Здоровое питание: полезные рецепты>
    ]>
    """

    print(Entry.objects.filter(headline__startswith='Как'))
    # <QuerySet [<Entry: Как правильно заниматься йогой>, <Entry: Как создать стильный образ на каждый день>]>
    print(Entry.objects.filter(headline__endswith='ния'))
    # <QuerySet [<Entry: Топ-10 фитнес-тренеров для вдохновения>, <Entry: Секреты успешного похудения>]>

    # Вывести записи между 01.01.2023 и 31.12.2023
    import datetime

    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    print(Entry.objects.filter(pub_date__range=(start_date, end_date)))
    """
    <QuerySet [
    <Entry: Оазисы Сахары: красота и опасность>, 
    <Entry: Рецепты блюд из итальянской кухни>, 
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Десерты для настоящих сладкоежек>, 
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Здоровое питание: полезные рецепты>, 
    <Entry: Секреты успешного похудения>, 
    <Entry: История моды: от ретро до современности>, 
    <Entry: Уход за кожей и волосами: лучшие советы>, 
    <Entry: Интервью с известными модельерами и дизайнерами>
    ]>
    """
    # При данной постановке задачи (вывод за конкретный год) будет проще воспользоваться __year результат будет аналогичен
    print(Entry.objects.filter(pub_date__year=2023))

    # Вывести записи старше 2022 года
    print(Entry.objects.filter(pub_date__year__lt=2022))
    """
    <QuerySet [
    <Entry: Новые гаджеты и устройства: обзор рынка>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>, 
    <Entry: Инновации в области виртуальной реальности>
    ]>
    """
    # Вывести все записи за февраль доступных годов, отобразить название, дату публикации, заголовок
    print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
    """
    <QuerySet [
    {'blog__name': 'ИТ-новости и технологии', 'pub_date': datetime.date(2022, 2, 1), 'headline': 'Развитие интернета вещей: будущее или реальность?'}, 
    {'blog__name': 'Мода и стиль', 'pub_date': datetime.date(2023, 2, 1), 'headline': 'Уход за кожей и волосами: лучшие советы'}, 
    {'blog__name': 'Мода и стиль', 'pub_date': datetime.date(2023, 2, 1), 'headline': 'Интервью с известными модельерами и дизайнерами'}
    ]>
    """
    # Вывести username авторов у которых есть публикации с 1 по 15 апреля 2023 года, вывести без использования range. Пример для работы с __day
    print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(
        pub_date__day__lte=15).values_list("author__name").distinct())
    # Сначала отфильтровываем по году, затем по дням, затем получаем значения имен у авторов и говорим, чтобы не было повторов
    """
    <QuerySet [
    ('andrey_author',), 
    ('dmitriy_creative',), 
    ('alexander89',), 
    ('irina_blogger',), 
    ('ivan_wordsmith',), 
    ('maxim_writer',)
    ]>
    """
    # Вывести статьи опубликованные в понедельник (так как datetime работает по американской системе,
    # то начало недели идёт с воскресенья, а заканчивается субботой, поэтому понедельник второй день в неделе)
    print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))
    """
    <QuerySet [
    {'blog__name': 'Путешествия по миру', 'pub_date': datetime.date(2022, 8, 1), 'headline': 'Приключения в Амазонке'}, 
    {'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2023, 5, 1), 'headline': 'Здоровое питание: полезные рецепты'}, 
    {'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2024, 1, 1), 'headline': 'Топ-10 фитнес-тренеров для вдохновения'}, 
    {'blog__name': 'Фитнес и здоровый образ жизни', 'pub_date': datetime.date(2024, 4, 1), 'headline': 'Как правильно заниматься йогой'}, 
    {'blog__name': 'ИТ-новости и технологии', 'pub_date': datetime.date(2024, 4, 1), 'headline': 'Последние тренды в мире искусственного интеллекта'}
    ]>
    """

    import datetime

    # Вывод всех записей по конкретной дате
    print(Entry.objects.filter(pub_date__date=datetime.date(2021, 6, 1)))
    # <QuerySet [<Entry: Новые гаджеты и устройства: обзор рынка>]>

    # Вывод всех записей новее конкретной даты
    print(Entry.objects.filter(pub_date__date__gt=datetime.date(2024, 1, 1)))
    """
    <QuerySet [
    <Entry: Как правильно заниматься йогой>, 
    <Entry: Последние тренды в мире искусственного интеллекта>, 
    <Entry: Как создать стильный образ на каждый день>
    ]>
    """

    # Вывод записей по конкретному времени
    print(Entry.objects.filter(pub_date__time=datetime.time(12, 00)))
    """
    <QuerySet [
    <Entry: Как создать стильный образ на каждый день>, 
    <Entry: История моды: от ретро до современности>, 
    <Entry: Уход за кожей и волосами: лучшие советы>, <Entry: Интервью с известными модельерами и дизайнерами>
    ]>
    """

    # Вывод записей по временному диапазону с 6 утра до 17 вечера
    print(Entry.objects.filter(pub_date__time__range=(datetime.time(6), datetime.time(17))))
    """
    <QuerySet [
    <Entry: Как правильно заниматься йогой>, 
    <Entry: Секреты успешного похудения>, 
    <Entry: Последние тренды в мире искусственного интеллекта>, 
    <Entry: Развитие интернета вещей: будущее или реальность?>, 
    <Entry: Новые гаджеты и устройства: обзор рынка>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>, 
    <Entry: Инновации в области виртуальной реальности>, 
    <Entry: Тенденции моды на текущий сезон>, 
    <Entry: Как создать стильный образ на каждый день>, 
    <Entry: История моды: от ретро до современности>, 
    <Entry: Уход за кожей и волосами: лучшие советы>, 
    <Entry: Интервью с известными модельерами и дизайнерами>]>
    """

    # Вывести всех авторов которые не указали город
    print(AuthorProfile.objects.filter(city__isnull=True))
    """
    <QuerySet [
    <AuthorProfile: anna_journey>, 
    <AuthorProfile: natalia_author>, 
    <AuthorProfile: vladimir_writer>, 
    <AuthorProfile: alexandra_creative>, 
    <AuthorProfile: svetlana_writer>, 
    <AuthorProfile: larisa_thinker>
    ]>
    """

    # Вывести записи где в тексте статьи встречается патерн \w*стран\w*
    print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))
    """
    <QuerySet [
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>
    ]>
    """
    # Вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru
    print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)'))
    """
    <QuerySet [
    <Entry: Изучение красот Мачу-Пикчу>, 
    <Entry: Знакомство с Парижем>, 
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>, 
    <Entry: Инновации в области виртуальной реальности>, 
    <Entry: Как создать стильный образ на каждый день>, 
    <Entry: Уход за кожей и волосами: лучшие советы>, 
    <Entry: Интервью с известными модельерами и дизайнерами>
    ]>
    """
    # Если необходимо вывести записи авторов с почтовыми доменами @gmail.com и @mail.ru, но чтобы значения не повторялись, то используем distinct()
    print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())
    """
    <QuerySet [
    <Entry: Изучение красот Мачу-Пикчу>, 
    <Entry: Знакомство с Парижем>, 
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Кибербезопасность: защита вашей конфиденциальности>, 
    <Entry: Инновации в области виртуальной реальности>, 
    <Entry: Как создать стильный образ на каждый день>, 
    <Entry: Уход за кожей и волосами: лучшие советы>, 
    <Entry: Интервью с известными модельерами и дизайнерами>
    ]>
    """

    all_obj = Blog.objects.all()
    print("Вывод всех значений в таблице Blog\n", all_obj)

    all_obj = Blog.objects.first()
    print("Вывод первого значения в таблице Blog\n", all_obj)

    all_obj = Blog.objects.all()
    obj_first = all_obj.first()
    print("Разные запросы на вывод в Blog\n", f"Первое значение таблицы = {obj_first}\n",
          f"Все значения = {all_obj}")

    all_obj = Blog.objects.all()
    for idx, value in enumerate(all_obj):
        print(f"idx = {idx}, value = {value}")
    print(all_obj[0])  # Получение 0-го элемента
    print(all_obj[2:4])  # Получение 2 и 3 элемента
    """Получение последнего элемента не осуществимо через обратный индекс
    all_obj[-1] - нельзя
    можно воспользоваться latest('<name_field>'), где <name_field> - имя колонки в БД.

    Почти все операции над БД не требуют предварительного получения всех элементов, постоянная запись Blog.objects.all()
    просто для примера.
    """
    print(all_obj.latest("id"))  # Получение последнего элемента
    print(Blog.objects.latest("id"))  # Одинаково работает

    # Пример получения элемента по одному условию
    print(Blog.objects.get(id=1))
    # Пример получения элемента по двум условиям. Условия работают с оператором И, т.е. выведется строка, только с
    # совпадением и первого и второго параметра.
    print(Blog.objects.get(id=1, name="Путешествия по миру"))
    # Если нет совпадений, то выйдет исключение "db.models.Blog.DoesNotExist: Blog matching query does not exist."
 #   print(Blog.objects.get(id=2, name="Путешествия по миру"))

    print(Blog.objects.filter(id__gte=2))  # Вывод всех строк таблицы Blog у которых значение id >= 2.

    print(Blog.objects.exclude(id__gte=2))  # Вывод всех строк таблицы Blog кроме тех у которых значение id >= 2.
    #  <QuerySet [<Blog: Путешествия по миру>]>

    # Пример для get
    try:
        Blog.objects.get(id=2, name="Путешествия по миру")
    except Blog.DoesNotExist:
        print("Не существует")
    # Пример для filter
    print(Blog.objects.filter(id=2, name="Путешествия по миру").exists())

    print(Blog.objects.count())  # Можно ко всей таблице
    print(Blog.objects.filter(id__gte=2).count())  # Можно к запросу
    all_data = Blog.objects.all()
    filtred_data = all_data.filter(id__gte=2)
    print(filtred_data.count())  # Можно к частным запросам

    filtered_data = Blog.objects.filter(id__gte=2)
    print(filtered_data.order_by("id"))  # упорядочивание по возрастанию по полю id
    print(filtered_data.order_by("-id"))  # упорядочивание по уменьшению по полю id
    print(filtered_data.order_by("-name", "id"))  # упорядочивание по двум параметрам, сначала по первому на уменьшение,
    # затем второе на увеличение. Можно упорядочивание провести по сколь угодно параметрам.

    from django.db.models import Count

    # Запрос, аннотирующий количество статей для каждого блога,
    # при этом добавляется новая колонка number_of_entries для вывода
    entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
    print(entry)
    """
    <QuerySet [
    {'name': 'Путешествия по миру', 'number_of_entries': 5}, 
    {'name': 'Кулинарные искушения', 'number_of_entries': 5}, 
    {'name': 'Фитнес и здоровый образ жизни', 'number_of_entries': 5}, 
    {'name': 'ИТ-новости и технологии', 'number_of_entries': 5}, 
    {'name': 'Мода и стиль', 'number_of_entries': 5}
    ]>
    """

    from django.db.models import Count

    blogs = Blog.objects.alias(number_of_entries=Count('entries')).filter(number_of_entries__gt=4)
    print(blogs)
    """
    <QuerySet [
    <Blog: Путешествия по миру>, 
    <Blog: Кулинарные искушения>, 
    <Blog: Фитнес и здоровый образ жизни>, 
    <Blog: ИТ-новости и технологии>, 
    <Blog: Мода и стиль>
    ]>
    """

    ## Выведет ошибку, так как поле number_of_entries не существует, виду различий между alias и annotate
    # blogs = Blog.objects.alias(number_of_entries_new=Count('entries')).filter(number_of_entries__gt=4).values('blog', 'entries_new')

    from django.db.models import Avg, Q

    # Вычислить среднюю оценку только для уникальных значений
    average_rating = Entry.objects.aggregate(
        average_rating1=Avg('rating', distinct=True)
    )
    print(average_rating)  # {'average_rating1': 3.6999999999999993}

    # Вычислить среднюю оценку с заданным значением по умолчанию(допустим
    # значение у поля None), если агрегация не возвращает результат
    average_rating_with_default = Entry.objects.aggregate(
        average_rating2=Avg('rating', default=5.0)
    )
    print(average_rating_with_default)  # {'average_rating2': 3.46}

    # Вычислить среднюю оценку только для статей, опубликованных после 2023 года
    average_rating = Entry.objects.aggregate(
        average_rating3=Avg('rating', filter=Q(pub_date__year__gt=2023)))
    print(average_rating)  # {'average_rating3': 2.925}

    from django.db.models import Count

    # Вычислить число уникальных авторов статей(которые написали хотя бы одну статью)
    count_authors = Entry.objects.aggregate(
        count_authors=Count('author', distinct=True)
    )
    print(count_authors)  # {'count_authors': 12}

    # Получить статьи с количеством тегов
    entries_with_tags_count = Entry.objects.annotate(
        tag_count=Count('tags')).values('id', 'tag_count')
    print(entries_with_tags_count)
    """
    <QuerySet [
    {'id': 1, 'tag_count': 2}, 
    {'id': 2, 'tag_count': 1}, 
    {'id': 3, 'tag_count': 2}, 
    {'id': 4, 'tag_count': 2},
    ...
    """

    from django.db.models import Max, Min

    # Вычислить максимальную и минимальную оценку
    calc_rating = Entry.objects.aggregate(
        max_rating=Max('rating'), min_rating=Min('rating')
    )
    print(calc_rating)  # {'max_rating': 5.0, 'min_rating': 0.0}

    from django.db.models import StdDev, Variance

    # Вычислить среднее квадратическое отклонение и дисперсию оценки
    calc_rating = Entry.objects.aggregate(
        std_rating=StdDev('rating'), var_rating=Variance('rating')
    )
    print(calc_rating)  # {'std_rating': 1.6577092628081682, 'var_rating': 2.748}

    from django.db.models import Sum

    # Вычислить общее число комментариев в БД
    calc_rating = Entry.objects.aggregate(
        sum_comments=Sum('number_of_comments')
    )
    print(calc_rating)  # {'sum_comments': 134}

    filtered_data = Blog.objects.filter(id__gte=2).order_by("id")
    print(filtered_data)  # упорядочивание по возрастанию по полю id
    """
    <QuerySet [
    <Blog: Кулинарные искушения>, 
    <Blog: Фитнес и здоровый образ жизни>, 
    <Blog: ИТ-новости и технологии>, 
    <Blog: Мода и стиль>
    ]>
    """
    print(filtered_data.reverse())  # поменяли направление
    """
    <QuerySet [
    <Blog: Мода и стиль>, 
    <Blog: ИТ-новости и технологии>, 
    <Blog: Фитнес и здоровый образ жизни>, 
    <Blog: Кулинарные искушения>
    ]>
    """

    # Если порядок не указан или в модели, или через order_by, то reverse работать не будет
    filtered_data = Blog.objects.filter(id__gte=2)
    print(filtered_data)
    print(filtered_data.reverse())

#    print(Entry.objects.order_by('author', 'pub_date').distinct('author', 'pub_date'))  # Не работает в SQLite
    # distinct('author', 'pub_date') - оставляет уникальные строки по колонкам author, pub_date
    # distinct() - старается оставить уникальные данные по всем колонкам
    # Аналогично с поиском по полю можно обращаться к связанным данным distinct('author__name', 'pub_date')

    # Обычный запрос
    print(Blog.objects.filter(name__startswith='Фитнес'))
    # <QuerySet [<Blog: Фитнес и здоровый образ жизни>]>

    # Запрос раскрывающий значения
    print(Blog.objects.filter(name__startswith='Фитнес').values())
    """
    QuerySet [{'id': 3, 'name': 'Фитнес и здоровый образ жизни', 
    'tagline': 'Позаботьтесь о своем здоровье, достигните физической формы и ощутите преимущества активного образа жизни!'}]>
    """

    # Вывод всех строк с их раскрытием
    print(Blog.objects.values())
    """
    <QuerySet [
    {'id': 1, 'name': 'Путешествия по миру', 'tagline': 'Откройте новые горизонты и погрузитесь в удивительные приключения вместе с нами!'}, 
    {'id': 2, 'name': 'Кулинарные искушения', 'tagline': 'Раскройте вкусовые грани и наслаждайтесь миром кулинарии вместе с нами!'}, 
    {'id': 3, 'name': 'Фитнес и здоровый образ жизни', 'tagline': 'Позаботьтесь о своем здоровье, достигните физической формы и ощутите преимущества активного образа жизни!'}, 
    {'id': 4, 'name': 'ИТ-новости и технологии', 'tagline': 'Будьте в курсе последних новостей, трендов и инноваций в мире информационных технологий!'}, 
    {'id': 5, 'name': 'Мода и стиль', 'tagline': 'Выражайте свою индивидуальность, следите за модными тенденциями и создавайте неповторимые образы вместе с нами!'}
    ]>
    """
    # Вывод всех строк с сохранением в запросе только необходимых столбцов
    print(Blog.objects.values('id', 'name'))  # Обратите внимание, что данные отсортированы по полю name
    """
    <QuerySet [
    {'id': 4, 'name': 'ИТ-новости и технологии'}, 
    {'id': 2, 'name': 'Кулинарные искушения'}, 
    {'id': 5, 'name': 'Мода и стиль'}, 
    {'id': 1, 'name': 'Путешествия по миру'}, 
    {'id': 3, 'name': 'Фитнес и здоровый образ жизни'}]>
    """

    # Вывод всех строк с их раскрытием
    print(Blog.objects.values_list())
    """
    <QuerySet [
    (1, 'Путешествия по миру', 'Откройте новые горизонты и погрузитесь в удивительные приключения вместе с нами!'), 
    (2, 'Кулинарные искушения', 'Раскройте вкусовые грани и наслаждайтесь миром кулинарии вместе с нами!'), 
    (3, 'Фитнес и здоровый образ жизни', 'Позаботьтесь о своем здоровье, достигните физической формы и ощутите преимущества активного образа жизни!'), 
    (4, 'ИТ-новости и технологии', 'Будьте в курсе последних новостей, трендов и инноваций в мире информационных технологий!'), 
    (5, 'Мода и стиль', 'Выражайте свою индивидуальность, следите за модными тенденциями и создавайте неповторимые образы вместе с нами!')
    ]>
    """
    # Вывод всех строк с сохранением в запросе только необходимых столбцов
    print(Blog.objects.values_list('id', 'name'))  # Обратите внимание, что данные отсортированы по полю name
    """
    <QuerySet [
    (4, 'ИТ-новости и технологии'), 
    (2, 'Кулинарные искушения'), 
    (5, 'Мода и стиль'), 
    (1, 'Путешествия по миру'), 
    (3, 'Фитнес и здоровый образ жизни')
    ]>
    """

    """
    Допустим, у нас есть три конкретных блога. Мы хотим получить объединение записей из этих трех блогов в один QuerySet.
    """
    blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру')
    blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения')
    blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни')
    result_qs = blog_a_entries.union(blog_b_entries, blog_c_entries)
    print(result_qs)
    """
    <QuerySet [
    <Entry: Изучение красот Мачу-Пикчу>, 
    <Entry: Приключения в Амазонке>, 
    <Entry: Знакомство с Парижем>, 
    <Entry: Открывая тайны Колизея>, 
    <Entry: Оазисы Сахары: красота и опасность>, 
    <Entry: Рецепты блюд из итальянской кухни>, 
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Экзотические специи и их использование>, 
    <Entry: Десерты для настоящих сладкоежек>, 
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Здоровое питание: полезные рецепты>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: Как правильно заниматься йогой>, 
    <Entry: Секреты успешного похудения>
    ]>
    """
    # Для такой задачи может хорошо подойти in (ответ будет аналогичен), правда порядок может быть другой
    print(Entry.objects.filter(
        blog__name__in=['Путешествия по миру', 'Кулинарные искушения', 'Фитнес и здоровый образ жизни']))
    """
    <QuerySet [
    <Entry: Рецепты блюд из итальянской кухни>, 
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Экзотические специи и их использование>, 
    <Entry: Десерты для настоящих сладкоежек>, 
    <Entry: Гастрономическое путешествие по Франции>, 
    <Entry: Изучение красот Мачу-Пикчу>, 
    <Entry: Приключения в Амазонке>, 
    <Entry: Знакомство с Парижем>, 
    <Entry: Открывая тайны Колизея>, 
    <Entry: Оазисы Сахары: красота и опасность>, 
    <Entry: Упражнения для поддержания физической формы>, 
    <Entry: Здоровое питание: полезные рецепты>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: Как правильно заниматься йогой>, 
    <Entry: Секреты успешного похудения>
    ]>
    """

    """
    Допустим, у нас есть три конкретных блога. Мы хотим получить авторов, которые написали статью во всех из перечисленных блогах.
    """
    blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру').values('author')
    blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения').values('author')
    blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни').values('author')
    result_qs = blog_a_entries.intersection(blog_b_entries, blog_c_entries)
    print(result_qs)
    # <QuerySet [{'author': 1}, {'author': 9}, {'author': 20}]>

    """
    Вывести авторов, которые не написали ни одной статьи, в приведенных блогах
    """
    blog_a_entries = Entry.objects.filter(blog__name='Путешествия по миру').values('author')
    blog_b_entries = Entry.objects.filter(blog__name='Кулинарные искушения').values('author')
    blog_c_entries = Entry.objects.filter(blog__name='Фитнес и здоровый образ жизни').values('author')
    result_qs = Entry.objects.values('author').difference(blog_a_entries, blog_b_entries, blog_c_entries)
    print(result_qs)
    # <QuerySet [{'author': 5}, {'author': 7}, {'author': 8}]>

    # А допустим так (один из возможных запросов) можно узнать кто вообще не написал ни одной статьи в любой блог,
    # так как нет записей у этого автора в таблице Entry в поле author
#    print(Author.objects.filter(entry__author=None))

    from django.db import connection

    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  0  Запросы =  []
    """
    entry = Entry.objects.get(id=5)
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  1  Запросы =  [...]
    """
    blog = entry.blog
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  2  Запросы =  [...,...]
    """
    print('Результат запроса = ', blog)
    """
    Результат запроса =  Путешествия по миру
    """

    # from django.db import models
    # class Topping(models.Model):
    #     name = models.CharField(max_length=30)
    #
    #
    # class Pizza(models.Model):
    #     name = models.CharField(max_length=50)
    #     toppings = models.ManyToManyField(Topping)
    #
    #     def __str__(self):
    #         return "%s (%s)" % (
    #             self.name,
    #             ", ".join(topping.name for topping in self.toppings.all()),
    #         )
    #
    # Pizza.objects.all()
    # "Hawaiian (ham, pineapple)", "Seafood (prawns, smoked salmon)"

    from django.db import connection

    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  0  Запросы =  []
    """
    entry = Entry.objects.all()
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  0  Запросы =  [], ввиду ленивости QuerySet
    """
    for row in entry:
        tags = [tag.name for tag in row.tags.all()]
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    print('Результат запроса = ', tags)
    """
    Число запросов =  26 Запросы = [...]
    """

    from django.db import connection

    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  0  Запросы =  []
    """
    entry = Entry.objects.prefetch_related("tags")
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  0  Запросы =  [], ввиду ленивости QuerySet
    """
    for row in entry:
        tags = [tag.name for tag in row.tags.all()]
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    print('Результат запроса = ', tags)
    """
    Число запросов =  2 Запросы = [...]
    """

    from django.db.models import F

    """
    Вывести статьи где число комментариев на сайте больше числа комментариев на сторонних ресурсах
    """
    print(Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks')).values('id',
                                                                                       'number_of_comments',
                                                                                       'number_of_pingbacks'))
    """
    <QuerySet [
    {'id': 3, 'number_of_comments': 7, 'number_of_pingbacks': 5}, 
    {'id': 5, 'number_of_comments': 4, 'number_of_pingbacks': 0}, 
    {'id': 6, 'number_of_comments': 10, 'number_of_pingbacks': 0}, 
    {'id': 15, 'number_of_comments': 5, 'number_of_pingbacks': 4}, 
    {'id': 18, 'number_of_comments': 20, 'number_of_pingbacks': 1},
    {'id': 19, 'number_of_comments': 12, 'number_of_pingbacks': 6}
    ]>
    """

    """
    С аннотациями можно создать новый столбец с вычислением определенных характеристик
    """
    print(Entry.objects.annotate(sum_number=F('number_of_pingbacks') + F('number_of_comments')).values('id',
                                                                                                       'number_of_comments',
                                                                                                       'number_of_pingbacks',
                                                                                                       'sum_number'))
    """
    <QuerySet [
    {'id': 1, 'number_of_comments': 2, 'number_of_pingbacks': 10, 'sum_number': 12}, 
    {'id': 2, 'number_of_comments': 14, 'number_of_pingbacks': 30, 'sum_number': 44},
    ...
    ]>
    """

    """
    Или с alias для дальнейшего использования
    """
    print(Entry.objects.alias(sum_number=F('number_of_pingbacks') + F('number_of_comments')).
          annotate(val1=F('sum_number') / F('number_of_comments')).values('id',
                                                                          'number_of_comments',
                                                                          'number_of_pingbacks',
                                                                          'val1'))
    """
    <QuerySet [
    {'id': 1, 'number_of_comments': 2, 'number_of_pingbacks': 10, 'val1': 6}, 
    {'id': 2, 'number_of_comments': 14, 'number_of_pingbacks': 30, 'val1': 3}, 
    {'id': 3, 'number_of_comments': 7, 'number_of_pingbacks': 5, 'val1': 1}, 
    {'id': 4, 'number_of_comments': 2, 'number_of_pingbacks': 5, 'val1': 3}, 
    ...
    ]>
    """
    # Можно заметить, что расчёт не до конца правильный, всё приведено к типу int,
    # так как что annotate, что alias не способны управлять типом полей, для этого есть другие функции например
    # aggregate, ExpressionWrapper

    from django.db.models import Q

    # Получение всех записей, у которых заголовок содержит 'ключевое слово' или текст содержит 'определенное слово'
    entries = Entry.objects.filter(
        Q(headline__icontains='тайны') | Q(body_text__icontains='город'))
    print(entries)
    """
    <QuerySet [
    <Entry: Изучение красот Мачу-Пикчу>, 
    <Entry: Знакомство с Парижем>, 
    <Entry: Открывая тайны Колизея>
    ]>
    """

    from datetime import date

    # Получение записей блога "Путешествия по миру" с датами публикаций между 1 мая 2022 и 1 мая 2023
    entries = Entry.objects.filter(
        Q(blog__name='Путешествия по миру') & Q(pub_date__date__range=(date(2022, 5, 1), date(2023, 5, 1))))
    print(entries)
    """
    <QuerySet [
    <Entry: Приключения в Амазонке>, 
    <Entry: Знакомство с Парижем>, 
    <Entry: Открывая тайны Колизея>, 
    <Entry: Оазисы Сахары: красота и опасность>
    ]>
    """

    # Получить статьи, у которых либо имеется оценка больше 4, либо число комментариев меньше 10 (используя XOR)
    entries = Entry.objects.filter(Q(rating__gt=4) ^ Q(number_of_comments__lt=10))
    print(entries)
    """
    <QuerySet [
    <Entry: Изучение красот Мачу-Пикчу>, 
    <Entry: Приключения в Амазонке>, 
    <Entry: Открывая тайны Колизея>, 
    <Entry: Оазисы Сахары: красота и опасность>, 
    <Entry: Приготовление собственного хлеба>, 
    <Entry: Здоровое питание: полезные рецепты>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: Инновации в области виртуальной реальности>, 
    <Entry: Как создать стильный образ на каждый день>, 
    <Entry: История моды: от ретро до современности>, 
    <Entry: Уход за кожей и волосами: лучшие советы>, 
    <Entry: Интервью с известными модельерами и дизайнерами>
    ]>
    """

    from django.db.models import Case, When, BooleanField, CharField

    # Получение всех записей с полем is_popular, которое равно True, если значение поля rating больше равно 4, иначе False
    entries = Entry.objects.annotate(
        is_popular=Case(
            When(rating__gte=4, then=True),
            default=False,
            output_field=BooleanField()
        )
    ).values('id', 'rating', 'is_popular')
    print(entries)
    """
    <QuerySet [
    {'id': 1, 'rating': 0.0, 'is_popular': False}, 
    {'id': 2, 'rating': 5.0, 'is_popular': True}, 
    {'id': 3, 'rating': 4.7, 'is_popular': True}, 
    {'id': 4, 'rating': 3.3, 'is_popular': False}, 
    {'id': 5, 'rating': 3.4, 'is_popular': False},
    ...
    ]>
    """

    from django.db.models import Count, Value

    # Создание описательной метки для числа тегов в статье
    entries = Entry.objects.annotate(
        count_tags=Count("tags"),
        tag_label=Case(
            When(count_tags__gte=3, then=Value('Много')),
            When(count_tags=2, then=Value('Средне')),
            default=Value('Мало'),
            output_field=CharField()
        )
    ).values('id', 'count_tags', 'tag_label')
    print(entries)
    """
    <QuerySet [
    {'id': 1, 'count_tags': 2, 'tag_label': 'Средне'}, 
    {'id': 2, 'count_tags': 1, 'tag_label': 'Мало'}, 
    {'id': 3, 'count_tags': 2, 'tag_label': 'Средне'}, 
    {'id': 4, 'count_tags': 2, 'tag_label': 'Средне'},
    ...
    ]>
    """

    from django.db.models import Subquery

    # Получаем список ID авторов без биографии
    subquery = AuthorProfile.objects.filter(bio__isnull=True).values('author_id')

    # Фильтруем записи блога по авторам
    query = Entry.objects.filter(author__in=Subquery(subquery))
    print(query)
    """
    <QuerySet [
    <Entry: Знакомство с Парижем>, 
    <Entry: Инновации в области виртуальной реальности>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: Приключения в Амазонке>, 
    <Entry: Рецепты блюд из итальянской кухни>, 
    <Entry: Как правильно заниматься йогой>
    ]>
    """
    # Аналогично можно подключиться так, так как есть непрямая связь между Author и AuthorProfile через первичный ключ
    print(Entry.objects.filter(author__authorprofile__bio__isnull=True))
    """
    <QuerySet [
    <Entry: Приключения в Амазонке>, 
    <Entry: Знакомство с Парижем>, 
    <Entry: Рецепты блюд из итальянской кухни>, 
    <Entry: Топ-10 фитнес-тренеров для вдохновения>, 
    <Entry: Как правильно заниматься йогой>, 
    <Entry: Инновации в области виртуальной реальности>
    """

    from django.db import connection

    # Составляем SQL-запрос
    sql = """
    SELECT id, headline
    FROM db_train_alternative_entry
    WHERE headline LIKE '%%тайны%%' OR body_text LIKE '%%город%%'
    """

    # Выполняем запрос
    # with connection.cursor() as cursor:
    #     cursor.execute(sql)
    # results = cursor.fetchall()

    # Выводим результаты
    for result in result_qs:
        print(result)
    """
    (1, 'Изучение красот Мачу-Пикчу')
    (3, 'Знакомство с Парижем')
    (4, 'Открывая тайны Колизея')
    """

    # Выполняем сырой SQL-запрос
    results = Entry.objects.raw(
        """
        SELECT id, headline
        FROM db_train_alternative_entry
        WHERE headline LIKE '%%тайны%%' OR body_text LIKE '%%город%%'
        """
    )

    # Выводим результаты
    for result in results:
        print(result.id, result.headline)
    """
    1 Изучение красот Мачу-Пикчу
    3 Знакомство с Парижем
    4 Открывая тайны Колизея
    """

    from django.db.models import F, Window, Avg, Max, Min

    # Получаем queryset статей блога с аннотациями, используя оконные функции
    queryset = Entry.objects.annotate(
        avg_comments=Window(
            expression=Avg('number_of_comments'),
            partition_by=F('blog'),
        ),
        max_comments=Window(
            expression=Max('number_of_comments'),
            partition_by=F('blog'),
        ),
        min_comments=Window(
            expression=Min('number_of_comments'),
            partition_by=F('blog'),
        ),

    ).values('id', 'headline', 'avg_comments', 'max_comments', 'min_comments')
    print(queryset)
    """
    <QuerySet [
    {'id': 1, 'headline': 'Изучение красот Мачу-Пикчу', 'avg_comments': 5.8, 'max_comments': 14, 'min_comments': 2}, 
    {'id': 2, 'headline': 'Приключения в Амазонке', 'avg_comments': 5.8, 'max_comments': 14, 'min_comments': 2}, 
    {'id': 3, 'headline': 'Знакомство с Парижем', 'avg_comments': 5.8, 'max_comments': 14, 'min_comments': 2}, 
    {'id': 4, 'headline': 'Открывая тайны Колизея', 'avg_comments': 5.8, 'max_comments': 14, 'min_comments': 2}, 
    {'id': 5, 'headline': 'Оазисы Сахары: красота и опасность', 'avg_comments': 5.8, 'max_comments': 14, 'min_comments': 2}, 
    {'id': 6, 'headline': 'Рецепты блюд из итальянской кухни', 'avg_comments': 5.6, 'max_comments': 10, 'min_comments': 2}, 
    {'id': 7, 'headline': 'Приготовление собственного хлеба', 'avg_comments': 5.6, 'max_comments': 10, 'min_comments': 2}, 
    {'id': 8, 'headline': 'Экзотические специи и их использование', 'avg_comments': 5.6, 'max_comments': 10, 'min_comments': 2},
    {'id': 9, 'headline': 'Десерты для настоящих сладкоежек', 'avg_comments': 5.6, 'max_comments': 10, 'min_comments': 2}, 
    {'id': 10, 'headline': 'Гастрономическое путешествие по Франции', 'avg_comments': 5.6, 'max_comments': 10, 'min_comments': 2},
    {'id': 11, 'headline': 'Упражнения для поддержания физической формы', 'avg_comments': 3.0, 'max_comments': 7, 'min_comments': 0}, 
    {'id': 12, 'headline': 'Здоровое питание: полезные рецепты', 'avg_comments': 3.0, 'max_comments': 7, 'min_comments': 0}, 
    ...
    ]>
    """










