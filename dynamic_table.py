class dynamic_table:
    
# accepts a list of items, returns a binary array denoting item selections
    def calculate_solutions(self, items, capacity):
        t_x = len(items) + 1
        t_y = capacity + 1
        table = [[0 for x in xrange(t_x)] for y in xrange(t_y)]

        for prev,item in enumerate(items):
            i = prev + 1
            print "i  :  ", str(i)
            print "value  : ", str(item.value)
            print "weight : ", str(item.weight)
            print "----------------" 
            for c in xrange(len(table)):
                #if the value in the previous capacity slot is better, take it
                if table[c][prev] > table[c][i]:
                    table[c][i] = table[c][prev]
                #if the current item can be added to a previous solution and remain under capacity
                if item.weight + c <= capacity and table[c+item.weight][i] < table[c][prev] + item.value:
                    table[c+item.weight][i] = table[c][prev] + item.value
        for r in table:
            print r
        print "----------------" 
        print "SOLUTION : ", str(table[t_y-1][t_x-1])
        taken = self.unpack_table(table,items)
        print taken
        print "----------------" 

    def unpack_table(self,table,items):
        c = len(table) - 1
        i = len(table[0]) - 1
        taken = [0]*i
        cursor = table[c][i]
        while cursor != 0:
            cursor = table[c][i]
            if table[c][i-1] != cursor:
                taken[i-1] = 1
                c = c - items[i-1].weight
            i = i-1
        return taken


