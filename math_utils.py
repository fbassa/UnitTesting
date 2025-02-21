class MathUtils:

  @staticmethod
  def add(a: int | float, b: int | float) -> int | float:
    return a + b

  @staticmethod
  def subtract(a: int | float, b: int | float) -> int | float:
    return a - b

  @staticmethod
  def divide(a: int | float, b: int | float) -> float:

    if b == 0:
      raise ValueError("You cannot divide by zero!")

    return a / b

  @staticmethod
  def multiply(a: int | float, b: int | float) -> float:

    return a * b

  @staticmethod
  def exponent(a: int | float, b: int | float) -> float:
    return a ** b

  @staticmethod
  def mod(a: int | float, b: int | float) -> float:
    if b == 0:
      raise ValueError("You cannot divide by zero!")
    return a % b











