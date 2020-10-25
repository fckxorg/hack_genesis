from random import choice


class Deductor:
    def __init__(self):
        self.rules = list()

    def add_rule(self, rule, value):
        self.rules.append((rule, value))

    def set_fallback(self, value):
        self.fallback = value

    def __call__(self, value):
        values = list(map((lambda pair: pair[1]), filter(
            (lambda f: f[0](value)), self.rules)))

        if len(values) == 1:
            return values[0]
        elif len(values) > 1:
            print("Note: several values are possible for given predicates. Perhaps list of predicates is ill-formed")
            return choice(values)
        else:
            if self.fallback is not None:
                return self.fallback
            else:
                raise ValueError("No viable option")
