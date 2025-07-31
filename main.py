import time
import matplotlib.pyplot as plt
from utils import is_free, find_alt_point

# Конфигурация маршрута
route = [(0, 0), (1, 0), (2, 0), (3, 0)]
obstacles = [(2, 0), (2, 1)]
equipment_points = [(3, 0)]

# Настройка графика
plt.ion()
fig, ax = plt.subplots()
ax.set_title("Autonomous Platform Simulation")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Рисуем маршрут, препятствия и точки оборудования
xs, ys = zip(*route)
ax.plot(xs, ys, linestyle='-', label="Route")
ox, oy = zip(*obstacles)
ax.scatter(ox, oy, marker='x', label="Obstacles")
ex, ey = zip(*equipment_points)
ax.scatter(ex, ey, marker='s', label="Equipment Points")

marker, = ax.plot([], [], marker='o', markersize=12, label="Robot")
ax.legend(loc="upper left")
ax.set_xlim(min(xs) - 1, max(xs) + 1)
ax.set_ylim(min(ys) - 1, max(ys) + 1)

# Главный цикл с обходом и анимацией
for point in route:
    if not is_free(point, obstacles):
        print(f"Obstacle at {point}! Trying to avoid...")
        alt = find_alt_point(point, obstacles)
        if alt:
            print(f" -> Avoiding via {alt}")
            point = alt
        else:
            print(f" -> Cannot avoid, skipping {point}")
            continue

    print(f"Moving to {point}")
    marker.set_data([point[0]], [point[1]])
    fig.canvas.draw()
    plt.pause(1)

    if point in equipment_points:
        print(f"[EQUIPMENT] Activated at {point}")
        marker.set_markerfacecolor('red')
        fig.canvas.draw()
        plt.pause(0.5)
        marker.set_markerfacecolor('blue')

plt.ioff()
plt.show()
