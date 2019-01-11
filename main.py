import fire

from ML import test


class CLI:
    def test(self, msg: str = "Hello World", digit: int = 0, shuffle: bool = False):
        test(digit, shuffle)
        print(msg)


def main():
    fire.Fire(CLI)
