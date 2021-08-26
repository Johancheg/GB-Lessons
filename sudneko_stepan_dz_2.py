my_list = {}
with open(r"C:\Users\m_s.sudneko\Documents\GIT\GB\GB-Lessons\nginx_logs.txt", encoding='UTF-8') as f:
    string = f.readline()
    while string != '':
        userts = string[:string.find(' ') - 1]
        my_list.setdefault(userts,0)
        my_list[userts] += 1
        string = f.readline()
# print(my_list)
user_ad, max_req = max(my_list.items(), key=lambda k_v: k_v[1])
print(user_ad, max_req)