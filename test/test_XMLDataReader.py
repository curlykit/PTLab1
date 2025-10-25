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
        <subject1>100</subject1>
        <subject2>100</subject2>
    </student>
    <student name="Петров Петр Петрович">
        <subject1>90</subject1>
        <subject2>85</subject2>
    </student>
</root>"""

        expected_data = {
            "Иванов Иван Иванович": [
                ("subject1", 100),
                ("subject2", 100)
            ],
            "Петров Петр Петрович": [
                ("subject1", 90),
                ("subject2", 85)
            ]
        }
        return xml_content, expected_data
