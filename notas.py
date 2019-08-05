import pandas as pd
import numpy as np


def __main__():
    #TODO Adicionar o arquivo HTML
    data = pd.read_html(input('Path do HTML_Boletim: '))[0]
    materias = getMaterias(data)
    provas = 'Nac 1º,AM 1º,PS 1º,Nac 2º,AM 2º,PS 2º'.split(',')
    boletim = pd.DataFrame(np.zeros((len(materias), len(provas))), materias, provas)


   #TODO ADICIONAR AS NOTAS NO BOLETIM
    cout = 0
    for i in range(len(provas)):
        setGrades(boletim, materias, provas[i], takeGrades(data)[cout])
        cout += 1

    #TODO INCREMENTAR Falta PS p/6, Médias, total
    boletim['MD 1º'] = boletim['Nac 1º'] * 0.2 + boletim['AM 1º'] * 0.3 + boletim['PS 1º'] * 0.5
    boletim['MD 2º'] = boletim['Nac 2º'] * 0.2 + boletim['AM 2º'] * 0.3 + boletim['PS 2º'] * 0.5
    boletim['PS 1º p/6'] = (6 - boletim['MD 1º']) / 0.5
    boletim['PS 2º p/6'] = (6 - boletim['MD 2º']) / 0.5
    boletim['Total'] = boletim['MD 1º'] + boletim['MD 2º']
    boletim.to_excel('Boletim.xlsx', sheet_name='1')
    print(boletim)


def getMaterias(data):
    lista = []
    for i in range(9):
        lista.append(data.loc[i+1][0])
    return lista

def takeGrades(data):
    nac1 = (getGrades(data, 1, 1))  # Get nacs 1ºS
    am1 = (getGrades(data, 1, 2))  # Get am 1ºS
    ps1 = (getGrades(data, 1, 3))  # Get ps 1ºS
    nac2 = (getGrades(data, 2, 1))  # Get nacs 2ºS
    am2 = (getGrades(data, 2, 2))  # Get am 2ºS
    ps2 = (getGrades(data, 2, 3))  # Get ps 2ºS
    allnotas = [nac1, am1, ps1, nac2, am2, ps2]
    return allnotas

def getGrades(data, semestre, tipo): #TIPO (nac = 1, am = 2, ps = 3)
    grades = []
    x = tipo if semestre == 1 else tipo + 5
    for i in range(9):
        grades.append(data.loc[i+1][x])
    return grades

def setGrades(boletim, materias, prova, notas):
    cout = 0
    for m in materias:
        if notas[cout] == '-':
            r = 0
        else:
            r = float(notas[cout]) if float(notas[cout]) <= 10 else float(notas[cout])/10
        boletim.loc[m, prova] = r
        cout += 1

    return boletim


#------------------------------------------------------------------------------------------------- TODO EXEC
__main__()

