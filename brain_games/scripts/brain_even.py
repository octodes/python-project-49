#!/usr/bin/env python3
"""Brain even game script."""


from brain_games import brain_engine
from brain_games.games import even


def main():
    """Run Brain even game."""
    brain_engine.play(even)


if __name__ == '__main__':
    main()