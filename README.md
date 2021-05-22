# vityasa-intern-assignment
solved all the three questions for of vityasa-intern-hiring-h1-2021

# setup
1. Clone this repo into your desktop ```https://github.com/agajareiitr/vityasa-intern-assignment.git```
2. make a virtual environment using pipenv and install Django in it
3. use ```python manage.py runserver``` to runsrever
4. for Questions-1 go to ```127.0.0.1:8000/api/items``` and make a ```POST``` request with required parameters to see items
5. for Questions-2 ```booking``` go to ```127.0.0.1:8000/api/booking``` and make a ```POST or GET``` request with required parameters to book and see all bookings
6. for Questions-2 ```cancel``` go to ```127.0.0.1:8000/api/cancel``` and make a ```POST``` request with required parameters to cancel the booking
7. for Questions-3 go to ```127.0.0.1:8000/api/plot``` and make a ```POST``` request with required parameters to see if it forms a square
----
# Sample Inputs for Questions:

## 1. Question-1 POST/items
```
{
  "data":[1, 4, -1, "hello", "world", 0, 10, 7]
}
```

## 2. Question-2 POST/booking
```
{
  "slot": 2, "name": "Diana"
}
```
## 3. Question-2 POST/cancel
```
{
  "slot": 2, "name": "Akash"
}
```
## 4. Question-2 POST/plot
```
{
  "x1": 1, "y1": 1,
  "x2": 1, "y2": 6,
  "x3": 6, "y3": 1,
  "x4": 6, "y4": 6
  
}```

