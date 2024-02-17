def increment(num):
    try:
        return int(num) + 1
    except ValueError:
        print("An error occurred:")

a = increment("dd1")
