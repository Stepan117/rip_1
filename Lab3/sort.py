data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]
if __name__ == '__main__':
    result = sorted(data, key=abs, reverse=True)
    print('Без использования lambda-функции: ', result)
    result_with_lambda = sorted(data, key=lambda x: x if x >= 0 else -x, reverse=True)
    print('При использовании lambda-функции: ', result_with_lambda)
