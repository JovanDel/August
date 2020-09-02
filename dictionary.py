gpas = {
            "Mark Lassof"   :3.45,
            "Fred Smith"    :2.99,
            "Mary Johnson"  :2.55,
            "John Hadley"   :1.95,
            "Louis Lane"    :3.15,
            "Brett Smith"   :4.0,
        }

print ("The GPA is:", (gpas["Mark Lassof"]))
print ("The GPA is:", (gpas["Fred Smith"]))

gpas ["Louis Lane"] = 2.75
gpas ["Thomas Smith"] = 2.61
del gpas ["Fred Smith"]

if gpas in("Mark Lassof"):
    print ("Mark is present")
