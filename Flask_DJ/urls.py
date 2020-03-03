from importlib import import_module
from typing import Iterator, Tuple, Callable, List
from flask import Flask


class Path:
    """
    Creator of your application paths
    :param app: Your flask application
    """
    def __init__(self, app: Flask):
        self.app = app

    def _add_url(self, url: str, view_func: Callable, methods: List) -> bool:
        debug = self.app.debug
        self.app.add_url_rule(url, view_func=view_func, methods=methods)
        print(f'add url: {url}\n' if debug else '', end='')
        return True

    def add_absolute_path(self, url: str, view_func: Callable, *, methods=['GET']) -> bool:
        """Adds a URL directly"""
        return self._add_url(url, view_func, methods)

    def add_relative_path(self, url: str, path_params: Iterator[Tuple[str, Callable, List]]) -> bool:
        """Adds URLs lists"""
        for url_, view_func, methods_ in path_params:
            if not self._add_url(url + url_, view_func, methods_):
                return False
        return True

    @staticmethod
    def get_relative_path(url: str, view_func: Callable, *, methods=['GET']) -> Tuple[str, Callable, List]:
        """Call this function if you want to connect url data relative to"""
        return url, view_func, methods


def get_module(path: str):
    try:
        pack = import_module(path)
        return pack
    except ModuleNotFoundError:
        raise ImportError(f"Не удалось найти {path}")


def get_patterns(path: str) -> List:
    pack = get_module(path)
    try:
        patterns = getattr(pack, 'urlpatterns')
        return patterns
    except AttributeError:
        raise AttributeError(f'Файл {path} не содержит urlpatterns')


def include(path: str):
    """
    Creates an iterator from the urlpatterns of the transmitted file.
    :param path: file containing urlpatterns
    """
    patterns = get_patterns(path)
    for args in patterns:
        if isinstance(args, bool):
            continue
        yield args
