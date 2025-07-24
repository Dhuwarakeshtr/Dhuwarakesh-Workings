class SetOfFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def evenodd():
        Num=int(input("Enter a number: "))
        if((Num%2)==0):
            print(Num,"is Even number")
            answer=Num,"is Even number"
        else:
            print(Num,"is Odd number")
            answer=Num,"is Odd number"
        return answer

    def Eligible():
        Gender=input("Enter the Gender:")
        Age=int(input("Enter the AGe:"))
        if(Gender=="Male" and Age>21):
            print("ELIGIBLE")
            Message="ELIGIBLE"
        elif(Gender=="Male" and Age<21):
            print("NOT ELIGIBLE")
            Message="NOT ELIGIBLE"
        elif(Gender=="Female" and Age<18):
            print("NOT ELIGIBLE")
            Message="NOT ELIGIBLE"
        else:
            print("ELIGIBLE")
            Message="ELIGIBLE"
        return Message

    def percentage():
        S1=int(input("Subject1="))
        S2=int(input("Subject2="))
        S3=int(input("Subject3="))
        S4=int(input("Subject4="))
        S5=int(input("Subject5="))
        Total=S1+S2+S3+S4+S5
        Percentage=(Total/500)*100
        print("Total :",Total)
        print("Percentage :",Percentage)

    def Triangle():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        A=(h*b)/2
        print("Area of Triangle:",A)
        h1=int(input("Height1:"))
        h2=int(input("Height2:"))
        b1=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        B=h1+h2+b1
        print("Perimeter of Triangle:",B)
    