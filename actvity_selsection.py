def activity_selection(start, finish):
    n = len(start)
    activities = sorted(range(n), key=lambda i: finish[i])
    selected = []
    last_finish = -1
    for i in activities:
        if start[i] >= last_finish:
            selected.append(i)
            last_finish = finish[i]
    return selected

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

chosen = activity_selection(start, finish)

print("Selected activities are:")
for i in chosen:
    print(f"Activity {i} (Start={start[i]}, Finish={finish[i]})")
