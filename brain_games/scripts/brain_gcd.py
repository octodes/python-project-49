#!/usr/bin/env python3
"""Brain gcd game script."""


from brain_games import brain_engine
from brain_games.games import gcd


def main():
    """Run Brain gcd game."""
    brain_engine.play(gcd)


if __name__ == '__main__':
    main()
