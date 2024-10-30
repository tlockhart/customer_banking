# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

def validate_input(prompt, number_type=float):
    """Prompt user for input and validate it as a specified number type.
    
    Args:
        prompt (str): The input prompt for the user.
        number_type (type): The type to which input should be converted (float or int).
        
    Returns:
        float or int: Validated number of the specified type.
    """
    while True:
        # Replaces the first occurrence of a comma (",") with an empty string. 
        # By specifying 1, it ensures that only one comma is removed if it exists
        user_input = (input(prompt)).strip().replace(',', '')
        # print("INPUT: ", user_input)
        if number_type == "number":
            number_type = float
        try:
            # Convert input to the specified number type
            return number_type(user_input)
        except ValueError:
            if number_type == "number":
                connector = "a"
                type_name = "decimal"
                print(f"Please enter an integer, with an optional decimal point (e.g., 5 or 5.0).")
            elif number_type.__name__ == "float":
                connector = "a"
                # type_name = number_type.__name__
                type_name = "decimal"
                print(f"Please enter an integer, with an optional decimal point (e.g., 5 or 5.0).")
            elif number_type.__name__ == "int":
                connector = "an"
                # type_name = number_type.__name__
                type_name = "integer"
                print(f"Please enter the value as {connector} {type_name}.")
            
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = validate_input("Enter the savings account balance: ", "number")
    savings_interest = validate_input("Enter the savings account interest rate (in %): ", float)
    savings_maturity = validate_input("Enter the number of months for the savings account: ", int)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f'Savings Balance: {updated_savings_balance:,.2f}, Savings Earned Interest: {interest_earned:.2f}')

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = validate_input("Enter the cd account balance: ", float)
    cd_interest = validate_input("Enter the cd account interest rate (in %): ", float)
    cd_maturity = validate_input("Enter the number of months for the cd account: ", int)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f'New CD Balance: {updated_cd_balance:,.2f}, CD Earned Interest: {interest_earned:.2f}')

if __name__ == "__main__":
    # Call the main function.
    main()