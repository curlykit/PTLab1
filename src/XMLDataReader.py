# -*- coding: utf-8 -*-
import xmltodict
from src.Types import DataType
from src.DataReader import DataReader


class XMLDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            xml_data = xmltodict.parse(file.read())

        students: DataType = {}

        if 'root' in xml_data:
            for student_element in xml_data['root']:
                if isinstance(student_element, str):
                    continue

                student_name = list(student_element.keys())[0]
                subjects = []

                for subject, grade in student_element[student_name].items():
                    if subject != '@name':
                        subjects.append((subject, int(grade)))

                students[student_name] = subjects

        return students
