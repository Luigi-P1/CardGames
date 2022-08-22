import unittest

import pytest
from parameterized import parameterized
import re
import postHandActions


class CompareHandsTest(unittest.TestCase):

    @parameterized.expand([
        [21, ["KS", "2S", "9D"], 21, ["KC", "AC"]],
        [19, ["KS", "9D"], 21, ["KC", "AC"]],
        [17, ["KS", "7D"], 20, ["KC", "QC"]],
    ])
    def testLosingOutcomes(self, P_total, P_hand, D_total, D_hand):
        outcome = postHandActions.compareHands(P_total, P_hand, D_total, D_hand)
        self.assertEqual(outcome, "Lose!")

    @parameterized.expand([
        [21, ["KS", "2S", "9D"], 20, ["KC", "10C"]],
        [19, ["KS", "9D"], 18, ["KC", "8C"]],
    ])
    def testWiningOutcomes(self, P_total, P_hand, D_total, D_hand):
        outcome = postHandActions.compareHands(P_total, P_hand, D_total, D_hand)
        self.assertEqual(outcome, "Win!")

    @parameterized.expand([
        [21, ["KS", "AS"], 21, ["AC", "10C"]],
        [19, ["KS", "9D"], 19, ["KC", "9C"]],
        [19, ["KS", "4D", "5S"], 19, ["KC", "9C"]],
    ])
    def testDrawingOutcomes(self, P_total, P_hand, D_total, D_hand):
        outcome = postHandActions.compareHands(P_total, P_hand, D_total, D_hand)
        self.assertEqual(outcome, "Draw!")

    @parameterized.expand([
        [21, ["KS", "AS"], 20, ["QC", "10C"]],
        [21, ["KS", "AS"], 21, ["AC", "5C", "5S"]],
    ])
    def testDrawingOutcomes(self, P_total, P_hand, D_total, D_hand):
        outcome = postHandActions.compareHands(P_total, P_hand, D_total, D_hand)
        self.assertEqual(outcome, "BlackJack!!!")


class PayOutTest(unittest.TestCase):

    @parameterized.expand([
        [20, 10, 35],
        [20, 5, 27.5],
    ])
    def testBlackJack(self, stack, bet, expected_stack):
        actual_stack = postHandActions.payOut(stack, bet, "BlackJack!!!")
        self.assertEqual(expected_stack, actual_stack)

    def testWin(self):
        stack = 20
        bet = 2
        expected_stack = 22
        actual_stack = postHandActions.payOut(stack, bet, "Win!")
        self.assertEqual(expected_stack, actual_stack)

    @parameterized.expand([
        [20, 10, 10],
        [10, 10, 0],
    ])
    def testLose(self, stack, bet, expected_stack):
        actual_stack = postHandActions.payOut(stack, bet, "Lose!")
        self.assertEqual(expected_stack, actual_stack)


class EndOfGameOutput(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_sout(self):
        postHandActions.goodBye(300, 600)
        captured = self.capsys.readouterr()
        message = captured.out
        self.assertIn("won", message)

    def test_sout1(self):
        postHandActions.goodBye(300, 100)
        captured = self.capsys.readouterr()
        message = captured.out
        self.assertIn("lost", message)

    def test_sout2(self):
        postHandActions.goodBye(300, 300)
        captured = self.capsys.readouterr()
        message = captured.out
        self.assertIn("even", message)

    def test_numerical_sout(self):
        postHandActions.goodBye(300, 600)
        captured = self.capsys.readouterr()
        message = captured.out
        self.assertIn("300", message)

    def test_numerical_sout1(self):
        postHandActions.goodBye(300, 100)
        captured = self.capsys.readouterr()
        message = captured.out
        self.assertIn("200", message)

    def test_numerical_sout2(self):
        postHandActions.goodBye(300, 300)
        captured = self.capsys.readouterr()
        message = captured.out
        hasDigit = bool(re.search(r'\d', message))
        self.assertFalse(hasDigit)
