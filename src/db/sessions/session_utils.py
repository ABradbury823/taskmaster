from hashlib import sha512
from secrets import token_hex


def generate_sequence_key(length: int = 32):
  """
  Generates a random sequence key.

  Parameters:
    length (int) - Length, in bytes, of the key. Default = 32 -> 64 characters.

  Returns:
    A random sequence of bytes represented as a string. 
  """
  # use python secrets to generate random hexstring
  return token_hex(length)

def hash_string(string: str):
  """Hash a string to a random hexadecimal code"""
  return sha512(string.encode()).hexdigest()