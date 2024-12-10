{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPwbSEsoiJv7CCSvTfWkFNH",
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
        "<a href=\"https://colab.research.google.com/github/yulia3006/Univercity/blob/main/Extra_Tasks/Ex_task_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "6OoHjWYPBTwd"
      },
      "outputs": [],
      "source": [
        "import random\n",
        "\n",
        "n = 0  #счётчик попыток\n",
        "number = random.randint(0, 100)\n",
        "print(f'Компьютер загадал число {number}')\n",
        "\n",
        "while True:\n",
        "    d = input('Введите число: ')\n",
        "    if d.lower() == 'Выход':\n",
        "        break\n",
        "    if not d.isdigit():\n",
        "        print('Введите число:')\n",
        "        continue\n",
        "    n += 1\n",
        "    d = int(d)\n",
        "    if d == number:\n",
        "        print(f'Поздравляем! Вы угадали число за {n} попытки!')\n",
        "        break\n",
        "    elif d > number:\n",
        "        print('Ваше число больше!')\n",
        "    elif d < number:\n",
        "        print('Ваше число меньше!')\n"
      ]
    }
  ]
}