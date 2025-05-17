# Contributor Guide

## Task Distribution

### Team Roles and Responsibilities

| Member | Responsibilities |
|--------|-----------------|
| **ZARAGOZA, Marie Criz** | • Writing Activity Documentation Report with LaTeX<br>• Apply CSS styling to improve app interface |
| **CURADA, John Paul M.** | • Oversee project development<br>• Lead Development of App Interface |
| **LUCERO, Ken Audie S.** | • Provide pseudocode, simulation, and discussion for Travelling Salesman Algorithm <br>• Provide one (1) pseudocode, simulation, and discussion for OPTIMIZED Travelling Salesman Algorithm |
| **FAELDONIA, Elias Von Isaac R.** | • Analysis of Time Complexity Provide a detailed analysis of the time complexity of each brute force algorithm stated above. Please show and explain why do you get that time complexity.<br> • Compare these algorithms in a tabular form and showing the Strengths, Weaknesses, and 5 Real World Application
| **OJA, Ma. Izabelle L.** | • Provide pseudocode, simulation, and discussion for Selection Sort<br>• Provide one (1) pseudocode, simulation, and discussion for OPTIMIZED Selection Sort Algorithm |
| **RACELIS, Michael Richmond V.** | • Provide pseudocode, simulation, and discussion for Knapsack Problem Algorithm<br>• Provide one (1) pseudocode, simulation, and discussion for OPTIMIZED Knapsack Problem Algorithm|
| **CANSINO, Florence Lee F.** | • Provide pseudocode, simulation, and discussion for Sequential Search<br>• Provide one (1) pseudocode, simulation, and discussion for OPTIMIZED Sequential Search Algorithm |
| **RAMILO, Gian G.** | • Lead  |
| **MAGTANONG, Gabriel Andre E.** | • Provide pseudocode, simulation, and discussion for Bubble Sort<br>• Provide one (1) pseudocode, simulation, and discussion for OPTIMIZED Bubble Sort Algorithm  |

## Contribution Workflow

### Getting Started

1. **Clone the Repository**
   ```
   git clone https://github.com/G6-DesAlgorithmists/g6-mp2-desalgo
   cd g6-mp2-desalgo
   ```

2. **Switch to Development Branch**
   ```
   git checkout dev
   ```

3. **Update Your Local Repository**
   ```
   git pull origin dev
   ```

4. **Create Your Task Branch**
   ```
   git checkout -b <branch-name>
   ```
   
   Your branch name should correspond to your task:
   - `brute-force/bubble-sort`
   - `optimized/selection-sort`
   - etc.

### Directory Structure

1. **Navigate to the Correct Directory**
   - For brute force algorithms: `algorithms/brute_force/`
   - For optimized algorithms: `algorithms/optimized/`

2. **Create Your Algorithm File**
   - Ensure your file name corresponds to the function name
   - Example: `bubble_sort.py` for the bubble sort algorithm

### Coding Standards

#### Function Structure

Each algorithm function must include:

1. **Clear Function Name**
   - Use descriptive names that follow the Reddick VBA naming convention
   - Function names should be in `snake_case`

2. **Properly Formatted Docstring**
   - Brief description of the function's purpose
   - Detailed description of how the algorithm works
   - Documentation of all arguments with their types
   - Specification of what it returns and the return type
   - Example of how to use the function

3. **Function Body**
   - Well-commented logic implementation
   - Clear variable naming
   - Efficient implementation of the algorithm

4. **Return Statement**
   - Properly return the expected result

#### Example Function Template

```python
def bubble_sort(intArray):
    """
    Sort an array using the bubble sort algorithm.
    
    Description:
    This function implements the bubble sort algorithm which repeatedly steps
    through the list, compares adjacent elements, and swaps them if they are
    in the wrong order.
    
    Arguments:
        intArray (list): The list of integers to be sorted.
    
    Returns:
        list: The sorted list in ascending order.
    
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    # Create a copy of the array to avoid modifying the original
    arr = intArray.copy()
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize if no swaps occur
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if current element is greater than next
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # If no swapping occurred in this pass, array is sorted
        if not swapped:
            break
    
    # Return the sorted array
    return arr
```

### Committing Your Changes

1. **Check Your Changes**
   ```
   git status
   ```

2. **Add Your Files**
   ```
   git add algorithms/brute_force/your_algorithm.py
   ```

3. **Commit with a Descriptive Message**
   ```
   git commit -m "Add brute force implementation of bubble sort"
   ```

4. **Push to Your Branch**
   ```
   git push origin <your-branch-name>
   ```

### Submitting Your Work

1. **Create a Pull Request**
   - Go to the GitHub repository
   - Click on "Pull Requests" > "New Pull Request"
   - Select your branch to merge into `dev`
   - Provide a detailed description of your implementation (links of your resources)

2. **Respond to Feedback**
   - Be ready to address any feedback or requested changes
   - Make additional commits to your branch if needed
   - madiwara po si JP

## Guidelines

- **Quality**: Ensure high-quality, well-tested code with no errors
- **Documentation**: Thoroughly document your algorithm with comments and proper docstrings
- **Testing**: Include test cases to verify your algorithm works correctly
- **Respect**: Follow the project structure and coding standards
- **Communication**: Use the group chat for questions or clarification

Thank you for contributing to our Machine Problem 2 project on Brute Force Algorithms! (SANA PUMASA) 