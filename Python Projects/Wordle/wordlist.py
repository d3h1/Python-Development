import pathlib
import sys
from string import ascii_letters

in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])

words = sorted(
    {
        word.lower()
        for word in in_path.read_text(encoding='utf-8').split()
        if all(letter in ascii_letters for letter in word)
    },
    # This allows only letters from A-Z, does not pass ASCII chars
    key = lambda word: (len(word), word),
    
    # can use re.fullmatch(r"\w+", word): to give other languages a go
)
out_path.write_text("\n".join(words))