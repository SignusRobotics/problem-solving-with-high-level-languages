#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

def get_rules(syntax='python.syntax'): 
    """Fetch regex from syntax file. 

    Args: 
        syntax (file) : Syntax file with regex 
    
    Returns: 
        rules (dict) : Returns a dictionary with names as keys and regex as values. 
    """
    with open(syntax) as file:
        lines = [line.strip() for line in file]
        rules = {}
        for rule in lines:
            split = rule.split('"')
            if len(split) == 3:
                reg = split[1].strip()
                _, name = split[2].split(':')
                name = name.strip()
                rules[name] = reg
            else: 
                a = len(split) 
                delim = '"'
                reg2 = delim.join(split[1:a-1])  
                reg = reg2.strip()
                _, name = split[a-1].split(':')
                name = name.strip()
                rules[name] = reg
    return rules


def get_color(theme='python.theme'):
    """Fetch colors from theme file. 

    Args: 
        theme (file) : Theme file with colors 
    
    Returns: 
        colors (dict) : Returns a dictionary with names as keys and format of colors as values. 
    """

    with open(theme) as file:
        lines = [line.strip() for line in file]
        colors = {}
        for color in lines:
            split = color.strip().split(':')
            c_format = split[1].strip()
            name = split[0].strip()
            colors[name] = c_format
    return colors


def check_match_in_new_regex(last_regex, line, string, code): 
    """Take a last_regex from a regex and a line and extract the color index. 

    Args: 
        last_regex (regex_code): the last regex that was found in the current line  
        line (str): original_line without formatting 
        string (str): the current regex 
        code (color_code) : last matched regex color format 

    Returns: 
        the color index in last codes list 
    """ 
    find_gr = re.search(last_regex, line)

    gr = []

    for match in find_gr.groups():
        gr.append(match)

    for i in range(0, len(gr)):
        search_word = re.search(string, gr[i])
        
        if search_word != None:
            return i
    return None


def color_matches(matchobj, line, code):
    """Returns colored line with correct color formatting if more than one color.  

    Args: 
        matchobj (object of matches) : the current lines matches for the current regex 
        line (str) : line that is colored 
        code (color_code) : code for the correct color  
    
    Returns: 
        colored line (str) 
    """
    code_sep = code.split(' ')
    if len(code_sep) > 1:
        i = 0
        for match in matchobj.groups(): 
            start_code, end_code = color_code(code_sep[i])

            if match != None:
                line = re.sub(match, start_code + match + end_code, line)
            i = i + 1
        return line
    else:
        start_code, end_code = color_code(code)
        for match in matchobj.groups(): 
            line = re.sub(match, start_code + match + end_code, line)
        return line

def words_in_match(line, regex_in, color): 
    """Find all matches with and without colors. 

    Args: 
        line (str): the search object 
        regex_in (pattern) : search pattern 
        color (color_code) : coloring format in a list 
    
    Returns: 
        words (list, str): list of words with colorformatting 
        w_without (list, str) : list of words without colorformatting 
    """
    words = []
    w_without = [] 
    
    match = re.findall(regex_in, line)
    start_code, end_code = color_code(color)

    for m in match:
        w_without.append(m)
        word = re.sub(regex_in, start_code + m + end_code, m)
        words.append(word)
    return words, w_without


def color_code(color): 
    """start and stop for the given color code. 

    Args: 
        color (color_code) : coloring format 

    Returns: 
        start_code : color format string start 
        stop_code : color format string stop        
    """
    start_code = "\033[{}m".format(color)
    end_code = "\033[0m"
    return start_code, end_code

def highlighter_function(rules, colors, sourcefile_to_color, match_filter=False): 
    """Highlights the regex that matches the line with given color code 

    Args: 
        rules (dict) : dictionary with name of the regex (value) 
        colors (dict) : dictionary with name of the colors (value) 
        sourcefile_to_color (file) : the file to search in 

    Returns: 
        new_doc (list of str) : All lines from the sourcefile with color formatting where matches occure. 
     """ 
    name = []
    reg = []
    color_format = []

    for key in rules:
            name.append(key)
            reg.append(rules[key])

    for key in colors:
        color_format.append(colors[key])

    with open(sourcefile_to_color) as file:
        lines = [line for line in file]
        new_doc = []
        for line in lines:
            original_line = line         
            match = []
            last_code = 0
            found = False
            for j in range(0, len(reg)):
                search_line = re.search(reg[j], original_line)
                if search_line != None:
                    found = True 
                    regex_in = reg[j]
                    code = (color_format[j])  
                    
                    if last_code != 0 and code != last_code:
                        words, w_without = words_in_match(
                            line, regex_in, code)
                        line_decomp = []
                        temp_line = line
                        # define last group and color:
                        code_index = check_match_in_new_regex(
                            last_regex, original_line, regex_in,  last_code)
                        if code_index == None:
                            start_code = "\033[0m\033[{}m".format(
                                list(last_code.split())[0])
                        else:
                            start_code = "\033[0m\033[{}m".format(
                                list(last_code.split())[code_index])
                        end_code = "\033[0m"
                        for i_w in range(0, len(words)):
                            if j == len(reg)-1:
                                _, w_without = words_in_match(
                                    original_line, regex_in, code)
                                # line_with color:
                                l_with_color = temp_line.split(w_without[i_w][0], 1)
                                l_without_color = original_line.split(
                                    w_without[i_w], 1)

                                if l_without_color[0] != '':
                                    comment_part = w_without[0]
                                    start, stop = color_code(code)
                                    comment_part = start + comment_part + stop
                                    uncomment_part = l_with_color[0]
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
                                if len(l) > 1:  
                                    temp_line = l[1]
                                    line_decomp.append(start_code)
                            if i_w == len(words)-1 and len(l) > 1 and l[1] != '':
                                line_decomp.append(l[1])

                        delim = ''
                        line = delim.join(line_decomp)
                    else:
                        line = color_matches(search_line, line, code)
                        
                    last_code = code
                    last_regex = reg[j] 
            if match_filter == True and found == True:         
                new_doc.append(line.strip())
            if match_filter == False:          
                new_doc.append(line.strip())

        return new_doc

if __name__ == '__main__':
    if len(sys.argv) == 1:
        syntaxfile = 'pythonsyntax/python.syntax'
        themefile = './pythonsyntax/python.theme'
        sourcefile_to_color = 'test.py'
    else:
        syntaxfile = sys.argv[1]
        themefile = sys.argv[2]
        sourcefile_to_color = sys.argv[3]

    rules = get_rules(syntaxfile)
    colors = get_color(themefile)
    
    new_doc = highlighter_function(rules, colors, sourcefile_to_color)
    
    for l in new_doc:
        print(l)