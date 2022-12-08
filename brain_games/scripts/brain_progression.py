#!/usr/bin/env python3
"""Brain progression game script."""


from brain_games import brain_engine
from brain_games.games import progression


def main():
    """Run Brain progression game."""
    brain_engine.play(progression)


if __name__ == '__main__':
    main()
