class uint1024_t():
    # можно ли переопределить оператор сложения, вычитания и умножения
    # должна ли операция сложения быть коммутативной
    # как заранее можно определить размер вводимой строки
    def __init__(self, number=0) -> None:
        if type(number) == str:
            number = int(number)

        self.array = [0]*155
        i = 154
        while number:
            self.array[i] = number % 100
            number //= 100
            i -= 1

    def __add__(self, other):
        if type(other) != uint1024_t:
            other = uint1024_t(other)
        kek = uint1024_t()
        rem = 0
        for i in range(154, -1, -1):
            temp_res = self.array[i] + other.array[i] + rem
            rem = temp_res // 100
            kek.array[i] = temp_res % 100
        else:
            if rem != 0:
                raise Exception
        return kek

    def __sub__(self, other):
        if type(other) != uint1024_t:
            other = uint1024_t(other)
        kek = uint1024_t()
        rem = 0
        for i in range(154, -1, -1):
            temp_res = 100 + self.array[i] - other.array[i] - rem
            rem = int(not(temp_res // 100))
            kek.array[i] = temp_res % 100
        else:
            if rem != 0:
                raise Exception
        return kek

    def __mul__(self, other):
        if type(other) != uint1024_t:
            other = uint1024_t(other)
        kek = uint1024_t()
        flag = False
        for i in range(155):
            if other.array[i] != 0:
                flag = True
                other = other - 1
        while flag:
            flag = False
            for i in range(155):
                if other.array[i] != 0:
                    flag = True
                    other -= 1
            kek += self
        return kek

    def __str__(self):
        i = 0
        while i < len(self.array) and self.array[i] == 0:
            i += 1
        if i == len(self.array):
            return '0'
        else:
            res = str(self.array[i])
            i += 1
        while i != len(self.array):
            res += str(self.array[i] // 10)
            res += str(self.array[i] % 10)
            i += 1
        return res


n1 = uint1024_t(10)
n2 = uint1024_t(2**102)
print(n2)
print(str(n2) == str(2**1024 - 21))
