# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from src.Types import DataType
from src.DataReader import DataReader


class XMLDataReader(DataReader):

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()
        
        students: DataType = {}
        
        for student_elem in root:
            student_name = student_elem.attrib.get('name', '')
            subjects = []
            
            for subject_elem in student_elem:
                subject_name = subject_elem.tag
                grade = int(subject_elem.text)
                subjects.append((subject_name, grade))
            
            if student_name:
                students[student_name] = subjects
        
        return students
