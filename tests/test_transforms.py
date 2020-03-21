import unittest

from jiwer.transforms import *


class TestSentencesToListOfWordsTransform(unittest.TestCase):
    def test_normal(self):
        cases = [
            ("this is a test", ["this", "is", "a", "test"]),
            ("", [""]),
            (["this is one", "is two"], ["this", "is", "one", "is", "two"]),
            (["one", "two", "three", "", "five"], ["one", "two", "three", "", "five"]),
        ]

        self._apply_test_on(SentencesToListOfWords(), cases)

    def test_weird_delimiter(self):
        cases = [
            ("this_is_a_test", ["this", "is", "a", "test"]),
            ("", [""]),
            (["this_is_one", "is_two"], ["this", "is", "one", "is", "two"]),
            (["one", "two", "three", "", "five"], ["one", "two", "three", "", "five"]),
        ]

        self._apply_test_on(SentencesToListOfWords("_"), cases)

    def _apply_test_on(self, tr, cases):
        for inp, outp in cases:
            self.assertEqual(tr(inp), outp)


class TestRemoveSpecificWords(unittest.TestCase):

    def test_normal(self):
        cases = [
            ("yhe about that bug", "about that bug"),
            ("yeah about that bug", "about that bug"),
            ("one bug", "one bug"),
            (["yhe", "about", "bug"], ["about", "bug"]),
            (["yeah", "about", "bug"], ["about", "bug"]),
            (["one", "bug"], ["one", "bug"]),
            (["yhe about bug"], ["about bug"]),
            (["yeah about bug"], ["about bug"]),
            (["one bug"], ["one bug"])
        ]

        self._apply_test_on(RemoveSpecificWords(["yhe", "yeah"]), cases)

    def _apply_test_on(self, tr, cases):
        for inp, outp in cases:
            print("input:",  inp)
            print("outp:", outp)
            print("t:", tr(inp))
            self.assertEqual(outp, tr(inp))
