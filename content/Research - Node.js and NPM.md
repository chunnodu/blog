Title: Research: Node.js and NPM
Date: 2021-01-22
Category: Research
Tags: Research


I joined the Estes Park working group late last year to get more hands on with Knowledge Graphs and Semantic web technology and jumped in on a research project. The premise was, knowing the RDF stack solves for enterprise knowledge graphs, are there more mainstream non-RDF alternatives which support W3C Semantic Web standards and are equally viable?

One of the technologies I looked at this month with this goal in mind was Node.js/NPM. My biggest takeaway, surprisingly unrelated to the specific technology or questions I needed to answer was that when doing research, having a network of experts to talk to first can be more useful for focusing your efforts than jumping right into the haystack. By getting on the phone with a young developer associate in Nigeria, and eventually the [DLVR Logistics](www.dlvr.ng) CTO who's an expert developer working out of Germany I was able to piece together all I needed to move forward.

Here's the summary of my deep dive into Node.js/NPM - a major question's unanswered, but progress still.

#### Why should we care?
It's a way of programming with Javascript(JS), bringing in-browser functionality to the operating system. The developer took Google's Javascript engine that runs the chrome browser and placed it inside a C++ container, turning it into a server side language. JS was originally written as a front end language and is fast and dynamic not statically typed, meaning you don't need to declare the structure as javascript infers it, as opposed to say C++ where you define integer or float or string and at compilation it checks if it actually is what you declared. Also, JS was built around the concept of events, and this encourages speed as events can happen in parallel.

#### What problems does the tech stack solve?
- Allows for non blocking read/write, basically doesn't need to wait for functions to be completed before running others
- Uses JSON objects so eliminates need for data conversion, & bottleneck which can be caused by databases for concurrent applications

#### How does the tech work to solve problems we care about?
- Based on the open web stack, runs over standard port 80 and you can run javascript natively on your OS/local machine
- Supports real time, 2 way connections & allows for free data exchange between client and server as both can initiate communication
- Single threaded so doesn't max out RAM, supports 10's of thousands of concurrent connections
- Node.js is the runtime, express is a node.js framework use dfor server functionality. Modern web applications stacks are typically MEAN: mongodb, express, angular, node.js or MERN: mongodb, express, react, node.js

#### What are the advantages of using the tech?
- Great for platform as a service, real time applications e.g chat
wide adoption, so lots of packages have been developed, and support is more widely available. Node JS has a built in package manager (NPM) to manage dependencies and show status,how many modules are installed etc.
- Compact APIs, file size is small
- Lots of users like to program in javascript so there's interest in building stuff from the developer community
#### What are the downsides?
- Not so good for batch jobs where serial tasks are being completed and task completion time doesn't matter i.e end of day. 
- Node.js has an in-built web server, not as efficient as apache for heavy CPU intensive operations

#### What alternatives are worth comparing and contrasting with the tech in question?
- Comparable with python, php and other server side languages like Golang.

#### How would we rank each in terms of viability (10 most viable)
Still unanswered