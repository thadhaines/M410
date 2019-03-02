function [  ] = compTZwErr( f,fp, F, a, b, n )
%compTZwErr calculate and display results with error aprx
%   f = function to integrate
%   fp = first derivative of f
%   F = 1st integral of f
%   a, b = bracket to integrate
%   n = number of composites

h= (b-a)/n;
[cTZapprox, error] = comTZ(f,fp,a,b,n);
exact = F(b)-F(a);
exactErr = abs(exact-cTZapprox);
fprintf('a  \t\t\tb   \t\tn   \t\th  \t\t\tAprx  \t\tErrB  \t\tExactErr  \tintegral\n')
fprintf('%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t\n' ...
    ,a,b,n,h,cTZapprox, error,exactErr,exact)
end

