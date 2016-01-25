def large(all_nums):
    res = all_nums[0]
    for i in all_nums:
        if res < i:
            res = i
    return res

def small(all_nums):
    res = all_nums[0]
    for i in all_nums:
        if res > i:
            res = i
    return res


largest = None
smallest = None
all_numbers = []

while True:

    num = raw_input("Enter a number: ")
    if num == "done":
        break

    try:
        all_numbers.append(int(num))
    except:
        print "Invalid input"
        continue


largest = large(all_numbers)
smallest = small(all_numbers)

print "Maximum is", largest
print "Minimum is", smallest