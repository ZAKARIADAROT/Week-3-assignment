def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount if it's 20% or more."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call function and display result
final_price = calculate_discount(original_price, discount_percent)
print(f"The final price after discount is: {final_price}")



    
    