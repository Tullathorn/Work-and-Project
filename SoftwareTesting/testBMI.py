%%writefile test_bmi.py

#Calculate BMI function
def calculate_bmi(weight, height):
    if not isinstance(weight, (int, float)) or not isinstance(height, (int, float)):
        return "Invalid input"
    if height == 0:
        raise ZeroDivisionError("Height cannot be zero")
    if height < 0:
        raise ValueError("Height cannot be negative")
    if weight < 0:
        raise ValueError("Weight cannot be negative")
    if weight == 0:
        raise ValueError("Weight cannot be zero")


    bmi = weight / (height**2)


    if bmi < 18.5:
        return "UnderWeight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "OverWeight"
    else:
        return "Obese"

#NormalWeight
def test_normal_bmi():
    # BMI = 70 / (1.75^2) = 22.86 → Normal
    assert calculate_bmi(70, 1.75) == "Normal"

# เพิ่ม test cases ต่อ...

#UnderWeight
def test_underWeight_bmi():
    assert calculate_bmi(50, 1.78) == "UnderWeight"

#OverWeight
def test_overWeight_bmi():
    assert calculate_bmi(65, 1.50) == "OverWeight"

#Obese
def test_obese_bmi():
    assert calculate_bmi(90, 1.70) == "Obese"

#edge cases
import pytest

def test_boundary_values():
    assert calculate_bmi(41.4, 1.5) == "UnderWeight" #bmi=18.4
    assert calculate_bmi(56.025, 1.5) == "Normal" #bmi=24.9
    assert calculate_bmi(67.275, 1.5) == "OverWeight" #bmi=29.9
    assert calculate_bmi(67.5, 1.5) == "Obese" #bmi=30

def test_zero_height():
    with pytest.raises(ZeroDivisionError):
        calculate_bmi(70, 0)

def test_negative_height():
    with pytest.raises(ValueError):
        calculate_bmi(70, -1.75)

def test_zero_weight():
    with pytest.raises(ValueError):
        calculate_bmi(0, 1.75)

def test_negative_weight():
    with pytest.raises(ValueError):
        calculate_bmi(-70, 1.75)

def test_not_numeric_value():
  assert calculate_bmi('','')== "Invalid input"
  assert calculate_bmi('a', 1.75) == "Invalid input"
  assert calculate_bmi(70, 'a') == "Invalid input"
  assert calculate_bmi('', 1.75) == "Invalid input"
  assert calculate_bmi('a', '') == "Invalid input"
  assert calculate_bmi('a', 'a') == "Invalid input"
  assert calculate_bmi(1.75, "string") == "Invalid input"
  assert calculate_bmi("string", 1.75) == "Invalid input"
  assert calculate_bmi("string", "string") == "Invalid input"
