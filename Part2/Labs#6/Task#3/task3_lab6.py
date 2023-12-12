from mrjob.job import MRJob
from mrjob.step import MRStep
import re

class SortWordFrequency(MRJob):
    def steps(self):
        return [
            MRStep(mapper = self.mapper, reducer=self.reducer)
        ]
    
    def mapper(self, _, line):
        # Tokenize the line into words using a simple regex
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    SortWordFrequency.run()
