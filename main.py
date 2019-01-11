import fire

from ML import test


class CLI:
    def test(self, msg, args: str = "yes"):
        test(args)
        print(msg)


def main():
    fire.Fire(CLI)
