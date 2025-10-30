# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def normal_xml_content(self) -> tuple[str, DataType]:
        """Фикстура: нормальный случай с корректными данными"""
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
        """Фикстура: пустой XML файл"""
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<students>
</students>"""
        return xml_content, {}

    @pytest.fixture()
    def xml_with_special_chars(self) -> tuple[str, DataType]:
        """Фикстура: XML с кириллическими символами"""
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

    def test_read_normal_case(self, normal_xml_content, tmpdir) -> None:
        """Тест 1: Корректное чтение нормального XML файла"""
        xml_content, expected_data = normal_xml_content
        p = tmpdir.mkdir("datadir").join("normal.xml")
        file_path = str(p)
        self.write_xml_file(xml_content, file_path)
        reader = XMLDataReader()
        result_data = reader.read(file_path)
        assert result_data == expected_data
        assert len(result_data) == 2
        assert "Иванов Иван Иванович" in result_data
        assert "Петров Петр Петрович" in result_data

    def test_read_empty_file(self, empty_xml_content, tmpdir) -> None:
        """Тест 2: Чтение пустого XML файла"""
        xml_content, expected_data = empty_xml_content
        p = tmpdir.mkdir("datadir").join("empty.xml")
        file_path = str(p)
        self.write_xml_file(xml_content, file_path)
        reader = XMLDataReader()
        result_data = reader.read(file_path)
        assert result_data == expected_data
        assert len(result_data) == 0

    def test_read_with_special_chars(self, xml_with_special_chars, tmpdir):
        """Тест 3: Чтение XML с кириллицей"""
        xml_content, expected_data = xml_with_special_chars
        p = tmpdir.mkdir("datadir").join("special.xml")
        file_path = str(p)
        self.write_xml_file(xml_content, file_path)
        reader = XMLDataReader()
        result_data = reader.read(file_path)
        assert result_data == expected_data
        assert "Сидоров Алексей" in result_data
        student_data = result_data["Сидоров Алексей"]
        assert ("программирование", 100) in student_data
        assert ("английский", 95) in student_data

    def write_xml_file(self, content: str, filepath: str) -> None:
        """Вспомогательный метод для записи XML"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
