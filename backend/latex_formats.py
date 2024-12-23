latex = {

"S": r'''
\documentclass[a4paper,11pt]{article}

%% Package imports
\usepackage{latexsym}
\usepackage{xcolor}
\usepackage{float}
\usepackage{ragged2e}
\usepackage[empty]{fullpage}
\usepackage{wrapfig}
\usepackage{lipsum}
\usepackage{tabularx}
\usepackage{titlesec}
\usepackage{geometry}
\usepackage{marvosym}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage{fancyhdr}
\usepackage{multicol}
\usepackage{graphicx}
\usepackage{cfr-lm}
\usepackage[T1]{fontenc}
\usepackage{fontawesome5}

%% Color definitions
\definecolor{darkblue}{RGB}{0,0,139}

%% Page layout
\setlength{\multicolsep}{0pt} 
\pagestyle{fancy}
\fancyhf{} %% clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\geometry{left=1.4cm, top=0.8cm, right=1.2cm, bottom=1cm}
\setlength{\footskip}{5pt} %% Addressing fancyhdr warning

%% Hyperlink setup (moved after fancyhdr to address warning)
\usepackage[hidelinks]{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=darkblue,
    filecolor=darkblue,
    urlcolor=darkblue,
}

%% Custom box settings
\usepackage[most]{tcolorbox}
\tcbset{
    frame code={},
    center title,
    left=0pt,
    right=0pt,
    top=0pt,
    bottom=0pt,
    colback=gray!20,
    colframe=white,
    width=\dimexpr\textwidth\relax,
    enlarge left by=-2mm,
    boxsep=4pt,
    arc=0pt,outer arc=0pt,
}

%% URL style
\urlstyle{same}

%% Text alignment
\raggedright
\setlength{\tabcolsep}{0in}

%% Section formatting
\titleformat{\section}{
  \vspace{-4pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-7pt}]

%% Custom commands
\newcommand{\resumeItem}[2]{
  \item{
    \textbf{#1}{\hspace{0.5mm}#2 \vspace{-0.5mm}}
  }
}

\newcommand{\resumePOR}[3]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1}\hspace{0.3mm}#2 & \textit{\small{#3}} 
    \end{tabular*}
    \vspace{-2mm}
}

\newcommand{\resumeSubheading}[4]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & \textit{\footnotesize{#4}} \\
        \textit{\footnotesize{#3}} &  \footnotesize{#2}\\
    \end{tabular*}
    \vspace{-2.4mm}
}

\newcommand{\resumeProject}[4]{
\vspace{0.5mm}\item
    \begin{tabular*}{0.98\textwidth}[t]{l@{\extracolsep{\fill}}r}
        \textbf{#1} & \textit{\footnotesize{#3}} \\
        \footnotesize{\textit{#2}} & \footnotesize{#4}
    \end{tabular*}
    \vspace{-2.4mm}
}

\newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-4pt}}

\renewcommand{\labelitemi}{$\vcenter{\hbox{\tiny$\bullet$}}$}
\renewcommand{\labelitemii}{$\vcenter{\hbox{\tiny$\circ$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*,labelsep=1mm]}
\newcommand{\resumeHeadingSkillStart}{\begin{itemize}[leftmargin=*,itemsep=1.7mm, rightmargin=2ex]}
\newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=*,labelsep=1mm,itemsep=0.5mm]}

\newcommand{\resumeSubHeadingListEnd}{\end{itemize}\vspace{2mm}}
\newcommand{\resumeHeadingSkillEnd}{\end{itemize}\vspace{-2mm}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-2mm}}
\newcommand{\cvsection}[1]{%%
\vspace{2mm}
\begin{tcolorbox}
    \textbf{\large #1}
\end{tcolorbox}
    \vspace{-4mm}
}

\newcolumntype{L}{>{\raggedright\arraybackslash}X}%%
\newcolumntype{R}{>{\raggedleft\arraybackslash}X}%%
\newcolumntype{C}{>{\centering\arraybackslash}X}%%

%% Commands for icon sizing and positioning
\newcommand{\socialicon}[1]{\raisebox{-0.05em}{\resizebox{!}{1em}{#1}}}
\newcommand{\ieeeicon}[1]{\raisebox{-0.3em}{\resizebox{!}{1.3em}{#1}}}

%% Font options
\newcommand{\headerfonti}{\fontfamily{phv}\selectfont} %% Helvetica-like (similar to Arial/Calibri)
\newcommand{\headerfontii}{\fontfamily{ptm}\selectfont} %% Times-like (similar to Times New Roman)
\newcommand{\headerfontiii}{\fontfamily{ppl}\selectfont} %% Palatino (elegant serif)
\newcommand{\headerfontiv}{\fontfamily{pbk}\selectfont} %% Bookman (readable serif)
\newcommand{\headerfontv}{\fontfamily{pag}\selectfont} %% Avant Garde-like (similar to Trebuchet MS)
\newcommand{\headerfontvi}{\fontfamily{cmss}\selectfont} %% Computer Modern Sans Serif
\newcommand{\headerfontvii}{\fontfamily{qhv}\selectfont} %% Quasi-Helvetica (another Arial/Calibri alternative)
\newcommand{\headerfontviii}{\fontfamily{qpl}\selectfont} %% Quasi-Palatino (another elegant serif option)
\newcommand{\headerfontix}{\fontfamily{qtm}\selectfont} %% Quasi-Times (another Times New Roman alternative)
\newcommand{\headerfontx}{\fontfamily{bch}\selectfont} %% Charter (clean serif font)

\begin{document}

%s

\end{document}
''',




# fullname, Contact2 - phone | email, Contact2 - linkedin | github, Contact1 or Contact2
"Head": r'''
%% Header
%s
\vspace{2mm}
''',

"Body": r'''
%% Body
%s
\vspace{2mm}
''',



"Objective": r'''
\section{\textbf{Objective}}
\vspace{1mm}
\small{
    %s
}
\vspace{-2mm}
''',



"Title": r'''
\begin{center}
    {\Huge\textbf{%s}}
\end{center}
\vspace{-6mm}
''',


"GeographicalInfoField": r'''
\begin{center}
    \small{
    %s
    }
\end{center}
\vspace{-6mm}
''',


#Phone and Email are terminal
"PhoneEmail": r'''
\begin{center}
    \small{
    %s | %s
    }
\end{center}
\vspace{-6mm}
''',

#LinkedInField, GitHubField are both nonterminal
"LinkedInGitHub": r'''
\begin{center}
    \small{
    %s | %s
    }
\end{center}
\vspace{-6mm}
''',


#href, visible_label
"LinkedInField": r'''
\socialicon{\faLinkedin} {%s}
''',


#href, visible_label
"GitHubField": r'''
\socialicon{\faGithub} {%s}
''',



"ProjectSection": r'''
\section{\textbf{Projects}}
\vspace{-0.4mm}
\resumeSubHeadingListStart
    %s
\resumeSubHeadingListEnd
''',

# description, tools
# either {Month Year} or {Month Year - Month Year}
# achievements
"Project" : r'''
\resumeProject
  {%s}
  {%s}
  {%s}
  %%{{}[\href{https://github.com/your-username/project-a}{\textcolor{darkblue}{\faGithub}}]}
  %s
''',

"ProjectAchievements": r'''
\resumeItemListStart
    %s
\resumeItemListEnd
''',


# \resumeSubheading
# {University Name}{City, Country}
# {Degree Name}{Month Year - Month Year}
# \resumeItemListStart
# \item GPA: X.XX/4.00
# \resumeItemListEnd

# Education: Institution | GeographicalInfoField | Degree Name | MMYYYY_Date | GPA
"EducationSection" : r'''
\section{\textbf{Education}}
\vspace{-0.4mm}
\resumeSubHeadingListStart

%s

\resumeSubHeadingListEnd
\vspace{-6mm}
''',

"Education": r'''
\resumeSubheading
    {%s}{%s}
    {%s}{%s}
\resumeItemListStart
\item GPA: %s
\resumeItemListEnd
''',

"ExperienceSection": r'''
\section{\textbf{Experience}}
\vspace{-0.4mm}
  \resumeSubHeadingListStart
  
  %s
  
  \resumeSubHeadingListEnd
\vspace{-6mm}
''',

"Experience": r'''
\resumeSubheading
    {{%s}}{%s}
    {%s}{%s}
    %s
''',

"ExperienceTasks": r'''
\resumeItemListStart
    %s
\resumeItemListEnd 
''',


"Skills" : r'''
\section{\textbf{Skills}}
\vspace{-0.4mm}
 \resumeHeadingSkillStart
    %s
 \resumeHeadingSkillEnd
''',

#comma separated
"ProgrammingLanguageSkills" : r'''
  \resumeSubItem{Programming Languages:}
    {%s}
''',

#comma separated
"WebTechnologySkills" : r'''
  \resumeSubItem{Web Technologies:}
    {%s}
''',

#comma separated
"DatabaseSystemSkills" : r'''
 \resumeSubItem{Database Systems:}
    {%s}
''',

#comma separated
"DataScienceMLSkills" : r'''
  \resumeSubItem{Data Science \& Machine Learning:}
    {%s}
''',

#comma separated
"CloudSkills" : r'''
  \resumeSubItem{Cloud Technologies:}
    {%s}
''',

#comma separated
"DevOpsSkills": r'''
 \resumeSubItem{DevOps \& Version Control:}
    {%s}
''',

#comma separated, two fields
"OtherSkills" : r'''
  \resumeSubItem{%s}
    {%s}
''',


"SelfSummarySection": r'''
\section{\textbf{Objective}}
\vspace{1mm}
\small{
%s
}
\vspace{-2mm}
''',






}
