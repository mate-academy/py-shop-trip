# Сheck Your Code Against the Following Points

## Don't Repeat Yourself

1. Write your code, so you don't have duplicated lines or whole blocks of code.

Good example:

```python
if "cat" in animal_list:
    print("found")
else:
    print("not found")

print("the end")
```

Bad example:

```python
if "cat" in animal_list:
    print("found")
    print("the end")
else:
    print("not found")
    print("the end")
```

2. Pay attention to avoid code duplication by using classes and functions

## Code Style

1. Use descriptive and correct variable names.

Good example:

```python
with open("some_config_file.json", "r") as config:
    pass
```

Bad example:

```python
with open("some_config_file.json", "r") as scf:
    pass
```

2. Use one style of quotes in your code. Double quotes are preferable.

3. Make sure that yor architecture is clear and your code is readable.

4. Make sure you write the correct path to the JSON file.

5. Make sure you use exactly `import datetime`, not the other way of import.

## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
