import fire


class CLI:
    def __init__(self, msg):
        self.lol = msg


if __name__ == '__main__':
    cli = fire(CLI("mao"))
    print(CLI("lol").lol)
