from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class SortWordFrequency(MRJob):
    def steps(self):
        return [
            MRStep(mapper = self.mapper, reducer=self.reducer),
            MRStep(mapper = self.mapper_sort, reducer=self.reducer_sort)
        ]
    
    def mapper(self, _, line):
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)


    def mapper_sort(self, word, total):
        yield '%04d' % int(total), word

    def reducer_sort(self, total, words):
        for word in words:
            yield word, int(total)

if __name__ == '__main__':
    SortWordFrequency.run()
