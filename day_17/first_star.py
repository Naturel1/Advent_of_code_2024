class Machine:
    def __init__(self, program: list[int], registers: dict[str, int]):
        self.program = program
        self.registers = registers
        self.pointer = 0

    def run(self) -> list[int]:
        result = []
        try:
            while self.pointer < len(self.program):
                print(f"A: {self.registers['A']}, B: {self.registers['B']}, C: {self.registers['C']}, Pointer: {self.pointer}")
                opcode = self.program[self.pointer]
                if opcode == 0:
                    print("adv")
                    self.adv()
                    print(f"opcode 0, operand: {self.get_operand()}")
                elif opcode == 1:
                    print("bxl")
                    print(f"opcode 1, operand: {self.get_operand()}")
                    self.bxl()
                elif opcode == 2:
                    print("bst")
                    print(f"opcode 2, operand: {self.combo_operand()}")
                    self.bst()
                elif opcode == 3:
                    print("jnz")
                    print(f"opcode 3, operand: {self.get_operand()}")
                    self.jnz()
                elif opcode == 4:
                    print("bxc")
                    print(f"opcode 5, operand: {self.get_operand()}")
                    self.bxc()
                elif opcode == 5:
                    print("out")
                    print(f"opcode 4, operand: {self.combo_operand()}")
                    result.append(self.out())
                elif opcode == 6:
                    print("bdv")
                    print(f"opcode 6, operand: {self.get_operand()}")
                    self.bdv()
                elif opcode == 7:
                    print("cdv")
                    print(f"opcode 7, operand: {self.get_operand()}")
                    self.cdv()

            return result
        except IndexError:
            print(f"register A: {self.registers['A']}, B: {self.registers['B']}, C: {self.registers['C']} halted")
            return result


    def get_operand(self) -> int:
        return self.program[self.pointer + 1]

    def combo_operand(self):
        operand = self.get_operand()
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.registers["A"]
        elif operand == 5:
            return self.registers["B"]
        elif operand == 6:
            return self.registers["C"]
        elif operand == 7:
            raise ValueError("Operand 7 not supported")

    def adv(self) -> None:
        self.registers["A"] = self.registers["A"] // (2**self.combo_operand())
        self.pointer += 2

    def bxl(self) -> None:
        operand = self.get_operand()
        self.registers["B"] = self.registers["B"] ^ operand
        self.pointer += 2

    def bst(self) -> None:
        self.registers["B"] = self.combo_operand() % 8
        self.pointer += 2

    def jnz(self) -> None:
        if self.registers["A"] != 0:
            self.pointer = self.get_operand()
        else:
            self.pointer += 2

    def bxc(self) -> None:
        self.registers["B"] = self.registers["B"] ^ self.registers["C"]
        self.pointer += 2

    def out(self) -> int:
        result = self.combo_operand() % 8
        self.pointer += 2
        return result

    def bdv(self) -> None:
        self.registers["B"] = self.registers["A"] // (2**self.combo_operand())
        self.pointer += 2

    def cdv(self) -> None:
        self.registers["C"] = self.registers["A"] // (2**self.combo_operand())
        self.pointer += 2

def import_data(path: str) -> tuple[list[int], dict[str, int]]:
    registers = {}
    with open(path, 'r') as file:
        raw_registers, raw_program = file.read().strip().split("\n\n")
    for line in raw_registers.split("\n"):
        data = line.strip().split()
        registers[data[1][0]] = int(data[2])
    temp = raw_program.strip().split(" ")
    program = [int(x) for x in temp[1].split(",")]
    return program, registers

def main():
    program, registers = import_data("input.txt")
    print(registers)
    print()
    print(program)
    machine = Machine(program, registers)
    result = machine.run()
    print(f"The result is : {result}")
    # print(f"string result : {''.join(map(str, result))}")

if __name__ == "__main__":
    main()