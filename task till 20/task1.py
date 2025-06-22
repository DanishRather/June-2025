def Reverse_fun(x):
    list_word=[]
    char=""
    for each_char in x: #Seperating Each character as a word
        if each_char != " ":
            char+=each_char
        else:
            list_word.append(char)
            char = "" 
    list_word.append(char) 
    char=""

    for i in range(len(list_word)-1,-1,-1): #Reversing the each word 
        char=char+list_word[i]+" "
    
    return char


output = Reverse_fun(input("Enter any String "))
print(output)





# s= input("Enter the String")
# space=[]
# if " " not in s:
#     print(s)
# else:
#     space=s.split(" ")
#     space.reverse()
#     print(" ".join(space))