import json
import sys

users = []

# script works by parsing index.json
# which is a map of user IDs to usernames and tags
with open('index.json', encoding='utf8') as f:
    # by default it's all on one line, so we just need to read the first line
    # unless you've edited it and added a line or formatted the file
    parsed = json.loads(f.readlines()[0])

    for user_id in parsed.keys():
        value = parsed[user_id]
        # only keep track of DMs
        # maybe servers could come later if anyone actually uses this script and wants it
        if value is not None and 'Direct Message' in value:
            value = value[len('Direct Message with '):]
            # -v (verbose mode) will prompt the user if they want to add
            # in case you want to manually filter out bots or people you don't want to add again
            if '-v' in sys.argv:
                if 'y' in input('Store user ' + value + ' (y/n)? ').lower():
                    users.append(value)
            else:
                users.append(value)
    f.close()

# writes the list of users to friends.txt in the same directory
with open('friends.txt', 'w+', encoding='utf8') as f:
    # remove contents of file and write new list
    f.truncate(0)
    f.write('\n'.join(users))
    f.close()

print("Wrote friends to friends.txt")
