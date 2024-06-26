## ASSERT CTR

`assert`

### Умова

#### test_check_ctr

Реалізувати функцію `test_check_ctr`, яка перевіряє, що функція `ctr` повертає коректний результат.
* Якщо так - нічого не робить.
* Якщо ні - робить assert з рядком "Wrong ctr calculation"

Функція `ctr` спеціально написана з багами, які ваш мікротест має відловити.

##### Приклад

```python
>>> test_check_ctr(2, 2, 1.0)
>>> test_check_ctr(1, 2, 0.5)
AssertionError: Wrong ctr calculation
````

#### ctr_correct_implementation

Реалізувати функцію `ctr_correct_implementation`
* Якщо кліків більше ніж показів - робить assert з рядком
"Clicks greater than shows"
* Інакше вважає CTR виходячи з документації

Зверніть увагу, що завжди потрібно повертати `float`,
тому що вихідний тип слід зберігати однаковим для будь-яких входів.

Функція `ctr_correct_implementation` - це правильно реалізована версія функції `ctr` з додаванням assert-ів.

##### Приклад

```python
>>> ctr_correct_implementation(1, 2)
0.5
>>> ctr_correct_implementation(3, 2)
AssertionError: Clicks greater than shows
````

### Про задачу

#### Предметна область

[CTR](https://ua.wikipedia.org/wiki/CTR_(Інтернет)) - сама згадувана метрика в рекламі.
Наприклад, ви серфіте інтернет і бачите рекламу ШАД 4 рази. На 4-й раз - кликаєте.
Тоді для вас ctr цієї реклами – 0.25.

Метрику можна інтерпретувати як "імовірність кліку з реклами". Тому в Яндексі часто опускають конвертацію у %.

Кліків може виявитися більшим за покази.
Наприклад, ви побачили банер 1 раз і 2 рази на ньому випадково клікнули.
У цьому випадку повторний клік часто позначають легким фродом,
  для розрахунків використовують лише 1й клік.

#### Використання assert

Юзкейзи для [assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement):
 
* у тестах

`test_check_ctr` - невеликий тест на некоректну реалізацію ctr

* для sanity check (дебагу) при розробці

Функція `ctr_correct_implementation` **завжди** буде викликатись, коли кліків <= ніж показів.
Але так як ми не впевнені, що не облажалися ніде, то тимчасово вставляємо в assert

> Важливо! Не використовуйте assert для оповіщення про реальні помилки всередині програми,
тому що ці перевірки можуть вирізати компілятором у режимі з оптимізацією