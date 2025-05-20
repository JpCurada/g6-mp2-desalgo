class self_organizing_list:
    """
    This class enables the self organization list when searching as it position the most frequent search infront of the array to improve the performance of sequential search

    Reference:
        https://www.geeksforgeeks.org/self-organizing-list-count-method/
        
    Functions:
        print(): print the self organization list
        search(key): search and update the location of the list by descending order of frequency in each item
    """
    
    #insert the array to the self organizing list
    def __init__(self, intArray):
        self.list = [[x, 0] for x in intArray]
        self.length = len(intArray)

    #print the list
    def print(self):
        """
        This function print the organized list
        
        Argument:
            self (obj): Object of self_organizing_list
        
        Return:
            string: the string format of organized list

        Example:
            >>>obj.print()
            32, 12, 33, 55, 22
        """
        return print(", ".join(str(item[0]) for item in self.list))
    
    def search(self, key):
        """
        This function search the key and update the location in response to its frequency
        
        Argument:
            self (obj): Object of self_organizing_list
            key (int): The item to be search
        
        Return:
            integer: The index of the key to the current organized list

        Example:
            >>>obj.search(55)      [32, 12, 33, 55, 22] -> [55, 32, 12, 33, 22]
            0
        """
        
        intIndex = -1

        #get the index of the key
        for i in range(self.length):
            if(self.list[i][0] == key):
                intIndex = i
                self.list[i][1] += 1
                break

        if(intIndex == -1):
            return print("no key found")
        
        #change position base on the frequency in descending order
        while (intIndex > 0 and self.list[intIndex][1] > self.list[intIndex - 1][1]):
            self.list[intIndex], self.list[intIndex - 1] = self.list[intIndex - 1], self.list[intIndex]
            intIndex -= 1

        return intIndex

    