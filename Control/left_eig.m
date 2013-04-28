function [L] = left_eig(A)

[E,V] = eig(A);
L = inv(V);

end
