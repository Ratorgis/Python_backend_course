from pathlib import Path
import sys

def tree (direction: Path, prefix: str = '') -> str:
    items = sorted(direction.iterdir())
    count = len(items)

    for idx, elem in enumerate(items):
        connect = '└──' if idx == count - 1 else '├──' 
        print(prefix + connect + elem.name)

        if elem.is_dir():
            extention = '│ ' if idx != count else '  '
            extention += ' '
            tree(elem, prefix + extention)

if __name__ == '__main__':
    root = sys.argv[-1]
    print('.')
    tree(root)

