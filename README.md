
#Pokémon Go Base Stats

There are three base stats in Pokémon Go: Attack, Defense and Stamina.

Base stats are calculated using Generation VI stats, with the following formulas




#EVs (Effort Values)

There is no recorded data to support the existance of Effort Values in Pokémon Go.

#IVs (Initial Values)

IVs function like a Pokémon's "Genes", every stat has an IV ranging from 0 to 15 for each stat.

These stats are provided randomly for every Pokémon, caught or hatched, and although as insignificant as 15 points may seem, they are required for Ace Trainers to obtain when searching Pokémon with perfect stats. On some occasions they are even the tipping point in a close matchup.

#Pokémon Go Stats IV Modification

Without IV's every Pokémon of the same species would have the same HP and CP when at the maximum level.




CP Multiplier - CP Multiplier is a fixed valued, based on Pokémon level.

Pokémon Level - Pokémon Level can be assumed within ~2.5 levels based on the current "Power Up" dust cost.

IV Calculations

Knowing the CP formula (More on this in the next section), and using the guess and check method we can calculate the possible IV combinations for any given Pokémon.


Lets break that down a little more...


Knowing that CP, Base Stamina, Base Attack, Base Defense and CP Multiplier are static values (Where CP Multiplier has 2 possible values based on Pokémon level). We can guess and check for IVs in the range of 0-15, to find all possible combinations that match the Pokémon's CP.

#CP Calculations

Now that we have possible IV's, we can take the sets with the highest and lowest average to assume the best and worst possible sets. After plugging those IV sets back in to the broken down CP formula, we can scale the CP Multiplier to calculate the CP range for a paritcular Pokémon at any given level. We can also use a set of 15 Stamina, 15 Attack, 15 Defense to assume the best possible CP and 0 Stamina, 0 Attack, 0 Defense to assume the worst possible CP.


#HP Calculations

After all the information we have gathered above we can easily calculate the possible HP ranges using the following formula

