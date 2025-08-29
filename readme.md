# PEP-8

Pythonic code adheres to Python’s design principles and philosophy and emphasizes readability, simplicity, and clarity.

Proper spacing , well defined names , adhereing to naming conventions for classes (CamelCase), variables/functions (snake_casing), package (thispackage) and Constants → UPPER_CASE

**Blank_Lines**

Surround top-level functions and classes with two blank lines.
Surround method definitions inside classes with a single blank line.
Use blank lines sparingly inside functions to show clear steps.

**Maximum Line Length and Line Breaking**

Python will assume line continuation if code is contained within parentheses, brackets, or braces:

```python
def function(arg_one, arg_two,
             arg_three, arg_four):
    return arg_one
```

If it’s impossible to use implied continuation, then you can use backslashes ("\") to break lines instead:

```python
from package import example1, \
    example2, example3
```

If you need to break a line around binary operators, like + and \*, then you should do so before the operator.

```python
total = (first_variable
         + second_variable
         - third_variable)
```

Good call — writing clean code is like training your brain to **think like a professional developer**. PEP 8 is Python’s style guide, and while it’s long, there are some **essentials** that really make a difference in how your code looks and feels.

Here are the **core essentials from PEP 8** you should focus on:

---

### 📝 **Formatting & Layout**

1. **Indentation**: Use **4 spaces per indentation level** (no tabs).

   ```python
   def my_function():
       if True:
           print("PEP8 says 4 spaces")
   ```

2. **Line Length**: Keep lines **≤ 79 characters** (72 for docstrings/comments).

   - Break long lines with `\` or better, with parentheses.

3. **Blank Lines**:

   - **2 blank lines** between top-level functions/classes.
   - **1 blank line** between methods inside a class.

---

### 🧩 **Naming Conventions**

- **Variables, functions, methods** → `snake_case`

  ```python
  total_price = calculate_discount(price, discount_rate)
  ```

- **Classes, exceptions** → `CamelCase`

  ```python
  class OrderManager:
      pass
  ```

- **Constants** → `UPPER_CASE`

  ```python
  MAX_RETRY = 3
  ```

- Don’t use single-letter names (except loop indices).

---

### 📚 **Imports**

- One import per line:

  ```python
  import os
  import sys
  ```

- Imports order:

  1. Standard library
  2. Third-party packages
  3. Local application code

  With **blank lines** between groups.

---

### 💡 **Whitespace Rules**

- **Around operators**:

  ```python
  x = 5 + 3
  y = x * 2
  ```

- **After commas, colons, semicolons**:

  ```python
  items = [1, 2, 3]
  ```

- **No extra spaces** inside parentheses/brackets/braces:

  ```python
  good = (1, 2)
  bad = ( 1, 2 )
  ```

---

### 🔎 **Comments & Docstrings**

- **Inline comments**: after 2 spaces, short and clear.

  ```python
  x = x + 1  # Increment counter
  ```

- **Block comments**: full sentences, explain why not what.
- **Docstrings**: use `"""` triple quotes, describe the function/class/module.

  ```python
  def add(a, b):
      """Return the sum of a and b."""
      return a + b
  ```

---

### ⚙️ **Programming Recommendations**

- Don’t compare to `True`/`False` directly:

  ```python
  if is_valid:      # Good
  if is_valid == True:  # Bad
  ```

- Use `is None` / `is not None`, not `== None`.
- Avoid using `l`, `O`, or `I` as variable names (look too much like 1 and 0).

---

### 🚀 Quick Checklist (for pros)

✅ 4-space indentation
✅ Max 79 chars per line
✅ Blank lines separate logical sections
✅ Snake_case for functions/vars, CamelCase for classes
✅ Imports in correct order
✅ Whitespace used consistently
✅ Docstrings + comments explain intent

---

Would you like me to also show you a **before vs. after example** (messy code → PEP 8 compliant code), so you can visually see the difference professionals aim for?
