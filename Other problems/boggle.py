# Find all valid words on the board using a Trie

# Create the Trie and TrieNode classes
class TrieNode:
  def __init__(self, char=None):
    self._children = {}
    self._char = char
    self._is_complete_word = False
    
  def get_char(self):
    return self._char
  
  def get_child(self, char):
    return self._children.get(char)
  
  def terminates(self):
    return self._is_complete_word
  
  def set_terminates(self, is_complete_word):
    self._is_complete_word = is_complete_word        
  
  def add(self, word):
    current = self
    for letter in word:
        if letter not in current._children:
            current._children[letter] = TrieNode(letter)
        current = current._children[letter]
    current._is_complete_word = True    
  
class Trie:
  def __init__(self, words=[]):
    self._root = TrieNode();
    self._depth = 0
    self._longest_word = None
    self._n_of_complete_words = 0
    self.add_words(words)
  
  def get_root(self):
    return self._root
  
  def get_depth(self):
    return self._depth
  
  def set_depth(self, word):
    if len(word) > self._depth:
        self._depth = len(word)
        self._longest_word = word
        
  def get_longest_word(self):
    return self._longest_word
  
  def get_size(self):
    return self._n_of_complete_words
  
  def add_words(self, words=[]):
    for word in words:
      if not self.contains(word, True):
        self._n_of_complete_words += 1
        self.set_depth(word)
        self._root.add(word)
  
  def contains(self, prefix, is_complete_word=False):
    current = self._root
    for char in prefix:
      current = current.get_child(char)
      if current is None:
        return False
    return not is_complete_word or current.terminates()
  


# Implement a real dictionary lookup
from urllib.request import urlopen

"""Vocabulary implements given list of words 
with 3 or more letters using a Trie data structure
"""
class Vocabulary():
  def __init__(self, url):
    self._valid_words = Trie(line.decode('utf-8').strip().upper() for line in urlopen(url) if len(line) > 3)
    
  def is_prefix(self, word):
    return self._valid_words.contains(word.upper(), False)
  
  def is_valid_word(self, word):
    return self._valid_words.contains(word.upper(), True)
  
  def get_longest_word(self):
    return self._valid_words.get_longest_word()
  
  def get_size_longest_word(self):
    return self._valid_words.get_depth()
  
  def get_size(self):
    return self._valid_words.get_size()
  


  
# Implement Boggle class
from random import choice
from string import ascii_uppercase

class Boggle():
  def __init__(self, size=4, url=None):
    self._board = self._generate_game_board(size)
    self._vocab = self._generate_vocabulary(url)
  
  # Generate a square game board of a given size
  def _generate_game_board(self, size):
    return [[choice(ascii_uppercase) for _ in range(size)] for _ in range(size)]
  
  def create_new_board(self, size=None):
    self._board = self._generate_game_board(size) if size else self._generate_game_board(len(self._board))
    
  
  # Generate Vocabulary
  def _generate_vocabulary(self, url):
    return Vocabulary(url) if url else Vocabulary()
  
  def create_new_vocabulary(self, url):
    self._vocab = self._generate_vocabulary(url)

    
  # Print board
  def print_game_board(self):
    for row in self._board:
      print(row)
   

  # Find all valid words on the board (including diagonals)
  def boggle_finder(self):
    size = len(self._board)
    visited = [[False]*size for _ in range(size)]
    words_found = set()
    temp_word = []
    for i in range(size):
      for j in range(size):
        self._boggle_helper(self._board, self._vocab, visited, words_found, i, j, temp_word)
    return words_found

  def _boggle_helper(self, game_board, dictionary, visited, words_found, i, j, temp_word):
    visited[i][j] = True
    temp_word.append(game_board[i][j])

    w = ''.join(temp_word)
    if dictionary.is_prefix(w):
      if len(temp_word) >= 3 and dictionary.is_valid_word(w):
        words_found.add(w)

      adjacent = [(r, c) for c in range(j-1, j+2) for r in range(i-1, i+2) if not (r == i and c == j)]
      size = len(game_board)
      for row, col in adjacent:
        if (row in range(size)) and (col in range(size)) and (not visited[row][col]):
          self._boggle_helper(game_board, dictionary, visited, words_found, row, col, temp_word)

    temp_word.pop()
    visited[i][j] = False
  
  
  # Get vocabulary size
  def get_vocab_size(self):
    return self._vocab.get_size()
  
  def get_longest_word(self):
    return self._vocab.get_longest_word(), self._vocab.get_size_longest_word()



#####################################################################################################
# Test / Play

# Generate larger dictionary

import time

# Check running time
start_time = time.time()


SIZE = 40 # enter any size you want
VOCAB_URL = 'https://raw.githubusercontent.com/juemura/amli/master/english3.txt' # enter any word list

# Start new Boggle game
game = Boggle(SIZE, VOCAB_URL)

middle_time = time.time()
print("---Running time to create Boggle board and word prefix tree: {} seconds ---\n".format(middle_time - start_time))
print("Number of words added: {}".format(game.get_vocab_size()))
print("Longest word: {}, size: {}".format(*game.get_longest_word()))


game.print_game_board()

middle_time = time.time()

words = game.boggle_finder()
print("Found the following {} words".format(len(words)))
print(words)

end_time = time.time()
print("---Running time for 40x40 Full Boggle using a Trie: {} seconds ---\n".format(end_time - middle_time))
print("Size of the longest word found: {}".format(max(map(len, words))))

print("Total running time: {} seconds ---\n".format(end_time - start_time))



#####################################################################################################
"""
Number of words in the dictionary: 194206
---Running time to create Boggle board and word prefix tree: 2.665843963623047 seconds ---

---Running time for 40x40 Full Boggle using a Trie: 1.56943678855896 seconds ---

"""