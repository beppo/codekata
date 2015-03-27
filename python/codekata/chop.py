__author__ = 'mehmet'

class BinarySearch:
    @staticmethod
    def split_list(a_list):
        half = int(len(a_list)/2)
        print(a_list, half)
        return a_list[:half], a_list[half:]

    @staticmethod
    def chop(element, data, offset=0):
        # if list is empty return -1
        print(element, data, offset)
        if(not data):
          return -1
        # If element is same as the last element in list then calculate and return index
        if element == data[-1]:
            return offset + len(data) -1
        # If size of the data is one then return -1
        if len(data) == 1:
            return -1
        head, tail=BinarySearch.split_list(data)
        if element<= head[-1]:
            return BinarySearch.chop(element=element, data=head, offset=offset)
        else:
            return BinarySearch.chop(element=element, data=tail, offset=offset + len(head))