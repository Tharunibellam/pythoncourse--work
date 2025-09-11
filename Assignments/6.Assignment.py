import os
import re

# Predefined word lists for sentiment detection7
positive_words = ["good", "satisfied", "excellent", "happy", "love", "great"]
negative_words = ["bad", "poor", "sad", "angry", "hate", "disappointed"]

# Directory for storing feedback files
FOLDER = "feedbacks"
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

def analyze_feedback(file_path):
    """Analyze a feedback file and detect sentiment"""
    try:
        with open(file_path, "r") as f:
            content = f.read().lower()

        pos_found = [w for w in positive_words if re.search(r"\b" + w + r"\b", content)]
        neg_found = [w for w in negative_words if re.search(r"\b" + w + r"\b", content)]

        print(f"\n📂 Analyzing {os.path.basename(file_path)}...")
        print("   Positive words found:", pos_found)
        print("   Negative words found:", neg_found)

        if len(pos_found) > len(neg_found):
            print("   ➡️ Overall Sentiment: SATISFIED ✅\n")
        elif len(neg_found) > len(pos_found):
            print("   ➡️ Overall Sentiment: DISSATISFIED ❌\n")
        else:
            print("   ➡️ Overall Sentiment: NEUTRAL 😐\n")
    except FileNotFoundError:
        print("File not found!")

def create_feedback():
    """Create a new feedback file"""
    filename = input("Enter new feedback filename: ")
    filepath = os.path.join(FOLDER, filename)
    content = input("Enter customer feedback: ")
    with open(filepath, "w") as f:
        f.write(content)
    print("✅ Feedback created successfully!\n")

def modify_feedback():
    """Modify an existing feedback file"""
    files = os.listdir(FOLDER)
    if not files:
        print("⚠️ No feedback files available.\n")
        return
    print("Available feedback files:", files)
    filename = input("Enter the file you want to modify: ")
    filepath = os.path.join(FOLDER, filename)
    if os.path.exists(filepath):
        new_content = input("Enter new feedback content: ")
        with open(filepath, "w") as f:
            f.write(new_content)
        print("✏️ Feedback updated successfully!\n")
    else:
        print("⚠️ File not found.\n")

def main():
    """Main menu loop"""
    while True:
        print("📌 Customer Feedback Sentiment Tracker")
        print("1. Analyze a specific feedback")
        print("2. Analyze all feedbacks")
        print("3. Create new feedback")
        print("4. Modify feedback")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            filename = input("Enter feedback filename: ")
            analyze_feedback(os.path.join(FOLDER, filename))
        elif choice == "2":
            for file in os.listdir(FOLDER):
                analyze_feedback(os.path.join(FOLDER, file))
        elif choice == "3":
            create_feedback()
        elif choice == "4":
            modify_feedback()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
