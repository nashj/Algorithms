function [Ah, Bh, Ch, Dh] = observer_canonical(A,B,C,D)

O = observability(A,C);
Ah = O * A * inv(O);
Bh = O * B;
Ch = C * inv(O);
Dh = D;

end
