import subprocess
from grammar.nonterminal import S
from grammar.terminal import Terminal
import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Terminal):
            return obj.value
        return super().default(obj)

def main():
    filename = "generated_resume.tex"
    doc = S()
    doc.expand()
    with open('data.json', 'w') as f:
        json.dump(doc.context, f, cls=CustomJSONEncoder, indent=2)
    tex = doc.to_latex()
    print("HERE")
    with open(filename, "w") as f:
        f.write(tex)
    result = subprocess.run(['./laton', filename])

if __name__ == "__main__":
    main()
    
