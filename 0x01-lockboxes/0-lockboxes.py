#!/usr/bin/python3
"""0-lockboxes.py"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened"""
    n = len(boxes)
    unlocked = set([0])
    keys = boxes[0]
    stack = list(keys)
    while stack:
        key = stack.pop()
        if key < n and key not in unlocked:
            unlocked.add(key)
            stack.extend(boxes[key])
    return len(unlocked) == n
