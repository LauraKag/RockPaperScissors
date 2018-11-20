# -*- coding: utf-8 -*-

#%%

from Rockpaperscissor import rockpaperscissors

def test_Rockpaperscissor_returns_Playeronewon():
    
    assert rockpaperscissors("Rock","Scissors")
    assert rockpaperscissors("Scissors","Paper")
    assert rockpaperscissors("Paper","Rock")
    

def test_Rockpaperscissor_returns_Playertwowon():
    
    assert rockpaperscissors("Paper","Scissors")
    assert rockpaperscissors("Rock","Paper")
    assert rockpaperscissors("Scissors","Rock")
   
def test_Rockpaperscissor_returns_Noonewon():
    
    assert rockpaperscissors("Rock","Rock")
    assert rockpaperscissors("Scissors","Scissors")
    assert rockpaperscissors("Paper","Paper")
   
