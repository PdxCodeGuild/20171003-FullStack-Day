# Using the CLI

CLI stands for 'command-line interface', and it was the only way to use a computer before the development of GUIs 'graphical user interface'. It's still used to perform many computer operations that go 'under the hood'.

#### Opening the CLI

In OS X, the default CLI is called `Terminal`, which you can find by typing `terminal` in search, or under `Finder -> Applications -> Utilities`.

In Windows, the default CLI is `cmd`, which you can find by typing `cmd` in search, or pressing `Windows+R`, typing `cmd`, and hitting `enter`. This will work for executing python, but there's no color differentiation, and some commands like `ls` and `rm` won't work in `cmd`. A much better CLI is [Cmder](http://cmder.net/). Another option for Windows is [Powershell](https://msdn.microsoft.com/en-us/powershell/scripting/setup/installing-windows-powershell).

In Linux, you can open a terminal with `Ctrl + Alt + T`.

#### Common CLI Commands

- `pwd` displays the path of the current directory
- `ls` lists the contents of the current directory
- `cd <directoryname>` change directory
    - `cd ..` will bring you into the parent directory
    - `cd` alone will return you to your 'home' directory
- `mkdir <foldername>` create a new folder 
- `rmdir <foldername>` removes a folder
- `rm <filename>` removes a file
- `mv filename1 filename2` moves or renames a file
- `cp filename1 filename2` copies a file
- `up-arrow` will bring up the last command entered
- `tab` will attempt to autocomplete whatever you're typing
    - try `cd D` + `tab` + `tab`
- `ctrl+c` kill currently running process
