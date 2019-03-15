def test_dict():
    # A-A-A
    # Arrange -> подготовка данных
    first = {'id': 1, 'name': 'Ivan'}
    second = {'name': 'Ivan', 'id': 1}
    # Act -> выполнение целевого действия
    # пока нет
    # Assert -> проверка
    assert first == second

    # https://github.com/coursar/python-starter