input_list = [2,8,3,-3,0,-4,-10,5,-1]
positive_list = []
negative_list = []
having_zero = []
final_output = []
for data in input_list:
    if(data>0):
        positive_list.append(data)
    elif data == 0:
        having_zero.append(data)
    else:
        negative_list.append(data)


sort_positive = []

while positive_list:
    minimum_value = positive_list[0]
    for item in positive_list:
        if item<minimum_value:
            minimum_value = item
    sort_positive.append(minimum_value)
    positive_list.remove(minimum_value)


negative_list.sort()
sort_positive.extend(having_zero)
final_output.extend(sort_positive)
final_output.extend(negative_list)

print("final_output",final_output)
