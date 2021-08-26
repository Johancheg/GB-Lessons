res = []
with open(r"C:\Users\m_s.sudneko\Documents\GIT\GB\GB-Lessons\nginx_logs.txt", encoding='UTF-8') as f:
    for line in f:
        remote_addr = line.split('- -')
        req = line.split('"')
        request_type = req[1].split(' ')
        res.append((remote_addr[0], request_type[0], request_type[1]))
print(res)