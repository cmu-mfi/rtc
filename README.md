# README for the Robotics Training Center (RTC) Git Repository

This documentation is written in [Markdown][url01].

_Markdown_ files end in **.md**. You need a program to translate _Markdown_ code
into **.html**. The Makefile and build scripts are written to execute the
[Sphinx][url02] compiler, which is capable of translating **.md** files into a
variety of target formats. It is also capable of extracting documentation from
the source code of certain programming languages, and formatting that into
target representation.

## Installing _Sphinx_

_Sphinx_ installation documentation is available [here][url03].

Below are TLDR steps to build html pages locally.

**Install Dependencies**
```
git clone https://github.com/cmu-mfi/rtc.git
cd ./rtc
python -m venv ./.venv

# Linux/macOS Terminal
source .venv/bin/activate

# Windows CMD
call .venv\Scripts\activate.bat

pip install -U sphinx sphinx_rtd_theme myst_parser
```

**Build doc**
```
cd ./rtc

# Linux/macOS Terminal
source .venv/bin/activate

# Windows CMD
call .venv\Scripts\activate.bat

cd ./doc
make html
```
The HTML pages are in _build/html.  

---

### Troubleshooting macOS Sonoma (Version 14.5)

The instructions are good at getting started, but they do not explain the whole
process for a particular version of operating system (OS). This section is to
document some of the OS-specific experiences people have in getting started and
trying to build this repository.

#### Step 1. brew install sphinx-doc

At the macOS Darwin command line, type:  

> % brew install sphinx-doc

_Sphinx_ and its dependencies should install properly, but they will not link to
the homebrew application directory, hence you will be unable to invoke it at the
command line. In the installation message output, you will see a message similar
to the following:

> sphinx-doc is keg-only, which means it was not symlinked into /opt/homebrew,
> because this formula is mainly used internally by other formulae.
> Users are advised to use `pip` to install sphinx-doc.

The message is incorrect for the following reason:

> The default and _preferred_ version of _Python_ on POSIX operating systems
> like macOS Darwin is **Python3**, hence the command line should read:
 
> % pip3 install sphinx-doc

If you execute the "pip3 install sphinx-doc" command, macOS Darwin will throw an
error:

> error: externally-managed-environment
> 
> × This environment is externally managed
> ╰─> To install Python packages system-wide, try brew install
>     xyz, where xyz is the package you are trying to
>     install.
>     
>     If you wish to install a Python library that isn't in Homebrew,
>     use a virtual environment:
>     
>     python3 -m venv path/to/venv
>     source path/to/venv/bin/activate
>     python3 -m pip install xyz
>     
>     If you wish to install a Python application that isn't in Homebrew,
>     it may be easiest to use 'pipx install xyz', which will manage a
>     virtual environment for you. You can install pipx with
>     
>     brew install pipx
>     
>     You may restore the old behavior of pip by passing
>     the '--break-system-packages' flag to pip, or by adding
>     'break-system-packages = true' to your pip.conf file. The latter
>     will permanently disable this error.
>     
>     If you disable this error, we STRONGLY recommend that you additionally
>     pass the '--user' flag to pip, or set 'user = true' in your pip.conf
>     file. Failure to do this can result in a broken Homebrew installation.

The documentation for _pipx_ does not explain if it defaults to _Python2_ or
_Python3_. My attempt at installing and using _pipx_ failed, so I reverted to
using the virtual environment commands, directly.

#### Step 2. Create a Python3 **_Virtual Environment_**

Full documentation on _Python3_ virtual environments is [here][url04].

Python3 has a convenient way to isolate a combination of Python packages from
each other so that you need not worry about package conflicts and/or version
control issues. If you are already in the know, you probably created a virtual
environment already. If not, the instructions are provided further down the
_Sphinx_ installation instructions [web page][url05].

> - Please remember to use _Python3_ instead of _Python2_.
> - Give the virtual environment directory a name that is consistent with its
>   intended purpose

> % python3 -m venv ~/.venv-sphinx-doc

#### Step 3. Activate the _Python3_ _Virtual Environment_

Now that you built a _Sphinx_-specific virtual environment, every time that you
want to use _Sphinx_, you should activate its environment and run the code from
there. Consequently, you will perform the following step multiple times:

> % source ~/.venv-sphinx-doc/bin/activate

**If you have already completed the installation of the _Sphinx_ packages and
wish to use it to build the documentation tree, please skip the next step.**

Notes:  
1. You can *activate* a virtual environment multile times. Only one shell process will be created, however.  
2. Exit a _Python3_ virtual environment by typing **deactivate** at the command line prompt.  
3. Typing **exit** or **Ctrl-D** to exit the virtual environment will not only exit the virtual environment, but also kill the parent shell.  

#### Step 4. Install _Sphinx's Python3 Packages_

The following packages should be installed in the _Sphinx_ virtual environment
in order for it to work properly:

> (venv) % pip3 install -U sphinx  
> (venv) % pip3 install -U sphinx\_rtd\_theme  
> (venv) % pip3 install -U myst\_parser  

The individual commands can be merged into a single-line command:

> (venv) % pip3 install -U sphinx sphinx\_rtd\_theme myst\_parser

Notes:  
1. The "-U" switch indicates "upgrade". If there are updates for any _Python3_
package, it will be updated.  
2. The list of packages to install can be found in the GitHub repository file:
rtc / .github / workflows / documentation.yml  

#### Step 5. Build the Documentation

Go to the **rtc / doc** directory and run the _make_ command.

> (venv) % cd ../rtc/doc  
> (venv) % make html  

> build succeeded, 6 warnings.  
>   
> The HTML pages are in _build/html.  



[url01]: https://www.markdownguide.org/ "Markdown Homepage"
[url02]: https://www.sphinx-doc.org/ "Sphinx Homepage"
[url03]: https://www.sphinx-doc.org/en/master/usage/installation.html "Sphinx Installation Instructions"
[url04]: https://docs.python.org/3/library/venv.html "Python3 Virtual Environment Documentation"
[url05]: https://www.sphinx-doc.org/en/master/usage/installation.html#using-virtual-environments "Sphinx: Using Virtual Environments"
