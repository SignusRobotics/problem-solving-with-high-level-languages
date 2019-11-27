### Package  

Scripts: 
setup.py 
__init__.py 

install package with:
    pip3 install . --user

package 'data'

dependencies: pip3 install matplotlib pip3 install Flask 

### 6.4 and 6.5 Visualization through a web app 

run: 
export FLASK_APP=web_visualization.py 
windows: set instead of export 

export FLASK_ENV=development 

flask run 

Follow link ´´´http://127.0.0.1:5000/´´´ to page 



### 6.6 Documentation and help pages 

```pydoc3 -w data``` 
```pydoc -b 5555``` 