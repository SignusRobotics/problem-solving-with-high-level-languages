# README 
assignment5 folder: 
## 5.1 highlighter.py  

Defined in the script: 
#!/usr/bin/env python 

### Usage: 
Search through a given sourcefile with given syntax file and themefile. 

run alone with: 

```python3 highlighter.py [syntaxfile] [themefile] [sourcefile_to_color]```

Example:

```python3 highlighter.py ./pythonsyntax/python.syntax ./pythonsyntax/python.theme test.txt```


## 5.2 python.syntax, python.theme, python2.theme  

Syntax and color code for different python syntaxes. 
python.syntax is structured with the most spesific regexes listed first like function and class definitions. And True/False/None 

The comment is a special case for highlighter.py and is therefore always dependent to be listed as the last regex. 

Some of the regex have more than one regex to catch all variations. An example is the import statement. The first searches for the combinations of ```import .. from .. as ..``` and the other only for ```import ..```

The color.theme have color code for each regex in the syntax file. If there is more than one group the colors are given as a list of different colors. 

### Usage: 
Can be used with highlighter.py with a sourcefile. 

A demo can be found by running this:  

```python3 highlighter.py ./pythonsyntax/python.syntax ./pythonsyntax/python.theme test.txt```

## 5.3 favorite_language.syntax and favorite_language.theme 

Same as for 5.2 
I have used C as language. 

### Usage: 

A demo can be found by running this:  

```python3 highlighter.py favorite_language.syntax favorite_language.theme test.c```  


## 5.4 grep.py 
Searching for a list of regex, and outputs the lines that is found. 

It is possible to give a arg that specify if the results also are going to be colored. 

### Usage: 

```python3 grep.py --sourcefile_to_search [list of regex] highlight = [true/false]```

A demo can be found running this: 

```python3 grep.py --sourcefile_to_search test.txt --search_regex '^\s*(?P<def>def)\s(.*)\((.*)\).*:[\s*]?' '(["].*["])' '^\s*(import|from)\s\w*[\s]?(as|from)?\s\w*[\s]?(as)?\s\w*[\s*]?' '#.*(?:$|\n)' --highlight=true```

## 5.5 diff.py 

Give each line a +, - or 0. Dependent of the lines status of beign added, deleted or not changed. 

Result is saved in a file named diff_output.txt 

### Usage: 

python3 diff.py --sourcefile_original = [original file] --sourcefile_modified = [modified file] 

A demo can be found: 
```python3 diff.py --sourcefile_original=A.txt --sourcefile_modified=B.txt```

## 5.6 diff.syntax and diff.theme 
Searching for + and - in beginning of each line in a file that have been run with diff.py. 

Had some problems with encoding and/or escaping the + symbols in the regex, therefore I use another symbol (&) to show the potential output: 

```python3 highlighter.py diff.syntax diff.theme diff_output2.txt``` 
