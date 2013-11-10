function [out] = total_least_squares(X,Y)

N = size(X,2);
Z = [X Y];
[U,S,V] = svd(Z);
Vxy = V(1:N,N+1:end);
Vyy = V(N+1:end,N+1:end);
out = -Vxy * inv(Vyy);

end