### Instructions to Activate the Virtual Environment

To activate the virtual environment in this folder, follow these steps:

1. **Create the Virtual Environment**:

    ```bash
    python -m venv myenv
    ```

2. **Activate the Virtual Environment**:

    - On Windows:
    
      ```bash
      myenv\Scripts\activate
      ```

    - On macOS/Linux:
    
      ```bash
      source myenv/bin/activate
      ```

3. **Install the Specific Version of `testlib`**:

    ```bash
    pip install pytest
    ```



## FizzBuzz question

`control flow` `range` `list` `%` `job interview`

### Умова

Повернути список чисел від 1 до n. При цьому замість чисел, кратних трьох, там має бути слово "Fizz",
а замість чисел, кратних п'яти - слово "Buzz". Якщо число кратне і 3, і 5, замість них має бути слово " FizzBuzz " .

* Постарайтеся написати найпростіший і читабельніший варіант рішення
* Постарайтеся написати завдання за 5 хвилин і з першого разу
* Якщо будуть проблеми з `mypy` через несумісність `int` та `str`,
то вам допоможе задати для нового списку тип:
````
fizz_buzz_list: List[Union[int, str]] = []
````

### Приклад

```python
In [1]: from fizz_buzz.fizz_buzz import get_fizz_buzz

In [2]: get_fizz_buzz(3)
Out[2]: [1, 2, "Fizz"]
````

### Про задачу

Класичне завдання, ім'я якого стало загальним - "FizzBuzz question".

Вона використовується для попередніх співбесід. Попередні співбесіди потрібні тому, що
> the fact that 199 out of 200 applicants for every programming job can't write code at all

І як то кажуть в одній статті про успіхи у вирішенні:
> The majority of comp sci graduates може бути.
> I've also seen self-proclaimed senior programmers таке more than 10-15 minutes to write a solution.

У реальних завданнях повертати список із елементами різних типів – антипаттерн.
Намагайтеся так не робити у своєму продакшен коді.