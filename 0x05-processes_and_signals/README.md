# 0x05. Processes and signals


### Documentation
- [Linux PID](http://www.linfo.org/pid.html)
- [Linux process](https://www.thegeekstuff.com/2012/03/linux-processes-environment/)
- [Linux signal](https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/)

- [Special variables](https://www.tutorialspoint.com/unix/unix-special-variables.htm)
- PS COMMAND:
	- [ps Command, show all running porcesses](https://www.cyberciti.biz/faq/show-all-running-processes-in-linux/)
	- [mORE RUNNING](https://linuxize.com/post/ps-command-in-linux/)
	- [Flasg](https://phoenixnap.com/kb/list-processes-linux)
- psgrep command
	- [How to use it?](https://linuxize.com/post/pgrep-command-in-linux/)
	- [obtain PID with name_process](4-to_infinity_and_beyond)

- About time in linux:
	- [sleep](https://www.cyberciti.biz/faq/what-does-the-sleep-command-do-in-linux/)
	- [date and time](https://www.cyberciti.biz/faq/howto-set-date-time-from-linux-command-prompt/)

- Pkill Command:
	- [Use](https://www.howtoforge.com/linux-pkill-command/)

- SIGNALS:
	- [signals with kill on terminal](https://www.linuxjournal.com/content/bash-trap-command)
	- [Use trap command](https://www.youtube.com/watch?v=0btsvoSt76M&ab_channel=theurbanpenguin)
	- [video](https://www.youtube.com/watch?v=tF0Qau7zcsw&ab_channel=ProgrammingKnowledge)

- [/etc/init.d dict](https://www.ghacks.net/2009/04/04/get-to-know-linux-the-etcinitd-directory/)
- [& and &&](https://bashitout.com/2013/05/18/Ampersands-on-the-command-line.html)
- [Daemon](https://es.wikipedia.org/wiki/Daemon_(inform%C3%A1tica))
- []
# 0x05. Processes and signals

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
    <a href="http://www.linfo.org/pid.html" target="_blank" title="Linux PID">
     Linux PID
    </a>
   </li>
   <li>
    <a href="https://www.thegeekstuff.com/2012/03/linux-processes-environment/" target="_blank" title="Linux process">
     Linux process
    </a>
   </li>
   <li>
    <a href="https://www.thegeekstuff.com/2012/03/linux-signals-fundamentals/" target="_blank" title="Linux signal">
     Linux signal
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
     ps
    </code>
   </li>
   <li>
    <code>
     pgrep
    </code>
   </li>
   <li>
    <code>
     pkill
    </code>
   </li>
   <li>
    <code>
     kill
    </code>
   </li>
   <li>
    <code>
     exit
    </code>
   </li>
   <li>
    <code>
     trap
    </code>
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
   General
  </h3>
  <ul>
   <li>
    What is a PID
   </li>
   <li>
    What is a process
   </li>
   <li>
    How to find a process’ PID
   </li>
   <li>
    How to kill a process
   </li>
   <li>
    What is a signal
   </li>
   <li>
    What are the 2 signals that cannot be ignored
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
    All your files will be interpreted on Ubuntu 20.04 LTS
   </li>
   <li>
    All your files should end with a new line
   </li>
   <li>
    A
    <code>
     README.md
    </code>
    file, at the root of the folder of the project, is mandatory
   </li>
   <li>
    All your Bash script files must be executable
   </li>
   <li>
    Your Bash script must pass
    <code>
     Shellcheck
    </code>
    (version
    <code>
     0.7.0
    </code>
    via
    <code>
     apt-get
    </code>
    ) without any error
   </li>
   <li>
    The first line of all your Bash scripts should be exactly
    <code>
     #!/usr/bin/env bash
    </code>
   </li>
   <li>
    The second line of all your Bash scripts should be a comment explaining what is the script doing
   </li>
  </ul>
  <h2>
   More Info
  </h2>
  <p>
   For those who want to know more and learn about all signals, check out
   <a href="https://www.computerhope.com/unix/signals.htm" target="_blank" title="this article">
    this article
   </a>
   .
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/255)
</html>