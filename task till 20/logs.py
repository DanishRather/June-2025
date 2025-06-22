from datetime import datetime

def read_logs_from_file(file_path: str) -> list[str]:

    with open('log.txt','r') as file:
        data=file.readlines()
        # user_list = [[user:[time,state]]]
        user_list = []
        for each in data:
            each=each.strip()
            parts = each.split(",")
            date_time = parts[0].split(" ")
            if  len(date_time)==2 and len(parts)==3:
                dt = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                user_list.extend([[parts[1],dt,parts[2]]])
        analyze_logs(user_list)

user_dict={}
def analyze_logs(users):
    # user_dict={}
    for user in range(len(users)):
        temp=users[user]
        for each_log in range(user+1):
            if temp[0] == users[each_log][0]:
                start = temp[1]
                end = users[each_log][1]
                if users[user][0]  in user_dict:
                    print(user_dict[users[user][0]],"#####")
                    value = user_dict[temp[0]]
                    user_dict[temp[0]] = value + (start-end)/60
                else:
                    user_dict[users[user][0]] = (start-end)/6
            break    

for i in user_dict:
    print(user_dict[i])

read_logs_from_file('log.txt')
