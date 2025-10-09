class summ:
    def __init__(self, numm):
        self.numm = numm

    def calc_sum(self):
        total = 0
        for num in self.numm:
            total += num
        return total
nums = list(map(int, input().split()))
my_list = summ(nums)
print("Сумма:", my_list.calc_sum())