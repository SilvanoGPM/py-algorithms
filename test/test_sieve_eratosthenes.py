import unittest

from others.sieve_eratosthenes import sieve_eratosthenes


class SieveOfEratosthenesTest(unittest.TestCase):
    def test_sieve_eratosthenes(self):
        prime_numbers = sieve_eratosthenes(30)
        expect_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        self.assertListEqual(prime_numbers, expect_prime_numbers)
