class Sort:

    sort = SortInterface()
    
    def create(self, type):
        if type == 1:
            return MergeSort.sort()
