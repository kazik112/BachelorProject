# modules/data_store.py

# Центральне сховище результатів
results = {}

def set_result(key, value):
    """Зберігає значення результату за ключем."""
    results[key] = value

def get_result(key, default=0.0):
    """Повертає значення за ключем або значення за замовчуванням."""
    return results.get(key, default)

def get_all_results():
    """Повертає всі збережені результати."""
    return results.copy()

def clear_results():
    """Очищує всі збережені результати."""
    results.clear()
