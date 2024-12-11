class Parser:
    def parse_grammar(self, filepath: str) -> dict:
        try:
            with open(filepath, "r") as f:
                lines = [line for line in f.read().split("\n") if line != ""]

            rules = {}
            for line in lines:
                lhs, rhs = line.split("->")
                ruleset = []
                for right_side in rhs.split("|"):
                    pieces = right_side.strip().split(" ")
                    expansion = tuple(pieces[:-1])
                    proba = float(pieces[-1].strip("[").strip("]"))
                    ruleset.append((expansion, proba))
                rules[lhs.strip()] = ruleset
            return rules

        except Exception as e:
            print(f"{filepath} failed to parse:\n")
            raise e
