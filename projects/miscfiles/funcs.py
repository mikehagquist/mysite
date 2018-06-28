def get_bmr(myweight, myheight, myage):
    
    lbkg = 0.453592
    incm = 2.54
    
    if 1==1:
        myweight = myweight * lbkg
        myheight = myheight * incm
    
    bmr = (10*(myweight))+(6.25*(myheight))-((5*myage)+5)
    return bmr
    
def get_tdee(bmr, actlvl):
    tdee = bmr * actlvl
    return tdee
