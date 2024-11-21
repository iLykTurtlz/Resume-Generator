import requests
import zipfile
import os
import subprocess


#from latex_writer import LatexWriter
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



def create_zip(main_tex, dependencies, zip_path="resume.zip", base_dir="."):
    with zipfile.ZipFile(zip_path, "w") as zf:
        zf.write(os.path.join(base_dir, main_tex), os.path.basename(main_tex))
        for dep in dependencies:
            zf.write(os.path.join(base_dir, dep), os.path.basename(dep))
    return zip_path


def compile_latex(zip_file, main_tex="resume2.tex", output_pdf = "resume.pdf"):
    url = "http://latexonline.cc/compile"
    with open(zip_file, "rb") as file:
        response = requests.post(
            url, 
            files={"file": file},
            data={"target": main_tex}
        )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

    # Save the output PDF
    if response.status_code == 200:
        with open(output_pdf, "wb") as pdf:
            pdf.write(response.content)
        print(f"PDF compiled successfully: {output_pdf}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

class Variable:
    def __init__(self, name):
        self.name = name

class Section:
    def __init__(self, format_string, variables):
        self.format_string = format_string
        self.variables = variables

    def sub(self, number):
        new_str = self.format_string
        for i, variable in enumerate(self.variables):
            new_str = new_str.replace(f"var_{i}", "{\\" + f"{variable.name}{number}" + "}")
        print(new_str)
        return new_str

SECTIONS = {"SUMMARY": Section(f"var_0 var_1\\\\", [Variable("sectionSummary"), Variable("bullshit")])}

def generate_new_section_string(section, amount):
    new_str = ""
    for i in range(amount):
        new_str += section.sub(i)
    return new_str

def expand_sections(template_path, sections, amounts, output_template_path="tmp.tex"):
    with open(template_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    for amount, section in zip(amounts, sections):
        section_line = lines.index(f"% SECTION_{section} %")
        if section_line == -1:
            return
        lines[section_line] = generate_new_section_string(sections[section], amount)
    with open(output_template_path, "w") as f:
        f.write("\n".join(lines))
    return output_template_path

def main() -> None:
    dependency_path = "variables.tex"
    lw = LatexWriter(dependency_path)
    values = {
        "fullname" : "Paul Jarski",
        "email" : "pjarski@calpoly.edu",
        "phone" : "612-437-8276",
        "github" : "www.github.com/iLykTurtlz",
        "linkedin" : "www.linkedin.com/in/paul-jarski-a4a04386/",
        "city" : "San Luis Obispo",
        "state" : "CA",
        "zipcode" : "93410",
        "country" : "USA",
        "selfSummary0" : "I am a consumate badass.",
        "bullshit0": "BS 1",
        "selfSummary1": "fdsjiofjdso",
        "bullshit1": "BS 2",

        "companyA" : "Company A",
        "companyACity" : "Los Angeles",
        "companyAState" : "CA",
        "jobTitleA" : "Data Scientist",
        "companyAStart" : "December 2024",
        "companyAEnd" : "June2025",

        "universityName" : "California Polytechnic State University",
        "universityCity" : "San Luis Obispo",
        "universityState" : "CA",
        "degreeName" : "B.S. Computer Science",
        "degreeStart" : "September 2023",
        "degreeEnd": "June 2027",
        "GPA" : "3.97"
    }
    lw.write_all(values)

    expand_sections("resume_copy.tex", SECTIONS, [2])

    # zipped = create_zip("resume2.tex", [dependency_path], "resume.zip", base_dir=".")
    # compile_latex(zipped, "resume.pdf")

    # zipped = create_zip("test.tex", ["variables.tex"], "test_resume.zip")
    # compile_latex(zipped, "test.tex", "test.pdf")


    #LATON solution
    result = subprocess.run(['./laton', 'tmp.tex', 'variables.tex'])







if __name__ == "__main__":
    main()