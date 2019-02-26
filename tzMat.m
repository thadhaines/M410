%%  tzMat.m
%   Thad Haines         M410
%   Program Purpose:    calculate integral via trapezodail method
%                       created only to troubleshoot ipy scripts...

%
%   History:
%   02/25/19    18:51   init

%% init
clear; format compact; clc; close all;

%% Knowns
f = @(x) 2*sin(10.*x+1)+1;
fpp = @(x) -200.*sin(10.*x+1);

F = @(x) x - (1/5).*cos(10.*x+1);

tz = @(x0,h) 0.5*h*(f(x0)+f(x0+h));
tzErr = @(xi, h) h^3 .* fpp(xi);

