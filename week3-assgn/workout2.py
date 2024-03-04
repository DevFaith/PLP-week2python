

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after applying the discount.
    """
    try:
        if discount_percent >= 20:
            discount_amount = price * (discount_percent / 100)
            final_price = price - discount_amount
            return final_price
        else:
            return price
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        return None

def main():
    original_price_str = input("Enter the original price: ")
    discount_percentage_str = input("Enter the discount percentage (or leave blank): ")

    try:
        original_price = float(original_price_str)
        if discount_percentage_str:
            discount_percentage = float(discount_percentage_str)
        else:
            discount_percentage = 0  # Default to no discount

        final_price = calculate_discount(original_price, discount_percentage)
        if final_price is not None:
            print(f"Final price after applying the discount: ${final_price:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()
