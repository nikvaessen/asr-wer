import unittest
import jiwer


class TestWERInputMethods(unittest.TestCase):
    def test_input_gt_string_h_string(self):
        cases = [
            ("This is a test", "This is a test", 0),
            ("This is a test", "", 1),
            ("This is a test", "This test", 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_string_h_list(self):
        cases = [
            ("This is a test", ["This is a test"], 0),
            ("This is a test", [""], 1),
            ("This is a test", ["This test"], 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_string_h_list_of_list(self):
        cases = [
            ("This is a test", [["This is a test"]], 0),
            ("This is a test", [[""]], 1),
            ("This is a test", [["This test"]], 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_list_h_string(self):
        cases = [
            (["This is a test"], "This is a test", 0),
            (["This is a test"], "", 1),
            (["This is a test"], "This test", 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_list_h_list(self):
        cases = [
            (["This is a test"], ["This is a test"], 0),
            (["This is a test"], [""], 1),
            (["This is a test"], ["This test"], 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_list_h_list_of_list(self):
        cases = [
            (["This is a test"], [["This is a test"]], 0),
            (["This is a test"], [[""]], 1),
            (["This is a test"], [["This test"]], 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_list_of_list_h_string(self):
        cases = [
            ([["This is a test"]], "This is a test", 0),
            ([["This is a test"]], "", 1),
            ([["This is a test"]], "This test", 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_list_of_list_h_list(self):
        cases = [
            ([["This is a test"]], ["This is a test"], 0),
            ([["This is a test"]], [""], 1),
            ([["This is a test"]], ["This test"], 0.5),
        ]

        self._apply_test_on(cases)

    def test_input_gt_list_of_list_h_list_of_list(self):
        cases = [
            ([["This is a test"]], [["This is a test"]], 0),
            ([["This is a test"]], [[""]], 1),
            ([["This is a test"]], [["This test"]], 0.5),
        ]

        self._apply_test_on(cases)

    def _apply_test_on(self, cases):
        for gt, h, correct_wer in cases:
            wer = jiwer.wer(gt, h)
            self.assertAlmostEqual(wer, correct_wer, delta=1e-16)
