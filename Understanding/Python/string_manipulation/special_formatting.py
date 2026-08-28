"""Python also lets you perform additional handling on string formatting."""

number = 1234.56789
print(f"{number=}")
print(f"Fixed point: {number:.2f}")
print(f"Comma sep: ${number:,.2f}")

message = "Hello"
print(f"Left aligned : '{message:<10}'")
print(f"Right aligned : '{message:>10}'")
print(f"Center aligned : '{message:^10}'")

from datetime import datetime

now = datetime.now()
print(f"Current date and time: {now:%Y-%m-%d %H:%M:%S}")
print(f"Weekday name         : {now:%A}")
