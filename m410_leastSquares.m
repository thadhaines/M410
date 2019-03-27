%%  m410_leastSquares.m
%   Thad Haines         m410
%   Program Purpose:    Matlab linear least squares calculation, and plot

%
%   History:
%   03/13/19    12:46   init
%   03/13/19    13:31   finish

%% init
clear; format compact; clc; close all;
%% Knowns
% Change these according to your function and desired interval
f = @(x) 2.*sin(10.*x+1)+1;

x0 = 0;
x9 = (pi/5)*10;

%% Process- Nothing below here should have to be changed
x = linspace(x0,x9,10)'; % Create 10 equally spaced values on interval
x_hres = linspace(x0,x9,100); % create higher res interval for plotting

y = f(x); % find y values for each x value

Z = [ones(size(x,1),1) x ]; % Creation of Z according to class procedure

coef = (Z'*Z)\(Z'*y); % MATLAB solving for coefficients
b = coef(1);
m = coef(2);
g = @(x) m.*x+b; % estimated line of best fit from least squares method

%% Calculation of test point errors
% point 1 (note MATLAB doesn't do indexing from zero as HW would suggest)
tP1 = (x(1)+x(2))/2;
actualP1 = f(tP1);
estP1 = g(tP1);
exactErrP1 = abs(actualP1-estP1);

% point 2
tP2 = (x(5)+x(6))/2;
actualP2 = f(tP2);
estP2 = g(tP2);
exactErrP2 = abs(actualP2-estP2);

% point 3
tP3 = (x(9)+x(10))/2;
actualP3 = f(tP3);
estP3 = g(tP3);
exactErrP3 = abs(actualP3-estP3);

%% Terminal output to match HW 
fprintf('x0 \t\t\tx9 \t\t\tF(pt1)\t\tpt1Err \t\tF(pt2)\t\tpt2Err \t\tF(pt3)\t\tpt3Err\n')
fprintf('%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\t%.2e\n',...
    x0,x9,actualP1,exactErrP1,actualP2,exactErrP2,actualP3,exactErrP3)

%% Plot of known and estimated functions
figure
plot(x_hres,f(x_hres),'k.-') % plot of high resolution function on interval
hold on
plot(x,g(x),'ms:','linewidth',2) % plot of estimated line
grid on
plot(tP1,f(tP1),'gp','markersize',10,'linewidth',3) % test points
plot(tP2,f(tP2),'gp','markersize',10,'linewidth',3)
plot(tP3,f(tP3),'gp','markersize',10,'linewidth',3)
legend({'Actual f(x)','Least Squares Approx.','Test Points'},'location','best')
title({['f = ',func2str(f)];...
    ['Interval = [', num2str(x0),', ',num2str(x9),']']}) %fancy auto-title
set(gca,'FontSize',13)
%set(gcf,'Position',[2034 372 560 420])