function [Ah, Bh, Ch, Dh] = controller_canonical(A,B,C,D)

Ctrl = controllability(A,B);
Ah = inv(Ctrl) * A * Ctrl;
Bh = inv(Ctrl) * B;
Ch = C * Ctrl;
Dh = D;

end
