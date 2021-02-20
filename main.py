""" Module for navigating through .json files """

import json
from pprint import pprint


def read_file(path: str) -> dict:
    """
    Reads a .json file and converts it to a dictionary.
    """
    with open(path, 'r') as data:
        info_dict = json.load(data)

    return info_dict


def parse_info(info: object):
    """
    Function that navigates user in the .json file.
    """
    messages = {
        'dict_msg': 'Here are the keys of the dictionary, enter the key to get its value. Keys:',
        'list_msg': '\nThe object is a list, please enter the id of the element you want to get.\n',
        'list_note': 'NOTE! THE INDEXING STARTS FROM 1',
        'key_err': 'Check the key, you\'ve enetered, it seems that you\'ve misspelled it.\n',
        'value_err': 'Please, enter an integer value\n',
        'id_err': 'The index you\'ve entered is out of the range of the list(\n'
    }

    while True:

        if isinstance(info, dict):
            print(messages['dict_msg'])
            pprint(list(info.keys()))
            usr_key = input('Enter the key: ')
            try:
                info = info[usr_key]
            except KeyError:
                print(messages['key_err'])

        elif isinstance(info, list):
            print(messages['list_msg'], f'Length of the list: {len(info)}')
            print(messages['list_note'])
            usr_list_id = input('Enter the list id: ')

            try:
                info = info[int(usr_list_id) - 1]
            except ValueError:
                print(messages['value_err'])
            except IndexError:
                print(messages['id_err'])

        else:
            return info


def main(path: str) -> object:
    """
    Main function of the module.
    """
    info = read_file(path)
    return parse_info(info)


if __name__ == '__main__':
    try:
        path = input('Please enter path to the .json file:\n')
        print(main(path))
    except FileNotFoundError:
        print(f'Looks like there is no such file as {path}...')