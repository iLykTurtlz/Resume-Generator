
class LatexWriter:
    var_template = "\\newcommand{\\%s}{%s}\n"

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath

    def write(self, var_name: str, value: str) -> None:
        with open(self.filepath, "a") as f:
            f.write(LatexWriter.var_template % (var_name, value))

    def write_all(self, var_values: dict[str, str]) -> None:
        with open(self.filepath, "a") as f:
            for var, value in var_values.items():
                f.write(LatexWriter.var_template % (var, value))



