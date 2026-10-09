#!/usr/bin/env python3

import sys
import typing


if __name__ == "__main__":
    file: typing.IO[str]

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Acessing file '{sys.argv[1]}'")
        file_name = sys.argv[1]
        try:
            file = open(file_name)
            print("---\n")
            content = file.read()
            print(content)
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed.")

            print("Transform data:\n---\n")
            file = open(file_name, "r")
            file.write("#")
            content = file.read()
            print(content)
            file.close()
        except Exception as e:
            print(f"Error opening file '{file_name}': {e}")
