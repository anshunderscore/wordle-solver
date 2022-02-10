"""
Work in Progress
"""

import random
import statistics
import unittest
import wordguesser


class TestGuesser(unittest.TestCase):
    """Tests for guesser.py"""

    def test_hints(self):
        """Test the get_hints function"""
        solution = "aabbb"

        guess = "aaabb"
        self.assertEqual(wordguesser.generate_hints(guess, solution), {
            0: True,
            1: True,
            2: None,
            3: True,
            4: True
        })
        guess = "bbaaa"
        self.assertEqual(wordguesser.generate_hints(guess, solution), {
            0: False,
            1: False,
            2: False,
            3: False,
            4: None
        })
        guess = "later"
        self.assertEqual(wordguesser.generate_hints(guess, solution), {
            0: None,
            1: True,
            2: None,
            3: None,
            4: None
        })

    def test_guesses(self):
        """Test the guesses from the guess_word function"""

        wordguesser.CHECK_WORD = "check"
        guesses = []
        for guess in wordguesser.guess_word():
            guesses.append(guess)
        last_guess = guesses[-1][0]
        self.assertEqual(wordguesser.CHECK_WORD, last_guess)

    def test_average(self):
        """Get the average guesses it takes to get to the solution"""

        attempts = []
        for _ in range(5):
            wordguesser.CHECK_WORD = random.choice(wordguesser.WORDLIST)
            guesses = len(list(wordguesser.guess_word()))
            attempts.append(guesses)

        tries = statistics.mean(attempts)
        self.assertLessEqual(tries, 6)


if __name__ == "__main__":
    unittest.main()