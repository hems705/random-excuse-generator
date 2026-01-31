import random

# Categorized excuses
excuses = {
    "school": [
        "My dog ate my homework.",
        "I was absent yesterday.",
        "I forgot my notebook at home.",
        "Coffee spill on my notes.",
        "I had to attend a family event.",  
        "I was sick and couldn't complete the assignment."
    ],
    "work": [
        "I was stuck in traffic.",
        "My computer crashed.",
        "I had a sudden meeting.",
        "WiFi got disconnected.",
        "System update took longer than expected.",
        "I had a power outage at home."
    ],
    "personal": [
        "I had a family emergency.",
        "I was feeling unwell.",
        "I overslept today.",
        "I have fractured my arm.",
        "I had to take care of a personal matter."
    ]
}

while True:
    category = input("\nChoose a category (school/work/personal) or 'exit' to quit: ").lower()
    
    if category in excuses:
        print(f"\nAvailable excuses for '{category}':")
        for i, excuse in enumerate(excuses[category], 1):
            print(f"{i}. {excuse}")
        
        choice = input("\nEnter excuse number or press Enter for random: ").strip()
        
        if choice == "":
            # Random excuse
            selected = random.choice(excuses[category])
            print("\n🎯 Here's your random excuse:", selected)
        elif choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(excuses[category]):
                print("\n🎯 You selected:", excuses[category][index])
            else:
                print("❌ Invalid number. Please choose a valid excuse number.")
        else:
            print("❌ Invalid input. Please enter a number or press Enter.")
    
    elif category == "exit":
        print("\n👋 Goodbye! Stay creative with your excuses!")
        break
    else:
        print("❌ Invalid category. Please choose school, work, or personal.")
