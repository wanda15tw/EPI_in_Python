tasks = [5, 2, 1, 6, 4, 4, 4, 8]


def optimum_task_assignment(tasks):
    tasks.sort()

    return [(tasks[i], tasks[~i]) for i in range(len(tasks)//2)]
