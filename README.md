# titanic-data-analysis
Analysis of the survival of the Titanic passagers with plot graphs.

Plot graphs were generated as of the results of an analysis on the survival rates by age group, by sex, and by class.

## Hypothesis
The priority for lifeboats embarkation were probably as follows. Woman and children first! Then the riches. Forget about third class and old people.

### Survival rates by age group will display :

```
           total_survived  total_count survival_percentage
age_group
0-18                   70          139                 50%
19-30                  96          270                 36%
31-45                  86          202                 43%
46-55                  26           63                 41%
56-65                  11           32                 34%
66+                     1            8                 12%
```

### Survival rates by sex will display :

```
        total_survived  total_count survival_percentage
Sex
female             233          314                 74%
male               109          577                 19%
```

### Survival rates by class

```
        total_survived  total_count survival_percentage
Pclass
1                  136          216                 63%
2                   87          184                 47%
3                  119          491                 24%
```

### Conclusion
The analysis reveals that female passengers experienced substantially higher survival rates (74%) compared to males (19%). Among age groups, children (0-18 years) demonstrated the highest survival percentage at 50%. Furthermore, first-class passengers exhibited significantly greater survival rates (63%) compared to second-class (47%) and third-class passengers (24%).

## Data Source
https://www.agentsfordata.com/csv/sample

## Dependencies
- pandas
- numpy
- matplotlib

## Plots
![survivors by age group](img/survivors_by_age_group.png)

![survivors by sex](img/survivors_by_sex.png)

![percentage of survivors by class](img/percentage_of_survivors_by_class.png)