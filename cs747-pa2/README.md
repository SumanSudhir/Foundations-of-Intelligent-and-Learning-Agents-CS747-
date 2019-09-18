<center>
<h2>
CS 747: Programming Assignment 2
</h2>
</center>

<p>In this assignment, you will implement algorithms for finding an
optimal policy for a given MDP. The first part of the assignment is to
apply Linear Programming, based on the formulation presented in class.
The second part of the assignment is to implement Howard's Policy
Iteration. The third part of the assignment requires you to construct
MDPs whose optimal policies satisfy a specified condition; you will
use your solvers to validate your construction.</p>


<h3>Data</h3>

<p>This <a href="https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2019/pa-2/data.tar.gz">directory</a> provides a few samples
of input and output that you can use to test your code. The directory
contains four MDPs encoded as text files, with each file in the
following format.</p>

<pre><code>Number of states
Number of actions
Reward function
Transition function
Discount factor
Type
</code></pre>

<p>In these files, and also in the MDPs on which your algorithms will
be tested, the number of states S will be an integer greater than 0
and less than 150. Assume that the states are numbered 0, 1, 2,
�, (S - 1). Similarly, actions will be numbered 0, 1, 2,
�, (A - 1), where A is less than 100. The reward function will
be provided over S�A lines, each line containing S entries. Each
entry corresponds to R(s, a, s'), wherein state s, action a, and state
s' are being iterated in sequence from 0 to (S - 1), 0 to (A - 1), and
0 to (S - 1), respectively. A similar scheme is adopted for the
transition function T. Each reward lies between -1 and 1 (both
included). The discount factor is a real number in [0, 1]. However,
the discount factor will only be set to 1 if the underlying task is
episodic. The last field in the file, denoted Type, will either be
"continuing" or "episodic". If episodic, it is our convention that the
very last state (numbered S - 1) will be a terminal state. The MDP
will be such that for every starting state and policy, trajectories
will eventually reach the terminal state.</p>


<p>Below is a snippet of python code that is used to generate MDP files.</p>

<pre><code>print S
print A

for s in range(0, S):
    for a in range(0, A):
        for sPrime in range(0, S):
            print str(R[s][a][sPrime]) + "\t",

        print "\n",

for s in range(0, S):
    for a in range(0, A):
        for sPrime in range(0, S):
            print str(T[s][a][sPrime]) + "\t",

        print "\n",

print gamma
print type
</code></pre>


<h3>Solution</h3>

<p>Given an MDP, your program must compute the optimal value
function V* and an optimal policy &#960;* by applying the algorithm that
is specified through the command line. Create a shell script
called <code>planner.sh</code> to invoke your program. The arguments
to <code>planner.sh</code> will be</p>

<ul>
<li><code>--mdp</code> followed by a full path to the input MDP file, and</li>
<li><code>--algorithm</code> followed by one of <code>lp</code> and <code>hpi</code>.</li>
</ul>

<p>Make no assumptions about the location of the MDP file relative to
the current working directory; read it in from the full path that will
be provided. The algorithms specified above correspond to Linear
Programming and Howard's Policy Iteration, respectively. Here are a few examples of
how your planner might be invoked (it will always be invoked from its
own directory).</p>

<ul>
<li><code>./planner.sh --mdp /home/user/temp/data/mdp-7.txt --algorithm lp</code></li>
<li><code>./planner.sh --mdp /home/user/mdpfiles/mdp-5.txt --algorithm hpi</code></li>
</ul>

<p>You are free to implement the planner in any programming language
of your choice. You are not expected to code up a solver for LP;
rather, you can use available solvers as blackboxes (more below). Your
effort will be in providing the LP solver the appropriate input based
on the MDP, and interpreting its output appropriately. You are
expected to write your own code for Howard's Policy Iteration; you may
not use any custom-built libraries that might be available for the
purpose. You can use libraries for solving linear equations in the
policy evaluation step, but must write your own code for policy
improvement. Recall that Howard's Policy Iteration switches <b>all</b>
improvable states to some improving action; if there are two or more
improving actions at a state, you are free to pick any one.</p>


<h3>Output Format</h3>

<p>The output of your planner must be in the following format,
and <strong>written to standard output</strong>.</p>

<pre><code>V*(0)   &#960;*(0)
V*(1)   &#960;*(1)
.
.
.
V*(S - 1)   &#960;*(S - 1)
</code></pre>

<p>In the <code>data</code> directory provided, you will find four
output files corresponding to the MDP files, which have solutions in
the format above.</p>

<p>Since your output will be checked automatically, make sure you have
nothing printed to stdout other than the S lines as above in
sequence. If the testing code is unable to parse your output, you will
not receive any marks.</p>

<blockquote>
  <p><strong>Note:</strong></p>

  <ol>
  <li>Your output has to be written to the standard output, not to any file.</li>
  <li>For values, print at least 6 places after the decimal point. Print more if you'd like, but 6 (<code>xxx.123456</code>) will suffice.</li>
  <li>If your code produces output that resembles the solution files: that is, S lines of the form

<pre><code>value + "\t" + action + "\n"
</code></pre>

  or even

<pre><code>value + " " + action + "\n"
</code></pre>

  <p>you should be okay. Make sure you don't print anything else.</p></li>
  <li>If there are multiple optimal policies, feel free to print any one of them.</li>
  </ol>
</blockquote>

<h3>Effect of Discount Factor on Optimal Policies</h3>

<p>
  This part of the assignment requires you to design a family of MDPs
  that satisfy a specified property. While coming up with your answer,
  you can use your own solver to quickly check if you are on the right
  track.</p>

<p> What you need to construct is a family of MDPs that only differ in
  their discount factor: that is, they will all have the same set of
  states, set of actions, transition function, reward function, and type. The
  family must be such that all MDP instances with a discount factor in
  [0.01, 0.39]) must have the same (and unique) optimal policy
  &#960;<sub>1</sub>; all MDP instances with a discount factor in [0.41,
  0.74] must have the same (and unique) optimal policy &#960;<sub>2</sub>;
  all MDP instances with a discount factor in [0.76, 0.99]) must have the
  same (and unique) optimal policy &#960;<sub>3</sub>; such that
  &#960;<sub>1</sub> &#8800; &#960;<sub>2</sub>; &#8800; &#960;<sub>3</sub>; &#8800;
  &#960;<sub>1</sub>. The MDPs must all be continuing, and have
  exactly 2 actions. They may have at most 10 states.</p>

<p>Once you have worked out your family, encode it in the same format
  of the MDPs you have been provided. You only need to provide a
  single instance, with a discount factor of 0.5; call the
  instance <code>mdp-family.txt</code>. We will create multiple MDP
  instances that only differ in the discount factor, and run our own
  code to compute their optimal policies.</p>


<h3>Submission</h3>

Place these items in a directory named <code>submission</code>.

<ul class="plain">
<li>
  <code>planner.sh</code> and all the code that it needs to run.
</li>
<li>
<code>mdp-family.txt</code>.
</li>
<li>
<code>notes.txt</code> (You can describe your code and MDP construction if you would like us to see, but this item is optional.).
</li>
<li>
<code>references.txt</code> (See the section on Academic Honesty on the course web page.).
</li>
</ul>

<p>Compress the directory into <code>submission.tar.gz</code> and upload
on Moodle under Programming Assignment 2.</p>


<h3>Evaluation</h3>


<p>Your planner will be tested on a large number of MDPs. Your task is
to ensure that it prints out the correct solution (V* and &#960;*) in
each case, using each of the algorithms you have been asked to
implement. 4 marks each are allotted for the correctness of your
Linear Programming and Howard's Policy Iteration algorithms. 2 marks
are allotted for the correctness of the MDP family you construct. We
shall verify correctness by computing and comparing optimal policies
for a large number of MDPs from the family (obtained by varying the
discount factor in <code>mdp-family.txt</code>).</p>

<p>The TAs and instructor may look at your source code to corroborate
the results obtained by your program, and may also call you to a
face-to-face session to explain your code.</p>


<h3>Deadline and Rules</h3>

<p>Your submission is due by 11.55 p.m., Sunday, September 15. Finish
  working on your submission well in advance, keeping enough time to
  test your code and upload to Moodle.</p>

<p>Your submission will not be evaluated (and will be given a score of
  zero) if it is not uploaded to Moodle by the deadline. Do not send
  your code to the instructor or TAs through any other
  channel. Requests to evaluate late submissions will not be
  entertained.</p>

<p>Your submission will receive a score of zero if your code does not
execute on the sl2 machines. To make sure you have uploaded the right
version, download it and check after submitting (but before the
deadline, so you can handle any contingencies before the deadline
lapses). If your code needs any special libraries to run on the sl2
machines, it is <b>your</b> responsibility to get them installed. You
can do so
by <a href="https://bugs.cse.iitb.ac.in/bugs/enter_bug.cgi">filing a
bug</a> with the CSE system administrators.</p>

<p>You are expected to comply with the rules laid out in the "Academic
Honesty" section on the course web page, failing which you are liable
to be reported for academic malpractice.</p>



<h3>References for Linear Programming</h3>

<p>Although you are free to use any library of your choice for LP, we
recommend that you use the Python
library <code>PuLP</code> (<a href="https://pythonhosted.org/PuLP/">https://pythonhosted.org/PuLP/</a>)
or the <code>lp_solve</code> program
(<a href="http://lpsolve.sourceforge.net/5.5/">http://lpsolve.sourceforge.net/5.5/</a>). Both
of these are already installed on the <code>sl2</code> machines.</p>


<p><code>PuLP</code> is convenient to use directly from Python code:
here is a <a href="https://www.youtube.com/watch?v=7yZ5xxdkTb8">short
tutorial</a> and here is
a <a href="https://www.coin-or.org/PuLP/index.html">reference</a>.</p>

<p><code>lp_solve</code> can be used both through an API and through
the command line. Here is
a <a href="http://lpsolve.sourceforge.net/5.5/">reference</a> and here
is
an <a href="http://lpsolve.sourceforge.net/5.5/formulate.htm">introductory
example</a>.</p>
</body></html>

