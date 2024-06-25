# Small Updates

I'm resubmitting this repository in 2024, and after 2 years of working on the original, I still find my solution satisfactory. Yet, I felt some small updates are in order:

1. I marked the parent class methods as abstract methods to document their intent of being treated as an interface.
2. Fixed some incorrect logging usage.
3. Python 3.11 onwards broke the usage of implicit dataclass -> str behavior. I've added a `__str__` method to explicitly define how the value is used.

A few lines have changed on the instruction document, but I still think my solution ticks off all the necessary boxes.
