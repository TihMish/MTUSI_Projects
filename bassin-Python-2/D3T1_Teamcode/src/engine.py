"""Состояние знаний по контракту v3. Бюджет и показанные ID хранит main."""


def start():
    raise NotImplementedError('Верните начальное состояние знаний: словарь')


def observe(state, question, result):
    raise NotImplementedError('Обновите знания только по принятому ответу в шкале')
