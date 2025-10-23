# -*- coding: utf-8 -*-
from src.Types import DataType


class FindPerfectStudent:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find(self) -> str:
        perfect_students = []
        
        for student_name, subjects in self.data.items():
            all_perfect = all(grade == 100 for _, grade in subjects)
            if all_perfect:
                perfect_students.append(student_name)
        
        if perfect_students:
            return perfect_students[0]  # возвращаем первого найденного
        else:
            return "Студентов с 100 баллами по всем предметам не найдено"
