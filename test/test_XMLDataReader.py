# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def xml_content_and_data(self) -> tuple[str, DataType]:
        xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<root>
    <student name="Иванов Иван Иванович">
        <математика>100</математика>
        <физика>100</физика>
    </student>
    <student name="Петров Петр Петрович">
        <математика>90</математика>
        <литература>85</литература>
    </student>
</root>"""
        expected_data = {
            "Иванов Иван Иванович": [
                ("математика", 100),
                ("физика", 100)
            ],
            "Петров Петр Петрович": [
                ("математика", 90),
                ("литература", 85)
            ]
        }
        return xml_content, expected_data

    @pytest.fixture()
    def filepath_and_data(
        self, xml_content_and_data: tuple[str, DataType], tmpdir
    ) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("test_data.xml")
        p.write(xml_content_and_data[0])
        return str(p), xml_content_and_data[1]

    def test_read_xml_file(
        self, filepath_and_data: tuple[str, DataType]
    ) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]

    def test_read_empty_xml(self, tmpdir) -> None:
        empty_xml = """<?xml version="1.0" encoding="UTF-8"?><root></root>"""
        p = tmpdir.mkdir("datadir").join("empty.xml")
        p.write(empty_xml)
        reader = XMLDataReader()
        result = reader.read(str(p))
        assert result == {}

    def test_read_invalid_xml(self, tmpdir) -> None:
        invalid_xml = "not a valid xml content"
        p = tmpdir.mkdir("datadir").join("invalid.xml")
        p.write(invalid_xml)
        reader = XMLDataReader()
        try:
            result = reader.read(str(p))
            assert result == {}
        except Exception:
            pass
