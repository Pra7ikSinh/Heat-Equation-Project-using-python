To set up and run your project from GitHub on Windows, follow these detailed steps:

### Step 1: Install Git for Windows
1. **Download Git** from the official [Git website](https://git-scm.com/).
2. **Install Git**:
   - Run the installer and follow the setup instructions.
   - During installation, choose **Git from the command line** and use the default options.

### Step 2: Clone the Repository
1. **Open Command Prompt** (Press `Windows + R`, type `cmd`, and press Enter).
2. **Clone your GitHub repository**:
   ```bash
   git clone https://github.com/Pra7ikSinh/Heat-Equation-Project-using-python.git
   ```

3. **Navigate to the project directory**:
   ```bash
   cd Heat-Equation-Project-using-python
   ```

### Step 3: Install Python
1. **Download Python**: Go to the [Python website](https://www.python.org/downloads/) and download the latest version.
2. **Install Python**:
   - Ensure you check **Add Python to PATH** during installation.
   - Follow the installation steps.

3. **Verify Python Installation**:
   ```bash
   python --version
   ```

### Step 4: Install Required Libraries
1. **Install `numpy` and `matplotlib`**:
   ```bash
   pip install numpy matplotlib
   ```

### Step 5: Run the Scripts
1. **Run the 1D Heat Equation script**:
   ```bash
   python 1DHeatEqaution.py
   ```

2. **Run the 2D Heat Equation script**:
   ```bash
   python 2DHeatEquation.py
   ```

By following these steps, you can successfully set up and run your heat equation project on Windows.