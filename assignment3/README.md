# README 

### wc.py 
Consideration: a character also containing spaces between words. 

Defined in the script: 
#!/usr/bin/env python

$ chmod a+x wc.py 


run with: 

$ wc [arg]

arg: * : all documents in the folder. 
    *.py :  all python scripts. All files of the same type.

Output example: 

```
  163   588  5347 complex.py
  249   663  5770 test_complex.py
   60   155  1184 wc.py
  472  1406 12301 total
```

### test_complex.py 

All tests have been executed with pytest using the Python extension in Visual Studio Code on Windows 10. Was not able to install pytest in Ubuntu using WSL (Windows subsystem for Linux). ```.vscode/settings.json``` for pytest configuration.

Has followed red green principle for writing the code and tests. I have never done that before, but it was really helpful when implemeting especially the "__r" methods.

### complex.py 

Implemented by using red green test workflow. Solved by only testing with int, not float, but implemented support for both.

