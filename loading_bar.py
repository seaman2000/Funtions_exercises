def loading_bar(loading_percent: int):

    loading_list = []

    for percent_ in range(loading_percent // 10):
        loading_list.append("%")

    for dots in range((100 - loading_percent) // 10):
        loading_list.append(".")

    return loading_list

number = int(input())

if number != 100:
    print(f"{number}%" , end=" ")
    print(f"[{''.join(loading_bar(number))}]\n"
          f"Still loading...")

else:
    print(f"{number}% Complete!")
    print(f"[{''.join(loading_bar(number))}]")