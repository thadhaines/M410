function [x] = GaussNaive(A,b)
%A = coefficent matrix
%b = right hand side vector
%x = solution vector for system Ax=b

[m,n] = size(A);
if m~=n, error('Matrix A must be square'); end

nb = n+1;
Aug = [A b];
for k = 1:n-1
    for i = k+1:n
        factor = Aug(i,k)/Aug(k,k);
        Aug(i,k:nb) = Aug(i,k:nb)-factor*Aug(k,k:nb);
    end
end
x = zeros(n,1);
x(n) = Aug(n,nb)/Aug(n,n);
for i = n-1:-1:1
    x(i) = (Aug(i,nb)-Aug(i,i+1:n)*x(i+1:n))/Aug(i,i);
end

end

