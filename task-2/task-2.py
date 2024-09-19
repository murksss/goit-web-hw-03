import time
from concurrent.futures import ProcessPoolExecutor


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result
    return wrapper


@timer
def factorize(*_numbers):
    results = []
    for num in _numbers:
        tmp_result = []
        for i in range(1, num + 1):
            if num % i == 0:
                tmp_result.append(i)
        results.append(tmp_result)

    return results


def factorize_in_process(num: int) -> list:
    results = []
    for i in range(1, num + 1):
        if num % i == 0:
            results.append(i)
    return results


def factorize_with_processes(*_numbers):
    start = time.time()

    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(factorize_in_process, number) for number in _numbers]
        results = [future.result() for future in futures]  # Ожидаем результаты всех процессов

    end = time.time()
    print(end - start)
    return results


def main():
    numbers = [106_022_222, 151_062_222, 10_652_222, 10_622_222]

    print("Sequential execution:", end=' ')  # Sequential execution: 9.53975224494934
    factorize(*numbers)

    print("\nParallel execution:", end=' ')  # Parallel execution: 5.778592586517334
    factorize_with_processes(*numbers)


if __name__ == '__main__':
    main()
