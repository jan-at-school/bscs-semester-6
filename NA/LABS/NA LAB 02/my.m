syms x
f = cos(x);
t1 = (taylor(f, x, 'Order', 2+1));
t2 = (taylor(f, x, 'Order', 4+1));
t3 = (taylor(f, x, 'Order', 6+1));
fplot([f t1 t2 t3])
