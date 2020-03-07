from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        set = Set()
        assert set.size == 0
        assert (1 in set) is False
    
    def test_init_with_list_contains(self):
        list = [1, 2, 3, 4, 5]
        set = Set(list)

        assert set.size == 5
        for item in list:
            assert (item in set) is True
    
    def test_add_contains(self):
        list = [1, 2, 3, 4, 5]
        set = Set()

        for item in list:
            set.add(item)
        assert set.size == 5
        for item in list:
            assert (item in set) is True
    
    def test_remove(self):
        list = [1, 2, 3, 4, 5]
        set = Set(list)

        set.remove(2)
        set.remove(4)
        assert set == Set([1,3,5])
        assert set.size == 3
    
    def test_union(self):
        set = Set([1,3,5])
        other_set = Set([2,4])
        empty_set = Set()

        union = set.union(other_set)
        assert union == Set([1,2,3,4,5])

        union = empty_set.union(set)
        assert union == set

    def test_intersection(self):
        set = Set([1, 2, 3, 4, 5])
        other_set = Set([1, 2, 3, 6])
        empty_set = Set()

        intersection = set.intersection(other_set)
        assert intersection == Set([1, 2 ,3])
        intersection = empty_set.intersection(set)
        assert intersection == Set()
    
    def test_difference(self):
        set = Set([1, 2, 3, 4, 5])
        other_set = Set([1, 2, 3, 6])
        empty_set = Set()

        difference = set.difference(other_set)
        assert difference == Set([4, 5])
        difference = empty_set.difference(set)
        assert difference == Set()
    
    def test_subset(self):
        set = Set([1, 2, 3, 4, 5])
        other_set = Set([1, 2, 3])
        empty_set = Set()

        assert set.is_subset(other_set) is True
        assert other_set.is_subset(set) is False
        assert set.is_subset(empty_set) is True
        assert empty_set.is_subset(set) is False