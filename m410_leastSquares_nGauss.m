%%  m410_leastSquares_nGauss.m
%   Thad Haines         m410
%   Program Purpose:    Matlab linear least squares calculation, and plot

%   History:
%   03/13/19    12:46   init
%   03/13/19    13:31   finish
%   03/27/19    13:12   change to perform Naive Gauss Method least squares
%   03/27/19    13:36   finish*2

%% init
clear; format compact; clc; close all;
%% Knowns
% Change these according to your function and desired interval
f = @(x) 2.*sin(10.*x+1)+1;
%f = @(x) 1./x;
%f = @(x) nthroot(x,3) # use to avoid complex results

x0 = -1;
x9 = x0+2*(pi/5);

%% Process- Nothing below here should have to be changed
x = linspace(x0,x9,10)'; % Create 10 equally spaced values on interval
x_hres = linspace(x0,x9,500); % create higher res interval for plotting

y = f(x); % find y values for each x value

Z = [ones(size(x,1),1), x, x.^2 ]; % Creation of Z according to class procedure

coef = (Z'*Z)\(Z'*y); % MATLAB solving for coefficients <- Not used

A = Z'*Z;
b = Z'*y;
a = GaussNaive(A, b);

g = @(x) a(1)+a(2).*x + a(3).*x.^2; % estimated line of best fit

%% Calculation of residuals
r = norm(Z*a-y);
rt = norm(Z'*Z*a-Z'*y); % seems super wrong sometimes...

%% Terminal output to match HW 
fprintf('x0 \t\t\tx9 \t\t\ta0\t\t\ta1 \t\t\ta2\t\t\tResidual\tTransposed Residual\n')
fprintf('%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\n',...
    x0,x9,a(1),a(2),a(3),r, rt)

%% Plot of known and estimated functions
figure
plot(x_hres,f(x_hres),'.-','color',[.7 .7 .7]) % plot of actual f on interval
hold on
plot(x,f(x),'kp--')
hold on
plot(x,g(x),'ms:','linewidth',2) % plot of estimated line
grid on

legend({'Actual f(x)','Sampled f(x)','Least Squares Approx.',},'location','best')
title({['f = ',func2str(f)];...
    ['Interval = [', num2str(x0),', ',num2str(x9),']']}) %fancy auto-title
set(gca,'FontSize',13)