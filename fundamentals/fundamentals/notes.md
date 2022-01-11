# python Vs JS

```js
function add(x, y){
    if(x != 5){
        return x + y;
    }
    return "Not gonna do it!"
}

console.log(add(5, 7))

function repeatAddition(a,b){
    let sum = 0
    for(let i = 0; i < b; i++){
        sum += a
    }
    return sum
}
repeatAddition(5,3)
```

```py

def add(x,y):
    if(x not 5):
        return x + y
    return "Not gonna do it!"

print(add(5, 7))

def repeatAddition(a, b):
    sum = 0
    for x in range(b):
        sum += a
    return sum

repeatAddition(5,3)
```
 # Data types

### js
 1. strings --> "  "
 2. numbers
    1. ints --> 1, 2
    2. floats--> 1.1 , 2.2
3. booleans --> true false
4. arrays --> [0,1,2,3,4]
5. objects [key: value]

### python
1. strings -> "" Or ''
2. number
    1. ints
    2. floats
3. booleans -> True or False OR 1 , 0
4. lists -> [0,1,2,3,4]
5. dict {'key': 'value'}


```js
let sum = 42
console.log(typeof sum) // return int
```

```python
sum = 42
print(type(sum)) # return number
```

## String

```js
let name = 'mike'
let age = 31

let statement =
```

```python
```

## List

- index -> integer starting at 0
- use[]
- they are mutable

```js
let arr = ['tyler', 'joe']
arr.push('curtis')
arr.pop()
```

```python
arr = ['tyler', 'joe']
arr.append('curtis')
arr.pop()
```


