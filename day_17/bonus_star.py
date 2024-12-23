import copy

# author : https://topaz.github.io/paste/#XQAAAQDGDAAAAAAAAAA0m0pnuFI8c82uRLGFT29CJ7fiGSnteloQEwWngOs7kGOyG45+0ZzntpM5ile28s2PCa5H01x0OQ9Q6v/2LyL/gOCczVbvsvLNI8Qst9qTJaHpblyjmNH3OiAjkPNpqszWPs7DND88EXFvD33KFRnS+atBlJL1yOhgt0DsQd3zSuOLFzEpWKPrECNaf7AQXCJaUUA6YkB3/o9n3WB4ixQw6cZn/m2r4ygzCYANhOswFdTiZYYAheNTS6gbubxZSV8X03n3UqNEef666uDiPF6AQ5gRjggrB27bPJ8KDRwlCBxeP+hR5y8fwnMSeSKH1GsmejhiMkvRn2AhDcIosW4tGjHJxcZ/ZPhgxPiUtZNptuhY5Za7VRiSs/RJdHQ7wCNHA8TDTz/CqoXXH2GtQTDWalHIts6zIDYqppiE8lAMpL7aGLOQwBWDP7i4zrCMH1manqJJUkmk327dAnKXk8jPvYcMuHjC0MfyR+e+jHLpmg0eQmAHukIATDOGwf8I29E4YbuoOrlppyWswuQlO8oEJ6Yg6qNtWZAHZlztFuIKtLwILlLMvbfg43KMi2G7Bl6FQa3zvH0ic2/WnBuuuzeD4IU+NmpwQSCtxE7QDSJiSsvYxOB6UuEWZl0AzuvKajQJwJNNMiXb4bMkid0FaBHurHsTPXYtcfR4mKswqAsh9OmZDaaRuGhEio4K/D50XvuIiZAAtr4Ghyr/OtaeVC0Euu5tEKzH0hdpyBCnMLB4U96mAg8V3BsKg2G1H75ONMnsqbqWjYKuXv5lleFEdUM94sNcDD88VkEAzdCknqw+QEfSkc0xZUVdF654xXOrzZFLLgdAFT6qP0+COo3zJXyU/7uqqcEEe+m7fjAgrH6aSgWNBKVLQk5g72HxESdqhcyK4Hrc6T7dHF/5ckWVKJstKQtevqv8RdM4TIzE/4RQXvPD9hTlrTET2QZ04K4UqHGh0Fp1U95tZcGFk0pArr4GcoLwBascpkDJKNbdc72uiBM+VkxrkZwr0psufwRsy/wchrB9M7FUM6MajVB47z3vcXBQP8VdhzVKLybjICgqYsXCBmlNawK/1U1c03NKNyM3SYKPD71b5Udya6VuUEQI2qHSyd/qFEXgNYY5u+gBgUwjeS4Q63SbPhjPvX+Yox7AYzpiQWpwVLM9aiaECD8HyttK57KspUxwNwcfa6praODEytVlOFnVNY+dZn7EmqUFEqe4drPtRJu90UTuJ5lUi9oXtmftNPIMNqTs5kMzLT6KA3ftg2JPzyDBOrE//2BMdgA=

OriginalRegisterList = []
with open("input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        if Line.startswith("Reg"):
            _, _, A = Line.split()
            OriginalRegisterList.append(int(A))
        elif Line.startswith("Pro"):
            _, A = Line.split()
            Originalprogram = tuple(map(int, A.split(",")))
            CompareString = A
OriginalRegisterT = tuple(OriginalRegisterList)



def Program(RegA, RegisterTuple, Part):
    ProgramLength = len(Originalprogram)
    Register = {}
    for v, r in enumerate(["A","B","C"]):
        Register[r] = RegisterTuple[v]
    Pointer = 0
    OutputList = []
    Register["A"] = RegA

    def Combo(Operand):
        if Operand < 4:
            return Operand
        if Operand == 4:
            return Register["A"]
        if Operand == 5:
            return Register["B"]
        if Operand == 6:
            return Register["C"]
        else:
            print("7 combo detected")

    while Pointer < ProgramLength-1:
        PointerJump = True
        Operator, Operand = Originalprogram[Pointer:Pointer+2]
        if Operator == 0: #adv
            Numerator = Register["A"]
            Denom = 2**Combo(Operand)
            Register["A"] = Numerator // Denom
        elif Operator == 1: #bxl
            B = Register["B"]
            Register["B"] = B ^ Operand
        elif Operator == 2: #bst
            Register["B"] = Combo(Operand) % 8
        elif Operator == 3: #jnz
            if Register["A"] != 0:
                Pointer = Operand
                PointerJump = False
        elif Operator == 4: #bxc
            B, C = Register["B"], Register["C"]
            Register["B"] = B ^ C
        elif Operator == 5: #out
            Output = Combo(Operand) % 8
            if Part == 2:
                return Output, Register["A"]
            OutputList.append(Output)

        elif Operator == 6: #bdv
            Numerator = Register["A"]
            Denom = 2**Combo(Operand)
            Register["B"] = Numerator // Denom
        elif Operator == 7: #cdv
            Numerator = Register["A"]
            Denom = 2**Combo(Operand)
            Register["C"] = Numerator // Denom

        if PointerJump:
            Pointer += 2

    OutputString = ""
    for t in OutputList:
        OutputString += str(t)
        OutputString += ","
    OutputString = OutputString[:-1]
    if Part == 1:
        return OutputString
    else:
        return True, OutputString

Part1Answer = Program(OriginalRegisterT[0],OriginalRegisterT,1)


Place = len(Originalprogram)-1
CurrentRegAs = [0]

while Place >= 0:
    NextRegAs = []
    ExpectedOutput = Originalprogram[Place]
    #print(ExpectedOutput, Place)
    for RA in CurrentRegAs:
        NewRA = RA*8
        for y in range(8):
            CRA = NewRA + y
            NewOutput, PassedA = Program(CRA, OriginalRegisterT, 2)
            #print(CRA, NewOutput, NewOutput==ExpectedOutput, PassedA)
            if NewOutput == ExpectedOutput:
                NextRegAs.append(CRA)

    Place -= 1
    CurrentRegAs = copy.deepcopy(NextRegAs)

print(CurrentRegAs)

Part2Answer = min(CurrentRegAs)

print(Program(Part2Answer,OriginalRegisterT,1))

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")