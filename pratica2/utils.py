from bson import json_util


def verify_messages(result):
    if result:
        print("Success!")
    else:
        print("Error!")

def read_doc_bson(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(json_util.loads(line))
    return data

def dump_result(result):
    return json_util.loads(json_util.dumps(result))

def print_map(title, result):
   print(title)
   for key in result:
      print(f" -> {key} - {result[key]}")
