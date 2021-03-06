# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


 
Make a cheat sheet for yourself: a list of commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.
<table>
<tr><td>pwd </td><td>print working directory</td></tr>
<tr><td>hostname </td> <td>name of computer</td></tr>
<tr><td>cd </td><td> change directory</td></tr>
<tr><td>cd .. </td><td>go up a directory</td></tr>
<tr><td>mkdir </td><td>make a directory</td></tr>
<tr><td>ls  </td><td>list directory</td></tr>
<tr><td>rmdir </td><td>remove directory</td></tr>
<tr><td>pushd </td><td>creates a "bookmark" to current directory</td></tr>
<tr><td>popd  </td><td>returns to last pushd directory</td></tr>
<tr><td>touch </td><td>make a new empty file</td></tr>
<tr><td>cp  </td><td>copy file "cp oldfilename.txt newfilename.txt"</td></tr>
<tr><td>rmv </td><td>changes name of file "mv oldname newname"</td></tr>
<tr><td>cat  </td><td>show full uneditable file with pagination</td></tr>
<tr><td>rm </td><td>removing a file</td></tr>
<tr><td>-r </td><td>recursive i.e. rm-r removes all subdirectories & files</td></tr>
<tr><td>-x </td><td>only what is noted</td></tr>
<tr><td>-a </td><td>shows subdirectory (all)</td></tr>
<tr><td>-lh  </td><td>shows prints sized in human readable form</td></tr>
<tr><td>-l </td><td>long listing format</td></tr>
<tr><td>-v </td><td>not equal to</td></tr>
<tr><td>$|$  </td><td>action after pipe is affected on file before piping</td></tr>
<tr><td>$<$  </td><td>sends input from right into program on left</td></tr>
<tr><td>$>$  </td><td>takes output from the left then writes to the right</td></tr>
<tr><td>$>>$ </td><td>takes output from the left and appends it to the file on the right</td></tr>
<tr><td>*  </td><td>matches anything</td></tr>
<tr><td>find.  </td><td>find with . indicating "start  here"</td></tr>
<tr><td>grep  </td><td>Globally search a Regular Expression & Print</td></tr>
<tr><td>help or man  </td><td>offers help - follow help with item name to get more info on item</td></tr>
<tr><td>env</td><td>lists current environment variables</td></tr>
<tr><td>remove-item  </td><td>to delete environment variable</td></tr>
</table>

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

>ls = list contents of directory

>ls -a = list contents of directory "all" including hidden files

>ls -l = list contents of directory with long listing form

>ls -lh = list contents of directory with long listing form with sizes listed in human readable form

>Combining parameters allows you to produce the specific output you desire in one line of command line code.

---


---

What does `xargs` do? Give an example of how to use it.

>xargs allows you to create a line that works like a function so the parameters that meet your criteria are fed into xargs as a list. The line of code then executes on each item in the list and iterates until complete on all xargs elements.  If the command line code contains the complete list, then the arguement list is too long to execute.  xargs basically breaks down the list into single line iterations of the function.

`find. -name *2.txt | xargs cat -a less`
>This will print a limited amount of the contents of each text file ending in "2" that is in the current working directory including hidden files.

---
