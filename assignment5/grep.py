import argparse
import re


def color_format(color):
    start_code = "\033[{}m".format(color)
    end_code = "\033[0m"
    return start_code, end_code


def search_regex(regex, line):
    search_for_regex = re.search(regex, line)
    if search_for_regex != None:
        return True
    else:
        return False


def color_regex_in_line(line, regex, color):
    start, stop = color_format(color)
    return re.sub(regex, start + regex + stop, line)


def test(matchobj, line, color):
    start, stop = color_format(color)

    for match in matchobj.groups():
        line = re.sub(match, start + match + stop, line)
        # print(line)
    return line


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='grep')
    parser.add_argument('--sourcefile_to_search',
                        default='test.txt', help='source file')
    parser.add_argument(
        '--search_regex', default=['^\\s*(?P<def>def)\\s(.*)\\((.*)\\).*:[\\s*]?', 'from', "(?P<import>import)\s.*\s(from)\s.*\s(as).*", '#.*(?:$|\n)', 'test', '#.*(?:$|\n)', 'def', 'bla', 'import', '#',  'True'], help='source file')
    parser.add_argument('--highlight', default='true',
                        help='highlight where search is positive')

    args = parser.parse_args()
    regex = args.search_regex
    filename = args.sourcefile_to_search
    color_regex_flag = args.highlight
    if color_regex_flag == 'true':
        color_regex_flag = True
    else:
        color_regex_flag = False

    color_list = ['0;34', '0;33', '0;36', '0;35', '0;32']

    for i in color_list:
        print(color_regex_in_line('test', 'test', i))

    nr_regex = len(regex)

    color_theme = []
    for i in range(0, len(regex)):
        j = i % len(color_list)
        color_theme.append(color_list[j])

    result_list = []

    with open(filename) as file:
        lines = [line for line in file]

        for line in lines:
            i = 0
            new_line = line
            line_append_key = False

            for item in regex:
                search_line_result = search_regex(item, line)
                if search_line_result == True:
                    line_append_key = True

                    if color_regex_flag == True:
                        match = re.search(item, line)
                        # print(match)
                        new_line = test(match, new_line, color_theme[i])
                        # new_line = color_regex_in_line(
                        #    line, item, color_theme[i])

                i = i + 1
            if line_append_key == True:
                if color_regex_flag == True:
                    result_list.append(new_line)
                else:
                    result_list.append(line)

            i = 0

    for item in result_list:
        print(item)
