import random

def guess():
    words = ["computer", "sweet", "darling", "evolution", "happiness", "joy", "satan", "gravity", "brother",
    "mountain", "ocean", "desert", "volcano", "rainforest", "galaxy", "blackhole", "satellite",
    "atom", "molecule", "neutron", "telescope", "internet", "software", "hardware", "encryption",
    "batman", "superman", "spiderman", "thor", "wolverine", "zeus", "poseidon", "hercules", "odin",
    "dragon", "wizard", "unicorn", "mermaid", "elf", "pneumonia", "juxtaposition", "onomatopoeia"]
    attempts = 8
    trial = 0

    print("\n Welcome Friend! Prepare for the Best. ")

    word = random.choice(words).lower()  # Pick a random word
    reveal_one = max(1, len(word) // 3)  # Reveal at least 1 letter
    guessed_word = list("-" * len(word))  # Hidden word as dashes

    revealed = random.sample(range(len(word)), reveal_one)  # Pick random positions to reveal

    for i in revealed:
        guessed_word[i] = word[i]  # Reveal those positions

    print(f"\n Hint: {' '.join(guessed_word)}\n")  # Show the hint with some revealed letters

    while trial < attempts:
        inputter = input(" Enter the full word: ").strip().lower()

        if inputter == word:
            print(f"\n Correct! The word was '{word}'. You won! \n")
            return 

        else:
            trial += 1
            remaining_attempts = attempts - trial
            print(f" Wrong! Try again.")
            print(f" You have {remaining_attempts} attempts left.\n")

    print(f"\n Game Over! The correct word was '{word}'. Better luck next time!\n")


guess()
