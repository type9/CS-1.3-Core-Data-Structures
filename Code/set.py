class Set():
    '''Set strucutre implemented using dictionary'''
    def __init__(self, elements=[]):
        self.dict = {}
        self.size = 0
        '''0(n) init'''
        for element in elements:
            self.add(element)
    
    def __str__(self):
        items = []
        for element in self.dict.keys():
            items.append(element)
        return f'Set({items})'

    def __eq__(self, other): 
        return self.dict == other.dict
    
    def __add__(self, other):
        return self.union(other)
    
    def __sub__(self, other):
        return self.difference(other)

    def __contains__(self, element):
        '''O(1)'''
        return element in self.dict

    def add(self, element):
        '''O(1)'''
        self.dict[element] = True
        self.size += 1
    
    def remove(self, element):
        '''O(1)'''
        if element in self:
            del self.dict[element]
            self.size -= 1
    
    def union(self, other_set):
        '''O(m) time under all conditions'''
        union = Set(self.dict)
        for element in other_set.dict.keys():
            if not element in self:
                union.add(element)
        return union

    def intersection(self, other_set):
        '''O(n) time under all conditions'''
        if self.size > other_set.size:
            self, other_set = other_set, self

        intersection = Set()
        for element in self.dict.keys():
            if element in other_set:
                intersection.add(element)

        return intersection
    
    def difference(self, other_set):
        '''O(m) time under all conditions'''
        difference = self
        for element in other_set.dict.keys():
            if element in difference:
                difference.remove(element)
        return difference
        
    def is_subset(self, other_set):
        '''O(n) time under all condictions'''
        if other_set.size > self.size:
            return False

        for element in other_set.dict.keys():
            if element not in self:
                return False
        return True

if __name__ == "__main__":
    A = Set([1, 2 ,3, 4 ,5])
    B = Set([1, 3, 5])
    C = Set([2, 4, 6])

    print(B + C)
    print(A - B)
    print(A.difference(B))
    print(A - C)
    print((A - C) == B)