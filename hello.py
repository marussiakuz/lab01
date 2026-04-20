import typer

def main(
    name: str,  # Required argument - user's first name
    lastname: str = typer.Option("", help="User's last name."),  # Optional last name
    formal: bool = typer.Option(False, "--formal", "-f", help="Use formal greeting."),  # Flag for formal greeting style
):
    """
    Greets the user, optionally using last name and formal style.
    
    Args:
        name: User's first name (required parameter)
        lastname: User's last name (optional, defaults to empty string)
        formal: Flag for formal greeting (defaults to False)
    
    Returns:
        None: Function prints the greeting to console
    """
    # Check if formal greeting should be used
    if formal:
        # Print formal greeting with last name
        print(f"Good day, {name} {lastname}!")
    else:
        # Print informal greeting with only first name
        print(f"Hello, {name}!")

# Program entry point
if __name__ == "__main__":
    # Run the typer CLI with the main function
    typer.run(main)
