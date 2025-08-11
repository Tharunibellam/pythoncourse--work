# main.py
import program as mp

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Check Balanced Brackets")
        print("2. Second Largest Number (No sort())")
        print("3. Palindrome Number")
        print("4. Count Vowels & Consonants")
        print("5. Binary Search")
        print("6. Check Duplicates (No set())")
        print("7. Prime Numbers in Range")
        print("8. Rotate Matrix 90° Clockwise")
        print("9. Check String Permutations")
        print("10. Pascal's Triangle")
        print("0. Exit")
        print("----------------------------")
        
        choice = input("Enter your choice: ")
        
        if choice == "0":
            print("Exiting program. Goodbye!")
            break
        elif choice == "1":
            mp.check_balanced_brackets()
        elif choice == "2":
            mp.second_largest()
        elif choice == "3":
            mp.palindrome_number()
        elif choice == "4":
            mp.vowels_consonants_count()
        elif choice == "5":
            mp.binary_search_program()
        elif choice == "6":
            mp.contains_duplicates()
        elif choice == "7":
            mp.primes_in_range()
        elif choice == "8":
            mp.rotate_matrix()
        elif choice == "9":
            mp.are_permutations()
        elif choice == "10":
            mp.pascals_triangle()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()