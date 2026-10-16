#!/usr/bin/env python3

import sys
import typing


if __name__ == "__main__":
    file: typing.IO[str]

    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
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

            print("\nTransform data:\n---\n")

            file = open(file_name, "r")
            lines = []
            for line in file:
                lines.append(line.rstrip("\n") + "#\n")
            new_text = "".join(lines)
            print(new_text)
            file.close()

            print("---")
            new_file = input("Enter new file name (or empty): ")

            if new_file:
                print(f"Saving data to '{new_file}'")
                file = open(new_file, "w")
                file.write(new_text)
                file.close()
                print(f"Data saved in file '{new_file}'.")
            else:
                print("Not saving data.")

        except Exception as e:
            print(f"Error opening file '{file_name}': {e}")
