#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import re


def read_lines_from_file(file):
    """Read line form file. 

    Args: 
        file (filename): inputfile

    Returns: 
        line (str): all lines
    """
    lines = []
    f = open(file, 'r')
    lines = f.read()
    f.close()
    return lines


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


def check_line(o_line, modified_lines):
    found = False
    for i in range(0, len(modified_lines)):
        if o_line == modified_lines[i]:
            found = True
            return i


# trekker ut det som er igjen, + :
def get_modified_lines(original_lines, modified_lines):

    # potensial appended lines: 
    #p = len(modified_lines) - len(original_lines)
    #print(p) 

    lines_appended = {} 


    for m in range(0, len(modified_lines)):
        found = False

        for o in range(0, len(original_lines)):

            #print(found)

            if modified_lines[m] == original_lines[o]: 
                found = True  

                #print( modified_lines[m],original_lines[o])
                break
                
            if o == len(original_lines)-1: 
                #print( modified_lines[m],original_lines[o])
                #print(found)

                if found == False:  

                    #print('modified line new', modified_lines[m])
                    lines_appended[m] = modified_lines[m]
                    #lines_appended.append(modified_lines[m], m)
    #print(lines_appended) 
    print("added: ", lines_appended)
    return lines_appended 

def check_lines_in_new_doc(): 
    pass 


def new_doc_list(original_lines,modified_lines):

    lines_appended = {} 
    lines_new = []
    last_m = 0

    for o in range(0, len(original_lines)):
        found = False
        for m in range(0, len(modified_lines)): 
            
            if original_lines[o] == modified_lines[m] : 
                found = True  
                #print(o,m)
                diff = m-last_m 
                #print(diff)
                diff_abs = abs(diff) 
                #print(m-last_m)

                #print("lines modified from last check", diff_abs) 

                if diff > 1:
                    for i in range(m-diff_abs,m): 
                        #lines_appended[i] = modified_lines[i] 
                        #print(i)
                        lines_new.append('+'+modified_lines[i]) 
                lines_new.append('0'+modified_lines[m]) 
                    

                last_m = m 
                last_o = o 

                
            
                

                #print( modified_lines[m],original_lines[o])
                break
            
                
            if m == len(modified_lines)-1: 
                #print( modified_lines[m],original_lines[o])
                #print(found)
                if found == False:  

                    #print('modified line new', modified_lines[m])
                    lines_appended[m] = modified_lines[m] 
                    lines_new.append('-'+original_lines[o])
                    
                    #lines_appended.append(modified_lines[m], m)
    return lines_new 




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='grep')
    parser.add_argument('--sourcefile_original',
                        default='A.txt', help='source file original')
    parser.add_argument('--sourcefile_modified',
                        default='B.txt', help='source file modified')

    args = parser.parse_args()
    originalfile = args.sourcefile_original
    modifiedfile = args.sourcefile_modified

    txt = read_lines_from_file(originalfile)

    #print(txt.split('\n'))
    original_lines = txt.split('\n')
    print("original: ", original_lines) 

    m_txt = read_lines_from_file(modifiedfile)

    modified_lines = m_txt.split('\n')
    #print(modified_lines)
    print("modifisert: ", modified_lines)

    last_line = ''
    i = 0

    new_doc = [] 

    a = get_modified_lines(original_lines,modified_lines) 
    #print(a)

    # going through all lines in original_file
    for l in (original_lines):
        if check_line(l, modified_lines) != None:
            #print(check_line(l, modified_lines))
            #print("line is modified")

            new_doc.append('0' + l)
        else:
            #print("line is deleted")
            new_doc.append('-' + l)

            # remember index and line in original file
        last_line = l
        i = i + 1
    
    for j in a.values()	: 
        new_doc.append('+'+j)
    
    
    #print(len(original_lines)-1)
    for keys in a.keys(): 
        number = keys 
        #print(number)

        #if len(original_lines)-2 < number: 
        #    print(number)

    new_doc = new_doc_list(original_lines,modified_lines) 
    #for j in a.values()	: 
    for keys in a.keys(): 
        #if keys > len(original_lines):
#           new_doc.append('+'+j)
        new_doc.append('+'+a[keys])

    #print(new_doc) 
    print("modifications", new_doc)
