import pandas as pd


def pk_bicimad(): 
    pk_bicimad = pd.read_csv('../datasets/pk_bicimad.csv')
    return pk_bicimad

def bicimadf(): 
    bicimad = pd.read_csv('../datasets/pk_bicimad.csv')
    return bicimadf

def bicimad(): 
    bicimad = pd.read_csv('../datasets/pk_bicimad.csv')
    return bicimad

def residentes():
    residentes = pd.read_csv('../datasets/residentes.csv')
    return residentes

def parkings():
    parkings = pd.read_csv('../datasets/parkings.csv')
    return parkings
    
def publicos_dis():
    publicos_dis = pd.read_csv('../datasets/publicos-dis.csv')
    return publicos_dis