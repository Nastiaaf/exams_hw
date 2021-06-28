# First assignment - Magic List

class MagicList:
    # New list's size
    list_size = 1

    # Defining the constructor
    def __init__(self, lst=[None]):
        self.lst = lst

    # Overload "set item" so we will be able to set item in index
    def __setitem__(self, key, value):
        # We can only write to 0 - len(lst) indexes
        if self.list_size - 1 >= key >= 0:
            self.lst[key] = value
        elif key == self.list_size:
            self.lst.extend([value])
            self.list_size += 1
        else:
            raise IndexError("You can only insert from index 0 up to index: " + str(self.list_size-1))

    def __str__(self):
        # Print the magic list we built
        return str(self.lst)

#------------------
# For debugging purposes
arr = MagicList()
arr[0] = 1
arr[1] = 2
arr[2] = 3
# arr[-1] = 5
print(arr)
#------------------
