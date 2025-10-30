# -*- coding: utf-8 -*-
from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], tuple[str, str]]:
    args = ["-p", "/home/user/file.txt"]
    return args, ("/home/user/file.txt", "text")


@pytest.fixture()
def correct_arguments_with_format() -> tuple[list[str], tuple[str, str]]:
    args = ["-p", "/home/user/file.txt", "-f", "xml"]
    return args, ("/home/user/file.txt", "xml")


@pytest.fixture()
def correct_arguments_with_text_format() -> tuple[list[str], tuple[str, str]]:
    args = ["-p", "/home/user/file.txt", "-f", "text"]
    return args, ("/home/user/file.txt", "text")


@pytest.fixture()
def noncorrect_arguments_missing_path() -> list[str]:
    return ["/home/user/file.txt"]


@pytest.fixture()
def noncorrect_arguments_empty() -> list[str]:
    return []


def test_get_path_from_correct_arguments(correct_arguments_string):
    """Тест 1: Корректные аргументы без указания формата"""
    args, expected_result = correct_arguments_string
    expected_path, expected_format = expected_result
    path, file_format = get_path_from_arguments(args)
    assert path == expected_path
    assert file_format == expected_format


def test_get_path_from_correct_arguments_with_xml_format(
    correct_arguments_with_format
):
    """Тест 2: Корректные аргументы с указанием формата xml"""
    args, expected_result = correct_arguments_with_format
    expected_path, expected_format = expected_result
    path, file_format = get_path_from_arguments(args)
    assert path == expected_path
    assert file_format == expected_format


def test_get_path_from_correct_arguments_with_text_format(
    correct_arguments_with_text_format
):
    """Тест 3: Корректные аргументы с явным указанием формата text"""
    args, expected_result = correct_arguments_with_text_format
    expected_path, expected_format = expected_result
    path, file_format = get_path_from_arguments(args)
    assert path == expected_path
    assert file_format == expected_format


def test_get_path_from_noncorrect_arguments_missing_path(
    noncorrect_arguments_missing_path
):
    """Тест 4: Некорректные аргументы - отсутствует флаг -p"""
    with pytest.raises(SystemExit) as exc_info:
        get_path_from_arguments(noncorrect_arguments_missing_path)
    assert exc_info.type == SystemExit


def test_get_path_from_noncorrect_arguments_empty(noncorrect_arguments_empty):
    """Тест 5: Некорректные аргументы - пустой список"""
    with pytest.raises(SystemExit) as exc_info:
        get_path_from_arguments(noncorrect_arguments_empty)
    assert exc_info.type == SystemExit


def test_get_path_returns_tuple_of_two_strings():
    """Тест 6: Проверяем, что функция возвращает кортеж из двух строк"""
    args = ["-p", "/home/user/file.txt"]
    result = get_path_from_arguments(args)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], str)
