% Size of board
int: N = 10;

% Board variables
array[1..N, 1..N] of var 0..1: positions;

% 1 queen per row / column
constraint forall (i in 1..N) (sum (j in 1..N) (positions[i, j]) == 1);
constraint forall (j in 1..N) (sum (i in 1..N) (positions[i, j]) == 1);

% Diagonal constraints
constraint forall (d in 0..(N-1)) (sum (k in 0..(N-d-1)) ( positions[1+k, 1+k+d]  ) <= 1);
constraint forall (d in 1..(N-1)) (sum (k in 0..(N-d-1)) ( positions[1+k+d, 1+k]  ) <= 1);
constraint forall (d in 0..(N-1)) (sum (k in 0..(N-d-1)) ( positions[N-d-k, 1+k]  ) <= 1);
constraint forall (d in 1..(N-1)) (sum (k in 0..(N-d-1)) ( positions[N-k, 1+k+d]  ) <= 1);

solve satisfy;
 
output [show2d(positions)];