#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


def get_rules(syntax='python.syntax'):  # BlaBla

    with open(syntax) as file:
        lines = [line.strip() for line in file]
        rules = {}
        for rule in lines:
            split = rule.split('"')
            reg = split[1].strip()
            _, name = split[2].split(':')
            name = name.strip()
            rules[name] = reg
        # print(rules)
    return rules


def get_color(theme='python.theme'):

    with open(theme) as file:
        lines = [line.strip() for line in file]
        colors = {}
        for color in lines:
            split = color.strip().split(':')
            c_format = split[1].strip()
            name = split[0].strip()
            colors[name] = c_format
    return colors


def check_match_in_new_regex(matchobj, line, string, code):
    gr = []

    for match in matchobj.groups():
        gr.append(match)

    for i in range(0, len(gr)):
        #print(string, gr[i])
        search_word = re.search(string, gr[i])
        # print(search_word)

        if search_word != None:
            return i
    return None


def test(matchobj, line, code):

    code_sep = code.split(' ')
    if len(code_sep) > 1:
        i = 0
        for match in matchobj.groups():
            start_code = "\033[{}m".format(code_sep[i])
            end_code = "\033[0m"
            # print(match)

            if match != None:
                line = re.sub(match, start_code + match + end_code, line)
                code_before = code_sep[i]
            i = i + 1
        return line
    else:
        start_code = "\033[{}m".format(code)
        end_code = "\033[0m"
        for match in matchobj.groups():
            line = re.sub(match, start_code + match + end_code, line)
        return line


def words_in_match(match, regex_in, color):
    words = []
    w_without = []
    start_code, end_code = color_code(color)

    for m in match:
        w_without.append(m)
        word = re.sub(regex_in, start_code + m + end_code, m)
        words.append(word)
    return words, w_without


def color_code(color):
    start_code = "\033[{}m".format(color)
    end_code = "\033[0m"
    return start_code, end_code


if __name__ == '__main__':

    # define default
    if len(sys.argv) == 1:
        #syntaxfile = 'naython.syntax'
        #themefile = 'naython.theme'
        #sourcefile = 'hello.ny'

        syntaxfile = './pythonsyntax/python2.syntax'

        themefile = './pythonsyntax/python.theme'
        sourcefile = 'test.py'
    else:
        syntaxfile = sys.argv[1]
        themefile = sys.argv[2]
        sourcefile = sys.argv[3]

    rules = get_rules(syntaxfile)
    colors = get_color(themefile)

    name = []
    reg = []
    color_format = []

    for key in rules:
        name.append(key)
        reg.append(rules[key])

    for key in colors:
        color_format.append(colors[key])
    filename = 'test.py'

    with open(filename) as file:
        lines = [line for line in file]

        a = len(lines)
        print(a)

        new_doc = []
        for line in lines:

            original_line = line

            # Define empty lists
            all_word = []
            all_char = []

            for character in line:
                all_char.append(character)
            for word in line.split():
                all_word.append(word)

            format_code = []
            match = []

            last_code = 0
            for j in range(0, len(reg)):
                search_line = re.search(reg[j], original_line)

                if search_line != None:
                    regex_in = reg[j]
                    code = (color_format[j])  # '0;32'

                    if last_code != 0 and code != last_code:
                        match = re.findall(regex_in, line)
                        words, w_without = words_in_match(
                            match, regex_in, code)
                        line_decomp = []
                        temp_line = line
                        # define last group and color:
                        find_gr = re.search(last_regex, original_line)
                        code_index = check_match_in_new_regex(
                            find_gr, original_line, regex_in,  last_code)

                        if code_index == None:
                            start_code = "\033[0m\033[{}m".format(
                                list(last_code.split())[0])
                        else:
                            start_code = "\033[0m\033[{}m".format(
                                list(last_code.split())[code_index])

                        end_code = "\033[0m"

                        for i_w in range(0, len(words)):
                            if j == len(reg)-1:
                                m_comment = re.findall(regex_in, original_line)
                                _, w_without = words_in_match(
                                    m_comment, regex_in, code)
                                # line_with color:
                                l_w_c = temp_line.split(w_without[i_w][0], 1)
                                l_without_color = original_line.split(
                                    w_without[i_w], 1)

                                if l_without_color[0] != '':
                                    comment_part = w_without[0]
                                    start, stop = color_code(code)
                                    comment_part = start + comment_part + stop
                                    uncomment_part = l_w_c[0]
                                    line_decomp.append(uncomment_part)
                                    line_decomp.append(comment_part)
                                    break

                                else:
                                    comment_part = w_without[0]
                                    start, stop = color_code(code)
                                    line_decomp.append(
                                        start + comment_part + stop)
                                    break

                            l = temp_line.split(w_without[i_w], 1)

                            if l[0] != '':
                                line_decomp.append(l[0])
                                line_decomp.append(end_code)
                                line_decomp.append(words[i_w].strip())
                                if len(l) > 1:  # l[1] != '':
                                    temp_line = l[1]
                                    line_decomp.append(start_code)
                            if i_w == len(words)-1 and len(l) > 1 and l[1] != '':
                                line_decomp.append(l[1])

                        delim = ''
                        line = delim.join(line_decomp)

                        last_code = code
                        last_regex = reg[j]
                    else:
                        name_reg = str(name[j])

                        line = test(search_line, original_line, code)
                        last_code = code
                    last_regex = reg[j]
            new_doc.append(line.strip())

         # return new_doc
    for l in new_doc:
        print(l)
