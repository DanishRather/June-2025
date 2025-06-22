def Fact_list(lst):
    fact=1
    output=[]
    list_length=len(lst)
    for each_num in range(list_length):
        num = lst[each_num]
        while(num):
            fact=fact*num
            num=num-1
        output.append(fact)
        fact=1
    return output

output = Fact_list(list(map(int, input("Enter comma-separated integers: ").split(','))))
# output= Fact_list(list(input("Enter comma-seperated ingeters: ").split(",")))
print(output)
# nums = [int(x) for x in input("Enter space-separated integers: ").split()]
# print(nums)

# x = input("Enter the List of integers")
# print(type(x[2]))
# fact=1 
# output=[]
# for i in range(len(x)):
#     integer = x[i]

#     while(integer):
#         fact=fact*integer
#         integer=integer-1
#         print(integer,fact)
#     fact=1
#     output.append(fact)
#     print("================")
# print(output)