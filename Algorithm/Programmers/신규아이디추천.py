# could be better with 're'

def solution(new_id):
    new_id = new_id.lower()
    temp = ""
    for i in new_id:
        if 'a'<=i<='z' or '0'<=i<='9' or i in ['-','_','.']:
            temp += i
    new_id = temp
    
    prev = ''
    temp = ''
    for i in (new_id+'?'):
        if prev == '.' and i == '.':
            continue
        else:
            temp+= prev
        prev = i
        
    if len(temp) > 0 and temp[0] == '.':
        temp = temp[1:]
    if len(temp) > 0 and temp[-1] == '.':
        temp = temp[:-1]
           
    if len(temp) == 0:
        temp = 'a'
    
    if len(temp)>=16:
        temp = temp[:15]
        if temp[-1] =='.':
            temp = temp[:-1]
    
    if len(temp) <= 2:
        plus = temp[-1]
        while len(temp) <3:
            temp+=plus
    answer = temp
    return answer
