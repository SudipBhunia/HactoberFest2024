qs = ["What is the captial of India? ", "Which one is Input device? ", "Who is the PM of India? "]
option = [["1. New Delhi", "2. Kolkata", "3. Chennai", "4. Goa"], ["1. Moniter", "2. Printer", "3. Keyboard", "4. Scanner"], ["1. B.Obama", "2. V.Putin", "3. D.Trump", "4. N.Modi"]]
answer = [[1],[3],[4]]
opt = "Y"
cash = 0
while(opt.upper() == "Y"):
    for j in range(len(qs)):
        print(qs[j])
        for i in option[j]:
            print(i)
        ans = int(input("Enter your option number: "))
        if ans in answer[j]:
            print("Your answer is right and you won $100")
            cash += 100
            print("Your current balance:",cash)
            opt = input("Do you want to go net question? Y / N: ")
            if opt.upper() == "N":
                break
        else:
            print("Wrong answer!")
            opt = "N"
            break
else:
    print("You have won $",cash)
            
