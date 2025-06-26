from logic import *

# Define symbols for each character being a Knight or a Knave
AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")
BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")
CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
knowledge1 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
# Puzzle 2
knowledge2 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # A says "We are the same kind"
    Implication(AKnight, Or(
        And(AKnight, BKnight),
        And(AKnave, BKnave)
    )),
    Implication(AKnave, Not(Or(
        And(AKnight, BKnight),
        And(AKnave, BKnave)
    ))),

    # B says "We are of different kinds"
    Implication(BKnight, Or(
        And(AKnight, BKnave),
        And(AKnave, BKnight)
    )),
    Implication(BKnave, Not(Or(
        And(AKnight, BKnave),
        And(AKnave, BKnight)
    )))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave." (unknown which)
# B says "A said 'I am a knave.'" and "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # A either said "I am a knight" or "I am a knave"
    # Case 1: A said "I am a knight"
    Implication(AKnight, AKnight),
    # Case 2: A said "I am a knave"
    Implication(AKnave, Not(AKnave)),  # contradiction for a Knight saying they are a Knave

    # B says A said "I am a knave" and C is a knave
    Implication(BKnight, And(AKnave, CKnave)),
    Implication(BKnave, Not(And(AKnave, CKnave))),

    # C says A is a knight
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

# List of all puzzles and their knowledge
puzzles = [
    ("Puzzle 0", knowledge0),
    ("Puzzle 1", knowledge1),
    ("Puzzle 2", knowledge2),
    ("Puzzle 3", knowledge3)
]

def main():
    puzzle_symbols = [
        [AKnight, AKnave],
        [AKnight, AKnave, BKnight, BKnave],
        [AKnight, AKnave, BKnight, BKnave],
        [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    ]
    for (name, knowledge), symbols in zip(puzzles, puzzle_symbols):
        print(name)
        for symbol in symbols:
            if model_check(knowledge, symbol):
                print(f"{symbol.name}")

if __name__ == "__main__":
    main()
