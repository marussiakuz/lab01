"""CLI greeting application using Typer."""

import typer
from typing import Optional


def main(
    name: str,
    lastname: Optional[str] = typer.Option(
        default="",
        help="User's last name.",
    ),
    formal: bool = typer.Option(
        default=False,
        "--formal",
        "-f",
        help="Use formal greeting.",
    ),
) -> None:
    """
    Greet a user with optional last name and formal style.

    Args:
        name: User's first name (required positional argument).
        lastname: User's last name (optional, defaults to empty string).
        formal: Flag to enable formal greeting style (defaults to False).

    Returns:
        None: This function prints the greeting to stdout.

    Examples:
        >>> main("John")
        Hello, John!

        >>> main("John", lastname="Doe", formal=True)
        Good day, John Doe!
    """
    if formal:
        print(f"Good day, {name} {lastname}!")
    else:
        print(f"Hello, {name}!")


if __name__ == "__main__":
    typer.run(main)
