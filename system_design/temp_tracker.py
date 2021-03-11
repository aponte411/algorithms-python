import unittest

class TempTracker:
    MAX_TEMP = 111
    def __init__(self):
        # for mean
        self.num_readings = 0
        self.total_sum = 0.0
        self.mean = None
        # mode
        self.counts = [0 for _ in range(self.MAX_TEMP)]
        self.max_occurence = 0
        self.mode = 0
        # max and min
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def insert(self, temperature: int):
        # mode
        # increment count in dictionary
        self.counts[temperature] += 1
        # update max_occurence
        if self.counts[temperature] > self.max_occurence:
            self.max_occurence = self.counts[temperature]
            self.mode = temperature

        # mean
        self.num_readings += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.num_readings
        # max
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature



    def get_max(self) -> int:
        return self.max_temp

    def get_min(self) -> int:
        return self.min_temp

    def get_mean(self) -> float:
        return self.mean

    def get_mode(self) -> int:
        return self.mode


class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)


unittest.main(verbosity=2)
