# -*- coding: utf-8 -*-
from src.main import get_path_from_arguments
import pytest


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], tuple[str, str]]:
    args = ["-p", "/home/user/file.txt"]
    return args, ("/home/user/file.txt", "text")


@pytest.fixture()
def correct_arguments_with_format() -> tuple[
    list[str], tuple[str, str]
]:
    args = ["-p", "/home/user/file.txt", "-f", "xml"]
    return args, ("/home/user/file.txt", "xml")


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


def test_get_path_from_correct_arguments(
    correct_arguments_string: tuple[list[str], tuple[str, str]]
) -> None:
    path, file_format = get_path_from_arguments(correct_arguments_string[0])
    expected_path, expected_format = correct_arguments_string[1]
    assert path == expected_path
    assert file_format == expected_format


def test_get_path_from_correct_arguments_with_format(
    correct_arguments_with_format: tuple[
        list[str], tuple[str, str]
    ]
) -> None:
    args = correct_arguments_with_format[0]
    path, file_format = get_path_from_arguments(args)
    expected_path, expected_format = correct_arguments_with_format[1]
    assert path == expected_path
    assert file_format == expected_format


def test_get_path_from_noncorrect_arguments(
    noncorrect_arguments_string: list[str]
) -> None:
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])
    assert e.type == SystemExit
