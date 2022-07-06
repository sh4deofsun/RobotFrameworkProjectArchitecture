*** Settings ***
Library  myLib.py

*** Test Cases ***
Demo Preprod
    Set Environment  preprod
    Assign To Preprod
    Log  Preprod

Demo Test
    Assign To Test
    Log  Test

Demo Library
    Import Libraries  Collections
    Set To Dictionary  ${D1}  key=value  second=2

Demo Variable
    Import Variables  Deneme