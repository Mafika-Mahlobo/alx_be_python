def perform_operation(num1, num2, operation):
    
    try:
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                if num2 == 0:
                    return "Could not divide by 0"
                elif not isinstance(num2, (int, float)):
                    return "both numbers must be integers"
                return num1 / num2

    except ValueError as e:
        return f"An Error has occured. {e}"