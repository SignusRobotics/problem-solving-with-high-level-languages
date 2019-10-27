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
        #print(rules)
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


def color_format_comment(split_text, regex_in, line, code):

    start_code = "\033[{}m".format(code)
    end_code = "\033[0m"

    test = line.split(split_text, 1)

    if len(test) > 1:
        test2 = test[1]
    else:
        test2 = test[0]

    return re.sub(regex_in, start_code + split_text + test2 + end_code, line)


def color_format_func(regex_in,  line, code):  # Blabla
    # print(regex_in)
    start_code = "\033[{}m".format(code)
    end_code = "\033[0m"
    return re.sub(regex_in, start_code + regex_in + end_code, line)


def func_farge(matchobj):
    blue = 34
    start_def = "\033[{}m".format(blue)
    end_def = "\033[0m"

    green = 32
    start_comment = "\033[{}m".format(green)
    end_comment = "\033[0m"
    if matchobj.group(4) == None:
        match4 = ' '
    else:
        match4 = matchobj.group(4)

    pink = 31
    start_params = "\033[{}m".format(pink)
    end_params = "\033[0m"

    print(matchobj.group(1, 3, 4))
    return "{}{}{} {}({}{}{}): {}{}{}".format(
        start_def, matchobj.group(1), end_def,
        matchobj.group(2),
        start_params, matchobj.group(3), end_params,
        start_comment, match4, end_comment)


def check_match_in_new_regex(matchobj, line, string, code):
    # print(string)

    gr = []
    #start_code = "\033[{}m".format(0)
    #end_code = "\033[0m"
    #word = string
    # print(word)

    for match in matchobj.groups():
        gr.append(match)
    #print(gr)
    # print('groups')
    for i in range(0, len(gr)):
        #    gr[i]
        # print(gr[i])
        search_word = re.search(string, gr[i])
        # print(search_word)
        if search_word != None:
            # print(i)

            return i
    return None


def test(matchobj, line, code):
    #print(len(code.split(' ')))
    #code_before = 0

    code_sep = code.split(' ')
    if len(code_sep) > 1:
        i = 0
        # for i in range(0, len(code_sep)):
        #start_code = "\033[{}m".format(code_sep[i])
        #end_code = "\033[0m"
        # print(code_sep[i])
        for match in matchobj.groups():
            start_code = "\033[{}m".format(code_sep[i])
            # print(match)
            end_code = "\033[0m"
            # print(match)
            line = re.sub(match, start_code + match + end_code, line)
            #line = re.sub(match, "\033[{}m".format(code_before) + start_code + match + end_code +   "\033[0m", line)
            #line = "\033[{}m".format(code_before) + line +  "\033[0m"
            code_before = code_sep[i]
            i = i + 1
            # print(line)
        # print(code_before)
        return line
    else:
        start_code = "\033[{}m".format(code)
        end_code = "\033[0m"
        #print(line, code)
        # if len(matchobj.groups()) == 1:
        # print(matchobj.groups())
        for match in matchobj.groups():

            # print(match)
            line = re.sub(match, start_code + match + end_code, line)
        return line
    # else:
    #    return ''

def words_in_match(match, regex_in, color): 
    words = [] 
    
    w_without = []
    #print(color)
    start_code, end_code = color_code(color)
    
    for m in match:
        #print(m)
        w_without.append(m)
        word = re.sub(regex_in, start_code + m + end_code, m) 
        #print(m)
        words.append(word) 

    return words , w_without

def color_code(color): 
    #print(color)
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


#    if len(sys.argv) > 4 or len(sys.argv) < 4 :
#        sys.exit(0)

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
    # print(color_format)
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

            #if len(all_word) != 0:
            last_code = 0
            for j in range(0, len(reg)):
                #search_line = re.search(reg[j], line)
                search_line = re.search(reg[j], original_line)

                if search_line != None:
                    regex_in = reg[j]
                    code = (color_format[j])  # '0;32'

                    if last_code != 0 and code != last_code:
                        
                        # print(search_line.groups())

                        match = re.findall(regex_in, line)
                        #print(match)
              
                        #words= []
                        words, w_without = words_in_match(match, regex_in, code) 
                        
                        
                        #print(w_without)

                        line_decomp = []
                        temp_line = line
                        #print(temp_line)
                        
                        
                        #print(temp_line[0])
                        #print(line.split())
                        
                        #print(words)
                        #for w in words: 
                        
                        # define last group and color: 
                        find_gr = re.search(last_regex, original_line)
                        code_index = check_match_in_new_regex(find_gr, original_line, regex_in,  last_code) 
                        #print(code_index)
                        #print(original_line) 
                        
                        if code_index == None:  
                            start_code = "\033[0m\033[{}m".format(list(last_code.split())[0]) 
                        else: 
                            start_code = "\033[0m\033[{}m".format(list(last_code.split())[code_index]) 

                        end_code = "\033[0m"
                        
                        
                        for i_w in range(0,len(words)):
                            if j == len(reg)-1: 
                                m_comment = re.findall(regex_in, original_line)
                                _, w_without = words_in_match(m_comment, regex_in, code) 
                                # line_with color:     
                                l_w_c = temp_line.split(w_without[i_w][0],1)
                                #print(l_w_c) 
                                
                                l_without_color = original_line.split(w_without[i_w], 1)
  

                                #print(w_without)
                                if l_without_color[0] != '':
                                    #comment_part = l_without_color[0]
                                    comment_part = w_without[0] #l_without_color[1]
                                    start, stop = color_code(code) 
                                    comment_part = start + comment_part + stop
                                    #print(comment_part)

                                    #line_decomp.append(start + comment_part + stop) 
                                    uncomment_part = l_w_c[0] # l_without_color[0] 
                                    
                                    #l = uncomment_part
                                    #print(uncomment_part)
                                    line_decomp.append(uncomment_part) 
                                    line_decomp.append(comment_part) 
                                    break


                                else: 
                                    comment_part = w_without[0] #l_without_color[1]
                                    #print(comment_part)
                                    start, stop = color_code(code)
                                    line_decomp.append(start + comment_part + stop) 
                                    break 

                                    
                            l = temp_line.split(w_without[i_w],1)
                            
                            #l = temp_line.split(words[i_w],1)

                            #print(l)
                            #print(*l)
                            #print(len(l))
                            
                            if l[0] != '': 
                                line_decomp.append(l[0]) 
                                
                                #print(l[0])
                                line_decomp.append(end_code)
                                
                                #line_decomp.append(w) 
                                line_decomp.append(words[i_w].strip()) 

                                #print(w)
                                if len(l) > 1: #l[1] != '':
                                    temp_line = l[1]
                                    line_decomp.append(start_code) 
                                    

                                
                            #if w == words[len(words)-1] and len(l) > 1 and l[1] != '':  
                            if i_w == len(words)-1 and len(l) > 1 and l[1] != '':  

                                #line_decomp.append(start_code) 
                                line_decomp.append(l[1])
                                #print(*line_decomp)
                                
                                
                        
                        delim = ''
                        line = delim.join(line_decomp)
                        #print(line)
                        #line = line_decomp.strip()
                      
                        last_code = code
                        last_regex = reg[j]
                    else:
                        name_reg = str(name[j])
                        line = test(search_line, original_line, code)
                        last_code = code
                    last_regex = reg[j]
                    # if j == len(reg)-1:
                        # print(*new_line)
            new_doc.append(line.strip())

         # return new_doc
    for l in new_doc:
        print(l)
