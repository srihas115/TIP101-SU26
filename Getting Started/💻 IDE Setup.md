[https://courses.codepath.org/courses/tip101/pages/ide_setup#feedback-modal](https://courses.codepath.org/courses/tip101/pages/ide_setup#feedback-modal)
## IDE Setup Guide


In this course, we will use Visual Studio Code (VS Code) as our primary code editor for Python. VS Code is a lightweight but powerful source code editor that runs on your desktop and is available for Windows, macOS, and Linux. It's widely used by developers because of its flexibility, a rich ecosystem of extensions, and built-in support for various programming languages.


### Prerequisites


You will need the following before starting:


- a computer running Windows, macOS, or Linux

- an internet connection

- a web browser


### Installation


#### Step 1: Installing VS Code


The first step is to download and install VS Code on your computer.


**For Windows:**


- Open your web browser and go to the [VS Code download page](https://code.visualstudio.com/Download).

- Click on the download link for your operating system (Windows, macOS, or Linux).

- Once the download is complete, run the installer and follow the on-screen instructions to install VS Code on your computer.

- Accept the license agreement.

- Choose the installation location or leave it as default.

- It's recommended to check the boxes for:

- "Add to PATH" so you can open VS Code from the terminal or command prompt.

- "Create a desktop icon" for easy access.

- Click **Install** and let the installation complete.

- After the installation is finished, you can launch VS Code by searching for it in your applications or by clicking on the desktop icon.


**For macOS:**


- After downloading the `.zip` file, locate it in your Downloads folder and double-click it to unzip.

- You will see the `Visual Studio Code` application. Drag this application into your **Applications** folder.

- You can now open VS Code from the Applications folder or by searching for it using Spotlight.


#### Step 2: Installing Python


Before you can use Python in VS Code, you need to have Python installed on your computer. If you're not sure, follow these steps to check if Python is installed.


**For Windows:**


- Open the **Command Prompt** by pressing `Win + R`, typing `cmd`, and pressing Enter.

- Type the following command and press Enter:

```python
python --version
```

If Python is installed, you will see the version number. If not, you will see an error message.


**For macOS:**


- Open the **Terminal** by pressing `Cmd + Space`, typing `Terminal`, and pressing Enter.

- Type the following command and press Enter:

```python
python3 --version
```

If Python is installed, you will see the version number. If not, you will see an error message.


If Python is not installed on your computer, follow these steps to install it.


- Go to the official Python website at [python.org](https://www.python.org/).

- On the downloads page, click on the **Download Python X.X.X** button to download the latest version of Python.


**For Windows:**


- After downloading the Python installer (`python-3.X.X.exe`), open it.

- In the installer, **check the box labeled "Add Python to PATH"** at the bottom of the window. This step is crucial to ensure that Python can be run from the command prompt.

- Click **Install Now** and follow the on-screen instructions to complete the installation.

- Once installation is complete, click **Close**.

- Confirm installation by reopening the Command Prompt and typing:

```python
python --version
```

You should now see the installed Python version.


**For macOS:**


- Open the downloaded `.pkg` installer.

- Follow the on-screen instructions to install Python. You may need to enter your password to authorize the installation.

- Once the installation is complete, open the Terminal and type:

```python
python3 --version
```

You should now see the installed Python version.


#### (Optional) Installing pip


`pip` is a package manager for Python that allows you to install and manage additional libraries and dependencies. It is included with Python versions 3.4 and above, so you may already have it installed. You can check if `pip` is installed by running the following command:


```python
pip --version
```

or for macOS:


```python
pip3 --version
```

If `pip` is not installed, you can install it by following the instructions on the official [pip installation guide](https://pip.pypa.io/en/stable/installation/).


### Step 3: Setting Up VS Code


Now that you have VS Code and Python installed on your computer, the next step is to configure VS Code for Python development.


- Open VS Code by searching for it in your applications or by clicking on the desktop icon.

- If it's your first time using VS Code, you will see a welcome screen with options to customize your settings. You can choose to skip this step for now.


**Installing the Python Extension**


The Python extension in VS Code adds important features such as IntelliSense (code completion), linting, debugging, code formatting, and more. To install the Python extension, follow these steps:


- Click on the **Extensions** icon in the sidebar (or press `Ctrl + Shift + X` / `Cmd + Shift + X` on macOS).

- In the search bar, type `Python` and press Enter.

- Look for the extension named `Python` by Microsoft and click on the **Install** button.

- Once installed, VS Code may prompt you to install any additional tools needed for Python, such as `pylint` for linting (highlighting errors). Follow the prompts to install these tools if needed.


**Configuring the Python Interpreter**


VS Code needs to use the correct Python interpreter to run your Python code. You can set the Python interpreter in VS Code by following these steps.


- Create a new Python file by clicking on the **New File** icon in the sidebar (or press `Ctrl + N` / `Cmd + N` on macOS) and saving it with a `.py` extension (e.g., `hello.py`).

- VS Code will detect that the file is a Python file and may prompt you to select a Python interpreter. If you don't see this prompt, you can manually select the interpreter:

- Open the **Command Palette** by pressing `Ctrl + Shift + P` (Windows) or `Cmd + Shift + P` (macOS).

- In the command bar, type `Python: Select Interpreter` and press Enter.

- You will see a list of available Python interpreters. Choose the one you installed earlier (usually Python 3.x.x).


### Step 4: Creating and Running a Python Program


Now that your environment is set up, let's create a simple Python program and run it in VS Code.


- Create a new Python file by clicking on the **New File** icon in the sidebar (or press `Ctrl + N` / `Cmd + N` on macOS) and saving it with a `.py` extension (e.g., `hello.py`).

- Write the following Python code in the file:

```python
print("Hello, World!")
```

- To run the program, right-click anywhere in the editor and select **Run Python File in Terminal**. You can also use the shortcut `Ctrl + F5` (Windows) or `Cmd + F5` (macOS).

- You should see the output `Hello, World!` printed in the terminal at the bottom of the VS Code window.


### Step 5: Making VS Code Your Own


VS Code is a highly customizable editor that allows you to tailor it to your preferences. You can adjust the layout, configure shortcuts, and add powerful extensions to create a coding space that suits your needs.


#### Themes


One of the easiest ways to personalize VS Code is by changing the color theme. You can choose from a variety of themes to change the appearance of the editor, making it easier on the eyes or more visually appealing. VS Code comes with several built-in themes, but you can also install custom themes from the marketplace.


Browsing themes in VS Code isn't very easy, though, since there isn't a gallery that you can quickly scan. Instead, you have to find each theme and open it in the marketplace to see what it looks like. However, [VS Code Themes](https://vscodethemes.com/) is a website that showcases a wide variety of themes with previews, making it easier to find one that suits your taste. Once you find a theme you like, you can select it, then choose the **VS Code** button to open the theme extension in the extension marketplace. From there, you can install the theme and apply it to your editor.


#### Linting and Formatting


Linting and formatting tools help keep your code clean and error-free by highlighting potential issues and automatically formatting your code. These tools are often included with the Python extension, but you can configure additional settings if needed.


**Enabling linting**


VS Code automatically enables linting (using `pylint` by default) when you install the Python extension.


To manually configure linting settings, go to the **Command Palette** (`Ctrl + Shift + P` / `Cmd + Shift + P`) and search for `Python: Enable Linting`. You can toggle linting on or off from here.


**Setting up code formatting**


To automatically format your Python code, you can use the `autopep8` or `black` code formatters. These formatters can be installed using `pip`:


```python
pip install autopep8
```

or


```python
pip install black
```

To configure the code formatter in VS Code, go to **File > Preferences > Settings** (or press `Ctrl + ,` / `Cmd + ,`), search for `Python Formatting Provider`, and choose `autopep8` or `black` as the formatter.


You can now format your code by right-clicking in the editor and selecting **Format Document** or using the shortcut `Shift + Alt + F` (Windows) or `Shift + Option + F` (macOS).


### Troubleshooting Common Issues


#### Python Not Recognized in VS Code


If you try to run Python code, but VS Code doesn't recognize Python, you may need to set the Python interpreter manually. Follow the steps in **Step 3** to configure the Python interpreter in VS Code.


If you're still having issues, make sure Python is added to the system PATH.


**For Windows:**


- Open the **Start Menu** and search for `Environment Variables`.

- Click on **Edit the system environment variables**.

- In the **System Properties** window, click on **Environment Variables**.

- In the **System Variables** section, look for the `Path` variable and click **Edit**.

- Click **New** and add the path to your Python installation directory (e.g., `C:\Python39` or `C:\Users\YourUsername\AppData\Local\Programs\Python\Python39`).

- Click **OK** to save the changes.


**For macOS:**


- Ensure `python3` is correctly installed and accessible from the terminal by typing `which python3`. You should see the path to the Python interpreter.


#### Python Extension Not Working Properly


If you have installed the Python extension but are experiencing issues with IntelliSense, linting, or debugging, try the following steps:


- Restart VS Code. Sometimes, extensions don't load properly the first time and simply restarting resolves the issue.

- Ensure the extension is up to date:

- Click on the **Extensions** icon in the sidebar.

- Look for the Python extension and check if there is an update available.

- Click on the **Update** button if an update is available and restart VS Code.

- Reinstall the Python extension:

- Click on the **Extensions** icon in the sidebar.

- Search for the Python extension and click **Uninstall**.

- Click **Install** to reinstall the extension and restart VS Code.


#### Linting Errors Not Showing


If you are not seeing linting errors in your Python code, ensure that linting is enabled in VS Code. Follow the steps in **Linting and Formatting** to enable linting.


#### Code Formatting Issues


If the code doesn't format correctly or automatically when you save it, check the following:


- Ensure the code formatter (`autopep8` or `black`) is installed. You can install them using `pip`:

```python
pip install autopep8
```

or

```python
pip install black
```

- Check the formatter settings in VS Code. Go to **File > Preferences > Settings** and search for `Python Formatting Provider`. Choose `autopep8` or `black` as the formatter.

- Try manually formatting the code by right-clicking in the editor and selecting **Format Document** or using the shortcut `Shift + Alt + F` (Windows) or `Shift + Option + F` (macOS).

- Go to **File > Preferences > Settings** and search for `Format On Save`. Ensure this setting is enabled to automatically format the code when you save the file.


### Backing Up and Sharing Your Work


Keeping your work safe and accessible is an essential part of any development process. Having a reliable backup and sharing solution can save you from losing progress and make it easier to collaborate.


#### Using Google Drive


Google Drive is a convenient tool for backing up and sharing your Python files with others. It allows you to store your files in the cloud and access them from any device with an internet connection. Follow these steps to create a folder in Google Drive, upload your Python files, and share them with others.


**Step 1: Creating a Folder in Google Drive**


- Open your web browser and go to [Google Drive](https://drive.google.com/).

- Sign in with your Google account if you haven't already.

- Click on the **New** button and select **Folder**.

- Name the folder (e.g., `TIP Unit 1 Problems`) and click **Create**.


**Step 2: Uploading Python Files to Google Drive**


- Open the folder you created in Google Drive.

- Click on the **New** button and select **File upload**.

- A file browser window will open. Navigate to the location on your computer where your Python files are stored.

- Select the files you want to upload (you can select multiple files by holding `Ctrl` or `Cmd`) and click **Open**.

- The files will be uploaded to the folder in Google Drive. You'll see the upload progress in the bottom-right corner of your screen.


**Step 3: Sharing the Google Drive Folder**


- Right-click on the folder in Google Drive and select **Share**.

- In the sharing window, enter the email addresses of the people you want to share the folder with. You can also adjust their permissions:

- **Viewer**: Can view the files but not edit them.

- **Commenter**: Can view and comment on the files.

- **Editor**: Can view, comment, and edit the files.

- Click **Send** to share the folder with the selected people.


Alternatively, you can click **Copy link** and share the link with anyone, then adjust the sharing settings as needed.


#### Using GitHub


GitHub is a powerful platform for version control, collaboration, and sharing your code with others. It allows you to create repositories to store your code, track changes, and work with others on projects. Follow these steps to create a GitHub account, create a repository, and upload your Python files.


**Step 1: Creating a GitHub Account**


- Open your web browser and go to [GitHub](https://www.github.com/).

- Click on **Sign up** and follow the prompts to create an account.

- Verify your email address to complete the registration process.


**Step 2: Setting Up Git in VS Code**


Before syncing your Python files with GitHub, you need to set up Git in VS Code. Follow these steps to configure Git:


- Open VS Code and go to the **Source Control** tab in the sidebar.

- Click on the **Initialize Repository** button to create a new Git repository.

- You will be prompted to select a folder for the repository. Choose the folder where your Python files are stored.

- Once the repository is initialized, you will see the files in the **Changes** section of the Source Control tab.


**Step 3: Committing and Pushing Changes to GitHub**


- In the Source Control tab, you will see the changes you made to your Python files. Click on the **+** button next to the files to stage them for commit.

- Enter a commit message in the text box at the top of the Source Control tab and click the checkmark icon to commit the changes.

- Click on the ellipsis (`...`) next to the commit message and select **Push** to push the changes to GitHub.

- You will be prompted to sign in to GitHub if you haven't already. Follow the prompts to complete the push.


### Using GitHub Copilot in VS Code


You may have the option of gaining access to GitHub Copilot, an AI-powered code completion tool, through the GitHub Student Developer Pack.


#### GitHub Student Developer Pack


To access the GitHub Student Developer Pack, follow these steps:


- Go to the [GitHub Student Developer Pack](https://education.github.com/pack) website.

- Click on the **Sign up for Student Developer Pack** button.

- Follow the prompts to verify your student status.

- Once your student status is verified, you will gain access to the GitHub Student Developer Pack, which includes GitHub Copilot.


#### GitHub Copilot Installation


To install GitHub Copilot in VS Code, follow these steps:


- Open VS Code and go to the **Extensions** tab in the sidebar.

- Search for `GitHub Copilot` in the extensions marketplace.

- Click on the **Install** button to install GitHub Copilot and GitHub Copilot Chat.

- Once installed, you will need to sign in to your GitHub account to activate GitHub Copilot.

- Follow the prompts to sign in and activate GitHub Copilot.


#### Using GitHub Copilot


You should disable the Copilot inline suggestions so it doesn't interfere with your learning process. To do this, follow these steps:


- Open VS Code and go to **File > Preferences > Settings** (or press `Ctrl + ,` / `Cmd + ,`).

- Search for `copilot enable auto completions`.

- Uncheck the box to disable inline suggestions.


GitHub Copilot can be a helpful tool for generating code snippets and providing suggestions as you write code. However, it's important to understand the code you're writing and not rely solely on Copilot for your learning.


#### Helpful Resources


- [Set up GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/setup)

- [Getting started with GitHub Copilot Chat in VS Code](https://code.visualstudio.com/docs/copilot/copilot-chat)

- [Code completions with GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/ai-powered-suggestions)

- [Using Copilot Chat in VS Code](https://code.visualstudio.com/docs/copilot/copilot-chat)

- [Making Copilot Chat an expert in your workspace](https://code.visualstudio.com/docs/copilot/workspace-context)
