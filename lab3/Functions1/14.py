def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

grams_input = float(input("Enter the weight in grams: 78"))
ounces_result = grams_to_ounces(grams_input)
print(f"{grams_input} grams is equal to {ounces_result:.2f} ounces.")