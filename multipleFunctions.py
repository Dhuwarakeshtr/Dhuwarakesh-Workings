class multipleFunctions():
    def BMI():
        Digit=float(input("Enter the BMI number :"))
        if(Digit<18.5):
            print("Under Weight")
            bmi="Under Weight"
        elif(Digit<24.9):
            print("Normal")
            bmi="Normal"
        elif(Digit<29.9):
            print("Over Weight")
            bmi="Over Weight"
        else:
            print("Obese")
            bmi="Obese"
        return bmi
    def Evenodd():
        Num=int(input("Enter the number: "))
        if((Num%2)==0):
            print("Even Number")
            ans="Even Number"
        else:
            print("Odd Number")
            ans="Odd Number"
        return ans