
class Knapsack():
    def __init__(self, item=[], rows=5, W=999):
        self.i = item[0]
        self.profit = item[1]
        self.weight = item[2]
        self.maxprofit = 0
        self.num_best = 0
        self.best_set = ["na" for item in range(len(items))]
        self.include = ["na" for item in range(len(items))]
        self.W = W
        self.w = [0 for row in range(rows + 1)]
        self.p = [0 for item in range(rows + 1)]
        self.n = rows

    def optimize(self, index, profit, weight):
        if (weight <= self.W and profit > self.maxprofit):
            self.maxprofit = profit
            self.num_best = self.i
            self.best_set = self.include

        if self.promising(self.i):
            self.include[self.i + 1] = "yes"
            self.optimize(self.i + 1, self.profit + self.p[self.i + 1], self.weight + self.W[self.i + 1])
            self.include[self.i + 1] = "no"
            self.optimize(self.i + 1, self.profit, self.weight)

    def promising(self, index):
        if (self.weight >= self.W):
            return False
        else:
            j = self.i + 1
            bound = self.profit
            totweight = self.weight
            while (j <= self.n and totweight + self.w[j] < self.W):
                totweight += self.w[j]
                bound += self.p[j]
                j += 1
            k = j
            if(k <= self.n):
                bound += (self.W - totweight) * self.p[k]/self.w[k]
            return bound > self.maxprofit


# Main
items = [[1, 20, 2, 10], [2, 30, 5, 6], [3, 35, 7, 5], [4, 12, 3, 4], [5, 3, 1, 3]]
W = 9
knap = Knapsack(items[0], len(items[0]), W)
results = []
for item in items:
    results.append(knap.optimize(item[0], item[1], item[2]))

print(results)






