## Project Overview

This project contains handout materials and homeworks for 2024 python course. 

## Course page

- [Python Essential українською](https://lms.cbs.com.ua/course/view.php?id=53) 
## Installation Instructions

### Prerequisites
- Ensure you have [PyCharm](https://www.jetbrains.com/pycharm/download/) installed on your computer.
- Ensure you have [Git](https://git-scm.com/downloads) installed.

### Steps to Download and Open This Project in PyCharm

1. **Clone the Repository**
    - Open your terminal (command prompt or Git Bash).
    - Clone the repository using the following command:
      ```sh
      git clone https://github.com/yourusername/your-repository.git
      ```
    - Replace `https://github.com/yourusername/your-repository.git` with the actual URL of your repository.

2. **Open the Project in PyCharm**
    - Launch PyCharm.
    - Click on `Open` or `Open Project`.
    - Navigate to the directory where you cloned the repository and select the project folder.
    - Click `OK` to open the project.

3. **Set Up the Virtual Environment**
    - In PyCharm, open the terminal.
    - Create a virtual environment:
      ```sh
      python -m venv myenv
      ```
    - Activate the virtual environment:
      - On Windows:
        ```sh
        myenv\Scripts\activate
        ```
      - On macOS and Linux:
        ```sh
        source myenv/bin/activate
        ```

4. **Install Project Dependencies**
    - If your project has a `requirements.txt` file, install the dependencies:
      ```sh
      pip install -r requirements.txt
      ```

5. **Run the Project**
    - Once the dependencies are installed, you can run your project by navigating to the main script or module and clicking the run button in PyCharm.

## Additional Notes
- Ensure to keep your `.env` and `myenv` directories private as they contain sensitive information and dependencies specific to your environment.
