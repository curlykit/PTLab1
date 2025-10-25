# -*- coding: utf-8 -*-
from src.Types import DataType
from src.FindPerfectStudent import FindPerfectStudent
import pytest


class TestFindPerfectStudent:

    @pytest.fixture()
    def input_data_with_perfect(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 100),
                ("физика", 100),
                ("химия", 100)
            ],
            "Петров Петр Петрович": [
                ("математика", 90),
                ("физика", 85),
                ("химия", 95)
            ],
            "Сидоров Сидор Сидорович": [
                ("математика", 100),
                ("физика", 100),
                ("химия", 100)
            ]
        }

    @pytest.fixture()
    def input_data_without_perfect(self) -> DataType:
        return {
            "Иванов Иван Иванович": [
                ("математика", 90),
                ("физика", 100),
                ("химия", 100)
            ],
            "Петров Петр Петрович": [
                ("математика", 85),
                ("физика", 95),
                ("химия", 90)
            ]
        }

    def test_find_with_perfect_students(
        self, input_data_with_perfect: DataType
    ) -> None:
        finder = FindPerfectStudent(input_data_with_perfect)
        result = finder.find()
        assert result == "Иванов Иван Иванович"

    def test_find_without_perfect_students(
        self, input_data_without_perfect: DataType
    ) -> None:
        finder = FindPerfectStudent(input_data_without_perfect)
        result = finder.find()
        expected = "Студентов с 100 баллами по всем предметам не найдено"
        assert result == expected

    def test_find_empty_data(self) -> None:
        finder = FindPerfectStudent({})
        result = finder.find()
        expected = "Студентов с 100 баллами по всем предметам не найдено"
        assert result == expected
