import subprocess
from grammar.nonterminal import S
from grammar.terminal import Terminal
from data_generators.generators import ResumeDataGenerator
import json
import os

LATON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "laton")

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Terminal):
            return obj.value
        return super().default(obj)

def generate_resume(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    output_filename = os.path.join(output_folder, "generated_resume")
    
    # Generate the resume content
    doc = S()
    doc.expand()
    ResumeDataGenerator().generate(doc.context)

    # Write JSON
    with open(f"{output_filename}.json", 'w') as f:
        json.dump(doc.context, f, cls=CustomJSONEncoder, indent=2)

    # Write LaTeX
    tex = doc.to_latex()
    with open(f"{output_filename}.tex", "w") as f:
        f.write(tex)

    # compile Latex
    subprocess.run([LATON_PATH, "generated_resume.tex"], cwd=output_folder)
    


if __name__ == "__main__":
    generate_resume(".")
    
