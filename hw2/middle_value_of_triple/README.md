## Instructions to Activate the Virtual Environment

Для активації природного середовища в цьому стилі, наступні кроки:

1. **Create the Virtual Environment**:

     ``` bash
     python -m venv myenv
     ````

2. **Activate the Virtual Environment**:

     - On Windows:
    
       ``` bash
       myenv\Scripts\activate
       ````

     - On macOS/Linux:
    
       ``` bash
       source myenv/bin/activate
       ````

3. **Install the Specific Version of `testlib`**:

     ``` bash
     pip install pytest
     ````

## MIDDLE VALUE OF TRIPLE

`control flow` `max` `min` `job interview`

### Умова

Написати функцію, яка повертатиме середнє значення трьох чисел.

* Зробіть на порівняннях, постарайтеся мінімізувати їх кількість
* Спробуйте також зробити найчитабельніший на ваш погляд варіант без використання порівнянь

### Приклад

```python
>>> get_middle_value(1, 2, 3)
2
````

### Про задачу

Це дуже спірне та популярне завдання на співбесіді.
Цитата з останнього начерку на це завдання:

> По-моєму, це якесь непристойно просте завдання на два if-а, що вона перевіряє не дуже зрозуміло.
> (співбесідний 3-го рівня)

Тим не менш, це завдання все ще питають.