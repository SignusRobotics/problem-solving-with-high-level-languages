### 6.1, 6.2 and 6.3
#### Package data 

Install requirements: 
```pip3 install -r requirements.txt``` 


Scripts: 
setup.py 
__init__.py 
data.py 
fitting.py
visualize.py
diabetes.csv

install package with:
    ```pip3 install . --user``` 


package 'data'

dependencies: 
pip3 install matplotlib 
pip3 install Flask 

### 6.4 and 6.5 Visualization through a web app 
scripts: 
web_visualization.py
templates/web.html
run: 
export FLASK_APP=web_visualization.py 
windows: set instead of export 

export FLASK_ENV=development 

flask run 

```python3 web_visualization.py```

Follow link ´´´http://127.0.0.1:5000/´´´ to page 


### 6.6 Documentation and help pages 
Had some issues to automatically generate the correct urls for pydoc documentation. Modified the links manually. 



```pydoc3 -w data_package/*.py``` 
```pydoc3 -b 5555``` 