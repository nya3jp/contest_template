import sys

from sqrt import constraints


def main():
    _, out_file, golden_file = sys.argv[1:]
    with open(out_file, 'r') as f:
        a = float(f.read().strip())
    with open(golden_file, 'r') as f:
        b = float(f.read().strip())
    assert abs(a - b) <= constraints.VALUE_MAX, 'out=%f, ans=%f, diff=%f' % (a, b, abs(a - b))


if __name__ == '__main__':
    main()
