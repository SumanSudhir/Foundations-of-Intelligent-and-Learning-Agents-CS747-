echo episodic
./planner.sh --mdp /home/sounak/data/episodic/testmdp.txt --algorithm lp > outputSol
python diffCheck.py outputSol /home/sounak/data/episodic/testsol.txt

echo continuing
./planner.sh --mdp /home/sounak/data/continuing/testmdp.txt --algorithm lp > outputSol
python diffCheck.py outputSol /home/sounak/data/continuing/testsol.txt
