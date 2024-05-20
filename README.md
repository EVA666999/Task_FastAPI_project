<h1>FastAPI Менеджер задач</h1>

<p>Это API менеджера задач, построенный с использованием FastAPI и SQLAlchemy. Также включает поддержку WebSocket, Docker</p>

<h2>Особенности</h2>

<ul>
<li>Аутентификация пользователей (регистрация и вход)</li>
<li>Создание, чтение, обновление и удаление задач (операции CRUD)</li>
<li>Аутентификация на основе токенов с использованием JWT</li>
<<<<<<< HEAD
<li>Внедрение поддержки WebSocket для обновления пользователей о создании и изменении задач</li>
<li>интеграция с Docker для удобного развёртывания приложения</li>
<li>Интеграция с базой данных PostgreSQL</li>
=======
<li>Проект подключён к PostgreSQL</li>
>>>>>>> 9113e7c4850cf0e7cdc45be4513b63510388354c
</ul>

<h2>Установка</h2>

<ol>
<li>Клонируйте репозиторий:</li>
</ol>

<pre><code>git clone &lt;ссылка на репозиторий&gt;
</code></pre>

<ol start="2">
<li>Перейдите в каталог проекта:</li>
</ol>

<pre><code>cd &lt;каталог-проекта&gt;
</code></pre>

<ol start="3">
<li>Установите зависимости:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<ol start="4">
<li>Настройте базу данных:</li>
</ol>

<ul>
<li>Убедитесь, что у вас установлена и запущена PostgreSQL.</li>
<li>Обновите настройки подключения к базе данных в файле <code>app/db/database.py</code>.</li>
</ul>

<ol start="5">
<li>Запустите сервер FastAPI:</li>
</ol>

<pre><code>uvicorn app.main:app --reload
</code></pre>

<h2>Конечные точки API</h2>

<h3>Пользователи</h3>

<ul>
<li><code>POST /auth/register/</code>: Зарегистрировать нового пользователя.</li>
<li><code>POST /auth/login/</code>: Войти и получить токен доступа.</li>
</ul>

<h3>Задачи</h3>

<ul>
<li><code>POST /tasks/create</code>: Создать новую задачу.</li>
<li><code>GET /tasks</code>: Получить все задачи аутентифицированного пользователя.</li>
<li><code>PUT /task/{task_id}</code>: Обновить задачу.</li>
<li><code>DELETE /task/{task_id}</code>: Удалить задачу.</li>
</ul>

<h2>Использование</h2>

<ol>
<li>Зарегистрируйте нового пользователя, используя конечную точку <code>/auth/register/</code>.</li>
<li>Войдите под учетной записью зарегистрированного пользователя, используя конечную точку <code>/auth/login/</code>, чтобы получить токен доступа.</li>
<li>Используйте полученный токен доступа для аутентификации и доступа к другим конечным точкам, связанным с управлением задачами.</li>
</ol>

<h2>Аутентификация</h2>

<ul>
<li>Аутентификация на основе токенов реализована с использованием JWT.</li>
<li>Для доступа к конечным точкам, которые требуют аутентификации, включите токен JWT в заголовок <code>Authorization</code> запроса. Пример: <code>Authorization: Bearer &lt;токен-доступа&gt;</code></li>
</ul>
<<<<<<< HEAD

=======
>>>>>>> 9113e7c4850cf0e7cdc45be4513b63510388354c
