# deimport
A simple package to "deimport" already imported python packages.





## Installing using PyPi:
`pip install deimport`
## Usage
```python
from deimport.deimport import deimport
deimport(foo,verbose=True)
```
## Limitations:
deimport removes the module and its submodules from the globals and sys.modules. sometimes that trips the python module loading cache. if that happens all you have to do is something like :
```python
try:
  import foo
except:
  import foo
```
