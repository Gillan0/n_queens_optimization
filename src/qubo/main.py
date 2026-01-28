# Environment variable dependency
import os
from dotenv import load_dotenv

# Amplify dependencies
from amplify import VariableGenerator, AmplifyAEClient, ConstraintList
from amplify import equal_to, less_equal, solve

# Import environment variables 
load_dotenv()
token = os.getenv("FIXSTARS_TOKEN")

# Global variables declaration
N = 91

# Board initialization
gen = VariableGenerator()
board = gen.array("Binary", shape=(N, N))

# Constraints initialization
constraints = ConstraintList()

# Row constraints 
for i in range(0,N):
    row_sum = 0
    for j in range(0,N):
        row_sum += board[i,j]
    constraints += equal_to(row_sum, 1)

# Column constraints 
for j in range(0,N):
    col_sum = 0
    for i in range(0,N):
        col_sum += board[i,j]
    constraints += equal_to(col_sum, 1)

# Diagonal constraints
for d in range(0, N):
    diag_sum = 0
    for k in range(0, N-d):
        diag_sum += board[k,k+d]
    constraints += less_equal(diag_sum, 1)

for d in range(1, N):
    diag_sum = 0
    for k in range(0, N-d):
        diag_sum += board[k+d,k]
    constraints += less_equal(diag_sum, 1)

for d in range(0, N):
    diag_sum = 0
    for k in range(0, N-d):
        diag_sum += board[N-d-k-1, k]
    constraints += less_equal(diag_sum, 1)

for d in range(1, N):
    diag_sum = 0
    for k in range(0, N-d):
        diag_sum += board[N-k-1,k+d]
    constraints += less_equal(diag_sum, 1)

model = constraints

# Initializing and calling the client solver
client = AmplifyAEClient()
client.token = token
client.parameters.time_limit_ms = 10000    # Set run time to 10000 ms

print("Calling solver ...")
result = solve(model, client)
best = result.best

print(f"Execution time: {result.execution_time} seconds")
print(f"Best solution :\n{board.evaluate(result.best.values)}")
