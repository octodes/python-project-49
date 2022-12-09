#!/usr/bin/env python3
"""Calculator game starting script."""


from brain_games import brain_engine
from brain_games.games import calc


def main():
    """Run Brain calc game."""
    brain_engine.play(calc)


if __name__ == '__main__':
    main()
