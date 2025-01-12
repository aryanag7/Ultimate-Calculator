#!/usr/bin/python3

# Made by Jordan Leich on 6/1/2021

# Imports
import algebra
import calculator
import conversions
import restart
import end
import colors
import stocks


def start():
    choice = int(input('''
All Calculators and Converters!
(1) Basic Arithmetic Math (Add, Subtract, Multiply, Divide)
(2) Algebra (Slope)
(3) All Converters (Temperature, Mass, Length, Volume, Youtube Video & Audio)
(4) Stock Market Shares Calculator
(5) Restart
(6) Exit
Which calculator would you like to use: '''))
    print()

    if choice == 1:
        calculator.start()
    elif choice == 2:
        algebra.start()
    elif choice == 3:
        conversions.start()
    elif choice == 4:
        stocks.start()
    elif choice == 5:
        restart.restart()
    elif choice == 6:
        end.end()
    else:
        print(colors.red + 'User input error found... Restarting user input choice...\n', colors.reset)
        start()


start()
