import re

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    new_id = re.sub(r"[^0-9a-z\-\_\.]", "", new_id)
    # 3
    new_id = re.sub(r"\.\.+", r".", new_id)
    # 4
    new_id = re.sub(r"^\.|\.$", r"", new_id)
    # 5
    if not new_id:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = re.sub(r"\.$", r"", new_id[:15])
    # 7
    length = len(new_id)
    if length <= 2:
        new_id += new_id[-1]*(3-length)
        
    answer = new_id
    return answer
    