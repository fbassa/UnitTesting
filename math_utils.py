class MathUtils:
  """
<<<<<<< HEAD
  class that implement mathematical operations.
  """
=======
  Class that implements mathematical operations.
  """
  
>>>>>>> f5b3f136a668db0adb1c8dbf339974951e108e1b
  @staticmethod
  def add(a: int | float, b: int | float) -> int | float:
    """
    Just adds two numbers together.
    """
    return a + b

  @staticmethod
  def subtract(a: int | float, b: int | float) -> int | float:
    """
    Just subtracts two numbers.
    """
    return a - b

  @staticmethod
  def divide(a: int | float, b: int | float) -> float:
    """
    Just divides two numbers.
    """
    if b == 0:
      raise ValueError("You cannot divide by zero!")
<<<<<<< HEAD
    return a / b

=======
    return a / b 
  
>>>>>>> f5b3f136a668db0adb1c8dbf339974951e108e1b
