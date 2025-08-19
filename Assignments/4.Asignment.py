# main.py
import program as mp

def menu():
    while True:
        print("\n------ ADVANCED FUNCTION MENU ------")
        print("1. Longest Consecutive Sequence")
        print("2. Trie (Insert & Prefix Search)")
        print("3. Power of Two (Bit Manipulation)")
        print("4. Shortest Path in Binary Matrix")
        print("5. Reverse Words in String")
        print("6. Min Stack")
        print("7. Maximum Depth of Binary Tree")
        print("8. Group Anagrams")
        print("9. First Unique Character in String")
        print("10. Sliding Window Maximum")
        print("0. Exit")
        print("------------------------------------")

        choice = input("Enter your choice: ")

        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice == "1": mp.longest_consecutive_sequence()
        elif choice == "2": mp.trie_program()
        elif choice == "3": mp.power_of_two()
        elif choice == "4": mp.shortest_path_matrix()
        elif choice == "5": mp.reverse_words()
        elif choice == "6": mp.min_stack_program()
        elif choice == "7": mp.max_depth_tree()
        elif choice == "8": mp.group_anagrams()
        elif choice == "9": mp.first_unique_char()
        elif choice == "10": mp.sliding_window_maximum()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()