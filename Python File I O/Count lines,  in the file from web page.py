import requests
line_counter = 0
r=requests.get("https://stepic.org/media/attachments/course67/3.6.2/273.txt") #get request
#print(r.text)
for i in r.text.splitlines():
       line_counter += 1
print(line_counter)