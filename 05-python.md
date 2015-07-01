# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

[![Think Python](img/think_python.png)](http://www.greenteapress.com/thinkpython/)

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

Complete the following exercises to check your ability with Python.

These exercises are implemented with doctests, which are runnable tests inside docstrings. Fill in the function definitions. Correct solutions will make it possible to run (for example) `python -m doctest strings.py` with no messages about failures.

 * [Strings](python/strings.py)
 * [Lists](python/lists.py)


---

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

---
>>The biggest difference is that tuples are immutable and lists are mutable.  Therefore lists can not be keys in dictionaries because the key can not be mutable.

---

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

---
>>Sets are an unordered list of unique elements.  Lists can have duplicate element and are also ordered.  The answer does somewhat depend on the data in the list vs. the set.  For example you can have a set of item numbers in inventory but perhaps if you had a list of a customers items ordered, an inventory item number could appear twice if they ordered two of the same item.

---

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>>lamda is a one line minifunction that takes arguments and applies them to a small code/process and iterates as directed.  It can be used in sort as a way to prioritize which element are sorted by priority for example.  If you wanted to sort first by class course code and then alphabetically by student
    x=(('PR401.7', 'Charles Crown'),('PR403.6', 'Robert Red'),(PR401.7, 'Alice Adams'), ('PR403.6','Bob Evans')

    new_list=sorted(items, key=lambda x: (x[0], x[1])
    print new_list
    
    >>>(PR401.7, 'Alice Adams'),('PR401.7', 'Charles Crown'),('PR403.6','Bob Evans'),('PR403.6', 'Robert Red')



---


---

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

REPLACE THIS TEXT WITH YOUR RESPONSE

---


Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

```bash
./markov.py chains.txt 40
```

A possible output would be:

> show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.
