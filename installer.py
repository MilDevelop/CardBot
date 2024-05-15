import pip._internal as pip


def import_lib(name):
    try:
        return __import__(name)  # пытаемся импортировать
    except ImportError:
        pip.main(['install', name])  # ставим библиотеку если её нет
    return __import__(name)  # возвращаем библиотеку
environs = import_lib('environs')
