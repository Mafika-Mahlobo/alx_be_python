def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()

        try:
            choice = input("Enter your choice: ")

            if choice == '1':
                item = input("Enter the item to add: ")
                shopping_list.append(item)
                print(f"Item added: {item}")
                print()

            elif choice == '2':
                item = input("Enter the item to remove: ")
                shopping_list.remove(item)
                print(f"Item removed: {item}")
                print()

            elif choice == '3':
                print("Your cart: ", end="")
                for i in range(len(shopping_list)):
                    print(shopping_list[i], end=" ")
                print()
                print()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Invalid value. {e}")

if __name__ == "__main__":
    main()