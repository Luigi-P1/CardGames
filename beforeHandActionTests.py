import unittest
from io import StringIO

import pytest as pytest
from parameterized import parameterized
from unittest import mock
import beforeHandAction


class MakeDeckTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.deck = beforeHandAction.makeDeck()

    def test_length_of_list(self):
        self.assertEqual(52, len(self.deck))

    def test_unique_elements_of_deck(self):
        unique = True
        for i in range(0, len(self.deck)-2):
            for j in range(i+1, len(self.deck)-1):
                if self.deck[i] == self.deck[j]:
                    unique = False
        self.assertTrue(unique)

    def test_number_of_suits(self):
        noOfSuits = 0
        suits = []
        for i in self.deck:
            suit = str(i[-1])
            if suit not in suits:
                suits.extend(suit)
                noOfSuits += 1
        self.assertEqual(noOfSuits, 4)

    def test_number_of_values(self):
        noOfValues = 0
        values = []
        for i in self.deck:
            value = str(i[0])
            if value not in values:
                values.extend(value)
                noOfValues += 1
        self.assertEqual(noOfValues, 13)


class HandValueUpdateTest(unittest.TestCase):

    @parameterized.expand([
        "KH", "KS", "KD", "KC",
        "QH", "QS", "QD", "QC",
        "JH", "JS", "JD", "JC",
    ])
    def testValueForCourtCards(self, card):
        handTotal = beforeHandAction.handValueUpdate(card, 0, 0)[0]
        self.assertEqual(handTotal, 10)

    @parameterized.expand([
        "KH", "KS", "KD", "KC",
        "QH", "QS", "QD", "QC",
        "JH", "JS", "JD", "JC",
    ])
    def testAceCountForCourtCards(self, card):
        aceCount = beforeHandAction.handValueUpdate(card, 0, 0)[1]
        self.assertEqual(aceCount, 0)

    @parameterized.expand([
        "AH", "AS", "AD", "AC",
    ])
    def testValueForCourtCards(self, card):
        handTotal = beforeHandAction.handValueUpdate(card, 0, 0)[0]
        self.assertEqual(handTotal, 11)

    @parameterized.expand([
        "AH", "AS", "AD", "AC",
    ])
    def testAceCountForAces(self, card):
        aceCount = beforeHandAction.handValueUpdate(card, 0, 0)[1]
        self.assertEqual(aceCount, 1)

    @parameterized.expand([
        "2H", "2S", "2D", "2C",
    ])
    def testValueForTwos(self, card):
        handTotal = beforeHandAction.handValueUpdate(card, 0, 0)[0]
        self.assertEqual(handTotal, 2)

    @parameterized.expand([
        "2H", "2S", "2D", "2C",
    ])
    def testAceCountForTwos(self, card):
        aceCount = beforeHandAction.handValueUpdate(card, 0, 0)[1]
        self.assertEqual(aceCount, 0)

    @parameterized.expand([
        "3H", "3S", "3D", "3C",
    ])
    def testValueForThrees(self, card):
        handTotal = beforeHandAction.handValueUpdate(card, 0, 0)[0]
        self.assertEqual(handTotal, 3)

    @parameterized.expand([
        "3H", "3S", "3D", "3C",
    ])
    def testAceCountForThrees(self, card):
        aceCount = beforeHandAction.handValueUpdate(card, 0, 0)[1]
        self.assertEqual(aceCount, 0)

    @parameterized.expand([
        "10H", "10S", "10D", "10C",
    ])
    def testValueForTens(self, card):
        handTotal = beforeHandAction.handValueUpdate(card, 0, 0)[0]
        self.assertEqual(handTotal, 10)

    @parameterized.expand([
        "10H", "10S", "10D", "10C",
    ])
    def testAceCountForTens(self, card):
        aceCount = beforeHandAction.handValueUpdate(card, 0, 0)[1]
        self.assertEqual(aceCount, 0)


class AceCheckTest(unittest.TestCase):
    @parameterized.expand([
            [21, 1, 21],
            [22, 1, 12],
            [21, 0, 21],
            [22, 0, 22],
        ])
    def testAceCheckTotal(self, initialTotal, initialAceCount, expectedTotal):
        actualTotal = beforeHandAction.AceCheck(initialTotal, initialAceCount)[0]
        self.assertEqual(expectedTotal, actualTotal)

    @parameterized.expand([
            [21, 1, 1],
            [22, 1, 0],
            [21, 0, 0],
            [22, 0, 0],
        ])
    def testAceCheckTotal(self, initialTotal, initialAceCount, expectedAceCount):
        actualAceCount = beforeHandAction.AceCheck(initialTotal, initialAceCount)[1]
        self.assertEqual(expectedAceCount, actualAceCount)


class BetPlacementTests(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_greeting(self, mock_stdout):
        with mock.patch('builtins.input', return_value=42.81):
            result = beforeHandAction.betPlacement(100)
            self.assertEqual(result, 42.81)

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_stuff(self, mock_stdout):
        with mock.patch('builtins.input', return_value=0):
            with mock.patch('builtins.input', return_value=42.81):
                result = beforeHandAction.betPlacement(100)
                self.assertEqual(result, 42.81)

