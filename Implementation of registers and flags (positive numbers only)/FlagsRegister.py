class FlagsRegister:
    def __init__(self):
        self.zero = False
        self.negative = False
        self.overflow = False

    def update(self, value: list, overflow_occurred: bool = False):
        # Проверка флага zero (все биты равны 0)
        self.zero = all(bit == 0 for bit in value)

        # Флаг negative всегда False, так как работаем только с положительными числами
        self.negative = False

        # Флаг overflow устанавливается, если переполнение произошло
        self.overflow = overflow_occurred

    def __str__(self):
        return f"Z: {int(self.zero)}, N: {int(self.negative)}, O: {int(self.overflow)}"
