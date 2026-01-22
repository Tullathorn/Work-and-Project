%%writefile test_calculate_parking_fee.py

# ========== Production Code ==========

def hour(hours):
  if type(hours) == str:
     raise TypeError("ไม่สามารถใส่ตัวอักษรได้")
  if hours < 0:
    raise ValueError("ชั่วโมงไม่สามารถเป็นค่าติดลบได้")


  """ฟังก์ชั่นคำนวณค่าจอดรถตามนาที"""
  hour = hours // 1
  minute = (hours * 100) % 100
  if minute >= 1.0:
    hour = hour + 1

  if minute > 60:
    raise ValueError("นาทีไม่สามารถเกิน 60 ได้")

  if hour <= 1:
    return "20"
  elif hour >= 2 and hour <= 4:
    return "40"
  elif hour >= 5 and hour <= 7:
    return "60"
  else:
    return "80"

# ========================================
# Test Cases - Normal Cases
# ========================================
def test_one_hour():
    """ทดสอบ ใช้เวลาจอดรถน้อยกว่าหรือเท่ากับ 1 ชั่วโมง(<= 60 นาที)"""
    assert hour(0.10) == "20"
    assert hour(1.00) == "20"

def test_two_hour():
    """ทดสอบ ใช้เวลาจอดรถ 2-4 ชั่วโมง(61-240 นาที)"""
    assert hour(1.50) == "40"
    assert hour(4.00) == "40"

def test_five_hour():
    """ทดสอบ ใช้เวลาจอดรถ 5-7 ชั่วโมง(241-420 นาที)"""
    assert hour(5.00) == "60"
    assert hour(6.59) == "60"

def test_more_than_eight_hour():
    """ทดสอบ ใช้เวลาจอดรถตั้งแต่ 8 ชั่วโมงขึ้นไป(>= 421 นาที)"""
    assert hour(8.00) == "80"
    assert hour(10.50) == "80"


# ========================================
# Test Cases - Edge Cases
# ========================================
import pytest

def test_boundary_values():
    """ทดสอบค่าขอบเขต"""
    assert hour(0.59) == "20"  # ขอบบนของ 1 ชั่วโมง
    assert hour(1.01) == "40"  # ขอบล่างของ 2-4 ชั่วโมง
    assert hour(7.00) == "60"  # ขอบบนของ 5-7 ชั่วโมง
    assert hour(8.00) == "80"  # ขอบล่างของ 8 ชั่วโมงขี้นไป

def test_invalid_negative_score():
    """ชั่วโมงติดลบต้อง raise ValueError"""
    with pytest.raises(ValueError):
       hour(-1)
def test_invalid_over_100():
      """นาทีเกิน 60 ต้อง raise ValueError"""
      with pytest.raises(ValueError):
          hour(1.61)
def test_not_number():
      """นาทีเกิน 60 ต้อง raise ValueError"""
      with pytest.raises(TypeError):
          hour("love")
