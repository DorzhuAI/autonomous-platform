# Autonomous Platform Simulation

**Эмулятор автономной колесной платформы на Python с визуализацией через Matplotlib.**

---

## 📋 Описание

Этот проект демонстрирует простую эмуляцию автономного робота-платформы, выполняющего следующие задачи:

- **Движение** по заранее заданному списку координат (маршрут).
- **Обход препятствий**: если на маршруте встречается точка-препятствие, робот пытается объехать её вверх или вниз.
- **Активация оборудования**: в специальных точках робот “включает” оборудование (имитация действия).
- **Визуализация**: вся траектория и объезды отображаются анимированно на графике Matplotlib.

---

## ⚙️ Возможности

- Загрузка и исполнение произвольного маршрута (список кортежей `[(x1, y1), (x2, y2), …]`).
- Динамический обход препятствий (с простым алгоритмом “вверх/вниз”).
- Маркировка точек активации оборудования.
- Интерактивная анимация движения в реальном времени.
- Лёгкая модификация конфигурации (добавление новых точек, препятствий, логики).

---

## 🚀 Быстрый старт

1. **Клонируйте репозиторий**  
   ```bash
   git clone https://github.com/DorzhuAI/autonomous-platform.git
   cd autonomous-platform

2. **Установите зависимости**

bash

pip install -r requirements.txt


3. **Запустите эмуляцию**

bash

python main.py


Откроется окно с анимацией.

В консоли вы увидите логи о движении, объезде препятствий и активации оборудования.

Закройте окно и нажмите Enter в консоли, чтобы завершить скрипт.


Настройка конфигурации
Вы можете изменить в main.py следующие списки:

route — полный маршрут, список (x, y)

obstacles — координаты препятствий

equipment_points — где нужно “включить” оборудование


Лицензия
Этот проект лицензируется под MIT License.
См. файл LICENSE для подробностей.