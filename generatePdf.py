from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from datetime import datetime

# Create PDF
pdf_file = "Python_Complete_Learning_Guide.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
styles = getSampleStyleSheet()
story = []

# Define custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=28,
    textColor=colors.HexColor('#1f4788'),
    spaceAfter=10,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

heading_style = ParagraphStyle(
    'SectionHeading',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=colors.HexColor('#2e5c8a'),
    spaceAfter=12,
    spaceBefore=12,
    fontName='Helvetica-Bold',
    borderColor=colors.HexColor('#2e5c8a'),
    borderWidth=2,
    borderPadding=5,
)

question_style = ParagraphStyle(
    'Question',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=colors.HexColor('#d9534f'),
    spaceAfter=6,
    fontName='Helvetica-Bold'
)

answer_style = ParagraphStyle(
    'Answer',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.HexColor('#333333'),
    spaceAfter=6,
    alignment=TA_JUSTIFY,
    leftIndent=20
)

code_style = ParagraphStyle(
    'Code',
    parent=styles['Normal'],
    fontName='Courier',
    fontSize=9,
    textColor=colors.HexColor('#ffffff'),
    backColor=colors.HexColor('#2c3e50'),
    borderColor=colors.HexColor('#34495e'),
    borderWidth=1,
    borderPadding=8,
    leftIndent=20,
    rightIndent=20,
    spaceAfter=8
)

# Title Page
story.append(Paragraph("Python Complete Learning Guide", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Questions • Answers • Code Examples", styles['Normal']))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
story.append(Spacer(1, 0.5*inch))
story.append(PageBreak())

# ============= SECTION 1: BASIC PYTHON CONCEPTS =============
story.append(Paragraph("SECTION 1: Basic Python Concepts", heading_style))
story.append(Spacer(1, 0.1*inch))

basic_qa = [
    {
        "q": "What are the parameters of the print() statement?",
        "a": "The print() function has 4 main parameters: object(s), sep, end, and file. Parameters 2-4 are optional. 'sep' defines separator (default ' '), 'end' defines ending (default '\\n').",
        "code": "print('hello', 1, 2, sep='-', end='!')\n# Output: hello-1-2!"
    },
    {
        "q": "What are the main data types in Python?",
        "a": "Numbers (int, float, complex), Text (str), Boolean (True/False), Collections (list, tuple, dict, set), and mapped data types.",
        "code": "num = 5  # int\nfloat_num = 3.14  # float\ntext = 'hello'  # str\nbool_val = True  # boolean\nlst = [1, 2, 3]  # list\ntup = (1, 2, 3)  # tuple\ndct = {'key': 'value'}  # dict"
    },
    {
        "q": "What is type casting and what are its types?",
        "a": "Type casting is the conversion of one data type into another. Types: Explicit (manual conversion using int(), str(), float()) and Implicit (automatic conversion by Python).",
        "code": "# Explicit casting\na = '5'\nb = int(a)  # Convert string to int\nprint(type(b))  # <class 'int'>\nc = float('3.14')  # Convert to float\nd = str(123)  # Convert to string"
    },
    {
        "q": "Are strings mutable or immutable in Python?",
        "a": "Strings are immutable in Python. String methods don't change the original string but return a new string instead.",
        "code": "s = 'hello'\ns_new = s.upper()\nprint(s)  # Still 'hello' (unchanged)\nprint(s_new)  # 'HELLO' (new string)"
    },
    {
        "q": "What is the difference between for and while loops?",
        "a": "'for' loop is used with sequences and ranges. 'while' loop runs based on a condition. 'for' is used when you know iteration count, 'while' when you know the condition.",
        "code": "# for loop\nfor i in range(5):\n    print(i)  # Prints 0 to 4\n\n# while loop\ni = 0\nwhile i < 5:\n    print(i)\n    i += 1"
    },
    {
        "q": "What are list comprehensions and their syntax?",
        "a": "Concise way to create lists. Syntax: [Expression(item) for item in iterable if(Condition)]",
        "code": "lst1 = [i for i in range(10)]\nlst2 = [i for i in range(10) if i%2 == 0]  # Even numbers\nlst3 = [i*i for i in range(5)]  # Squares\nprint(lst3)  # [0, 1, 4, 9, 16]"
    },
    {
        "q": "What is the difference between tuple and list?",
        "a": "Tuples are immutable (cannot be modified after creation), while lists are mutable (can be changed, added, removed).",
        "code": "lst = [1, 2, 3]\nlst[0] = 99  # Works - lists are mutable\n\ntup = (1, 2, 3)\n# tup[0] = 99  # Error! - tuples are immutable"
    },
    {
        "q": "What are sets in Python and their characteristics?",
        "a": "Sets are unordered collections of unique items. They don't contain duplicate elements and are useful for membership testing and eliminating duplicates.",
        "code": "s = {1, 2, 3, 4, 5, 2, 4}\nprint(s)  # {1, 2, 3, 4, 5} - duplicates removed\nprint(type(s))  # <class 'set'>\ns.add(6)\ns.update({7, 8})"
    },
    {
        "q": "Explain dictionaries in Python with example.",
        "a": "Dictionaries are ordered (after Python 3.7) collections of key-value pairs. Items are accessed by keys, not by index.",
        "code": "d = {'john': 36, 'Ravi': 33, 'Neha': 26}\nprint(d['john'])  # 36\nprint(d.keys())  # dict_keys(['john', 'Ravi', 'Neha'])\nprint(d.values())  # dict_values([36, 33, 26])\nprint(d.items())  # Key-value pairs"
    },
    {
        "q": "How does exception handling work in Python?",
        "a": "Exception handling is the process of handling unwanted/unexpected events using try-except-finally blocks. Try block contains code that might cause error, except handles the error, finally always executes.",
        "code": "try:\n    x = 1 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')\nexcept Exception as e:\n    print(f'Error: {e}')\nfinally:\n    print('This always executes')"
    },
]

for i, qa in enumerate(basic_qa, 1):
    story.append(Paragraph(f"<b>Q{i}: {qa['q']}</b>", question_style))
    story.append(Paragraph(f"<b>Answer:</b> {qa['a']}", answer_style))
    story.append(Paragraph("<b>Code Example:</b>", styles['Normal']))
    
    for line in qa['code'].split('\n'):
        story.append(Paragraph(line if line.strip() else '&nbsp;', code_style))
    
    story.append(Spacer(1, 0.15*inch))

story.append(PageBreak())

# ============= SECTION 2: FILE I/O & FUNCTIONS =============
story.append(Paragraph("SECTION 2: File I/O & Functions", heading_style))
story.append(Spacer(1, 0.1*inch))

file_qa = [
    {
        "q": "How do you read and write files in Python?",
        "a": "Use open() with modes: 'r'(read), 'w'(write), 'a'(append), 'x'(create). Methods: read() returns entire file, readlines() returns list, write() writes string.",
        "code": "# Read file\nwith open('file.txt', 'r') as f:\n    content = f.read()  # Read entire file\n    lines = f.readlines()  # Read line by line\n\n# Write file\nwith open('file.txt', 'w') as f:\n    f.write('Hello World')"
    },
    {
        "q": "What are lambda functions and how to use them?",
        "a": "Lambda functions are anonymous functions defined using 'lambda' keyword. Syntax: lambda args: expression. Used for small, simple operations.",
        "code": "square = lambda x: x * x\nprint(square(5))  # 25\n\navg = lambda x, y, z: (x + y + z) / 3\nprint(avg(2, 3, 4))  # 3.0\n\n# Using with other functions\nresult = list(map(lambda x: x*2, [1, 2, 3]))\nprint(result)  # [2, 4, 6]"
    },
    {
        "q": "Explain map(), filter(), and reduce() functions.",
        "a": "Higher-order functions: map() applies function to all items, filter() filters items based on condition, reduce() accumulates values into single result.",
        "code": "from functools import reduce\n\nl = [1, 2, 3, 4, 5]\nmap_result = list(map(lambda x: x * 2, l))\nfilter_result = list(filter(lambda x: x > 2, l))\nreduce_result = reduce(lambda x, y: x + y, l)\n\nprint(map_result)      # [2, 4, 6, 8, 10]\nprint(filter_result)   # [3, 4, 5]\nprint(reduce_result)   # 15"
    },
    {
        "q": "What is the purpose of __name__ == '__main__'?",
        "a": "This is an idiom to determine if script is called directly or imported. Prevents code execution during import, runs only when script is executed directly.",
        "code": "def my_function():\n    print('Function called')\n\nif __name__ == '__main__':\n    my_function()\n    # This runs only when script is executed directly\n    # Not executed when imported in another file"
    },
]

for i, qa in enumerate(file_qa, 1):
    story.append(Paragraph(f"<b>Q{i}: {qa['q']}</b>", question_style))
    story.append(Paragraph(f"<b>Answer:</b> {qa['a']}", answer_style))
    story.append(Paragraph("<b>Code Example:</b>", styles['Normal']))
    
    for line in qa['code'].split('\n'):
        story.append(Paragraph(line if line.strip() else '&nbsp;', code_style))
    
    story.append(Spacer(1, 0.15*inch))

story.append(PageBreak())

# ============= SECTION 3: OBJECT-ORIENTED PROGRAMMING =============
story.append(Paragraph("SECTION 3: Object-Oriented Programming (OOPs)", heading_style))
story.append(Spacer(1, 0.1*inch))

oops_qa = [
    {
        "q": "What is OOP and its key features?",
        "a": "Object-Oriented Programming uses classes and objects. Key features: (1) Encapsulation - hide internal state and access via methods, (2) Inheritance - inherit from existing class, (3) Polymorphism - single entity in multiple forms.",
        "code": "# Example of OOP\nclass Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    \n    def display(self):\n        print(f'{self.name} is {self.age} years old')\n\np = Person('Harry', 25)\np.display()"
    },
    {
        "q": "What is a class and what is self?",
        "a": "A class is a blueprint for creating objects. 'self' is a reference to the current instance of the class and is used to access variables and methods of that class.",
        "code": "class Car:\n    def __init__(self, brand):\n        self.brand = brand  # self.brand belongs to this instance\n    \n    def info(self):\n        print(f'Brand: {self.brand}')\n\ncar1 = Car('Toyota')\ncar1.info()  # self automatically passed as first argument"
    },
    {
        "q": "What is a constructor and __init__ method?",
        "a": "Constructor is a special method called automatically when object is created. In Python, __init__() is the constructor. Used to initialize object's attributes. Always takes 'self' as first parameter.",
        "code": "class Employee:\n    def __init__(self, name, id):\n        self.name = name\n        self.id = id\n        print(f'{self.name} created with id {self.id}')\n\nemp = Employee('Harry', 18)  # Constructor called automatically"
    },
    {
        "q": "What are access modifiers and how are they implemented?",
        "a": "Access modifiers limit access to class properties/methods. Python has: Public (default, accessible anywhere), Protected (_name convention, accessible within class and subclasses), Private (__name - Name Mangling).",
        "code": "class MyClass:\n    def __init__(self):\n        self.public_var = 'Public'     # Public\n        self._protected_var = 'Protected'  # Protected\n        self.__private_var = 'Private'    # Private\n\nobj = MyClass()\nprint(obj.public_var)        # Works\nprint(obj._protected_var)    # Works but convention\n# print(obj.__private_var)   # Error!\nprint(obj._MyClass__private_var)  # Name Mangling"
    },
    {
        "q": "What are static methods and class methods?",
        "a": "Static methods (@staticmethod) belong to class, not instances. Don't take self. Class methods (@classmethod) take cls as first parameter and can modify class variables.",
        "code": "class Example:\n    class_var = 'ABC'\n    \n    @staticmethod\n    def static_method():\n        print('Static method')\n    \n    @classmethod\n    def class_method(cls):\n        cls.class_var = 'XYZ'\n        print(f'Class var: {cls.class_var}')\n\nExample.static_method()\nExample.class_method()"
    },
    {
        "q": "Explain instance vs class variables.",
        "a": "Class variables are defined at class level, shared across all instances. Instance variables are defined in __init__, specific to each instance. Instance variables take priority over class variables.",
        "code": "class Company:\n    company_name = 'XYZ'  # Class variable\n    \n    def __init__(self, emp_name):\n        self.emp_name = emp_name  # Instance variable\n\ncomp1 = Company('Harry')\ncomp2 = Company('Divya')\nprint(comp1.company_name)  # XYZ (shared)\nprint(comp1.emp_name)      # Harry (instance-specific)"
    },
    {
        "q": "What is object introspection?",
        "a": "Object introspection helps understand an object's attributes and methods. Tools: dir() returns all attributes, __dict__ returns attribute dictionary, help() gives documentation.",
        "code": "class Person:\n    def __init__(self, name):\n        self.name = name\n\np = Person('Harry')\nprint(dir(p))          # All attributes and methods\nprint(p.__dict__)      # {'name': 'Harry'}\nprint(help(Person))    # Documentation"
    },
    {
        "q": "Explain magic/dunder methods with examples.",
        "a": "Special methods starting with double underscores. Common ones: __str__() for string representation, __repr__() for official representation, __call__() to make object callable.",
        "code": "class Example:\n    def __init__(self, name):\n        self.name = name\n    \n    def __str__(self):\n        return f'Example: {self.name}'\n    \n    def __repr__(self):\n        return f'Example({self.name})'\n    \n    def __call__(self):\n        print('Object called as function')\n\nex = Example('Test')\nprint(str(ex))   # Uses __str__\nex()             # Uses __call__"
    },
]

for i, qa in enumerate(oops_qa, 1):
    story.append(Paragraph(f"<b>Q{i}: {qa['q']}</b>", question_style))
    story.append(Paragraph(f"<b>Answer:</b> {qa['a']}", answer_style))
    story.append(Paragraph("<b>Code Example:</b>", styles['Normal']))
    
    for line in qa['code'].split('\n'):
        story.append(Paragraph(line if line.strip() else '&nbsp;', code_style))
    
    story.append(Spacer(1, 0.15*inch))

story.append(PageBreak())

# ============= SECTION 4: INHERITANCE =============
story.append(Paragraph("SECTION 4: Inheritance Types", heading_style))
story.append(Spacer(1, 0.1*inch))

inheritance_qa = [
    {
        "q": "What is inheritance and explain different types?",
        "a": "Inheritance allows new classes to inherit properties and methods from existing class. Types: Single (one parent), Multiple (multiple parents), Multi-level (child inherits from parent which inherits from grandparent), Hierarchical (multiple children from one parent), Hybrid (combination).",
        "code": "# Single Inheritance\nclass Employee:\n    pass\n\nclass Manager(Employee):  # Inherits from Employee\n    pass\n\n# Multiple Inheritance\nclass Person:\n    pass\n\nclass Dancer:\n    pass\n\nclass Example(Person, Dancer):  # Inherits from both\n    pass"
    },
    {
        "q": "What is method overriding?",
        "a": "Changing the behavior of parent class method in child class. Child class provides its own implementation of parent's method.",
        "code": "class Shape:\n    def area(self):\n        return self.x * self.y\n\nclass Circle(Shape):\n    def area(self):  # Overriding parent method\n        return 3.14 * self.x * self.y\n\ncircle = Circle()\ncircle.area()  # Uses Circle's area method"
    },
    {
        "q": "What is the super() keyword?",
        "a": "super() is used to refer to parent class. Used to call parent class constructor and methods in child class.",
        "code": "class Parent:\n    def __init__(self, name):\n        self.name = name\n\nclass Child(Parent):\n    def __init__(self, name, age):\n        super().__init__(name)  # Call parent constructor\n        self.age = age\n\nchild = Child('Harry', 25)"
    },
    {
        "q": "What is MRO (Method Resolution Order)?",
        "a": "In multiple inheritance, MRO determines the order in which parent classes are searched when executing a method. Python uses C3 Linearization algorithm.",
        "code": "class A:\n    def show(self):\n        print('A')\n\nclass B(A):\n    pass\n\nclass C(A):\n    pass\n\nclass D(B, C):\n    pass\n\nprint(D.mro())  # Shows method resolution order\nd = D()\nd.show()  # Uses A's show method"
    },
]

for i, qa in enumerate(inheritance_qa, 1):
    story.append(Paragraph(f"<b>Q{i}: {qa['q']}</b>", question_style))
    story.append(Paragraph(f"<b>Answer:</b> {qa['a']}", answer_style))
    story.append(Paragraph("<b>Code Example:</b>", styles['Normal']))
    
    for line in qa['code'].split('\n'):
        story.append(Paragraph(line if line.strip() else '&nbsp;', code_style))
    
    story.append(Spacer(1, 0.15*inch))

story.append(PageBreak())

# ============= SECTION 5: ADVANCED CONCEPTS =============
story.append(Paragraph("SECTION 5: Advanced Python Concepts", heading_style))
story.append(Spacer(1, 0.1*inch))

advanced_qa = [
    {
        "q": "What are generators and how do they work?",
        "a": "Generators are special functions that yield values one at a time using 'yield' statement. They're memory-friendly because they generate values on-the-fly instead of storing all in memory.",
        "code": "def generator():\n    for i in range(5):\n        yield i  # Yields value and suspends\n\ngen = generator()\nfor value in gen:\n    print(value)  # Prints 0 to 4\n\n# Or use next()\ngen = generator()\nprint(next(gen))  # 0\nprint(next(gen))  # 1"
    },
    {
        "q": "What is function caching and lru_cache?",
        "a": "Function caching stores function results to avoid repeated computation. lru_cache decorator from functools caches results of recent function calls. Good for expensive computations.",
        "code": "from functools import lru_cache\nimport time\n\n@lru_cache(maxsize=None)\ndef fibonacci(n):\n    if n < 2:\n        return n\n    return fibonacci(n-1) + fibonacci(n-2)\n\n# First call computes, second call uses cache\nprint(fibonacci(10))  # Slower\nprint(fibonacci(10))  # Faster (cached)"
    },
    {
        "q": "What are decorators in Python?",
        "a": "Decorators are functions that modify/enhance other functions without changing their source code. They wrap a function and extend its behavior using @ notation.",
        "code": "def my_decorator(func):\n    def wrapper(*args, **kwargs):\n        print('Before function')\n        result = func(*args, **kwargs)\n        print('After function')\n        return result\n    return wrapper\n\n@my_decorator\ndef hello(name):\n    print(f'Hello {name}')\n\nhello('Harry')  # Prints: Before, Hello Harry, After"
    },
    {
        "q": "What is the walrus operator (:=)?",
        "a": "Walrus operator (assignment expression) added in Python 3.8. Allows assigning and using value in same expression. Useful in while and if statements.",
        "code": "# Without walrus\nl = [1, 2, 3, 4, 5]\nn = len(l)\nwhile n > 0:\n    print(l.pop())\n    n = len(l)\n\n# With walrus\nwhile (n := len(l)) > 0:\n    print(l.pop())\n\n# In if statement\nif (x := 10) > 5:\n    print(f'x is {x}')"
    },
    {
        "q": "What is regex (Regular Expressions)?",
        "a": "Regular expressions (import re) are patterns for matching and manipulating text. Special characters: [] (character class), ^ (start), $ (end), . (any char), * (0+ occurrences), + (1+ occurrences)",
        "code": "import re\n\npattern = r'[0-9]+'\ntext = 'I have 123 apples'\n\nmatch = re.search(pattern, text)\nif match:\n    print(match.group())  # 123\n\nall_matches = re.findall(r'[a-z]+', text)\nprint(all_matches)  # ['I', 'have', 'apples']"
    },
]

for i, qa in enumerate(advanced_qa, 1):
    story.append(Paragraph(f"<b>Q{i}: {qa['q']}</b>", question_style))
    story.append(Paragraph(f"<b>Answer:</b> {qa['a']}", answer_style))
    story.append(Paragraph("<b>Code Example:</b>", styles['Normal']))
    
    for line in qa['code'].split('\n'):
        story.append(Paragraph(line if line.strip() else '&nbsp;', code_style))
    
    story.append(Spacer(1, 0.15*inch))

story.append(PageBreak())

# ============= SECTION 6: TIME & ASYNC =============
story.append(Paragraph("SECTION 6: Time Module & Asynchronous Programming", heading_style))
story.append(Spacer(1, 0.1*inch))

time_qa = [
    {
        "q": "What is the time module and its common functions?",
        "a": "time module provides time-related functions. time.time() returns seconds since 1970, time.sleep(sec) waits, time.strftime() formats time as string based on format codes.",
        "code": "import time\n\n# Get current time\ncurrent = time.time()  # Seconds since 1970\nprint(current)\n\n# Sleep for 2 seconds\ntime.sleep(2)\n\n# Format time\nformatted = time.strftime('%D-%M-%Y %H:%M:%S')\nprint(formatted)  # Date and time formatted\n\n# Measure execution time\nstart = time.time()\n# ... code to measure ...\nend = time.time()\nprint(f'Time: {end - start} seconds')"
    },
    {
        "q": "What is asynchronous programming (AsyncIO)?",
        "a": "AsyncIO enables high-performance I/O operations in concurrent, non-blocking manner. Uses async/await keywords. Allows waiting for I/O without freezing program.",
        "code": "import asyncio\n\nasync def fetch_data():\n    print('Fetching...')\n    await asyncio.sleep(2)  # Simulate I/O\n    print('Done fetching')\n    return 'data'\n\nasync def main():\n    result = await fetch_data()\n    print(f'Result: {result}')\n\n# Run async function\nasyncio.run(main())"
    },
]

for i, qa in enumerate(time_qa, 1):
    story.append(Paragraph(f"<b>Q{i}: {qa['q']}</b>", question_style))
    story.append(Paragraph(f"<b>Answer:</b> {qa['a']}", answer_style))
    story.append(Paragraph("<b>Code Example:</b>", styles['Normal']))
    
    for line in qa['code'].split('\n'):
        story.append(Paragraph(line if line.strip() else '&nbsp;', code_style))
    
    story.append(Spacer(1, 0.15*inch))

# ============= FOOTER =============
story.append(PageBreak())
story.append(Paragraph("End of Python Learning Guide", heading_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph("This comprehensive guide covers Python basics, OOP, inheritance, file I/O, and advanced concepts.", styles['Normal']))
story.append(Spacer(1, 0.1*inch))
story.append(Paragraph(f"<i>Generated from: Notes.txt, OOPSNotes.txt, and medium.txt</i>", styles['Normal']))

# Build PDF
doc.build(story)
print(f"✅ PDF created successfully: {pdf_file}")
print(f"📄 Location: {pdf_file}")