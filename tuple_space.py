# tuple_space.py

import threading

class TupleSpace:
    def __init__(self):
        self.space = {}
        self.lock = threading.Lock()

    def put(self, key, value):
        with self.lock:
            if key in self.space:
                return False
            self.space[key] = value
            return True

    def read(self, key):
        with self.lock:
            return self.space.get(key)

    def get(self, key):
        with self.lock:
            return self.space.pop(key, None)

    def stats(self):
        with self.lock:
            n = len(self.space)
            total_key_size = sum(len(k) for k in self.space)
            total_value_size = sum(len(v) for v in self.space.values())
            return {
                'count': n,
                'avg_key': total_key_size / n if n else 0,
                'avg_value': total_value_size / n if n else 0,
                'avg_tuple': (total_key_size + total_value_size) / n if n else 0
            }
