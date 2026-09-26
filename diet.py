def bmi_calculator(weight,height): #body mass index
    bmi=weight/((height/100)**2) #weight must be in kg and height in m
    return round(bmi,2)

def bmr_calculator(weight,height,age,gender):#basal metabolic rate(diff. for male & female)
    if gender=='male':
        bmr=(10*weight)+(6.25*height)-(5*age)+5
        return bmr
    elif gender=='female':
        bmr=(10*weight)+(6.25*height)-(5*age)-161
        return bmr

def tdee_calculator(bmr,activity):#total daily enery expenditure(activity factor --> some other factor)
    #define all the factors
    activity_factor={
        'sedentary':1.20,
        'lightly active':1.375,
        'moderately active':1.55,
        'very active':1.725,
        'extra active':1.90
    }
    tdee=bmr*activity_factor[activity]
    return round(tdee,2)

def calorie_target(tdee,aim):
    if aim=='weight maintain':
        calorie=tdee
    elif aim=='weight loss':
        calorie= tdee-400
    elif aim=='weight gain':
        calorie=tdee+300
    return round(calorie,2)


# print(bmi_calculator(60,150))
# bmr=(bmr_calculator(63,160,23,'female'))
# tdee=(tdee_calculator(bmr,'very active'))
# print(calorie_target(tdee,'weight loss'))