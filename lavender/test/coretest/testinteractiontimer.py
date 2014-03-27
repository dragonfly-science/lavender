__author__ = 'lewis'

import unittest
import time

from core.interactiontimer import InteractionTimer


class MyTestCase(unittest.TestCase):
    def test_is_finished(self):
        timer = InteractionTimer.start();
        timer.stop()
        self.assertTrue(timer.is_finished)

    def test_is_not_finished(self):
        timer = InteractionTimer.start();
        self.assertFalse(timer.is_finished)

    def test_stopped_duration(self):
        timer = InteractionTimer.start();
        time.sleep(1.5);
        timer.stop();
        self.assertAlmostEqual(timer.duration, 1.5, 2);

    def test_running_duration(self):
        timer = InteractionTimer.start();
        time.sleep(1.5);
        self.assertAlmostEqual(timer.duration, 1.5, 2);

    def test_running_and_stopped_duration(self):
        timer = InteractionTimer.start();
        time.sleep(1.5);
        self.assertAlmostEqual(timer.duration, 1.5, 2);

        time.sleep(1.5);
        timer.stop();
        self.assertAlmostEqual(timer.duration, 3, 2);

        time.sleep(1.5);
        self.assertAlmostEqual(timer.duration, 3, 2);


if __name__ == '__main__':
    unittest.main()
