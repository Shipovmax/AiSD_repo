"""Create a Clock class for converting minutes to hours or seconds.

The user should specify a time value, for example 89 minutes, and also choose
whether to convert the given time to hours or to seconds. Use abstraction,
encapsulation, and a class constructor.
"""


class Clock:
    def __init__(self, minutes: int):
        self.__minutes = minutes

    def to_hours(self):
        return self.__minutes / 60

    def to_seconds(self):
        return self.__minutes * 60


# Tests

minutes = int(input("Enter the number of minutes: "))
clock = Clock(minutes)

choice = input("Convert to (hours/seconds): ").lower()

if choice == "hours":
    print("Hours:", clock.to_hours())
elif choice == "seconds":
    print("Seconds:", clock.to_seconds())
else:
    print("Invalid choice")
