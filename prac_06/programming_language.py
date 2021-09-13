class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection="", year=""):
        """Create a programming language object with the provided values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return the string of the programming languages values """
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Determine if typing is dynamic"""
        return self.typing == "Dynamic"
