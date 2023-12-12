from mrjob.job import MRJob
from mrjob.step import MRStep

class AverageNumberFriends(MRJob):
    def steps(self):
        return [
            MRStep(mapper = self.mapper_get_average,reducer=self.reducer_get_average)
        ]
    

    def mapper_get_average(self, _, line):
        (userId,userName,age,numFriends) = line.strip().split(',')
        yield int(age), int(numFriends)

    def reducer_get_average(self, key, values):
        total = 0
        count = 0

        for value in values:
            total += value
            count += 1

        average = total / count if count > 0 else 0

        # Emit the result for each group
        yield key, average.__format__('.2f')

if __name__ == '__main__':
    AverageNumberFriends.run()

