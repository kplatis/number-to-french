# Number to French

## Requirements

I used python `3.12` to develop but any previous version should be enough to run it

## Implementation

The implementation is done in `NumberToFrench` class.

## Limitation

- The converter can convert numbers of up to 9 digits. In that case a `ValueError` is raised
- The number cannot be negative. In that case a `ValueError` is raised

## How to use

```python
from number_to_french import NumberToFrench

word = NumberToFrench(1999).to_french_word()
```

An example based on the given input can be seen in `main.py`

## LLM Usage

Used ChatGPT LLM for generation of pydocs