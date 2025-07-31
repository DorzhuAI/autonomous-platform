# utils.py
def is_free(point, obstacles):
    return point not in obstacles

def find_alt_point(point, obstacles):
    """Пытаемся объехать вверх или вниз."""
    x, y = point
    for dy in (1, -1):
        alt = (x, y + dy)
        if is_free(alt, obstacles):
            return alt
    return None
