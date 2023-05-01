# high level

## what is 3sat
- NP-complete problems are all equavalent to each other, in the sense that
  one can be converted to another in polinomial time. This means, if one NP
  complete problem can be solved in P(olinomial) time, all NP-complete
  problems can be solved in P time.
  
## 3sat input format
- Generally, an 3sat problem is formulated as
     F = (<clause-1>) AND (<clause-2>) AND ... AND (clause-m)
  where each clause is of the format
     Clause = <var-1-literal> OR <var-2-literal> OR <var-2-literal>
  a boolean var(iable) is written as x-i, that can be 0(False) or 1(True)


# solver18

## executable
- solver18.py is the runnable file.
  python3 solver18.py will generate solution

## 3sat input files
- ROOT = .../solver18
- ROOT/configs/cfg60-266.json
  this file has 60 variables and 266 clauses, named as C0001 .. C0266
 