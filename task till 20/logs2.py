from datetime import datetime
def Read_text(data_file):
    user_list = []
    with open(data_file,'r') as file:
        data = file.readlines()
        for each_line in data:
            each_line=each_line.strip()
            each_line=each_line.split(",")
            if (
                len(each_line)==3 and
                len(each_line[0].split(" "))==2):
                user_list.extend([each_line])
            else:
                continue
            # print(user_list)
    # file.close()
    Make_dict(user_list)

def Make_dict(user_logs):
    user_dict={}
    value=0
    for i in range(len(user_logs)):
        if user_logs[i][2] == ' LOGIN':
            login_session=user_logs[i]
            for j in range(i+1,len(user_logs)):
                if user_logs[j][2]==" LOGOUT":
                    start = datetime.strptime(user_logs[i][0], "%Y-%m-%d %H:%M:%S")
                    end = datetime.strptime(user_logs[j][0], "%Y-%m-%d %H:%M:%S")
                    value=end-start
                    if user_logs[i][1] in user_dict:
                        x = user_dict[user_logs[i][1]]
                        user_dict[user_logs[i][1]]+=value
                        value=0
                    else:
                        user_dict[user_logs[i][1]]=value
                        value=0

    for key,value in user_dict.items():
        print("{} has been spend {}".format(key,value))


            

        # print(l,ind)
    

Read_text("log.txt")

                    # value = (datetime.strptime(user_logs[i][0], "%Y-%m-%d %H:%M:%S")-datetime.strptime(user_logs[i][0], "%Y-%m-%d %H:%M:%S"))/60
                    # dict_logs[i]=value
