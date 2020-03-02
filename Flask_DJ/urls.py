from importlib import import_module
from typing import Iterator, Tuple, Callable, List
from warnings import warn


class Path:
    def __init__(self, app):
        self.app = app

    def _add_url(self, url, func, methods):
        debug = self.app.debug
        if not (isinstance(url, str) and hasattr(func, '__call__')):
            warn(f"Некорректные данные", Warning)
            return False
        self.app.add_url_rule(url, view_func=func, methods=methods)
        print(f'add url: {url}\n' if debug else '', end='')
        return True

    def absolut_path(self, url, func, *, methods=['GET']):
        return self._add_url(url, func, methods)

    def relative_path(self, url: str, path_params: Iterator[Tuple[str, Callable, List]]):
        for url_, fnc, methods_ in path_params:
            if not self._add_url(url + url_, fnc, methods_):
                return False
        return True


def get_module(path):
    try:
        pack = import_module(path)
        return pack
    except ModuleNotFoundError:
        raise ImportError(f"Не удалось найти {path}")


def get_patterns(path):
    pack = get_module(path)
    try:
        patterns = getattr(pack, 'urlpatterns')
        return patterns
    except AttributeError:
        raise AttributeError(f'Файл {path} не содержит urlpatterns')


def include(path):
    patterns = get_patterns(path)
    for args in patterns:
        if isinstance(args, bool):
            continue
        yield args
