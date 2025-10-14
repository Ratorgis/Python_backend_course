import time
import random
from string import ascii_uppercase

def time_stats(repeat: int = 100) -> tuple[float, float]:
    def decorator(func):
        def wrapper(*args, **kwargs):
            times = []
            for i in range(repeat):
                start = time.perf_counter_ns()
                func(*args, **kwargs)
                end = time.perf_counter_ns()
                times.append(end - start)

            # Среднее
            total = 0
            for t in times:
                total += t
            mean_ns = total / len(times)

            # Медиана
            times.sort()
            n = len(times)
            if n % 2 == 1:
                median_ns = times[n // 2]
            else:
                median_ns = (times[n // 2 - 1] + times[n // 2]) / 2

            return mean_ns, median_ns
        return wrapper
    return decorator

@time_stats()
def check_set(collection, value) -> None:
    if value in collection:
        return True
    return False

@time_stats()
def check_list(collection, value) -> None:
    if value in collection:
        return True
    return False

def make_collections():
    size = random.randint(0, 10_000)
    data = [random.choice(ascii_uppercase) for i in range(size)]
    data_set = set(data)
    target = random.choice(data)
    return data, data_set, target, size


def run_tests(iterations = 20):
    for i in range(iterations):
        lst, st, target, size = make_collections()
        mean_s, med_s = check_set(st, target)
        mean_l, med_l = check_list(lst, target)
        print(f'{i + 1:02}) size = {size:5}')
        print(f' set  -> mean = {mean_s:.6f} s, median = {med_s:.6f} s')
        print(f' lsit -> mean = {mean_l:.6f} s, median = {med_l:.6f} s')
        print()

if __name__ == '__main__':
    run_tests(20)

