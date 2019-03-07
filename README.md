## Basic unit testing examples

#### Install this repo:

`pip install -e .`

There are 3 examples in here 

    * example1 is a dead simple case of testing fizzbuzz
    * example2 is a function that has a service that is mocked
    * example3 is a simple django app that also mocks out a service

Running the tests:

```
cd example1
python -m unittest test

cd example2
python -m unittest test

cd example3
python manage.py test
```