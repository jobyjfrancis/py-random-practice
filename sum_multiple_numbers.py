for i in range(10):
    current_num = i
    if current_num == 0:
        previous_num = 0
    else:
        previous_num = current_num - 1
    print("Current number: ", current_num, end=" ")
    print("Previous number: ", previous_num, end=" ")
    print("Sum: ", current_num + previous_num)


