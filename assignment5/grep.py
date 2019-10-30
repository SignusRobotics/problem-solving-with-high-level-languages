#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import re
import highlighter as h

def get_lines(filename, regex): 
    """Fetch lines from source file.  

    Args: 
        filename (file) : search file 
        regex (regex code) : list of regex 
    
    Returns: 
        new_list (list) : Returns a list of lines where match found 
    """

    new_list = [] 
        
    with open(filename) as file: 
        lines = [line for line in file] 
        for line in lines: 
            match = False 
            for j in range(0, len(regex)):
                search_line = re.search(regex[j], line)
                if search_line != None: 
                    match = match_search(regex[j], line)
                
            if match == True:             
                new_list.append(line.strip())
    return new_list 

def match_search(regex, line): 
    """Search regex in string 

    Args: 
        regex (regex pattern) : search pattern 
        line (str) : source to search
    
    Returns: 
        boolean value 
    """ 
    search_for_regex = re.search(regex, line)
    if search_for_regex != None:
        return True
    else:
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='grep')
    parser.add_argument('--sourcefile_to_search',
                        default='test.txt', 
                        help='source file')

    parser.add_argument('--highlight', 
                        default='true', 
                        choices=['true','false'],
                        help='highlight where search is positive')
    parser.add_argument('--search_regex', 
                        type=str, 
                        nargs="*", 
                        default=[
                            '^\s*(?P<def>def)\s(.*)\((.*)\).*:[\s*]?','(["].*["])',
                            '^\s*(import|from)\s\w*[\s]?(as|from)?\s\w*[\s]?(as)?\s\w*[\s*]?',
                            '#.*(?:$|\n)'], 
                        help='regex to search for')

    args = parser.parse_args()
    regex = args.search_regex
    print(regex)
    filename = args.sourcefile_to_search
    color_regex_flag = args.highlight
    
    if color_regex_flag == 'true':
        color_regex_flag = True
    else:
        color_regex_flag = False

    color_list = ['0;34', '0;33', '0;36', '0;35', '0;32']

    nr_regex = len(regex)

    color_theme = {}
    for i in range(0, len(regex)):
        j = i % len(color_list)
        color_theme[i] = color_list[j]
    regex_dict = {}
    
    for i in range(0, len(regex)):
        regex_dict[i] = regex[i]

    result_list = [] 

    if color_regex_flag == True:
        result_list = h.highlighter_function(regex_dict, color_theme, filename, match_filter = True) 
    else: 
        result_list = get_lines(filename, regex) 

    for item in result_list:
        print(item)