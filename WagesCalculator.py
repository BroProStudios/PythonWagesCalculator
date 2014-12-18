hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate of Pay:")
r = float(rate)
age = raw_input("enter your age:")
a = float(age)
pay = float(0)


if h <= 40 :
    pay = r * h
if h > 40 :
    pay = r * 40 + (r * 1.5 * (h - 40)) 
//Min-Wage check for under 18's
if a < 18 and r < 3.79:
    print "talk to your boss"
//Min-Wage check for 18-20 
if a >= 18 and a <= 20 and r < 5.13:
    print "Talk to your boss"
//Win-Wage Check for over 21
if a >= 21 and r < 6.50:
    print "talk to your boss"
    
    

print pay



raw_input("Press Any Key to exit")
