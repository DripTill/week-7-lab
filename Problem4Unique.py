# miguel jusino

def uniquel(alist):
    unique_list = []
    for num in alist:
        if num not in unique_list:
            unique_list.append(num)
        return unique_list

print(uniquel([1, 3, 3, 3, 6, 2, 3, 5, 500, 500]))