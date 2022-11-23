# Program to get BMI

# Methods for BMI Calculations
class BMI:
    def __init__(self, w, h):
        self.weight = w
        self.height = h

    def Calculate(self):
        self.height = self.height / 100
        Bmi = self.weight/(self.height**2)
        return Round_off2D(Bmi)

    @staticmethod 
    def Classify(Body_Mass_Index):
        if Body_Mass_Index < 18.5:
            return "Underweight"
        elif (Body_Mass_Index >= 18.5 and Body_Mass_Index < 25):
            return "Normal"
        elif (Body_Mass_Index >= 25 and Body_Mass_Index < 30):
            return "Overweight"
        elif Body_Mass_Index >= 30:
            return "Obesity"

# Extra functions
def Round_off2D(decimal):
    decimal = "{:.2f}".format(decimal)
    return float(decimal)

def Filter(x, m, values):
    x_var = x
    if values[0] in "0123456789":
        value = False
        while value is False:
            for i in x_var:
                if i not in values:
                    print("Invalid input.")
                    value = False
                    x_var = input(f"\n{m}")
                    break
                else:
                    value = True
        return x_var
    else:
        while x_var not in values:
            print("Invalid input.")
            x_var = input(f"\n{m}")
        return x_var

while True:
    # Start
    print("\nBMI Calculator.")

    # Get user input(weight and height) and filter the given input
    Message = "Enter your weight(kg) Enter only number/s >> "
    weight = float(Filter(input(Message), Message, "0123456789"))
    Message = "Enter your height(cm) Enter only number/s >> : "
    height = float(Filter(input(Message), Message, "0123456789"))

    # Compute BMI and classify
    BMIVar = BMI(weight, height).Calculate()
    print(f"Calculated BMI: {BMIVar}")
    ClassifyVar = BMI.Classify(BMIVar)
    print(f"Result: {ClassifyVar}\n")

    # Ask if the user want to calculate again, this will determine if you will break the loop or continue it
    Message = "Would you like to do another calculation?(yes/no): "
    loop = Filter(input(Message), Message, ["yes", "no"])
    if loop == "yes":
        continue
    else:
        print("ok bye.")
        break
