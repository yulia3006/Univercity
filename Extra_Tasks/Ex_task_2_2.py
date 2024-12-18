{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yulia3006/Univercity/blob/main/Extra_Tasks/Ex_task_2_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Дополнительное задание №2.2. Замыкания. Декораторы. Итераторы. Генераторы**"
      ],
      "metadata": {
        "id": "AFKOdzjAKWYc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**БАЗА:**\n",
        "\n",
        "- **Замыкания** позволяют создавать функции с сохраняющимся состоянием. Это полезно для создания фабричных функций и функций с настраиваемым поведением.\n",
        "- **Декораторы** позволяют модифицировать или расширять поведение функций без изменения их исходного кода."
      ],
      "metadata": {
        "id": "nBwTqfsSyaGg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "2VnR8e3twGfD"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **I. Замыкания и декораторы**"
      ],
      "metadata": {
        "id": "_ZPLUks08b1-"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "eVsLMeozyshu"
      },
      "source": [
        "### **Пункт №1**\n",
        "\n",
        "Напишите две функции создания списка из чётных чисел от 0 до N (N – аргумент функции): \\([0, 2, 4, ..., N]\\).\n",
        "\n",
        "- **Первая функция** должна использовать метод `append` для добавления элементов в список.\n",
        "- **Вторая функция** должна использовать **генератор списков** (list comprehensions) для создания списка.\n",
        "\n",
        "После этого, через **декоратор**, определите время работы этих функций."
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "\n",
        "def timeTest(function):\n",
        "  def inner_func(*args):\n",
        "    st=time.time()\n",
        "    function(*args)\n",
        "    et=(time.time()-st)\n",
        "    print (f'Время выполнения  кода {et:.10f}')\n",
        "    return function(*args)\n",
        "  return inner_func\n",
        "\n",
        "@timeTest\n",
        "def first_func(n):\n",
        "  massive=[]\n",
        "  for value in range(0,n,2): massive.append(value)\n",
        "  return massive\n",
        "\n",
        "@timeTest\n",
        "def second_func(n):\n",
        "  return [value for value in range(0,n,2)]\n",
        "\n",
        "\n",
        "n=int(input('Введите значение аргумента '))\n",
        "print(first_func(n))\n",
        "print(second_func(n))"
      ],
      "metadata": {
        "id": "04AwDHUyZe6F",
        "outputId": "07917661-4dea-45a0-dfab-75af89b418aa",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Введите значение аргумента 5\n",
            "Время выполнения  кода 0.0000045300\n",
            "[0, 2, 4]\n",
            "Время выполнения  кода 0.0000045300\n",
            "[0, 2, 4]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "_0Jy4QhEwGDd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Пункт №2**\n",
        "\n",
        "Напишите **декоратор** для кэширования результатов работы функции, вычисляющей значение n-го числа [**ряда Фибоначчи**](https://ru.wikipedia.org/wiki/Числа_Фибоначчи).\n",
        "\n",
        "То есть, при повторном вызове функции через декоратор уже имеющийся результат должен браться из кэша, а не вычисляться заново.\n",
        "\n",
        "**Например:**\n",
        "\n",
        "- При значении параметра `n = 5`, должна кэшироваться последовательность \\([0, 1, 1, 2, 3, 5]\\).\n",
        "- Вызывая после этого целевую функцию через декоратор ещё раз с `n = 3`, результат \\([0, 1, 1, 2]\\) должен браться из кэша.\n",
        "- Если последующее значение `n` больше предыдущего, например `n = 10`, вычисление должно продолжаться, начиная с закэшированной последовательности.\n",
        "\n",
        "*Подсказка: используйте **замыкание** для хранения кэша внутри декоратора.*\n"
      ],
      "metadata": {
        "id": "DfDtOSmDl7ic"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def cache_func(func):\n",
        "  cache={}\n",
        "  def inner(n):\n",
        "    if n<1: return None\n",
        "    if n in cache: return cache[n]\n",
        "    cache[n] = func(n)\n",
        "    return cache[n]\n",
        "  return inner\n",
        "\n",
        "@cache_func\n",
        "def fibonacci(n):\n",
        "    if n==1 or n==2: return 1\n",
        "    return fibonacci(n - 1) + fibonacci(n - 2)\n",
        "\n",
        "print(fibonacci(300))\n",
        "print(fibonacci(365))"
      ],
      "metadata": {
        "id": "CtbbsIBsZfHB",
        "outputId": "6c3d94af-20ce-49c8-fac5-232b34fc74a1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "222232244629420445529739893461909967206666939096499764990979600\n",
            "8531073606282249384383143963212896619394786170594625964346924608389878465365\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "CIiq8lr7wFkS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Пункт №3**\n",
        "\n",
        "Примените к функции из задания №2 сразу **два декоратора**:\n",
        "\n",
        "1. **Декоратор**, определяющий время выполнения функции.\n",
        "2. **Кэширующий декоратор** (из задания №2).\n",
        "\n",
        "Сравните время работы функции с использованием кэширования и без него.\n"
      ],
      "metadata": {
        "id": "zY5zVHuifDve"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "def timeTest(function):\n",
        "  def inner_func(*args):\n",
        "    st=time.time()\n",
        "    function(*args)\n",
        "    et=(time.time()-st)\n",
        "    print (f'Время выполнения  кода {et:.6f}')\n",
        "    return function(*args)\n",
        "  return inner_func\n",
        "\n",
        "def cache_func(func):\n",
        "  cache={}\n",
        "  def inner(n):\n",
        "    if n<1: return None\n",
        "    if n in cache: return cache[n]\n",
        "    cache[n] = func(n)\n",
        "    return cache[n]\n",
        "  return inner\n",
        "\n",
        "@timeTest\n",
        "def fibonacci(n):\n",
        "    if n==1 or n==2: return 1\n",
        "    return fibonacci(n - 1) + fibonacci(n - 2)\n",
        "print(\"Выполнение без кэширования\")\n",
        "fibonacci(5)\n",
        "\n",
        "@timeTest\n",
        "@cache_func\n",
        "def fibonacci(n):\n",
        "    if n==1 or n==2: return 1\n",
        "    return fibonacci(n - 1) + fibonacci(n - 2)\n",
        "\n",
        "print(\"Выполнение с кэшированием\")\n",
        "fibonacci(5)"
      ],
      "metadata": {
        "id": "dXuu8LJgg-0r",
        "outputId": "0dff21aa-ba00-47af-f4a4-6266e8da8b30",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Выполнение без кэширования\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000959\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.002829\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000892\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000030\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.004378\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000029\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000086\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.000030\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000029\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000000\n",
            "Выполнение с кэшированием\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.000001\n",
            "Время выполнения  кода 0.000039\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000081\n",
            "Время выполнения  кода 0.000000\n",
            "Время выполнения  кода 0.000112\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "5"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "fsSegPodwEwZ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Пункт №4**\n",
        "\n",
        "Создайте функцию **make_multiplier(n)**, которая принимает число **n** и возвращает функцию, умножающую переданное ей число на **n**.\n",
        "\n",
        "**Пример использования:**\n",
        "\n",
        "```python\n",
        "def make_multiplier(n):\n",
        "    # Ваш код\n",
        "\n",
        "times3 = make_multiplier(3)\n",
        "print(times3(5))  # Вывод: 15\n",
        "```"
      ],
      "metadata": {
        "id": "Ap04UA6ZtoK1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def make_multiplier(n):\n",
        "  def inner_func(i):\n",
        "    return n*i\n",
        "  return inner_func\n",
        "\n",
        "function=make_multiplier(3)\n",
        "print(function(5))"
      ],
      "metadata": {
        "id": "HasdSjestowl",
        "outputId": "e586d6da-ed46-4f61-d12b-dcc5f3b1a548",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "MIPkER_LwD_0"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Пункт №5**\n",
        "\n",
        "Реализуйте функцию с замыканием, которая настраивает округление чисел до заданного количества знаков после запятой.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "def rounder(n):\n",
        "    # Ваш код\n",
        "\n",
        "round_to_2 = rounder(2)\n",
        "print(round_to_2(3.14159))  # Вывод: 3.14\n",
        "```\n"
      ],
      "metadata": {
        "id": "mTwh5dIqto8N"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def rounder(n):\n",
        "  def inner_func(i):\n",
        "    return round(i, n)\n",
        "  return inner_func\n",
        "\n",
        "function=rounder(2)\n",
        "print(function(3.14159))"
      ],
      "metadata": {
        "id": "zjlE-viztpDo",
        "outputId": "9310b464-dc76-4cfc-a393-908a4713d077",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.14\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "6u2MeXBiwAyf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "Ag0rUJm-wIK1"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "```\n",
        "# Выбран кодовый формат\n",
        "\n",
        "```\n",
        "# Выбран кодовый формат\n",
        "```\n",
        "\n",
        "\n",
        "```\n",
        "\n",
        "### **Пункт №6**\n",
        "\n",
        "Напишите **декоратор**, который измеряет время исполнения функции и выводит его на экран, только если время превышает определённый порог.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "@time_threshold(threshold=0.5)\n",
        "def long_running_function():\n",
        "    # Долгий код\n",
        "\n",
        "long_running_function()\n",
        "# Выводится время выполнения только если оно больше 0.5 секунд\n",
        "```"
      ],
      "metadata": {
        "id": "i5A4zQl5tpKJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "\n",
        "def time_threshold(threshold):\n",
        "  def inner_func(func):\n",
        "    def inner_inner_func(*args):\n",
        "      st=time.time()\n",
        "      func(*args)\n",
        "      et=time.time()-st\n",
        "      if et>threshold:\n",
        "        print(f'Время выполнения программы {et}')\n",
        "      return func(*args)\n",
        "    return inner_inner_func\n",
        "  return inner_func\n",
        "\n",
        "@time_threshold(threshold=0.5)\n",
        "def long_running_function():\n",
        "  massive=[]\n",
        "  for i in range (1000000):\n",
        "    massive.append(i**2)\n",
        "long_running_function()"
      ],
      "metadata": {
        "id": "r0uUXlaWcRkX",
        "outputId": "865b519a-fccd-44b3-9570-4d98b3e682c3",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Время выполнения программы 0.5773806571960449\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **II. Итераторы и генераторы**"
      ],
      "metadata": {
        "id": "tu5ZanR_8j_R"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "### **Пункт №1. Генератор строк фиксированной длины**\n",
        "\n",
        "Напишите генератор `string_generator(char, times)`, который генерирует строки, состоящие из символа `char`, повторенного от 1 до `times` раз.\n",
        "\n",
        "```python\n",
        "# Пример использования:\n",
        "for s in string_generator('*', 5):\n",
        "    print(s)\n",
        "# Вывод:\n",
        "# *\n",
        "# **\n",
        "# ***\n",
        "# ****\n",
        "# *****\n",
        "```\n",
        "\n"
      ],
      "metadata": {
        "id": "7KQ8huR-8C_4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "ktfqCVPY-Mlx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def string_generator(char, times):\n",
        "  string=''\n",
        "  flag=0\n",
        "  while flag<times:\n",
        "    string+=char\n",
        "    yield string\n",
        "    flag+=1\n",
        "\n",
        "\n",
        "for s in string_generator('*',5):\n",
        "  print (s)"
      ],
      "metadata": {
        "id": "uvI-Ebqu98bW",
        "outputId": "0169f6eb-aee9-4bed-b807-08f07b91ecf5",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "*\n",
            "**\n",
            "***\n",
            "****\n",
            "*****\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "### **Пункт №2. Генератор бесконечной последовательности**\n",
        "\n",
        "Создайте бесконечный генератор `infinite_sequence()`, который с каждым вызовом возвращает следующее число, начиная с 1.\n",
        "\n",
        "```python\n",
        "# Пример использования:\n",
        "gen = infinite_sequence()\n",
        "for _ in range(5):\n",
        "    print(next(gen))\n",
        "# Вывод:\n",
        "# 1\n",
        "# 2\n",
        "# 3\n",
        "# 4\n",
        "# 5\n",
        "```\n",
        "\n",
        "---"
      ],
      "metadata": {
        "id": "zDtiD8Rl9Oqu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def infinite_sequence(start=1):\n",
        "  while True:\n",
        "    yield start\n",
        "    start+=1\n",
        "\n",
        "gen=infinite_sequence()\n",
        "for _ in range(5):\n",
        "  print(next(gen))"
      ],
      "metadata": {
        "id": "Yotj0YMK-Avy",
        "outputId": "8f6bb33a-e414-40f2-bec3-89af5d9a05d6",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "### **Пункт №3. Генератор комбинированных списков**\n",
        "\n",
        "Создайте генератор `combined_lists(lst1, lst2)`, который попеременно возвращает элементы из `lst1` и `lst2`. Если длины списков неравны, генератор должен остановиться при исчерпании более короткого списка.\n",
        "\n",
        "```python\n",
        "# Пример использования:\n",
        "for item in combined_lists([1, 2, 3], ['a', 'b', 'c', 'd']):\n",
        "    print(item)\n",
        "# Вывод:\n",
        "# 1\n",
        "# 'a'\n",
        "# 2\n",
        "# 'b'\n",
        "# 3\n",
        "# 'c'\n",
        "```"
      ],
      "metadata": {
        "id": "rJQEC1n19KHE"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "1h8fsmju-LQh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def combined_lists(lst1, lst2):\n",
        "  massive=[j for i in list(zip(lst1, lst2)) for j in i]\n",
        "  for s in massive:\n",
        "    yield s\n",
        "\n",
        "for item in combined_lists([1,2,3], ['a','b','c','d']):\n",
        "  print(item)"
      ],
      "metadata": {
        "id": "_kcrlmgU-Bmz",
        "outputId": "18035569-9964-4a72-8d01-a3d4d4e08e5a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "a\n",
            "2\n",
            "b\n",
            "3\n",
            "c\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "### **Пункт №4. Генератор перевернутой строки**\n",
        "\n",
        "Напишите генератор `reverse_string(s)`, который при каждом вызове возвращает следующий символ строки `s` в обратном порядке.\n",
        "\n",
        "```python\n",
        "# Пример использования:\n",
        "for char in reverse_string('hello'):\n",
        "    print(char)\n",
        "# Вывод:\n",
        "# o\n",
        "# l\n",
        "# l\n",
        "# e\n",
        "# h\n",
        "```"
      ],
      "metadata": {
        "id": "CEXaNzJX9B1D"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "L9WQ5Jpq-JaO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def reverse_string(string):\n",
        "  for char in reversed(list(string)):\n",
        "    yield char\n",
        "\n",
        "for char in reverse_string('hello'):\n",
        "  print(char)"
      ],
      "metadata": {
        "id": "5w9xT0eR-CBf",
        "outputId": "34d9c9f9-b61e-4fa4-cf25-dcc5b8063086",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "o\n",
            "l\n",
            "l\n",
            "e\n",
            "h\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "### **Пункт №5. Генератор степеней двойки**\n",
        "\n",
        "Создайте генератор `powers_of_two(n)`, который возвращает степени двойки от 2^0 до 2^n.\n",
        "\n",
        "```python\n",
        "# Пример использования:\n",
        "for num in powers_of_two(5):\n",
        "    print(num)\n",
        "# Вывод:\n",
        "# 1  # 2^0\n",
        "# 2  # 2^1\n",
        "# 4  # 2^2\n",
        "# 8  # 2^3\n",
        "# 16 # 2^4\n",
        "# 32 # 2^5\n",
        "```\n",
        "\n",
        "---"
      ],
      "metadata": {
        "id": "GNykcs8D8-Je"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def power_of_two(n):\n",
        "  start=0\n",
        "  for power in range(start, n+1):\n",
        "    yield 2**power\n",
        "\n",
        "for num in power_of_two(5):\n",
        "  print (num)"
      ],
      "metadata": {
        "id": "LjNW3m-y-CXj",
        "outputId": "54464fa6-0b5c-465f-e2fc-10b3c245d5ad",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "2\n",
            "4\n",
            "8\n",
            "16\n",
            "32\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "OU71icWn-Ggg"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Пункт №6. Генератор чисел из строки**\n",
        "\n",
        "Напишите генератор `number_extractor(s)`, который извлекает числа из заданной строки `s` и возвращает их как целые числа.\n",
        "\n",
        "```python\n",
        "# Пример использования:\n",
        "for num in number_extractor('abc123def45gh6'):\n",
        "    print(num)\n",
        "# Вывод:\n",
        "# 123\n",
        "# 45\n",
        "# 6\n",
        "```"
      ],
      "metadata": {
        "id": "w5gcNZCM829V"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "oJt2kxt8-FUP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def number_extractor(string):\n",
        "  number=''\n",
        "  for i in string:\n",
        "    if i.isdigit(): number+=i\n",
        "    elif number:\n",
        "      yield int(number)\n",
        "      number=''\n",
        "  if number:\n",
        "    yield int(number)\n",
        "for num in number_extractor('abc123def45gh6'):\n",
        "  print (num)"
      ],
      "metadata": {
        "id": "zDYVvuBX-C9M",
        "outputId": "a2837568-d116-4492-ae86-479713ce2239",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "123\n",
            "45\n",
            "6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "h6ztzyUn-D5n"
      }
    }
  ]
}