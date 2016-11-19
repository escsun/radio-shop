# radio-shop
<h3><b>Что это за проект?</b><h4>
<p>Здесь ведется разработка интернет-магазина радио деталей.</p>
<h3><b>Как запустить проект?</b></h3>
<p>В системе Linux (debian):</p>
<pre>
<code>mkdir django</code>
<code>cd django</code>
<code>virtualenv -p /usr/bin/python3 venv</code>
<code>source venv/bin/activate</code>
<code>pip install -U pip setuptools</code>
<code>cd radio-shop</code>
<code>pip install -r requiments.txt</code>
<code>python manage.py migrate</code>
<code>python manage.py createsuperuser</code>
<code>python manage.py runserver</code>
</pre>
<h3><b>Что на данный момент сделано?</b></h3>
<p><b>Авторизация:</b></p>
<p>Сделано поле email уникальным</p>
<p>Регистрация и авторизация</p>
<p>Regex позволяет использовать только латинские буквы, цифры, тире и знак подчеркивания</p>
<p>Отправка на электронную почту, для новых пользователей</p>
<p>Генерация кода активации</p>
<p>Сброс пароля по электронной почте</p>
<p>Смена пароля</p>
<p><b>Каталог:</b></p>
<p>Список категорий в виде реализации nested sets</p>
<p>Список товаров</p>
<h3><b>Что планируется сделать еще?</b></h3>
<p>Корзину</p>
<p>Поиск товаров</p>
<p>Фильтрация товара по характеристикам</p>
<h3><b>Помощь проекту?</b></h3>
<p>Если вы заметили что-то странное в проекте, или знаете как его улучшить, пожалуйста, создайте новый инцидент в разделе Issues - <a href="https://github.com/escsun/radio-shop/issues">https://github.com/escsun/radio-shop/issues</a> </p>
<h3><b>Безопасность?</b></h3>
<p>В случае обнаружения проблемы безопасности в проекте, пожалуйста, сообщите о ней на адрес <a href="mailto:ecssunarcher@gmail.com">ecssunarcher@gmail.com</a> до обнародования.</p>
<p>В письме желательно указать на место в коде, ответственное за уязвимость.</p>
<p>Хорошо, если вы также приведёте пример эксплуатации найденной уязвимости.</p>


