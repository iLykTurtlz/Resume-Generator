import subprocess
from grammar.nonterminal import S

def main():
    filename = "generated_resume.tex"
    doc = S()
    doc.expand()
    tex = doc.to_latex()
    print("HERE")
    with open(filename, "w") as f:
        f.write(tex)
    result = subprocess.run(['./laton', filename])

if __name__ == "__main__":
    main()
    
