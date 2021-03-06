import sys

class HourglassAnalyzer:
    hourglass_length = 3
    hourglass_offsets = [(0,0), (1,0), (2,0), (1,1), (0,2), (1,2), (2,2)]

    def get_max_hourglass(self, matrix):
        height = len(matrix)
        width = len(matrix[0])
        max_hourglass_sum = None
        for y in range(0, height - self.hourglass_length + 1):
            for x in range(0, width - self.hourglass_length + 1):
                hourglass_sum = sum([matrix[y + y_offset][x + x_offset] for (x_offset,y_offset) in self.hourglass_offsets])
                if max_hourglass_sum is None or hourglass_sum > max_hourglass_sum:
                    max_hourglass_sum = hourglass_sum
        return max_hourglass_sum

matrix = [map(int, line.split()) for line in list(sys.stdin)]
print HourglassAnalyzer().get_max_hourglass(matrix)