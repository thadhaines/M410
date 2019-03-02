function [I, error] = comTZ(f,fp,a,b,n)

h = (b-a)/n;
step = h/5;
% calculate endpoints
I = (f(a)+f(b))/2;

error = 0;
for i = 1:n-1
    %caclulate midpoints
    I = I + f(a+i*h);
    % test 5 points in bound for max xi
    cRange = a+(i-1)*h:step:a+i*h;
    error = error + h^3.*max(abs(fp(cRange)));
    
    
end
%scale by h
I = h*I;
end

