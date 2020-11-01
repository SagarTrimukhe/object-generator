import random
import string
import json
import configparser
import sys

config = configparser.ConfigParser()
config.read('config.ini')

# Inputs from user
input_json_file = open('input.json')

sample_input_obj = json.loads(input_json_file.read())

required_string_len = int(config['LENGTH']['String'])
required_int_len = int(config['LENGTH']['Integer'])


def get_element_type(element):
    if type(element) == type("string"):
        return "string"
    elif type(element) == type(123):
        return "int"
    elif type(element) == type(True):
        return "bool"
    elif type(element) == type([]):
        return "list"
    elif type({}) == type(element):
        return 'dict'


# generates a random string 'a-z' of given length
def random_string_gen(length):
    result = ''
    for x in range(length):
        result = result + random.choice(string.ascii_letters)

    return result


# generates a random number '0-9' of given length
def random_integer_gen(length):
    result = ''
    for x in range(length):
        result = result + random.choice(string.digits)

    return int(result)


# generates either True or False boolean value
def random_boolean_gen():
    return random.choice([True, False])


def random_array_gen(sample_arr, string_len=required_string_len):
    result = []
    arr_len = len(sample_arr)
    element_type = get_element_type(sample_arr[0])

    if element_type == 'string':
        for i in range(arr_len):
            result.append(random_string_gen(string_len))

    elif element_type == 'int':
        for i in range(arr_len):
            result.append(random_integer_gen(string_len))

    elif element_type == 'dict':
        for i in range(arr_len):
            result.append(random_objects_generator(sample_arr[0]))

    return result


def random_objects_generator(sample_obj, string_len=required_string_len, int_len=required_int_len):
    new_obj = {}
    obj_keys = sample_obj.keys()
    for k in obj_keys:
        element_type = get_element_type(sample_obj[k])
        if element_type == 'string':
            new_obj[k] = random_string_gen(string_len)
        elif element_type == 'int':
            new_obj[k] = random_integer_gen(int_len)
        elif element_type == 'bool':
            new_obj[k] = random_boolean_gen()
        elif element_type == 'list':
            new_obj[k] = random_array_gen(sample_obj[k])
        elif element_type == 'dict':
            new_obj[k] = random_objects_generator(sample_obj[k])

    return new_obj


def main(required_num_of_obj):
    output_arr = []

    for i in range(required_num_of_obj):
        output_arr.append(random_objects_generator(sample_input_obj))

    file = open('output.json', 'w')
    file.write(json.dumps(output_arr))
    file.close()

if __name__ == '__main__':
    try:
        main(int(sys.argv[1]))
    except Exception as e:
        print(e)
        print("Please pass the number of objects required.")
        print("Usage: python object-generator <number of obj required>")
        print("Eg: python object-generator 10")

