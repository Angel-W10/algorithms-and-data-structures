class pq(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue)==0

    def add(self, val):
        self.queue.append(val)

    def poll_max(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if(self.queue[i] > self.queue[max]):
                    max = i
            out = self.queue[max]
            del self.queue[max]
            return out
        except IndexError:
            print()
            exit()

    def poll_min(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min=i
            out = self.queue[min]
            del self.queue[min]
            return out
        except IndexError:
            print()
            exit()


if __name__ == "__main__":
    my_pq = pq()
    my_pq.add(12)
    my_pq.add(14)
    my_pq.add(0)
    my_pq.add(2)

    for i in my_pq.queue:
        print(i, end=" ")
    print("\n")
    while not my_pq.is_empty():
        print(my_pq.poll_min())