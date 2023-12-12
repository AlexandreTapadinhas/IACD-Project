from mrjob.job import MRJob
from mrjob.step import MRStep

class SortedAmountSpentByCustomer(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper, reducer=self.reducer_get_sum),
            MRStep(mapper=self.mapper_sort, reducer=self.reducer_sort)
        ]
    
    def mapper(self, _, line):
        customerId,productId,amount = line.strip().split(',')
        yield customerId, float(amount)
    
    def reducer_get_sum(self, customer_id, values):
        yield customer_id, sum(values)

    def combiner(self, customer_id, values):
        yield customer_id, sum(values)

    '''
    '%04.2fd' % float(total) == 0000.00 % total if total is 1234.56 the result becomes 1234.56 since the sort of a MapReduce job is lexicographical, 
    this will sort the results by the total amount spent being that the highest value is 6375.45 therefore the use of 04.2f will ensure that the result is sorted correctly
    '''
    
    def mapper_sort(self, customer_id, total):
        yield '%04.2f' % float(total), customer_id

    def reducer_sort(self, total, customer_ids):
        for customer_id in customer_ids:
            yield customer_id, float(total)


if __name__ == '__main__':
    SortedAmountSpentByCustomer.run()    
