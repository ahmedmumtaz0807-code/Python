# Body fat esmtimator
body_fat = float(input("Enter your body fat percentage:"))
if body_fat < 6:
    print("Essential fat")
elif body_fat < 14:
    print("athletes")
elif body_fat< 25:
    print("normal")
else:
    print("Obese")