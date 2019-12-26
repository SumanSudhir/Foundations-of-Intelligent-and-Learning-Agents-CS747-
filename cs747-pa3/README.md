</head>

<body data-gr-c-s-loaded="true">

<center>
<h2>
CS 747: Programming Assignment 3
</h2>
</center>

<p>In this assignment, you will implement an algorithm for estimating
  the value function of a policy for a given MDP from a trajectory of
  the form state, action, reward, state, action, reward, ….</p>

<br>
<h3>Data Format</h3> 


<p>The input to your "evaluator" will be a text file that provides
information in the following format.</p>

<pre><code>Number of states
Number of actions
Discount factor
state1 action1 reward1
state2 action2 reward2
state3 action3 reward3
.
.
.
stateN actionN rewardN
stateN+1
</code></pre>

<p>The number of states <code>S</code> and the number of
actions <code>A</code> will be integers greater than 0. Assume that the
states are numbered 0, 1, ..., <code>S</code> - 1, and the actions
numbered 0, 1, ..., <code>A</code> - 1. The discount factor will lie
between 0 (included) and 1 (excluded). The trajectory over time will
be long enough, and the dynamics of the underlying MDP such, that
there is at least one outgoing transition from each state in the
MDP. Note that the MDP is <i>not</i> episodic: that is, stateN+1 is not a
terminal state (and can occur within the trajectory multiple
times). The trajectory is merely a finite sequence generated according
to the underlying transition and reward functions, and terminated at
some arbitrary time step.</p>

<p>You can assume that <code>S</code> and <code>A</code> will not
exceed 50, and N, the total number of transitions in the trajectory,
will not exceed 500,000. In this <a href="https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2019/pa-3/data.tar.gz">data</a>
directory, you will find two sample data files (<code>d1.txt</code>
and <code>d2.txt</code>).</p>

<br>
<h3>Output</h3> 

<p>Given a data file, your evaluator must estimate the value
function <code>V</code> under the policy being followed. The output,
written to standard output, must be in the following format
(<code>Est-V</code> is your estimate of <code>V</code>).</p>

<pre><code>Est-V(0)
Est-V(1)
.
.
.
Est-V(S - 1)
</code></pre>

<p>In the data directory enclosed, you will find output files
corresponding to the two data files, which have solutions in the
format above. The values mentioned in these output files are indeed
the <i>true</i> values (under the same policy) from the MDP being
sampled. Naturally, as you will have to estimate values based on
samples alone, your estimates cannot be expected to match the true
values perfectly.</p>

<p>Notice that since this is a prediction problem, wherein a fixed
policy is being followed, the actual names of the actions
taken do not matter. Nor does it matter if the policy being followed
  is deterministic or stochastic. Your logic only needs to consider 
  the state, reward, and next state associated with each transition.</p>

<p>You are free to implement the evaluator in any programming language
of your choice. Since your output will be checked automatically, make
sure you have nothing printed to stdout other than the <code>S</code>
lines as above in sequence. If the testing code is unable to parse
your output, you will not receive any marks.</p>

<br>
<h3>Submission</h3> 

Create a directory called <code>submission</code>. The directory must
contain a script titled <code>evaluator.sh</code>, which must take in
exactly one command line argument corresponding to a data file. For
testing your code, the following command will be used from
your <code>submission</code> directory.<p></p>

<code>./evaluator.sh dataFileName</code>

<p>wherein <code>dataFileName</code> will include the full path.
  
</p><p>Include a file called <code>notes.txt</code> in the
<code>submission</code> directory, that describes the algorithm your
evaluator implements.


In summary: you will place the following files in <code>submission</code>.

</p><ul class="plain">
<li>
  <code>evaluator.sh</code> and all the code that it needs to run.
</li>
<li>
<code>notes.txt</code>
</li>
<li>
<code>references.txt</code> (see the section on Academic Honesty on the course web page)
</li>
</ul>

<p>Compress the directory into <code>submission.tar.gz</code> and upload
on Moodle under Programming Assignment 3.</p>


<br>
<h3>Evaluation</h3> 

<p>Your evaluator will be tested on trajectories generated from
different MDPs and policies. Your task is to ensure that it prints out
a good estimate of the true value function in each case. Performance
will be quantified based on the (unweighted) squared distance between
your estimate <code>Est-V</code> and the true value
function <code>V</code>: that is,</p>

<code>Error = &#8721;<sub>s&#8946;S</sub> (V(s) - Est-V(s))<sup>2</sup></code>.

<p>Recall that as a part of Programming Assignment 2, you had written
code for MDP planning. It will be a good idea for you to build a
testing framework using that code to (1) generate and record
trajectories of some fixed policy &#960; for some MDP M; (2) estimate
the value function of &#960; as required in this assignment; and (3) compare
your estimate with the true value function, which you can compute
using your own code from Programming Assignment 2. This is exactly
the scheme that we will use for evaluating your answers.</p>

<p>8 marks are reserved for the performance of your evaluator on
unseen trajectories, and 2 marks for your explanations
in <code>notes.txt</code>. Be sure to describe your approach and
explain why you chose it over alternative approaches.</p>

<p>The TAs and instructor may look at your source code and notes to
corroborate the results obtained by your program, and may also call
you to a face-to-face session to explain your code.</p>


<br>





