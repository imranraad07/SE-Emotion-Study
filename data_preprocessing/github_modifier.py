import argparse
import csv
import sys

import data_cleaner


parser = argparse.ArgumentParser()
parser.add_argument('--output_path', type=str, required=True)
parser.add_argument('--input_file', type=str, required=True)

args = parser.parse_args()

input_file = args.input_file
output_path = args.output_path

file_directory = input_file
# id,created_at,user,comment
output_file_directory = output_path
csv.field_size_limit(sys.maxsize)

headers = []
modified_data = []

with open(file_directory) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0


    for row in csv_reader:
        if line_count == 0:
            headers = row
            line_count = line_count + 1
        else:
            org_data = row
            github_chat = str(row[3])
            current_modified_comment = data_cleaner.filter_nontext(github_chat)
            if len(str(github_chat).split()) > 1:
                modified_data.append([row[0], row[1], row[2], row[3], current_modified_comment])
    print(len(modified_data))

headers.append('modified_comment')

with open(output_file_directory, mode='w') as f:
    fwriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    fwriter.writerow(headers)
    for row in modified_data:
        fwriter.writerow(row)
