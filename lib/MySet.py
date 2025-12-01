class MySet:


    def __init__(self, iterable=None):
        """Initialize the set with unique elements from the iterable, if given."""
        self.dictionary = {}
        if iterable:
            for item in iterable:
                self.dictionary[item] = True

    def add(self, item):
        """Add an element to the set."""
        self.dictionary[item] = True

    def delete(self, item):
        """Remove an element from the set, if it exists."""
        if item in self.dictionary:
            del self.dictionary[item]

    def has(self, item):
        """Check if an element exists in the set."""
        return item in self.dictionary

    def __repr__(self):
        return f"MySet({list(self.dictionary.keys())})"