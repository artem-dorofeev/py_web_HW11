# py_web_HW11

# poetry inint
# poetry add fastapi sqlalchemy alembic psycopg2 uvicorn pydantic["email"]
# poetry shell

# створення структури: створюємо теку - src, з наступними теками: 
# * conf - config.ini (зберігаємо налаштування - шлях до БД, порти, логіни і т.і.)
# * database - дб, моделі і т.і.
# repository - абстракція між модел'ю і рутером(контролером) можеть буди класи,функції, у нас будуть модулі (один клас або один модуль працює з однією таблицею в sql). Створюємо файли cats.py owners.py і 
# створюємо строку router = APIRouter(prefix="/owners", tags=['owners']), далі в декораторах змінюємо app на router, також видаляємо owners і tags=['owners'] бо ми вже це описали вишче

# routes - бізнес логіка Створюємо файли cats.py owners.py і переносимо туди методи з майну які створювались для кожного класу
# services - окремі сторонні сервіси



# робимо міграцію:
# alembic init migrations
# тека migrations - env.py:
# target_metadata = Base.metadata 
# імпортуємо from src.database.db import URI та from src.database.models import Base
# config.set_main_option("sqlalchemy.url", URI) - sqlalchemy.url ,беремо з файлу alembic.ini (sqlalchemy.url = driver://user:pass@localhost/dbname) URI з файлу db.py

# alembic revision --autogenerate -m 'Init'

# alembic upgrade head


# запуск сервера - uvicorn НАЗВА ФАЙЛА:арр
# uvicorn main:app --reload