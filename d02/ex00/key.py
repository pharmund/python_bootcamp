class key:
    passphrase: str
    passphrase = "zax2rulez"
    def __init__(self):
        passphrase = "zax2rulez"

    def __str__(self):
        return "GeneralTsoKeycard"

    def __len__(self):
        return 1337

    def __gt__(self, other):
        return 9001 > other

    def __getitem__(self, item):
        if item == 404:
            return 3

if __name__ == "__main__":
    a = key()
    assert len(a) == 1337
    assert a[404] == 3
    assert a > 9000
    assert a.passphrase == "zax2rulez"
    assert str(a) == "GeneralTsoKeycard"
