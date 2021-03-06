# NETWORKING...

## Resources

- [OSI model](https://en.wikipedia.org/wiki/OSI_model)
- [Different types of network](https://www.lifewire.com/lans-wans-and-other-area-networks-817376)
    - ![LAN vs WAN]([http://url/to/img.png](https://www.lifewire.com/thmb/c6N45eilZvKzYSxMlFBrQdMuUU4=/650x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/lans-wans-and-other-area-networks-817376-6e07f1a4121a4e13ac43660ea41ef9b9.png))
  - [LAN network](https://en.wikipedia.org/wiki/Local_area_network)
    - Ethernet and wifi
  - [WAN network](https://en.wikipedia.org/wiki/Wide_area_network)
    - [Internet](https://en.wikipedia.org/wiki/Internet)
- [MAC address](https://whatismyipaddress.com/mac-address)
  - MAC filtering
- [What is an IP address](https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/)
  - [Private and public address](https://www.iplocation.net/public-vs-private-ip-address)
  - [IPv4 and IPv6](https://www.webopedia.com/insights/ipv6-ipv4-difference/)
- [Hostnames](https://en.wikipedia.org/wiki/Hostname)
  - [Localhost](https://en.wikipedia.org/wiki/Localhost)
- [TCP and UDP]()
- [TCP/UDP ports List](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers)
- [What is ping /ICMP](https://en.wikipedia.org/wiki/Ping_%28networking_utility%29)
- [Positional parameters](https://wiki.bash-hackers.org/scripting/posparams)



0. OSI model
OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.

It is organized from the lowest level to the highest level:

- The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal
- The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc
Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process. It is a conceptual framework so we can better understand complex interactions that are happening. Most of the functionality in the OSI model exists in all communications systems.

![OSI](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220223T215611Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=c8e5203244fd566a7e88977d69f2648cf34b7755f9a10cd78e1268dfc0e00815)

In this project we will mainly focus on:

The Transport layer and especially TCP/UDP
On the Network layer with IP and ICMP
The image bellow describes more concretely how you can relate to every level.

![Levels](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220223T215611Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=702a57bf133a4614c1fbf538c395644ce247d2b9c4395a8e96bbd7f38697d7fe)
Questions:

What is the OSI model?

Set of specifications that network hardware manufacturers must respect
The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology
How is the OSI model organized?

Alphabetically
From the lowest to the highest level
Randomly

### 1

LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.

Questions:

- What type of network a computer in local is connected to?

1. Internet
2. WAN
3. LAN

- What type of network could connect an office in one building to another office in a building a few streets away?

1. Internet
2. WAN
3. LAN

- What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

1. Internet
2. WAN
3. LAN

### 2

Questions:

- What is a MAC address?

1. The name of a network interface
2. The unique identifier of a network interface
3. A network interface
- What is an IP address?

1. Is to devices connected to a network what postal address is to houses
2. The unique identifier of a network interface
3. Is a number that network devices use to connect to networks

### 3
Let’s fill the empty parts in the drawing above.

Questions:

- Which statement is correct for the TCP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process
- Which statement is correct for the UDP box:
1. It is a protocol that is transferring data in a slow way but surely
2. It is a protocol that is transferring data in a fast way and might loss data along in the process
- Which statement is correct for the TCP worker:
1. Have you received boxes x, y, z?
2. May I increase the rate at which I am sending you boxes?
# 0x07. Networking basics #0

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
    <a href="https://en.wikipedia.org/wiki/OSI_model" target="_blank" title="OSI model">
     OSI model
    </a>
   </li>
   <li>
    <a href="https://www.lifewire.com/lans-wans-and-other-area-networks-817376" target="_blank" title="Different types of network">
     Different types of network
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Local_area_network" target="_blank" title="LAN network">
     LAN network
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Wide_area_network" target="_blank" title="WAN network">
     WAN network
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Internet" target="_blank" title="Internet">
     Internet
    </a>
   </li>
   <li>
    <a href="https://whatismyipaddress.com/mac-address" target="_blank" title="MAC address">
     MAC address
    </a>
   </li>
   <li>
    <a href="https://www.bleepingcomputer.com/tutorials/ip-addresses-explained/" target="_blank" title="What is an IP address">
     What is an IP address
    </a>
   </li>
   <li>
    <a href="https://www.iplocation.net/public-vs-private-ip-address" target="_blank" title="Private and public address">
     Private and public address
    </a>
   </li>
   <li>
    <a href="https://www.webopedia.com/insights/ipv6-ipv4-difference/" target="_blank" title="IPv4 and IPv6">
     IPv4 and IPv6
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Localhost" target="_blank" title="Localhost">
     Localhost
    </a>
   </li>
   <li>
    <a href="https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/" target="_blank" title="TCP and UDP">
     TCP and UDP
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers" target="_blank" title="TCP/UDP ports List">
     TCP/UDP ports List
    </a>
   </li>
   <li>
    <a href="https://en.wikipedia.org/wiki/Ping_%28networking_utility%29" target="_blank" title="What is ping /ICMP">
     What is ping /ICMP
    </a>
   </li>
   <li>
    <a href="https://wiki.bash-hackers.org/scripting/posparams" target="_blank" title="Positional parameters">
     Positional parameters
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
     netstat
    </code>
   </li>
   <li>
    <code>
     ping
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
   OSI Model
  </h3>
  <ul>
   <li>
    What it is
   </li>
   <li>
    How many layers it has
   </li>
   <li>
    How it is organized
   </li>
  </ul>
  <h3>
   What is a LAN
  </h3>
  <ul>
   <li>
    Typical usage
   </li>
   <li>
    Typical geographical size
   </li>
  </ul>
  <h3>
   What is a WAN
  </h3>
  <ul>
   <li>
    Typical usage
   </li>
   <li>
    Typical geographical size
   </li>
  </ul>
  <h3>
   What is the Internet
  </h3>
  <ul>
   <li>
    What is an IP address
   </li>
   <li>
    What are the 2 types of IP address
   </li>
   <li>
    What is
    <code>
     localhost
    </code>
   </li>
   <li>
    What is a subnet
   </li>
   <li>
    Why IPv6 was created
   </li>
  </ul>
  <h3>
   TCP/UDP
  </h3>
  <ul>
   <li>
    What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)
   </li>
   <li>
    What is the main difference between TCP and UDP
   </li>
   <li>
    What is a port
   </li>
   <li>
    Memorize SSH, HTTP and HTTPS port numbers
   </li>
   <li>
    What tool/protocol is often used to check if a device is connected to a network
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
    All your Bash script files will be interpreted on Ubuntu 20.04 LTS
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
     shellcheck
    </code>
    without any error
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
   The second line of all your Bash scripts should be a comment explaining what is the script doing
  </p>
  <p>
   For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:
  </p>
  <p>
   What is the most important position in a software company?
  </p>
  <ol>
   <li>
    Project manager
   </li>
   <li>
    Backend developer
   </li>
   <li>
    System administrator
   </li>
  </ol>
  <pre><code>sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$
</code></pre>
  <p>
   Source for question 1
   <a href="https://twitter.com/devopsreact/status/831922429215662080" target="_blank" title="here">
    here
   </a>
  </p>
 </div>
</div>

[--LINK PROJECT--](https://intranet.hbtn.io/projects/259)
</html>