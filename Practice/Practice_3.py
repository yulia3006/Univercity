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
        "<a href=\"https://colab.research.google.com/github/yulia3006/Univercity/blob/main/Practice/Practice_3.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Практическая работа №3. Введение в ООП**\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "s-EuQCpnWXCn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Задание №1. Создайте класс Sphere для представления сферы в трехмерном пространстве**\n"
      ],
      "metadata": {
        "id": "TQ5SpdjdbD4D"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Обеспечьте следующие методы класса:\n",
        "\n",
        "1. Конструктор, принимающий 4 действительных числа: радиус, и 3 координаты центра шара. Если конструктор вызывается без аргументов, создать объект сферы с единичным радиусом и центром в начале координат. Если конструктор вызывается с аргументом, создать объект сферы с соответствующим радиусом и центром в начале координат.\n",
        "\n",
        "2. Метод get_volume (), который возвращает действительное число — объем шара, ограниченной текущей сферой.\n",
        "\n",
        "3. Метод get_square (), который возвращает действительное число — площадь внешней поверхности сферы.\n",
        "\n",
        "4. Метод get_radius (), который возвращает действительное число — радиус сферы.\n",
        "\n",
        "5. Метод get_center (), который возвращает тьюпл с 3 действительными числами — координатами центра сферы в том же порядке, в каком они задаются в конструкторе.\n",
        "\n",
        "6. Метод set_radius (r), который принимает 1 аргумент — действительное число, и меняет радиус текущей сферы, ничего не возвращая.\n",
        "\n",
        "7. Метод set_center (x, y, z), который принимает 3 аргумента — действительных числа, и меняет координаты центра сферы, ничего не возвращая. Координаты задаются в том же порядке, что и в конструкторе.\n",
        "\n",
        "8. Метод is_point_inside (x, y, z), который принимает 3 аргумента — действительных числа — координаты некоторой точки в пространстве (в том же порядке, что и в конструкторе), и возвращает логическое значение True или False в зависимости от того, находится эта точка внутри сферы."
      ],
      "metadata": {
        "id": "Q5Ow51wfASZH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "s0 = Sphere(0.5)\n",
        "print(s0.get_center())\n",
        "print(s0.get_volume())\n",
        "print(s0.is_point_inside(0 , -1.5, 0))\n",
        "s0.set_radius(1.6)\n",
        "print(s0.is_point_inside(0, -1.5, 0))\n",
        "print(s0.get_radius())"
      ],
      "metadata": {
        "id": "xYx3bR2Lbv42",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b4175499-7689-41a6-8ae0-7357c434def1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(0.0, 0.0, 0.0)\n",
            "0.5235987755982988\n",
            "False\n",
            "True\n",
            "1.6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "class Sphere:\n",
        "  def __init__(self, radius=1.0, x=0.0, y=0.0, z=0.0):\n",
        "    self.radius = radius\n",
        "    self.x = x\n",
        "    self.y = y\n",
        "    self.z = z\n",
        "\n",
        "  def get_volume(self):\n",
        "    return (4/3*math.pi*self.radius**3)\n",
        "\n",
        "  def get_square(self):\n",
        "    return(4*math.pi*self.radius**2)\n",
        "\n",
        "  def get_radius(self):\n",
        "    return self.radius\n",
        "\n",
        "  def get_center(self):\n",
        "    return (self.x, self.y, self.z)\n",
        "\n",
        "  def set_radius(self, r):\n",
        "    self.radius = r\n",
        "\n",
        "  def set_center(self, x, y, z):\n",
        "    self.x = x\n",
        "    self.y = y\n",
        "    self.z = z\n",
        "\n",
        "  def is_point_inside(self, x, y, z):\n",
        "    if abs(x - self.x) < self.radius and abs(y - self.y) < self.radius \\\n",
        "      and (abs(z - self.z) < self.radius):\n",
        "      return True\n",
        "    return False"
      ],
      "metadata": {
        "id": "d-vd-AYRdBId"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Задание №2. Создайте класс SuperStr, который наследует стандартный класс str и содержит 2 новых метода:**"
      ],
      "metadata": {
        "id": "UuJ9K_zAcaY_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Метод is_repeatance (s), который принимает 1 аргумент s и возвращает True или False в зависимости от того, может ли текущая строку быть получена целым количеством повторов строки s. Вернуть False, если s не является строкой. Считать, что пустая строка не содержит повторов.\n",
        "\n",
        "2. Метод is_palindrom (), который возвращает True или False в зависимости от того, является ли строка [палиндромом](https://ru.wikipedia.org/wiki/Палиндром). Регистрами символов пренебрегать. Пустую строку считать палиндромом."
      ],
      "metadata": {
        "id": "GX99X81VchPW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class SuperStr(str):\n",
        "\n",
        "  def __init__(self, string):\n",
        "    self.string = string\n",
        "\n",
        "  def is_repeatance(self, s):\n",
        "    if not isinstance(s, str):\n",
        "      return False\n",
        "    if self.string == \"\":\n",
        "      return False\n",
        "\n",
        "    while len(s) <= len(self.string):\n",
        "      if s == self.string:\n",
        "        return True\n",
        "      else: s += s\n",
        "    return False\n",
        "\n",
        "  def is_palindrom(self):\n",
        "    if not isinstance(self, str):\n",
        "      return False\n",
        "    if self.string.lower() == self.string[::-1].lower():\n",
        "      return True\n",
        "    return False"
      ],
      "metadata": {
        "id": "LtIAKDWFdEcr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "SuperStr.__mro__"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BsJcZQexUZPt",
        "outputId": "3cacb147-c06f-45e9-81ac-a6ad9f86555f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(__main__.SuperStr, str, object)"
            ]
          },
          "metadata": {},
          "execution_count": 42
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "a = SuperStr(\"шАЛАШ\")\n",
        "print(a.is_palindrom())\n",
        "print(a)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0tqZHglFaX9h",
        "outputId": "efd921a1-6531-4b05-ba8e-759f4915caea"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "шАЛАШ\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Тесты\n",
        "\n",
        "s = SuperStr(\"123123123123\")\n",
        "print(s.is_repeatance(\"123\")) # True\n",
        "print(s.is_repeatance(\"123123\")) # True\n",
        "print(s.is_repeatance(\"123123123123\")) # True\n",
        "print(s.is_repeatance(\"12312\")) # False\n",
        "print(s.is_repeatance(123)) # False\n",
        "print(s.is_palindrom()) # False\n",
        "print(s) # 123123123123 (строка)\n",
        "print(int(s)) # 123123123123 (целое число)\n",
        "print(s + \"qwe\") # 123123123123qwe\n",
        "p = SuperStr(\"123_321\")\n",
        "print(p.is_palindrom()) # True"
      ],
      "metadata": {
        "id": "oRO3alwicoNp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3ed054ac-eb83-48f8-d5a1-e9547033eb5e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n",
            "True\n",
            "False\n",
            "False\n",
            "False\n",
            "123123123123\n",
            "123123123123\n",
            "123123123123qwe\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Задание №3. В коде ниже представлен класс преподавателей и класс студентов (вы можете взять этот код за основу или написать свой).**"
      ],
      "metadata": {
        "id": "m9EGwLY9jZbw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Student:\n",
        "    def __init__(self, name, surname, gender):\n",
        "        self.name = name\n",
        "        self.surname = surname\n",
        "        self.gender = gender\n",
        "        self.finished_courses = []\n",
        "        self.courses_in_progress = []\n",
        "        self.grades = {}\n",
        "\n",
        "    def __str__(self):\n",
        "      string = ''\n",
        "      string += f\"Имя: {self.name}\\n\"\n",
        "      string += f\"Фамилия: {self.surname}\\n\"\n",
        "      string += f\"Средняя оценка за домашние задания: {float(self):.1f}\\n\"\n",
        "      string += \"Курсы в процессе изучения: \" + \", \".join(self.courses_in_progress) + \"\\n\"\n",
        "      string += \"Завершенные курсы: \" + \", \".join(self.finished_courses) + \"\\n\"\n",
        "      return string\n",
        "\n",
        "\n",
        "    def __bool__(self): #магический метод 1\n",
        "      if float(self) > 3:\n",
        "        return True\n",
        "      else:\n",
        "        return False\n",
        "\n",
        "    def __float__(self): #магический метод 2\n",
        "      summa = 0\n",
        "      grades_counter = 0\n",
        "      for k, v in self.grades.items():\n",
        "       for i in v:\n",
        "          summa += i\n",
        "          grades_counter += 1\n",
        "      average_grade = summa / grades_counter\n",
        "      return average_grade\n",
        "\n",
        "    def __lt__(self, other_student):\n",
        "      if float(self) < float(other_student):\n",
        "        return True\n",
        "      return False\n",
        "\n",
        "    def __gt__(self, other_student):\n",
        "      if float(self) > float(other_student):\n",
        "        return True\n",
        "      return False\n",
        "\n",
        "    def is_good_student(self):\n",
        "      if bool(self):\n",
        "        print(\"Да, это старательный студент.\")\n",
        "      else:\n",
        "        print(\"Нет, это кандидат на отчисление.\")\n",
        "\n",
        "\n",
        "    def add_courses(self, course_name):\n",
        "        self.finished_courses.append(course_name)\n",
        "\n",
        "    def rate_lecturer(self, lecturer, course, grade): #метод Студент оценивает лекции по предмету\n",
        "      if grade >= 1 and grade <= 10 and course in lecturer.courses_attached and\\\n",
        "        (course in self.finished_courses or course in self.courses_in_progress):\n",
        "        if not course in lecturer.courses_rating:\n",
        "          lecturer.courses_rating[course] = []\n",
        "        lecturer.courses_rating[course].append(grade)\n",
        "\n",
        "\n",
        "class Mentor:\n",
        "    def __init__(self, name, surname):\n",
        "        self.name = name\n",
        "        self.surname = surname\n",
        "        self.courses_attached = []\n",
        "\n",
        "    def rate_hw(self, student, course, grade):\n",
        "        student.grades[course] = [grade]"
      ],
      "metadata": {
        "id": "PlqK9m7KrT6e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "best_student = Student('Ruoy', 'Eman', 'your_gender')\n",
        "cool_mentor = Mentor('Some', 'Buddy')\n",
        "cool_mentor.rate_hw(best_student, 'Python', 10)\n",
        "\n",
        "print(\"Имя студента: \", best_student.name)\n",
        "print(\"Имя преподавателя: \", cool_mentor.name)\n",
        "print(\"Оценки студента по курсам: \", best_student.grades)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "oNc1-dVaw3ee",
        "outputId": "e422cda1-b91a-4af0-ffd6-ac24cd2adc15"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Имя студента:  Ruoy\n",
            "Имя преподавателя:  Some\n",
            "Оценки студента по курсам:  {'Python': [10]}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **3.1. Наследование**"
      ],
      "metadata": {
        "id": "08FkYxULrxE-"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "* Класс Mentor должен стать родительским классом для преподавателей. От него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания).\n",
        "\n",
        "> Имя, фамилю и список закрепленных курсов логично реализовать на уровне родительского класса."
      ],
      "metadata": {
        "id": "YNjsCv5ItOii"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class Lecturer(Mentor):\n",
        "  def __init__(self, name, surname):\n",
        "      super().__init__(name, surname)  # Вызываем конструктор предка\n",
        "      self.courses_rating = {}\n",
        "\n",
        "  def __str__(self):\n",
        "    string = ''\n",
        "    string += f\"Имя: {self.name}\\n\"\n",
        "    string += f\"Фамилия: {self.surname}\\n\"\n",
        "    string += f\"Средняя оценка за лекции: {float(self):.1f}\\n\"\n",
        "    return string\n",
        "\n",
        "  def __bool__(self): #магический метод 3\n",
        "    if float(self) > 5:\n",
        "      return True\n",
        "    else:\n",
        "      return False\n",
        "\n",
        "  def __float__(self):\n",
        "    summa = 0\n",
        "    grades_counter = 0\n",
        "    for k, v in self.courses_rating.items():\n",
        "      for i in v:\n",
        "        summa += i\n",
        "        grades_counter +=1\n",
        "    rating = summa / grades_counter\n",
        "    return rating\n",
        "\n",
        "\n",
        "  def is_good_lecturer(self):\n",
        "    if bool(self):\n",
        "      print(\"Да, экзамен пройдет хорошо.\")\n",
        "    else:\n",
        "      print(\"Нет, будь осторожен.\")\n",
        "\n",
        "\n",
        "class Reviewer(Mentor):\n",
        "  def __str__(self):\n",
        "    string = ''\n",
        "    string += f\"Имя: {self.name}\\n\"\n",
        "    string += f\"Фамилия: {self.surname}\\n\"\n",
        "    return string\n",
        "\n",
        "  def rate_hw(self, student, course, grade):\n",
        "    #if not course in self.courses_attached()\n",
        "    if not course in student.grades:\n",
        "      student.grades[course] = []\n",
        "    student.grades[course].append(grade)"
      ],
      "metadata": {
        "id": "1quZPRZKtIoc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **3.2. Атрибуты и взаимодействие классов**"
      ],
      "metadata": {
        "id": "oL8kB-uUtH5K"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "* Реализуйте возможность проставления оценок студентам только Reviewer-ам (реализуйте такой метод).\n",
        "\n",
        "* Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент (реализовать проверку)."
      ],
      "metadata": {
        "id": "ddcuJFCksWsY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# из класса Reviewer(Mentor)\n",
        "def rate_hw(self, student, course, grade):\n",
        "    if not course in student.grades:\n",
        "      student.grades[course] = []\n",
        "    student.grades[course].append(grade)\n",
        "\n",
        "\n",
        "#из класса Student\n",
        "def rate_lecturer(self, lecturer, course, grade): #метод Студент оценивает лекции по предмету\n",
        "      if grade >= 1 and grade <= 10 and course in lecturer.courses_attached and\\\n",
        "        (course in self.finished_courses or course in self.courses_in_progress):\n",
        "        if not course in lecturer.courses_rating:\n",
        "          lecturer.courses_rating[course] = []\n",
        "        lecturer.courses_rating[course].append(grade)"
      ],
      "metadata": {
        "id": "U30yyvuirv6H"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **3.3. Полиморфизм и магические методы**"
      ],
      "metadata": {
        "id": "i6PrwEBSu39u"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Перегрузите магический метод \\_\\_str__ у всех классов.\n",
        "У проверяющих он должен выводить информацию в следующем виде:\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "print(some_reviewer)\n",
        "Имя: Some\n",
        "Фамилия: Buddy\n",
        "```\n",
        "\n",
        "У лекторов:\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "print(some_lecturer)\n",
        "Имя: Some\n",
        "Фамилия: Buddy\n",
        "Средняя оценка за лекции: 9.9\n",
        "```\n",
        "\n",
        "А у студентов так:\n",
        "\n",
        "\n",
        "\n",
        "```\n",
        "print(some_student)\n",
        "Имя: Ruoy\n",
        "Фамилия: Eman\n",
        "Средняя оценка за домашние задания: 9.9\n",
        "Курсы в процессе изучения: Python, Git\n",
        "Завершенные курсы: Введение в программирование\n",
        "```\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "GvmtjlnmvF8b"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(st1)\n",
        "print(lect1)\n",
        "print(rev2)"
      ],
      "metadata": {
        "id": "gCJAL_EmwU0b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2e1de158-8353-421c-9a1f-3358f7d07fb5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Имя: Том\n",
            "Фамилия: Холланд\n",
            "Средняя оценка за домашние задания: 3.7\n",
            "Курсы в процессе изучения: Math, Informatics\n",
            "Завершенные курсы: \n",
            "\n",
            "Имя: Киллиан\n",
            "Фамилия: Мёрфи\n",
            "Средняя оценка за лекции: 6.0\n",
            "\n",
            "Имя: Райан\n",
            "Фамилия: Гослинг\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Реализуйте перегрузку других магических методов на Ваш выбор (не менее трёх), руководствуясь по смыслу контекстом представленных классов (студенты, преподаватели, оценки и т.д.)**"
      ],
      "metadata": {
        "id": "1DNE4TE3vfYI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(float(st1)) # возвращает среднюю оценку студента по всем предметам\n",
        "print(float(lect2)) # возвращает среднюю оценку лектора за лекции\n",
        "print(bool(lect2)) # если средняя оценка за лекции выше 5, то преподатель True\n",
        "print(st1 > st2) #__lt__ / __gt__ -- сравнивает рейтинг двух студентов, использует приведение к float(obj)"
      ],
      "metadata": {
        "id": "WNCf9PPMu4Gv",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b68b0256-cf74-4433-c4e5-be9982760cc0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.6666666666666665\n",
            "7.666666666666667\n",
            "True\n",
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **3.4. Тестирование**\n",
        "\n",
        "Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:\n",
        "\n",
        "* для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);\n",
        "* для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса)."
      ],
      "metadata": {
        "id": "X8xvLNT6u4Nn"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "lect1 = Lecturer(\"Киллиан\", \"Мёрфи\")\n",
        "lect2 = Lecturer(\"Кристиан\", \"Бэйл\")\n",
        "rev1 = Reviewer(\"Педро\", \"Паскаль\")\n",
        "rev2 = Reviewer(\"Райан\", \"Гослинг\")\n",
        "st1 = Student(\"Том\", \"Холланд\", \"attack helicoper\")\n",
        "st2 = Student(\"Дженна\", \"Ортега\", \"female\")\n",
        "\n",
        "st1.courses_in_progress = [\"Math\", \"Informatics\"]\n",
        "st2.courses_in_progress = [\"Math\", \"Informatics\"]\n",
        "\n",
        "lect1.courses_attached.append(\"Math\")\n",
        "lect2.courses_attached.append(\"Informatics\")\n",
        "\n",
        "rev1.courses_attached.append(\"Math\")\n",
        "rev2.courses_attached.append(\"Informatics\")\n",
        "\n",
        "rev1.rate_hw(st1, \"Math\", 3)\n",
        "rev1.rate_hw(st1, \"Math\", 4)\n",
        "rev1.rate_hw(st2, \"Math\", 5)\n",
        "rev1.rate_hw(st2, \"Math\", 3)\n",
        "\n",
        "print(st1.grades[\"Math\"])\n",
        "print(st2.grades[\"Math\"])\n",
        "rev2.rate_hw(st1, \"Informatics\", 4)\n",
        "rev2.rate_hw(st2, \"Informatics\", 4)\n",
        "\n",
        "st1.rate_lecturer(lect1, \"Math\", 1)\n",
        "st1.rate_lecturer(lect1, \"Math\", 8)\n",
        "st1.rate_lecturer(lect1, \"Math\", 5)\n",
        "st1.rate_lecturer(lect2, \"Informatics\", 6)\n",
        "\n",
        "st2.rate_lecturer(lect2, \"Informatics\", 10)\n",
        "st2.rate_lecturer(lect1, \"Math\", 10)\n",
        "st2.rate_lecturer(lect2, \"Informatics\", 7)\n",
        "\n",
        "print(lect1.courses_rating)\n",
        "print(lect2.courses_rating)\n",
        "print()\n",
        "lect1.is_good_lecturer()\n",
        "st2.is_good_student()\n",
        "print(float(st1))\n",
        "print(float(lect2))\n",
        "print(st1 > st2)\n",
        "print()\n",
        "print(st1)"
      ],
      "metadata": {
        "id": "uh8n08fdu4V_",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "442ce050-9d96-4a08-e940-a24867630388"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[3, 4]\n",
            "[5, 3]\n",
            "{'Math': [1, 8, 5, 10]}\n",
            "{'Informatics': [6, 10, 7]}\n",
            "\n",
            "Да, экзамен пройдет хорошо.\n",
            "Да, это старательный студент.\n",
            "3.6666666666666665\n",
            "7.666666666666667\n",
            "False\n",
            "\n",
            "Имя: Том\n",
            "Фамилия: Холланд\n",
            "Средняя оценка за домашние задания: 3.7\n",
            "Курсы в процессе изучения: Math, Informatics\n",
            "Завершенные курсы: \n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def student_average_grade(students_list, course):\n",
        "  summa = 0\n",
        "  counter = 0\n",
        "  for student in students_list:\n",
        "    for grade in student.grades[course]:\n",
        "      summa += grade\n",
        "    counter += len(student.grades[course])\n",
        "  return(summa/counter)\n",
        "\n",
        "def lecturer_average_grade(lecturers_list, course):\n",
        "  summa = 0\n",
        "  counter = 0\n",
        "  for lecturer in lecturers_list:\n",
        "    if course in lecturer.courses_rating:\n",
        "      for grade in lecturer.courses_rating[course]:\n",
        "        summa += grade\n",
        "      counter += len(lecturer.courses_rating[course])\n",
        "  return(summa/counter)\n",
        "\n",
        "students_list = [st1, st2]\n",
        "lecturers_list = [lect1, lect2]\n",
        "print(student_average_grade(students_list, \"Math\"))\n",
        "print(lecturer_average_grade(lecturers_list, \"Informatics\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vg3i2OP9RX7p",
        "outputId": "e77c93b3-7283-4973-e712-b9a9fcc530c7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3.75\n",
            "7.666666666666667\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## **Задание №4. Перегрузка операторов с помощью магических методов**\n"
      ],
      "metadata": {
        "id": "ehfo80anwJUM"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Цель задания:**\n",
        "\n"
      ],
      "metadata": {
        "id": "i_KsKg4awZOJ"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Разработать класс `Fraction` для работы с рациональными числами (дробями), реализовав перегрузку стандартных операторов через переопределение соответствующих магических методов. Ваша задача — обеспечить класс `Fraction` функциональностью, демонстрируемой в приведенном примере кода."
      ],
      "metadata": {
        "id": "JvIIB641watq"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Описание задания:**\n",
        "\n"
      ],
      "metadata": {
        "id": "BZ9kMLrYwcW_"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Создайте класс `Fraction`, который представляет собой обыкновенную дробь с числителем и знаменателем. Перегрузите основные арифметические операторы для выполнения операций над дробями, а также операторы сравнения. Обеспечьте возможность преобразования дроби в число с плавающей точкой и обратную операцию. Реализуйте обработку исключений при некорректных данных. Предоставьте понятное строковое и официальное представление дроби."
      ],
      "metadata": {
        "id": "6Qt56A-Bwe87"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Требования к заданию:**\n"
      ],
      "metadata": {
        "id": "1lv3NnB_whqP"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "1. **Класс `Fraction` должен:**\n",
        "\n",
        "   - Инициализироваться двумя целыми числами: числителем и знаменателем.\n",
        "   - Обрабатывать ситуацию когда знаменатель равен нулю, а именно выводить сообщение `\"Знаменатель не может быть нулем\"`.\n",
        "   - Упрощать дроби до несократимых при создании и после каждой арифметической операции.\n",
        "\n",
        "2. **Перегрузить следующие операторы путем переопределения магических методов:**\n",
        "\n",
        "   - **Сложение `+`** (`__add__`): сложение двух дробей, возвращает новую дробь.\n",
        "   - **Вычитание `-`** (`__sub__`): вычитание одной дроби из другой, возвращает новую дробь.\n",
        "   - **Умножение `*`** (`__mul__`): умножение двух дробей, возвращает новую дробь.\n",
        "   - **Деление `/`** (`__truediv__`): деление одной дроби на другую, возвращает новую дробь.\n",
        "   - **Равенство `==`** (`__eq__`): проверка равенства двух дробей.\n",
        "   - **Сравнения `>`, `<`, `>=`, `<=`**: сравнение дробей по их значению, реализовать методы `__lt__`, `__le__`, `__gt__`, `__ge__`.\n",
        "\n",
        "3. **Реализовать преобразование типов:**\n",
        "\n",
        "   - **Метод `__float__`**: преобразование дроби в число с плавающей точкой.\n",
        "\n",
        "4. **Дополнительные методы класса:**\n",
        "\n",
        "   - **`reciprocal()`**: возвращает новую дробь, обратную данной (числитель и знаменатель меняются местами).\n",
        "   - **Строковое представление** (`__str__`): возвращает строку вида `\"числитель/знаменатель\"`. Если знаменатель равен 1, возвращает только числитель в виде строки.\n",
        "   - **Официальное представление** (`__repr__`): возвращает строку вида `\"Fraction(числитель, знаменатель)\"`.\n",
        "\n",
        "5. **Обработка исключений:**\n",
        "\n",
        "   - При попытке создать дробь с нулевым знаменателем выводить в консоль сообщение `ValueError`.\n",
        "   - При попытке деления на нулевую дробь, выводить в консоль сообщение `ZeroDivisionError`.\n",
        "\n",
        "6. **Тестирование:**\n",
        "\n",
        "   - Написать код, демонстрирующий работу всех реализованных методов и операторов, используя примеры, приведенные ниже.\n",
        "   - Обеспечить корректную обработку исключений и вывод соответствующих сообщений.\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "4tJX8suPv0TY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "class Fraction:\n",
        "  def __init__(self, numerator, denumerator):\n",
        "    if denumerator == 0:\n",
        "      print(\"Знаменатель не может быть нулем\")\n",
        "    else:\n",
        "      gcd = math.gcd(numerator, denumerator)\n",
        "      self.numerator = int(numerator / gcd)\n",
        "      self.denumerator = int(denumerator / gcd)\n",
        "\n",
        "  def __float__(self):\n",
        "    return(self.numerator/self.denumerator)\n",
        "\n",
        "  def __str__(self):\n",
        "    if self.denumerator == 1:\n",
        "      return(str(self.numerator))\n",
        "    else:\n",
        "      return(f\"{self.numerator}/{self.denumerator}\")\n",
        "\n",
        "  def __repr__(self):\n",
        "    return (f\"Fraction({self.numerator}, {self.denumerator})\")\n",
        "\n",
        "  def reciprocal(self):\n",
        "    return(Fraction(self.denumerator, self.numerator))\n",
        "\n",
        "  def __add__(fr1, fr2):\n",
        "    if fr1.denumerator == fr2.denumerator:\n",
        "      return(Fraction(fr1.numerator+fr2.numerator, fr1.denumerator))\n",
        "    return(Fraction(fr1.numerator*fr2.denumerator + fr2.numerator*fr1.denumerator,\\\n",
        "                    fr1.denumerator*fr2.denumerator))\n",
        "\n",
        "  def __sub__(fr1, fr2):\n",
        "    if fr1.denumerator == fr2.denumerator:\n",
        "      return(Fraction(fr1.numerator-fr2.numerator, fr1.denumerator))\n",
        "    return(Fraction(fr1.numerator*fr2.denumerator - fr2.numerator*fr1.denumerator,\\\n",
        "                    fr1.denumerator*fr2.denumerator))\n",
        "\n",
        "  def __mul__(fr1, fr2):\n",
        "    return (Fraction(fr1.numerator*fr2.numerator, fr1.denumerator*fr2.denumerator))\n",
        "\n",
        "  def __truediv__(fr1, fr2):\n",
        "    return (Fraction(fr1.numerator*fr2.denumerator, fr1.denumerator*fr2.numerator))\n",
        "\n",
        "  def __eq__(fr1, fr2):\n",
        "    return fr1.numerator == fr2.numerator and fr1.denumerator == fr2.denumerator\n",
        "\n",
        "  def __lt__(fr1, fr2):\n",
        "    return fr1.numerator*fr2.denumerator < fr2.numerator*fr1.denumerator\n",
        "\n",
        "  def __gt__(fr1, fr2):\n",
        "    return fr1.numerator*fr2.denumerator > fr2.numerator*fr1.denumerator\n",
        "\n",
        "  def __le__(fr1, fr2):\n",
        "    return fr1.numerator*fr2.denumerator <= fr2.numerator*fr1.denumerator\n",
        "\n",
        "  def __ge__(fr1, fr2):\n",
        "    return fr1.numerator*fr2.denumerator >= fr2.numerator*fr1.denumerator\n",
        "\n",
        "  def from_float(n):\n",
        "    return Fraction(int(n*10000), 10000)"
      ],
      "metadata": {
        "id": "58JlCtFkxpmU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Тесты для класса `Fraction`:**\n"
      ],
      "metadata": {
        "id": "N5tZxFvIxdIy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Создание дробей\n",
        "f1 = Fraction(3, 4)\n",
        "f2 = Fraction(5, 6)\n",
        "\n",
        "# Сложение дробей\n",
        "f3 = f1 + f2\n",
        "print(f3)  # Ожидаемый вывод: 19/12\n",
        "\n",
        "# Вычитание дробей\n",
        "f4 = f1 - f2\n",
        "print(f4)  # Ожидаемый вывод: -1/12\n",
        "\n",
        "# Умножение дробей\n",
        "f5 = f1 * f2\n",
        "print(f5)  # Ожидаемый вывод: 5/8\n",
        "\n",
        "# Деление дробей\n",
        "f6 = f1 / f2\n",
        "print(f6)  # Ожидаемый вывод: 9/10\n",
        "\n",
        "# Проверка равенства\n",
        "print(f1 == Fraction(6, 8))   # Ожидаемый вывод: True\n",
        "\n",
        "# Сравнение дробей\n",
        "print(f1 > f2)    # Ожидаемый вывод: False\n",
        "print(f1 < f2)    # Ожидаемый вывод: True\n",
        "\n",
        "# Преобразование к float\n",
        "print(float(f1))  # Ожидаемый вывод: 0.75\n",
        "\n",
        "# Обратная дробь\n",
        "f7 = f1.reciprocal()\n",
        "print(f7)         # Ожидаемый вывод: 4/3\n",
        "\n",
        "# Создание дроби из float\n",
        "f8 = Fraction.from_float(0.75)\n",
        "print(f8)         # Ожидаемый вывод: 3/4\n",
        "\n",
        "# Проверка обработки исключений\n",
        "try:\n",
        "    f_invalid = Fraction(5, 0)\n",
        "except ValueError as e:\n",
        "    print(e)  # Ожидаемый вывод: Знаменатель не может быть нулем\n",
        "\n",
        "# Строковое и официальное представление\n",
        "print(str(f1))    # Ожидаемый вывод: 3/4\n",
        "print(repr(f1))   # Ожидаемый вывод: Fraction(3, 4)"
      ],
      "metadata": {
        "id": "U1UtgDM0xlqJ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6df0753d-7491-4c8c-eb56-43de2f7423b1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "19/12\n",
            "-1/12\n",
            "5/8\n",
            "9/10\n",
            "True\n",
            "False\n",
            "True\n",
            "0.75\n",
            "4/3\n",
            "3/4\n",
            "Знаменатель не может быть нулем\n",
            "3/4\n",
            "Fraction(3, 4)\n"
          ]
        }
      ]
    }
  ]
}