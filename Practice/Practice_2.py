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
        "<a href=\"https://colab.research.google.com/github/yulia3006/Univercity/blob/main/Practice/Practice_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Практическая работа №2. Парадокс дней рождения\n",
        "\n",
        "Парадокс дней рождения - это интересное явление в теории вероятностей, которое часто удивляет людей своим неожиданным результатом.\n",
        "\n",
        "**Суть парадокса:**\n",
        "- В группе из 23 или более человек вероятность того, что у хотя бы двух людей совпадут дни рождения, превышает 50%.\n",
        "- При увеличении группы до 60 человек эта вероятность возрастает до более чем 99%.\n",
        "\n"
      ],
      "metadata": {
        "id": "1ncSpTCzGI0m"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Почему это кажется парадоксальным:**\n",
        "Многие люди интуитивно полагают, что для такой высокой вероятности совпадения нужно гораздо больше людей. Это связано с тем, что мы часто неправильно оцениваем количество возможных пар в группе.\n",
        "\n",
        "**Объяснение:**\n",
        "- В группе из 23 человек можно составить 253 уникальные пары.\n",
        "- Каждая пара имеет шанс на совпадение дней рождения.\n",
        "- Большое количество возможных пар значительно увеличивает вероятность хотя бы одного совпадения."
      ],
      "metadata": {
        "id": "UZUUZiYSHucP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#### **Задание**"
      ],
      "metadata": {
        "id": "BOJhPY2rJKBI"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "\n",
        "\n",
        "- Напишите программу, которая симулирует парадокс дней рождения и проверяет его достоверность.\n",
        "\n",
        "- **Упрощение:** Для удобства расчетов считайте, что в каждом месяце 28 дней (всего 336 возможных дней рождения в году).\n",
        "\n",
        "- **Требования к программе:**\n",
        "\n",
        "  1. Создайте функцию `birthday(iterations, people=23)`, которая:\n",
        "    - Принимает параметр `iterations` - количество повторений эксперимента.\n",
        "    - Принимает параметр `people` - количество человек в группе (по умолчанию 23).\n",
        "    - Проводит указанное количество симуляций для группы из `people` человек.\n",
        "    - Возвращает **процент случаев**, когда было обнаружено совпадение дней рождения, в виде числа с плавающей точкой.\n",
        "\n",
        "  2. Алгоритм работы функции:\n",
        "    - Генерируйте случайные дни рождения для заданного количества людей.\n",
        "    - Проверяйте, есть ли совпадения дней рождения в этой группе.\n",
        "    - Повторите этот процесс указанное количество раз (`iterations`).\n",
        "    - Подсчитайте процент случаев, когда были обнаружены совпадения.\n",
        "\n",
        "  3. В основной части программы:\n",
        "    - Используйте функцию `birthday()` для проверки вероятности совпадений для групп разного размера (например, от 10 до 60 человек).\n",
        "    - Выведите результаты, показывающие, как изменяется вероятность совпадения с увеличением размера группы.\n",
        "\n",
        "**Пример использования:**\n",
        "\n",
        "```python\n",
        "result_23 = birthday(10000, 23)\n",
        "print(f\"Вероятность совпадения дней рождения в группе из 23 человек: {result_23:.2f}%\")\n",
        "\n",
        "result_60 = birthday(10000, 60)\n",
        "print(f\"Вероятность совпадения дней рождения в группе из 60 человек: {result_60:.2f}%\")\n",
        "```"
      ],
      "metadata": {
        "id": "EfjJMiSGGhLK"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "SF7PfOsOEtXJ",
        "outputId": "8347c5d9-b341-4567-8746-cc647b8071ed",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the number of people in the group: 23\n",
            "The probability of birthday coincidence in a group of 23 people: 53.67%\n"
          ]
        }
      ],
      "source": [
        "from random import randint\n",
        "\n",
        "def birthday(iterations: int, people: int):\n",
        "    count = 0\n",
        "    for _ in range(iterations):\n",
        "        birthdays_people = [randint(0, 336) for _ in range(people)]\n",
        "        if len(birthdays_people) != len(set(birthdays_people)):\n",
        "            count += 1\n",
        "    probability = (count / iterations) * 100\n",
        "    return probability\n",
        "\n",
        "result = int(input('Enter the number of people in the group: '))\n",
        "print(f\"The probability of birthday coincidence in a group of {result} people: {birthday(10000, result):.2f}%\")"
      ]
    }
  ]
}