# Test Case 1: Cek Angka Ganjil atau Genap (1 Baris)
def check_even_odd(number):
    return f"The number is {'Even' if number % 2 == 0 else 'Odd'}"

# Test
print(check_even_odd(4))
print(check_even_odd(7))

# Test Case 2: Cek Angka Positif, Negatif, atau Nol (1 Baris)
def check_sign(number):
    return f"The number is {'Positive' if number > 0 else ('Negative' if number < 0 else 'Zero')}"

# Test
print(check_sign(10))
print(check_sign(-5))
print(check_sign(0))

# Test Case 3: Cek Anagram
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Test
print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))

# Test Case 4: Hitung Faktorial
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

# Test
print(calculate_factorial(5))
print(calculate_factorial(0))

# Test Case 5: Cek Palindrome (1 Baris)
def is_palindrome(s):
    return s.lower() == s[::-1].lower()

# Test
print(is_palindrome("racecar"))
print(is_palindrome("python"))
print(is_palindrome("habibah"))

# Test Case 6: Cek Bilangan Armstrong
def is_armstrong_number(number):
    s = str(number)
    n = len(s)
    return sum(int(digit) ** n for digit in s) == number

# Test
print(is_armstrong_number(153))
print(is_armstrong_number(370))
print(is_armstrong_number(123))

# Test Case 7: Kelas BankAccount
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0.0
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Invalid withdrawal amount or insufficient funds"

# Test
account = BankAccount("Name")
print(account.deposit(1000))
print(account.withdraw(500))
print(account.withdraw(600))

# Test Case 8: Kelas Student
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."
    
    def get_average(self):
        if not self.grades:
            return "No grades recorded."
        average = sum(self.grades) / len(self.grades)
        return f"Average grade: {average:.1f}"

# Test
student = Student("Alice")
print(student.add_grade(90))
print(student.add_grade(80))
print(student.add_grade(70))
print(student.get_average())

# Test Case 9: Kelas Dasar Shape dan Turunan Circle & Rectangle
import math

class Shape:
    # Metode area() di kelas dasar harus raise error karena ini adalah 'abstract' concept
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        # Rumus luas lingkaran: pi * r^2
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        # Rumus luas persegi panjang: width * height
        return self.width * self.height

# Test
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Luas Lingkaran (r=5): {circle.area():.2f}") # Expected: 78.54
print(f"Luas Persegi Panjang (w=4, h=6): {rectangle.area()}") # Expected: 24