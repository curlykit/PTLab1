# -*- coding: utf-8 -*-
import xmltodict
from src.Types import DataType
from src.DataReader import DataReader


class XMLDataReader(DataReader):

    def read(self, path: str) -> DataType:
        with open(path, 'r', encoding='utf-8') as file:
            xml_data = xmltodict.parse(file.read())
        
        students: DataType = {}
        
        if 'root' in xml_data and xml_data['root'] is not None:
            student_elements = xml_data['root']
            
            # Если только один студент, xmltodict возвращает dict вместо list
            if isinstance(student_elements, dict):
                student_elements = [student_elements]
            
            for student_element in student_elements:
                # Получаем имя студента (первый ключ в словаре)
                student_name = list(student_element.keys())[0]
                student_data = student_element[student_name]
                
                subjects = []
                
                # Обрабатываем предметы и оценки
                for subject, grade in student_data.items():
                    if subject not in ['@name']:  # игнорируем атрибуты
                        subjects.append((subject, int(grade)))
                
                students[student_name] = subjects
        
        return students
