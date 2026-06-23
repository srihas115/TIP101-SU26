# Problem 5: Average Book Ratings

Write a function `average_book_ratings()`, that calculates the average rating for each book in a collection. The function takes one parameter: a dictionary `book_ratings` where each key-value pair represents a book title and a list of its ratings, respectively. Ratings are represented as floating-point numbers. The function should return a new dictionary with book titles as keys and their average rating.


```python
def average_book_ratings(book_ratings):
    pass
```

Example Input:


```python
book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
```

Example Output:


```python
{'The Great Gatsby': 4.166666666666667,
'To Kill a Mockingbird': 4.675000000000001}
```


<details>
  <summary>💡 <b>Hint: Looping over Key-Value Pairs</b></summary>

  <br>

This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To loop over both keys and values simultaneously, we often use the following syntax:


```python
for k, v in dict.items():
    # function body here
```

For a deeper understanding of how this syntax works, ask a generative AI tool to break down looping over a dictionary with `dict.items()` or search for existing examples using a search engine.
</details>
