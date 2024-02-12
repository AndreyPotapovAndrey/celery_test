import datetime
from tasks import cpu_bound


def main():
    # rusult_1 = cpu_bound(1, 2)
    # result_2 = cpu_bound(3, 4)
    # result_3 = cpu_bound(5, 6)
    # result_4 = cpu_bound(7, 8)
    #
    # print(rusult_1)
    # print(result_2)
    # print(result_3)
    # print(result_4)

    # Чтобы был прирост произподительности, нужно явно через код отдавать вычисления на Celery

    async_result_1 = cpu_bound.delay(1, 2)  # Delay обращается к брокеру и закидывает задачу на Celery
    async_result_2 = cpu_bound.delay(3, 4)  # Delay возвращает специальный объект async_rusult
    async_result_3 = cpu_bound.delay(5, 6)
    async_result_4 = cpu_bound.delay(7, 8)

    # print(async_rusult_1, async_rusult_2, async_rusult_3, async_rusult_4)

    result_1 = async_result_1.get()  # async_result обращается к backend и проверяет, обсчитано или нет
    result_2 = async_result_2.get()  # Особенность меиода get заключается в том, что мы не перейдём на следующую строку
    # кода, до тех пор, пока результат задачи не обсчитается
    result_3 = async_result_3.get()
    result_4 = async_result_4.get()

    print(result_1, result_2, result_3, result_4)


if __name__ == '__main__':
    start = datetime.datetime.now()
    main()
    print(datetime.datetime.now() - start)
