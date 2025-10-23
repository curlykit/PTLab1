# -*- coding: utf-8 -*-
import argparse
import sys
from src.CalcRating import CalcRating
from src.TextDataReader import TextDataReader
from src.XMLDataReader import XMLDataReader
from src.FindPerfectStudent import FindPerfectStudent


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    parser.add_argument("-f", dest="format", type=str, default="text",
                        help="File format: text or xml")
    args = parser.parse_args(args)
    return args.path, args.format


def main():
    path, file_format = get_path_from_arguments(sys.argv[1:])
    
    if file_format == "xml":
        reader = XMLDataReader()
    else:
        reader = TextDataReader()
        
    students = reader.read(path)
    print("Students: ", students)
    
    # Расчет рейтинга
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    
    # Поиск идеального студента
    perfect_finder = FindPerfectStudent(students)
    perfect_student = perfect_finder.find()
    print("Perfect student: ", perfect_student)


if __name__ == "__main__":
    main()
    