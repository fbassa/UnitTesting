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




