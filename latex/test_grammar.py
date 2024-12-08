import subprocess
from grammar.nonterminal import S
from grammar.terminal import Terminal
from data_generator import ResumeDataGenerator
import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Terminal):
            return obj.value
        return super().default(obj)


def main():
    filename = "generated_resume.tex"

    #We could make a wrapper class for these three steps...
    doc = S()
    doc.expand()
    ResumeDataGenerator().generate(doc.context)


    # write JSON
    with open('generated_resume_data.json', 'w') as f:
        json.dump(doc.context, f, cls=CustomJSONEncoder, indent=2)

    # write LaTeX
    tex = doc.to_latex()
    with open(filename, "w") as f:
        f.write(tex)
    result = subprocess.run(['./laton', filename])

    # Done!
    print(result)


if __name__ == "__main__":
    main()
    
