#!/usr/bin/env python
import json
import csv
import sys
import argparse


def main(argv):
    parser = argparse.ArgumentParser(description="GradingGorilla")
    parser.add_argument("file", help="The csv file to load")
    parser.add_argument("kt", type=int, help="The KT column")
    parser.add_argument("grade", type=int, help="The Grading column")
    args = parser.parse_args(argv)
    d = {}
    with open(args.file, "r") as f:
        reader = csv.reader(f, delimiter=";", quotechar="\"")
        for row in reader:
            d[row[args.kt]] = row[args.grade]
    tpl = ""
    with open("AssignmentTemplate.js", "r") as f:
        tpl = f.read()
    tpl = tpl.replace("/*grades*/", json.dumps(d))
    print(tpl)


if __name__ == "__main__":
    main(sys.argv[1:])


