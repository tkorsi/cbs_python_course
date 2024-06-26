## REVERSE LIST

`control flow` `iteration` `list` `len` `job interview``reversed``slicing``unpacking`

### Умова

Написати п'ять функцій.

**1.** `reverse_iterative` - бере список і **повертає новий** список, де елементи у зворотному порядку

* **Використовуйте тільки ітерацію**
* Не змінюйте вхідні списки всередині функції. На що це впливає і чому так не треба робити - поговоримо на наступній лекції
* Оцініть складність за часом і пам'яті - у вас має вийде О(n) та O(n)

**2.** `reverse_inplace_iterative` - **оновлює** переданий список так, щоб там елементи були у зворотному порядку

* **Використовуйте тільки ітерацію**
* Зверніть увагу, що вам не потрібно йти для цього по всьому списку
* Оцініть складність за часом та пам'яті - у вас має вийде О(n) та O(1)

**3.** `reverse_inplace` - **оновлює** переданий список так, щоб там елементи були у зворотному порядку

* **Використовуйте лише метод [`reverse()`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) у списку**

**4.** `reverse_reversed` - бере список і **повертає новий** список, де елементи у зворотному порядку

* **Використовуйте функцію `reversed`**
* Зверніть увагу, що результат роботи `reversed` потрібно ще привести до `list`

**5.** `reverse_slice` - бере список і **повертає новий** список, де елементи у зворотному порядку

* **Використовуйте слайси**


### Про задачу

Це завдання - це перше, що спливає в пам'яті при згадці скринінгових секцій.
> Знову завдання типу "Розгорни список" даватимуть, пф!
 
Вона всіх дратує, бо коротка і всім відома.
Але якщо відома, то вже на пітоні за 30 секунд треба її вміти писати =)

На секції у цьому випадку цікавлять перші дві реалізації.

Останні три реалізації - це pythonic way для того ж завдання. Спочатку їх у цій хаті не було,
але багато знайомих з пітон все одно намагалися ними скористатися. Давайте тоді все про них дізнаємось :)