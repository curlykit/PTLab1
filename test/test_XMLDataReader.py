# -*- coding: utf-8 -*-
import pytest
import os
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def normal_xml_content(self) -> tuple[str, DataType]:
        """Нормальный случай с корректными данными"""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<students>
    <student name="Иванов Иван Иванович">
        <математика>100</математика>
        <физика>95</физика>
        <химия>90</химия>
    </student>
    <student name="Петров Петр Петрович">
        <математика>85</математика>
        <литература>92</литература>
    </student>
</students>"""

        expected_data = {
            "Иванов Иван Иванович": [
                ("математика", 100),
                ("физика", 95),
                ("химия", 90)
            ],
            "Петров Петр Петрович": [
                ("математика", 85),
                ("литература", 92)
            ]
        }
        return xml_content, expected_data

    @pytest.fixture()
    def empty_xml_content(self) -> tuple[str, DataType]:
        """Пустой XML файл"""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<students>
</students>"""

        expected_data = {}
        return xml_content, expected_data

    @pytest.fixture()
    def xml_with_special_chars(self) -> tuple[str, DataType]:
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<root>
    <student name="Сидоров Алексей">
        <программирование>100</программирование>
        <английский>95</английский>
    </student>
</root>"""

        expected_data = {
            "Сидоров Алексей": [
                ("программирование", 100),
                ("английский", 95)
            ]
        }
        return xml_content, expected_data

    def write_xml_file(self, content: str, filepath: str) -> None:
        """Вспомогательный метод для записи XML с правильной кодировкой"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    def test_read_normal_case(self, normal_xml_content: tuple[str, DataType], tmpdir) -> None:
        """Тест 1: Корректное чтение нормального XML файла"""
        xml_content, expected_data = normal_xml_content
        
        # Создаем временный файл с правильной кодировкой
        p = tmpdir.mkdir("datadir").join("normal.xml")
        file_path = str(p)
        self.write_xml_file(xml_content, file_path)
        
        # Читаем данные
        reader = XMLDataReader()
        result_data = reader.read(file_path)
        
        # Проверяем что данные прочитаны правильно
        assert result_data == expected_data
        assert len(result_data) == 2
        assert "Иванов Иван Иванович" in result_data
        assert "Петров Петр Петрович" in result_data

    def test_read_empty_file(self, empty_xml_content: tuple[str, DataType], tmpdir) -> None:
        """Тест 2: Чтение пустого XML файла"""
        xml_content, expected_data = empty_xml_content
        
        p = tmpdir.mkdir("datadir").join("empty.xml")
        file_path = str(p)
        self.write_xml_file(xml_content, file_path)
        
        reader = XMLDataReader()
        result_data = reader.read(file_path)
        
        # Должен вернуться пустой словарь
        assert result_data == expected_data
        assert len(result_data) == 0

    def test_read_with_special_characters(self, xml_with_special_chars: tuple[str, DataType], tmpdir) -> None:
        """Тест 3: Чтение XML с кириллическими символами"""
        xml_content, expected_data = xml_with_special_chars
        
        p = tmpdir.mkdir("datadir").join("special.xml")
        file_path = str(p)
        self.write_xml_file(xml_content, file_path)
        
        reader = XMLDataReader()
        result_data = reader.read(file_path)
        
        # Проверяем что кириллица обработана корректно
        assert result_data == expected_data
        assert "Сидоров Алексей" in result_data
        assert ("программирование", 100) in result_data["Сидоров Алексей"]
        assert ("английский", 95) in result_data["Сидоров Алексей"]