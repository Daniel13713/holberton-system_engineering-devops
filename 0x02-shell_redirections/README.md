REDIRECTIONS

0. Hello World 
Write a script that prints “Hello, World”, followed by a new line to the standard output.
sol: echo "Hello, World"

1. Confused smiley
Write a script that displays a confused smiley "(Ôo)'.
sol: echo "\"(Ôo)'"

2. Let's display a file
Display the content of the /etc/passwd file.
sol: cat file

3. What about 2? 
Display the content of /etc/passwd and /etc/hosts
sol: cat file1 file2 ...

4. Display the last 10 lines of /etc/passwd
sol: 

5. Display the first 10 lines of /etc/passwd

6. Write a script that displays the third line of the file iacta.
The file iacta will be in the working directory
You’re not allowed to use sed

7. Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

8. Save current state of directory
Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.

9. Duplicate last line 
Write a script that duplicates the last line of the file iacta
The file iacta will be in the working directory


10. Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.
# 0x02. Shell, I/O Redirections and filters

<html>
<div class="panel panel-default" id="project-description">
 <div class="panel-body">
  <h2>
   Resources
  </h2>
  <p>
   <strong>
    Read or watch
   </strong>
   :
  </p>
  <ul>
   <li>
    <a href="http://linuxcommand.org/lc3_lts0070.php" target="_blank" title="Shell, I/O Redirection">
     Shell, I/O Redirection
    </a>
   </li>
   <li>
    <a href="http://mywiki.wooledge.org/BashGuide/SpecialCharacters" target="_blank" title="Special Characters">
     Special Characters
    </a>
   </li>
  </ul>
  <p>
   <strong>
    man or help
   </strong>
   :
  </p>
  <ul>
   <li>
    <code>
     echo
    </code>
   </li>
   <li>
    <code>
     cat
    </code>
   </li>
   <li>
    <code>
     head
    </code>
   </li>
   <li>
    <code>
     tail
    </code>
   </li>
   <li>
    <code>
     find
    </code>
   </li>
   <li>
    <code>
     wc
    </code>
   </li>
   <li>
    <code>
     sort
    </code>
   </li>
   <li>
    <code>
     uniq
    </code>
   </li>
   <li>
    <code>
     grep
    </code>
   </li>
   <li>
    <code>
     tr
    </code>
   </li>
   <li>
    <code>
     rev
    </code>
   </li>
   <li>
    <code>
     cut
    </code>
   </li>
   <li>
    <code>
     passwd (5)
    </code>
    (
    <em>
     i.e.
     <code>
      man 5 passwd
     </code>
    </em>
    )
   </li>
  </ul>
  <h2>
   Learning Objectives
  </h2>
  <p>
   At the end of this project, you are expected to be able to
   <a href="https://fs.blog/feynman-learning-technique/" target="_blank" title="explain to anyone">
    explain to anyone
   </a>
   ,
   <strong>
    without the help of Google
   </strong>
   :
  </p>
  <h3>
   Shell, I/O Redirection
  </h3>
  <ul>
   <li>
    What do the commands
    <code>
     head
    </code>
    ,
    <code>
     tail
    </code>
    ,
    <code>
     find
    </code>
    ,
    <code>
     wc
    </code>
    ,
    <code>
     sort
    </code>
    ,
    <code>
     uniq
    </code>
    ,
    <code>
     grep
    </code>
    ,
    <code>
     tr
    </code>
    do
   </li>
   <li>
    How to redirect standard output to a file
   </li>
   <li>
    How to get standard input from a file instead of the keyboard
   </li>
   <li>
    How to send the output from one program to the input of another program
   </li>
   <li>
    How to combine commands and filters with redirections
   </li>
  </ul>
  <h3>
   Special Characters
  </h3>
  <ul>
   <li>
    What are special characters
   </li>
   <li>
    Understand what do the white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, tilde and how and when to use them
   </li>
  </ul>
  <h3>
   Other Man Pages
  </h3>
  <ul>
   <li>
    How to display a line of text
   </li>
   <li>
    How to concatenate files and print on the standard output
   </li>
   <li>
    How to reverse a string
   </li>
   <li>
    How to remove sections from each line of files
   </li>
   <li>
    What is the
    <code>
     /etc/passwd
    </code>
    file and what is its format
   </li>
   <li>
    What is the
    <code>
     /etc/shadow
    </code>
    file and what is its format
   </li>
  </ul>
  <h2>
   Requirements
  </h2>
  <h3>
   General
  </h3>
  <ul>
   <li>
    Allowed editors:
    <code>
     vi
    </code>
    ,
    <code>
     vim
    </code>
    ,
    <code>
     emacs
    </code>
   </li>
   <li>
    All your scripts will be tested on Ubuntu 20.04 LTS
   </li>
   <li>
    All your scripts should be exactly two lines long (
    <code>
     $ wc -l file
    </code>
    should print 2)
   </li>
   <li>
    All your files should end with a new line (
    <a href="http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789">
     why?
    </a>
    )
   </li>
   <li>
    The first line of all your files should be exactly
    <code>
     #!/bin/bash
    </code>
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, describing what each script is doing
   </li>
   <li>
    You are not allowed to use backticks,
    <code>
     &amp;&amp;
    </code>
    ,
    <code>
     ||
    </code>
    or
    <code>
     ;
    </code>
   </li>
   <li>
    All your files must be executable
   </li>
   <li>
    You are not allowed to use
    <code>
     sed
    </code>
    or
    <code>
     awk
    </code>
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <p>
   Read your
   <code>
    /etc/passwd
   </code>
   and
   <code>
    /etc/shadow
   </code>
   files.
  </p>
  <p>
   Note: You do not have to learn about
   <code>
    fmt
   </code>
   ,
   <code>
    pr
   </code>
   ,
   <code>
    du
   </code>
   ,
   <code>
    gzip
   </code>
   ,
   <code>
    tar
   </code>
   ,
   <code>
    lpr
   </code>
   ,
   <code>
    sed
   </code>
   and
   <code>
    awk
   </code>
   yet.
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/208)
</html>