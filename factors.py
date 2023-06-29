#!/usr/bin/env python3

import sys
import time

class Factorizer:
    """
    Class to factorize numbers into two smaller factors.
    """
    
    def __init__(self, filename):
        """
        Initialize the Factorizer instance with a filename.
        
        Args:
            filename (str): The name of the file containing numbers to factorize.
        """
        self.filename = filename
    
    def factorize_number(self, n):
        """
        Factorize a given number into two smaller factors.
        
        Args:
            n (int): The number to factorize.
        
        Returns:
            list: A list of tuples representing factor pairs.
        """
        factors = []
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append((i, n // i))
                break
        if not factors:
            factors.append((n, 1))
        return factors
    
    def factorize_file(self):
        """
        Factorize numbers from a file and print the factorization.
        """
        start_time = time.time()
        with open(self.filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factors = self.factorize_number(number)
                p, q = factors[0]
                print(f"{number}={p}*{q}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        print(f"\nreal\t{minutes:.0f}m{seconds:.3f}s\nuser\t{minutes:.0f}m{seconds:.3f}s\nsys\t0m0.000s")

if __name__ == '__main__':
    """
    Entry point of the program.
    """
    filename = sys.argv[1]
    factorizer = Factorizer(filename)
    factorizer.factorize_file()

