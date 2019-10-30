#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import re


def read_lines_from_file(file):
    """Read lines from file. 

    Args: 
        file (filename): inputfile

    Returns: 
        lines (str): all lines
    """
    lines = []
    f = open(file, 'r')
    lines = f.read()
    f.close()
    return lines

def check_line(o_line, modified_lines): 
    """Check one string from original file in modified document 

    Args: 
        o_line (str) : 
        modified_lines (list, str) : 
    
    Returns: 
        return placement of line in modified document if found 
    """ 
    found = False
    for i in range(0, len(modified_lines)):
        if o_line == modified_lines[i]:
            found = True
            return i

def get_modified_lines(original_lines, modified_lines):
    """Check all lines from original file in modified document 

    Args: 
        original_lines (list, str) : all lines in original lines 
        modified_lines (list, str) : all lines in modified lines
    
    Returns: 
        lines_appended (dict, str) : dictionary with keys line placement and value from modified line
    """
    lines_appended = {} 

    for m in range(0, len(modified_lines)):
        found = False
        for o in range(0, len(original_lines)):
            if modified_lines[m] == original_lines[o]: 
                found = True  
                break
                
            if o == len(original_lines)-1: 
                if found == False:  
                    lines_appended[m] = modified_lines[m]
    print("added: ", lines_appended)
    return lines_appended 

def write_result_to_file(new_doc): 
    """write all changes to txt file

    Args: 
        new_doc (list, str) : list to write to txt file
    """
    f = open('diff_output.txt', 'w')  
    for i in new_doc: 
        f.write(i +'\n') 

    f.close()

def new_doc_list(original_lines,modified_lines):
    """Check all lines from original file in modified document 

    Args: 
        original_lines (list, str) : all lines in original lines 
        modified_lines (list, str) : all lines in modified lines
    
    Returns: 
        lines_new (list, str) : list of all lines from modified and original file, 
        with a + if added, - if deleted from original_file and 0 if not changed
    """ 
    lines_appended = {} 
    lines_new = []
    last_m = 0

    for o in range(0, len(original_lines)):
        found = False
        for m in range(0, len(modified_lines)): 
            
            if original_lines[o] == modified_lines[m] : 
                found = True  
                diff = m-last_m 
                diff_abs = abs(diff) 
                if diff > 1:
                    for i in range(m-diff_abs,m): 
                        lines_new.append('+'+modified_lines[i]) 
                lines_new.append('0'+modified_lines[m]) 

                last_m = m 
                last_o = o 
                break
                
            if m == len(modified_lines)-1: 
                if found == False:  
                    lines_appended[m] = modified_lines[m] 
                    lines_new.append('-'+original_lines[o])
    return lines_new 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='grep')
    parser.add_argument('--sourcefile_original',
                        default='A.txt', 
                        help='source file original')
    parser.add_argument('--sourcefile_modified',
                        default='B.txt', 
                        help='source file modified')

    args = parser.parse_args()
    originalfile = args.sourcefile_original
    modifiedfile = args.sourcefile_modified

    txt = read_lines_from_file(originalfile)

    original_lines = txt.split('\n')
    print("original: ", original_lines) 

    m_txt = read_lines_from_file(modifiedfile)

    modified_lines = m_txt.split('\n')
    print("modifisert: ", modified_lines)

    last_line = ''
    i = 0

    new_doc = [] 

    
    a = get_modified_lines(original_lines,modified_lines) 
    # going through all lines in original_file
    for l in (original_lines):
        if check_line(l, modified_lines) != None:
            new_doc.append('0' + l)
        else:
            new_doc.append('-' + l)
            # remember index and line in original file
        last_line = l
        i = i + 1
    
    for j in a.values()	: 
        new_doc.append('+'+j)
    
    
    for keys in a.keys(): 
        number = keys 
    
    new_doc = new_doc_list(original_lines,modified_lines) 
    for keys in a.keys(): 
        new_doc.append('+'+a[keys])

    print(new_doc) 
    print("modifications", new_doc)
    write_result_to_file(new_doc)