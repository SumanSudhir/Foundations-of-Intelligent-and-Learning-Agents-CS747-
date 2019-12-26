</head>

<body data-gr-c-s-loaded="true">

<center>
<h2>
CS 747: Programming Assignment 4
</h2>
</center>

<p>This assignment is meant to give you the experience of developing
both agent and environment. Consequently it is more open-ended than
your previous assignments. As a part of this assignment, you will
implement the <i>Windy Gridworld</i> task given as Example 6.5 by Sutton and
Barto (2018). You will program some agent-environment interactions,
record your results, and present you interpretations. You can use any
programming language of your choice for this assignment.</p>

<br>
<h3>Tasks</h3> 

<ol>
<li>Implement Windy Gridworld as an episodic MDP. The core of your
code will have to be a function (or functions) to obtain next state
and reward for a given state and action. You can use your own function
names and conventions.</li>

<li>Implement a Sarsa(0) agent as described in the example, and obtain
a baseline plot similar to the one accompanying the example (episodes
against time steps). You can set learning and exploration rates as you
see fit (just be sure to describe them in your report).</li>

<li>Get another plot when King's moves are permitted (that is, 8
actions in total), as described in Exercise 6.9.</li>

<li>Add stochasticity to the task as described in Exercise 6.10, and
again plot the resulting performance of the Sarsa agent. Make sure you
note down your convention for modeling corner cases.</li>

</ol>

<p>In all your experiments, generate at least ten independent runs by
varying the random seed. Plot the average statistic in the graphs.</p><p>

<br>
    
</p><h3>Submission</h3> 

Create a directory called <code>submission</code> and place the
following material in it.

<ol>
  <li> Your code for implementing the task and its variants;</li>
  <li> Code for your Sarsa agent;</li>
  <li> A script to run your simulations and gather data;</li>
  <li> Plots of your agent's performance;</li>
  <li> A README file describing how to run your code and obtain the plots; and</li>
  <li> A report presenting your observations from these experiments
  (as a pdf file named <code>report.pdf</code>). Place the plots in
  the report and provide accompanying commentary, rather than keeping
  the plots and text separate.</li>
</ol>
<p></p>

<p>Compress the directory into <code>submission.tar.gz</code> and upload
on Moodle under Programming Assignment 4.</p>

<p>Convince yourself that the results obtained match your
expectations. Feel free to be creative and use the simulation
environment to test related hypotheses you might find
interesting. Your observations (under 6) must explain the variations
observed across the three task settings, and report any particular
issues you encountered while experimenting with this task. Don't
hesitate to include additional numbers or graphs.</p>

<br>
<h3>Evaluation</h3> 

<p>Your marks will be divided roughly equally among the three tasks
you have to implement, in each case determined by the plot and the
accompanying observations.</p>

<p>The TAs and instructor may look at your source code and notes to
corroborate the results obtained by your program, and may also call
you to a face-to-face session to explain your code.</p>


<br>




</body><span class="gr__tooltip"><span class="gr__tooltip-content"></span><i class="gr__tooltip-logo"></i><span class="gr__triangle"></span></span></html>
