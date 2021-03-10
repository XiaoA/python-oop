"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Machine for finding random words from a dictionary

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["Japan", "sword", "Zen"]
    True

    >>> wf.random() in ["birdcatcher", "biophysicochemical", "brutification"]
    True

    >>> wf.random() in ["cabbagehead", "aardwolf", "youngster"]
    True
    """
    def __init__(self, path):
      """Reads dictionary and reports number of items read"""

      dict_file = open(path)

      self.words = self.parse(dict_file)
      
      print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["beachcomb", "carotid", "younker"]
    True

    >>> swf.random() in ["youngly", "youngling", "yacht"]
    True

    >>> swf.random() in ["persimmon", "woodsmanship", "waterdrop"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file and return a list of words, ignoring blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
     
