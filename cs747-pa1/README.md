<center>
<h2>
CS 747: Programming Assignment 1
</h2>
</center>

<p>In this assignment, you will implement and compare different
algorithms for sampling the arms of a stochastic multi-armed
bandit. Each arm provides i.i.d. rewards from a Bernoulli distribution
with mean in (0, 1). The objective is to minimise regret. The
algorithms you will implement are round-robin sampling, epsilon-greedy
exploration, UCB, KL-UCB, and Thompson Sampling. This is a relatively
straightforward assignment, which essentially puts to practice the
algorithms we have discussed in class.</p>

  <br>
<h3>Data and Scripts</h3>

<p><a href="https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2019/pa-1/cs747-pa1.tar.gz">This directory</a> has (1) a
subdirectory called <code>instances</code> containing three bandit
instances, (2) a <code>submission</code> subdirectory in which you
will place all your submission-related material. (3) a
script <code>check.sh</code> inside <code>submission</code> for
verifying the input-output behaviour of your program, and (4) a
file <code>outputFormat.txt</code> to illustrate the format of output
your code is expected to generate.</p>

<p>Bandit instances are encoded as text files with the mean rewards of
the arms provided one to a line. Hence the number of lines gives the
number of arms. The instances provided have 2, 5, and 25 arms.</p>

<p>The program you create will have to take in a number of command
line arguments. By running the checking script provided, you can make
sure that your program consumes the input parameters correctly and
produces the desired output. </p>

<p>You will have to perform multiple random executions of different
algorithms on the given instances, and place all your data in a text
file. The example provided shows you the expected format.</p>

<p><b>All</b> your submission materials should go into
the <code>submission</code> folder, which you will compress and
submit.</p>

<br>
<h3>Task</h3>

You have to write code, generate data by running the code, and compile
graphs and a report based on the data.

<h4>Code</h4>

<p>You will have to prepare a script called <code>bandit.sh</code>
that performs the following functions. You may use any programming
language of your choice internally to code up these functionalities;
you can also decide for yourself how to modularise the code and name
the internal functions. What we shall insist upon is the input-output
behaviour of <code>bandit.sh</code>, which we describe below.</p>

<code>bandit.sh</code> must accept the following command line parameters.

<ul class="plain">

<li>
<code>--instance in</code>, where <code>in</code> is a path to the instance file.
</li>

  <li>
<code>--algorithm al</code>, where <code>al</code> is one of <code>round-robin</code>, <code>epsilon-greedy</code>, <code>ucb</code>, <code>kl-ucb</code>, and <code>thompson-sampling</code>.
  </li>

  <li>
<code>--randomSeed rs</code>, where <code>rs</code> is a non-negative integer.
  </li>

  <li>
<code>--epsilon ep</code>, where <code>ep</code> is a number in [0, 1].
  </li>

  <li>
<code>--horizon hz</code>, where <code>hz</code> is a non-negative integer.
  </li>

</ul>

(Once you have finished coding bandit.sh, run <code>check.sh</code> to
make sure that you correctly read in all the command line
parameters. While testing your code, we will use a different version
of <code>check.sh</code>�with different parameters�and call
it inside your <code>submission</code> directory.)

<p>Your first task is to simulate a multi-armed bandit. You must read in
the bandit instance and have a function to generate a random 0-1
reward with the corresponding probability when a particular arm is
pulled. A single random seed will be passed to your program; you must
seed the random number generator in your simulation with this
seed. If any of your algorithms are randomised, they must also use
the same seed for initialisation.</p>

<p><b>Given a seed</b> and keeping other input parameters fixed, your
entire experiment must be <b>deterministic</b>: it should execute the
same way and produce the same result. Of course the execution will be
different for different random seeds; the point being made is that of
repeatability for a given seed. You should be able to implement this
property by initialising all the random number generators in your
program based on the seed provided as an input: you should not leave
them unseeded or use strategies such as seeding based on system
time. Make sure you understand this requirement; if the behaviour of
your code does not get fixed by the input random seed (keeping other
input parameters fixed), you will lose 6 marks.</p>

<p>Having set up the code to pull arms and generate rewards, you must
implement the following sampling algorithms: (1) round-robin, (2)
epsilon-greedy, (3) UCB, (4) KL-UCB, and (5) Thompson Sampling. You
are free to make assumptions on unspecified aspects such as how the
first few pulls get made, how ties get broken, how any
algorithm-specific parameters are set, and so on. But you must list
all such assumptions in your report. The only external parameter to
the given set of algorithms is epsilon for epsilon-greedy sampling,
which will be passed from the command line. Recall that on every
round, an algorithm can only use the sequence of pulls and rewards up
to that round (or statistics derived from the sequence) to decide
which arm to pull. Specifically, it is illegal for an algorithm to
have access to the bandit instance itself
(although <code>bandit.sh</code> has such access).</p>

<p>Passed an instance, a random seed, an algorithm, epsilon, and a
horizon, your code must run the algorithm on the instance for "horizon"
number of pulls and note down the cumulative reward REW. Subtracting
REW from the maximum expected cumulative reward possible (the product
of the maximum mean and the horizon) will give you REG, the cumulative
regret for the particular run. Note that this number can be negative
(and might especially turn up so on small horizons�why?).  When the
algorithm terminates, <code>bandit.sh</code> should output
a <b>single</b> line with six entries, separated by commas and
terminated with a newline ('\n') character. The line must be in this
format; <code>outputFormat.txt</code> contains a few such lines (in which
REG is set to arbitrary values just for the purpose of
illustration).</p>

<ul class="plain">
<li>
instance, algorithm, random seed, epsilon, horizon, REG
</li>
</ul>

<p>We will run your code on a subset of input parameters and validate
the output with an automatic script. You will lose 6 marks if your
code does not produce output in the format specified above.</p>

<p>Note that epsilon only needs to be used by <code>bandit.sh</code>
if the algorithm passed is <code>epsilon-greedy</code>; for other
algorithms it is a dummy parameter. Your output must still contain
epsilon (either the value passed to it or any other value) to retain
the six-column format.</p>

<h4>Output Data, Plots, Report</h4>

<p>Having written <code>bandit.sh</code>, run it for every combination of

</p><ul class="plain">
<li>
  <b>instance</b> from <code>"../instances/i-1.txt"</code>; <code>"../instances/i-2.txt"</code>; <code>"../instances/i-3.txt"</code>,
</li>
<li>
  <b>algorithm</b> from <code>round-robin</code>; <code>epsilon-greedy</code> with <code>epsilon</code> set to 0.002, 0.02, 0.2; <code>ucb</code>, <code>kl-ucb</code>, <code>thompson-sampling</code>,
</li>
<li>
  <b>horizon</b> from 50; 200; 800; 3200; 12800; 51200; 204800, and
</li>
<li>
  <b>random seed</b> from 0; 1; ...; 49.
</li>
</ul>

<p>It is best that you write your own wrapper script for generating
the output for all these input configurations. Place all the output
lines in a single file named <code>outputData.txt</code>.  Notice that
the file must have exactly 3 � 7 � 7 � 50 = 7350
lines. It will take you a considerable amount of time to generate data
(especially for longer horizons), and so do not leave this task to the
last minute. Since data for shorter horizons will anyway be generated
as a part of the longer-horizon experiments, you might be able to save
some time by recording intermediate regret values. However, your
submitted <code>bandit.sh</code> script must still only print a single
line corresponding to the horizon passed to it.</p>

<p>You will generate three plots: one for each instance. The plot will
have horizon on the x axis (use a log scale) and regret on y axis. It
will contain 7 lines: one for each algorithm (counting epsilon-greedy
as three algorithms). Each point will give the average regret from the
fifty random runs at the particular horizon for the algorithm. Make
sure you provide a clear key so the plot is easy to follow.</p>

<p>Include all three graphs in a file called <code>report.pdf</code>,
which should also state any assumptions in your implementation and
provide your interpretations of the results. Feel free to put down any
observations that struck you while working on this assignment. Do not
leave your graphs as separate files: they must be embedded
in <code>report.pdf</code>.</p>



<br>
<h3>Submission</h3>

Place these items in the <code>submission</code> directory.

<ul class="plain">
<li>
  <code>bandit.sh</code> and all the code that it needs to run.
</li>
<li>
<code>outputData.txt</code>
</li>
<li>
<code>report.pdf</code>
</li>
<li>
<code>references.txt</code> (see the section on Academic Honesty on the course web page)
</li>
</ul>

<p>Compress the directory into <code>submission.tar.gz</code> and upload
on Moodle under Programming Assignment 1.</p>


<br>
<h3>Evaluation</h3>

<p>We will evaluate you based on your report, and also run your code
to validate the results reported. If your code does not run on the sl2
machines or your report is absent/incomplete, you will not receive any
marks for this assignment.</p>

<p>1 mark each is reserved for the correctness of your implementation
of the round-robin, epsilon-greedy, and UCB algorithms, and 2 marks
each for KL-UCB and Thompson Sampling. Your presentation of the
results and accompanying observations in your report carry 3
marks.</p>

<p>The TAs and instructor may look at your source code and notes to
corroborate the results obtained by your agent, and may also call you
to a face-to-face session to explain your code.</p>


<br>

</body></html>

