import random


class RandomizedSet(object):

    def __init__(self):
        self.dictionary = {}
        self.array = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.dictionary:
            return False
        else:
            self.array.append(val)  # Append value to the list
            self.dictionary[val] = len(self.array) - 1  # Element as the key
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.dictionary:
            # Get index of the value from the dictionary
            index_of_value = self.dictionary.get(val)

            # Swap deleting value with last value in the list
            self.array[index_of_value] = self.array[-1]

            # Update index of the element
            self.dictionary[self.array[index_of_value]] = index_of_value

            # Remove last element from the list which is value you want to remove
            self.array.pop()

            # Delete value which is removed from the dictionary
            del self.dictionary[val]
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.array)  # Possible to use randint

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
