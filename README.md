# mercury
A multi-processing communication wrapper using redis PUB/SUB

## Usage
```python
import mercury

mercury_app = mercury.MercuryApp()

# The first purpose is to conveniently communicate with other mercury clients.
mercury_app.subscribe(target="")

``` 

## Mercury Monitor
```python
import mercury.monitor


```