# Общее описание решения
geometric_lib - проект, являющийся сборником функций для упрощения решения геометрических задач, таких как: нахождение площади и периметров геометрических фигур.

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

# Описание функций

## calculate.py : calc
Функция выводит на экран определенную характеристику заданной фигуры.

### Пример использования:
'''
$ python calculate.py
Enter figure name, available are ['circle', 'square', 'triangle']:
'''
> square
'''
Enter function name, available are ['perimeter', 'area']:
'''
> perimeter
'''
Input figure sizes separated by space:
'''
> 52
'''
Perimeter of square is 208
'''


## cirle.py : area
Функция возвращает площадь круга.

### Пример использования:
> area(4) -> 50.2654824574


## circle.py : perimeter
Фукнция возвращает длину окружности.

### Пример использования:
> perimeter(4) -> 25.132741228


## square.py : area
Функция взвращает площадь квадарата.

### Пример использования:
> area(3) -> 9


## square,py : perimeter
Функция возарщает периметр квадрата

### Пример использования:
> perimeter(4) -> 16


## triangle.py : area
Функция возвращает полупериметр треугольника.

### Пример использования:
> area(3, 4, 5) -> 6


## triangle.py : perimeter
Функция возвращает периметр треугольника.

### Пример использования:
> perimeter(3, 4, 5) -> 12


# История изменения проекта
- b5b0fae727ca72c317c383b39c0af73d6adcd81c : Update docs for calculate.py
- d76db2ac7f69cc920ae2e6F669Fb0671a7fa7d71 : Add calculate.py
- 51c40ebfd0e0b65f52fe5e54740cbb038e492db : Doc updated for triangle
- d080c7888b81955bad2ed78d58ad910526b5132a : Triangle added
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 : Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 : Circle and square added

