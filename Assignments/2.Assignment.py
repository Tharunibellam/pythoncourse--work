#Assignments 2
#WhatsApp Chat Data Analysis 
messages = []
n = int(input("Enter the number of messages: "))
for i in range(n):
 messages.append(input())
while True:
    print("\nAnalysis Options:")
    print("1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. (Reserved for future use)")
    print("13. Identify the user with the longest average message length")
    print("14. Count how many messages mention a specific user")
    print("15. Remove duplicate messages")
    print("16. Sort messages alphabetically")
    print("17. Extract all questions asked in the chat")
    print("18. Calculate the reply ratio between two users")
    print("19. Check for deleted messages")
    print("0. Exit")
    choice = input("Enter the choice: ").strip()
    if choice == '1':
        print("Total messages:", len(messages))
    elif choice == '2':
        users = set()
        for msg in messages:
            name = msg.split(':', 1)[0].strip()
            users.add(name)
        print("Unique users in the chat:", users)
    elif choice == '3':
        total = 0
        for msg in messages:
            if ':' in msg:
                text = msg.split(':', 1)[1].strip()
                total += len(text.split())
        print("Total words in the chat:", total)
    elif choice == '4':
        total = 0
        for msg in messages:
            if ':' in msg:
                text = msg.split(':', 1)[1].strip()
                total += len(text.split())
        if len(messages) > 0:
            avg = total / len(messages)
        else:
            avg = 0
        print("Average words per message: {:.2f}".format(avg))
    elif choice == '5':
        max_len = 0
        longest = ""
        for msg in messages:
            if ':' in msg:
                text = msg.split(':', 1)[1].strip()
                if len(text) > max_len:
                    max_len = len(text)
                    longest = msg
        print('Longest message: "{}"'.format(longest))
    elif choice == '6':
        user_count = {}
        for msg in messages:
            name = msg.split(':', 1)[0].strip()
            if name in user_count:
                user_count[name] += 1
            else:
                user_count[name] = 1
        max_user = ""
        max_count = 0
        for user in user_count:
            if user_count[user] > max_count:
                max_count = user_count[user]
                max_user = user
        print("Most active user: {} ({} messages)".format(max_user, max_count))
    elif choice == '7':
        user = input("Input: ")
        count = 0
        for msg in messages:
            name = msg.split(':', 1)[0].strip()
            if name == user:
                count += 1
        print("Messages sent by {}: {}".format(user, count))

    elif choice == '8':
        user = input("Input: ")
        word_count = {}
        for msg in messages:
            if ':' in msg:
                name, text = msg.split(':', 1)
                if name.strip() == user:
                    words = text.strip().lower().split()
                    for word in words:
                        if word in word_count:
                            word_count[word] += 1
                        else:
                            word_count[word] = 1
        max_word = ""
        max_count = 0
        for word in word_count:
            if word_count[word] > max_count:
                max_count = word_count[word]
                max_word = word
        if max_word:
            print('Most frequent word used by {}: "{}"'.format(user, max_word))
        else:
            print("No messages found for {}.".format(user))

    elif choice == '9':
        user = input("Input: ")
        user_msgs = []
        for msg in messages:
            name = msg.split(':', 1)[0].strip()
            if name == user:
                user_msgs.append(msg)
        if len(user_msgs) > 0:
            print('First message by {}: "{}"'.format(user, user_msgs[0]))
            print('Last message by {}: "{}"'.format(user, user_msgs[-1]))
        else:
            print("No messages found for {}.".format(user))
    elif choice == '10':
        user = input("Input: ")
        found = False
        for msg in messages:
            name = msg.split(':', 1)[0].strip()
            if name == user:
                found = True
                break
        if found:
            print("User '{}' found in the chat.".format(user))
        else:
            print("User '{}' not found in the chat.".format(user))

    elif choice == '11':
        word_count = {}
        for msg in messages:
            if ':' in msg:
                text = msg.split(':', 1)[1].strip().lower()
                words = text.split()
                for word in words:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        repeated = set()
        for word in word_count:
            if word_count[word] > 1:
                repeated.add(word)
        print("Common repeated words:", repeated)

    elif choice == '12':
        print("Reserved for future use.")

    elif choice == '13':
        user_word_count = {}
        user_msg_count = {}  
        for msg in messages:
            if ':' in msg:
                name, text = msg.split(':', 1)
                name = name.strip()
                words = text.strip().split()
                if name in user_word_count:
                    user_word_count[name] += len(words)
                    user_msg_count[name] += 1
                else:
                    user_word_count[name] = len(words)
                    user_msg_count[name] = 1
        max_avg = 0
        max_user = ""
        for user in user_word_count:
            avg = user_word_count[user] / user_msg_count[user]
            if avg > max_avg:
                max_avg = avg
                max_user = user
        if max_user:
            print("User with longest average message: {} (avg {:.1f} words)".format(max_user, max_avg))
        else:
            print("No messages found.")

    elif choice == '14':
        mention = input("Input: ")
        count = 0
        for msg in messages:
            if ':' in msg:
                text = msg.split(':', 1)[1]
                if mention in text:
                    count += 1
        print("Messages mentioning '{}': {}".format(mention, count))

    elif choice == '15':
        unique_msgs = []
        for msg in messages:
            if msg not in unique_msgs:
                unique_msgs.append(msg)   
        print("Unique messages count:", len(unique_msgs))
        for m in unique_msgs:
            print(m)

    elif choice == '16':
        sorted_msgs = sorted(messages)
        for m in sorted_msgs:
            print(m)

    elif choice == '17':
        questions = []
        for msg in messages:
            if '?' in msg:
                questions.append(msg)
        if questions:
            print("Questions in chat:")
            for q in questions:
                print(q)
        else:
            print("No questions found.")       
    elif choice == '18':
        user1 = input("First user: ")
        user2 = input("Second user: ")
        replies = 0
        prev_user = ""
        for msg in messages:
            name = msg.split(':', 1)[0].strip()
            if name == user2 and prev_user == user1:
                replies += 1
            prev_user = name
        print("Reply ratio from {} to {}: {} replies".format(user2, user1, replies))

    elif choice == '19':
        deleted_count = 0
        for msg in messages:
            if ':' in msg:
                text = msg.split(':', 1)[1].strip()
                if text == "This message was deleted":
                    deleted_count += 1
        print("Deleted messages found:", deleted_count)
    elif choice == '0':
        break
    else:
        print("Invalid choice. Try again.")

#with using with funtions
def count_messages(messages):
    print(f"Total messages: {len(messages)}")

def unique_users(messages):
    users = set()
    for msg in messages:
        name = msg.split(':', 1)[0].strip()
        users.add(name)
    print(f"Unique users in the chat: {users}")

def total_words(messages):
    total = 0
    for msg in messages:
        if ':' in msg:
            text = msg.split(':', 1)[1].strip()
            total += len(text.split())
    print(f"Total words in the chat: {total}")

def average_words(messages):
    total = 0
    for msg in messages:
        if ':' in msg:
            text = msg.split(':', 1)[1].strip()
            total += len(text.split())
    avg = total / len(messages) if messages else 0
    print(f"Average words per message: {avg:.2f}")

def longest_message(messages):
    max_len = 0
    longest = ""
    for msg in messages:
        if ':' in msg:
            text = msg.split(':', 1)[1].strip()
            if len(text) > max_len:
                max_len = len(text)
                longest = msg
    print(f'Longest message: "{longest}"')

def most_active_user(messages):
    user_count = {}
    for msg in messages:
        name = msg.split(':', 1)[0].strip()
        user_count[name] = user_count.get(name, 0) + 1
    max_user = max(user_count, key=user_count.get)
    print(f"Most active user: {max_user} ({user_count[max_user]} messages)")

def message_count_user(messages):
    user = input("Input: ")
    count = 0
    for msg in messages:
        name = msg.split(':', 1)[0].strip()
        if name == user:
            count += 1
    print(f"Messages sent by {user}: {count}")

def most_frequent_word_user(messages):
    user = input("Input: ")
    word_count = {}
    for msg in messages:
        if ':' in msg:
            name, text = msg.split(':', 1)
            if name.strip() == user:
                words = text.strip().lower().split()
                for word in words:
                    word_count[word] = word_count.get(word, 0) + 1
    if word_count:
        max_word = max(word_count, key=word_count.get)
        print(f'Most frequent word used by {user}: "{max_word}"')
    else:
        print(f"No messages found for {user}.")

def first_last_message_user(messages):
    user = input("Input: ")
    user_msgs = [msg for msg in messages if msg.split(':', 1)[0].strip() == user]
    if user_msgs:
        print(f'First message by {user}: "{user_msgs[0]}"')
        print(f'Last message by {user}: "{user_msgs[-1]}"')
    else:
        print(f"No messages found for {user}.")

def check_user_present(messages):
    user = input("Input: ")
    found = any(msg.split(':', 1)[0].strip() == user for msg in messages)
    if found:
        print(f"User '{user}' found in the chat.")
    else:
        print(f"User '{user}' not found in the chat.")

def common_repeated_words(messages):
    word_count = {}
    for msg in messages:
        if ':' in msg:
            text = msg.split(':', 1)[1].strip().lower()
            for word in text.split():
                word_count[word] = word_count.get(word, 0) + 1
    repeated = {word for word, count in word_count.items() if count > 1}
    print(f"Common repeated words: {repeated}")

def user_longest_avg_message(messages):
    user_word_count = {}
    user_msg_count = {}
    for msg in messages:
        if ':' in msg:
            name, text = msg.split(':', 1)
            name = name.strip()
            words = text.strip().split()
            user_word_count[name] = user_word_count.get(name, 0) + len(words)
            user_msg_count[name] = user_msg_count.get(name, 0) + 1
    max_avg = 0
    max_user = ""
    for user in user_word_count:
        avg = user_word_count[user] / user_msg_count[user]
        if avg > max_avg:
            max_avg = avg
            max_user = user
    if max_user:
        print(f"User with longest average message: {max_user} (avg {max_avg:.1f} words)")
    else:
        print("No messages found.")

def count_mentions(messages):
    mention = input("Input: ")
    count = 0
    for msg in messages:
        if ':' in msg:
            text = msg.split(':', 1)[1]
            if mention in text:
                count += 1
    print(f"Messages mentioning '{mention}': {count}")

def remove_duplicates(messages):
    unique_msgs = []
    for msg in messages:
        if msg not in unique_msgs:
            unique_msgs.append(msg)
    print(f"Unique messages count: {len(unique_msgs)}")
    for m in unique_msgs:
        print(m)

def sort_messages(messages):
    for m in sorted(messages):
        print(m)

def extract_questions(messages):
    questions = [msg for msg in messages if '?' in msg]
    if questions:
        print("Questions in chat:")
        for q in questions:
            print(q)
    else:
        print("No questions found.")

def reply_ratio(messages):
    user1 = input("First user: ")
    user2 = input("Second user: ")
    replies = 0
    prev_user = ""
    for msg in messages:
        name = msg.split(':', 1)[0].strip()
        if name == user2 and prev_user == user1:
            replies += 1
        prev_user = name
    print(f"Reply ratio from {user2} to {user1}: {replies} replies")

def check_deleted(messages):
    deleted_count = 0
    for msg in messages:
        if ':' in msg:
            text = msg.split(':', 1)[1].strip()
            if text == "This message was deleted":
                deleted_count += 1
    print(f"Deleted messages found: {deleted_count}")

def main():
    messages = []
    n = int(input("Enter the number of messages: "))
    for _ in range(n):
        messages.append(input())
    while True:
        print("\nAnalysis Options:")
        print("1. Count total number of messages")
        print("2. Identify unique users in the chat")
        print("3. Count total words in the chat")
        print("4. Calculate average words per message")
        print("5. Find the longest message sent")
        print("6. Find the most active user")
        print("7. Get message count for a specific user")
        print("8. Find the most frequently used word by a specific user")
        print("9. Retrieve the first and last message sent by a user")
        print("10. Check if a user is present in the chat")
        print("11. Find commonly repeated words")
        print("12. (Reserved for future use)")
        print("13. Identify the user with the longest average message length")
        print("14. Count how many messages mention a specific user")
        print("15. Remove duplicate messages")
        print("16. Sort messages alphabetically")
        print("17. Extract all questions asked in the chat")
        print("18. Calculate the reply ratio between two users")
        print("19. Check for deleted messages")
        print("0. Exit")
        choice = input("Enter the choice: ").strip()
        if choice == '1':
            count_messages(messages)
        elif choice == '2':
            unique_users(messages)
        elif choice == '3':
            total_words(messages)
        elif choice == '4':
            average_words(messages)
        elif choice == '5':
            longest_message(messages)
        elif choice == '6':
            most_active_user(messages)
        elif choice == '7':
            message_count_user(messages)
        elif choice == '8':
            most_frequent_word_user(messages)
        elif choice == '9':
            first_last_message_user(messages)
        elif choice == '10':
            check_user_present(messages)
        elif choice == '11':
            common_repeated_words(messages)
        elif choice == '12':
            print("Reserved for future use.")
        elif choice == '13':
            user_longest_avg_message(messages)
        elif choice == '14':
            count_mentions(messages)
        elif choice == '15':
            remove_duplicates(messages)
        elif choice == '16':
            sort_messages(messages)
        elif choice == '17':
            extract_questions(messages)
        elif choice == '18':
            reply_ratio(messages)
        elif choice == '19':
            check_deleted(messages)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

'''Enter the number of messages: 6
tharuni: Hello
sree: hi how or u
samatha: gud what about u
sreenivalusu: we are gud
tharuni: i am also gud
sree: had ur dinner 

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 1
Total messages: 6

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 2
Unique users in the chat: {'samatha', 'sree', 'sreenivalusu', 'tharuni'}

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 3
Total words in the chat: 19

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 4
Average words per message: 3.17

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 5
Longest message: "samatha: gud what about u"

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 6
Most active user: tharuni (2 messages)

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 7
Input: 8
Messages sent by 8: 0

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 9
Input: tharuni:Hello
No messages found for tharuni:Hello.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 10
Input: vindhya
User 'vindhya' not found in the chat.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 11
Common repeated words: {'gud', 'u'}

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 12
Reserved for future use.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 13
User with longest average message: samatha (avg 4.0 words)

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 14
Input: 15
Messages mentioning '15': 0

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 16
samatha: gud what about u
sree: had ur dinner
sree: hi how or u
sreenivalusu: we are gud
tharuni: Hello
tharuni: i am also gud

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 17
No questions found.

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 18
First user: tharuni
Second user: sree
Reply ratio from sree to tharuni: 2 replies

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 19
Deleted messages found: 0

Analysis Options:
1. Count total number of messages
2. Identify unique users in the chat
3. Count total words in the chat
4. Calculate average words per message
5. Find the longest message sent
6. Find the most active user
7. Get message count for a specific user
8. Find the most frequently used word by a specific user   
9. Retrieve the first and last message sent by a user      
10. Check if a user is present in the chat
11. Find commonly repeated words
12. (Reserved for future use)
13. Identify the user with the longest average message length
14. Count how many messages mention a specific user        
15. Remove duplicate messages
16. Sort messages alphabetically
17. Extract all questions asked in the chat
18. Calculate the reply ratio between two users
19. Check for deleted messages
0. Exit
Enter the choice: 0'''