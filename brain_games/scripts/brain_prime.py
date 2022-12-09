#!/usr/bin/env python3
"""Prime number identifier game."""


from brain_games import brain_engine
from brain_games.games import prime


def main():
    """Run Brain prime game."""
    brain_engine.play(prime)


if __name__ == '__main__':
    main()
