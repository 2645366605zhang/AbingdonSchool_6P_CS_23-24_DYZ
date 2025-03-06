import importlib.util

spec = importlib.util.spec_from_file_location(
    name = "my_module",  # note that ".test" is not a valid module name
    location = "Paper1_ALvl_2025_Python_Pub_0.0.0_expanded_symbols.py",
)
myModule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(myModule)

testCases = [
    "1+(2+3)",
    "3*(3+1)",
    "5+(1*4*(2+3)-8)*9",
    "1+1",
    "9*8/7+6-5*(4/3)+2-1",
    "3-6*(1+2)",
    "21/(1-9)",
    "3-(2-5)",
    "1+(5/2)*3",
    "4*(2+6)*(42/21)/2+(2^2)",
    "(2+1)*(3/3)"
]

testResults = []

for test in testCases:
    print(test)
    testResults.append(myModule.ConvertToRPN(test))

print("\n")

for result in testResults:
    print(", ".join(result))