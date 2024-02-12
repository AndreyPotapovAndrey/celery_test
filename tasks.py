import time
from celery import Celery

celery_app = Celery('tasks',
                    broker='redis://127.0.0.1:6379/1',
                    backend='redis://127.0.0.1:6379/2',
                    broker_connection_retry_on_startup=True
                    )


# Celery принимает довольно много аргументов. Но самых главных - 2.
# "broker" - адрес брокера - то, через что будут передаваться сообщения на Selery.
# В данном случае Redis, запущенный на локальной машине.
# По умолчанию в Redis "с ходу" есть несколько БД, которые мы можем использовать. Все они пронумерованы.
# brocker получает БД 1 (.../1)
# 2-й аргумент - "backend" - то, куда складируется результат. Результаты будут складываться в базу №2 (.../2)



@celery_app.task()
# Декоратор @celery_app.task превратил функцию cpu_bound в специальный объект (смотри метод delay в main.py)
def cpu_bound(a, b):
    time.sleep(0.5)
    return a + b

    # return 'Hello World'