from collections import deque

d = deque()

while True:
    try:
        command = input().strip()
    except EOFError:
        break

    if command == "!":  # конец
        break

    elif command.startswith("+"):  # добавить в начало
        num = int(command.split()[1])
        d.appendleft(num)

    elif command.startswith("-"):  # добавить в конец
        num = int(command.split()[1])
        d.append(num)

    elif command == "*":  # сумма первого и последнего
        if not d:  # если пусто
            print("error")
        else:
            print(d[0] + d[-1])
            d.popleft()
            if d:  # если после удаления ещё остались элементы
                d.pop()

