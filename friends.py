import json
import sys

print(sys.argv)

users = []

with open('index.json', encoding='utf8') as f:
    parsed = json.loads(f.readlines()[0])
    # print(parsed)
    for user_id in parsed.keys():
        value = parsed[user_id]
        # print(user_id, value)
        if value is not None and 'Direct Message' in value:
            value = value[len('Direct Message with '):]
            if '-v' in sys.argv:
                if 'y' in input('Store user ' + value + ' (y/n)? ').lower():
                    users.append(value)
            else:
                users.append(value)
    f.close()

with open('friends.txt', 'w+', encoding='utf8') as f:
    f.truncate(0)
    f.write('\n'.join(users))
    f.close()

print("Wrote friends to friends.txt")
