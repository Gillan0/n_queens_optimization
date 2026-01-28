# N-queens problem

## Introduction 
This repository is meant to host the source code of my final report for the "Efficient Search Methods
in Artificial Intelligence" course hosted at the University of Tokyo.

## File architecture
```
├── README.md
├── docs # Report related files
│   ├── main.pdf # Pdf rendition of the LaTeX file
│   ├── main.tex # Original LaTeX file
│   └── ressources # Images used in the report
└── src # Source code
    ├── graph.py # Draw the different graphs of the report.
    ├── minizinc
    │   ├── baseline_mode.mzn # Baseline Minizinc model
    │   └── main.mzn # Boolean variable of the MiniZinc model
    └── qubo
        ├── main.py # QUBO model using fixstars
        ├── .env # Holds the API token to access the fixstars API
        └── requirements.txt # Dependencies of QUBO model
``` 

## Running the programs
### MiniZinc
Copy and paste the content of the model you want into a MiniZinc editor and execute it.
### QUBO 
In order to run the QUBO program, one first needs a Fixstars account in order to get a token to use their API.
Firstly, change the token in ```src/qubo/.env```.
```
FIXSTARS_TOKEN = "..." # Insert your own Fixstars token
```
Then move to the correct directory and create a python virtual environment.
```
cd src/qubo
python3 -m venv .venv
```
Swithc to the virtual environment 
```
source .venv/bin/activate
```
Install dependencies and run the program. You can change the size of the problem before.
```
pip install -r requirements.txt
python3 main.py 
```
Once you're done, you can exit the virtual environment with 
```
deactivate
```