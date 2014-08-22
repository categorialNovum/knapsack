from operator import attrgetter

class ks_sort():

    def value_asc(self,items):
        return sorted(items, key=attrgetter('value'))

    def value_desc(self,items):
        return sorted(items, key=attrgetter('value'), reverse=True)

    def weight_asc(self,items):
        return sorted(items, key=attrgetter('weight'))

    def weight_desc(self,items):
        return sorted(items, key=attrgetter('weight'), reverse=True)

    def vw_ratio_asc(self,items):
        return sorted(items, key=attrgetter('vwratio'))

    def vw_ratio_desc(self,items):
        return sorted(items, key=attrgetter('vwratio'), reverse=True)
