# Statistics-Project-Mann-Whitney-U-Test-Python

This is statistics class project. 

It analyzes whether physical activity and general well-being are linked, using survey data from 60 Gdańsk residents of various ages. I'm using the Mann-Whitney U test to compare: whether exercise has no effect on well-being (H0​) or if it actually makes a difference (H1​). Essentially, I want to see if being active leads to feeling better.

Detailed information regarding the Mann-Whitney U test can be found [here](https://www.statology.org/mann-whitney-u-test/).

The data for this project has been shortened for sharing, but it still represents the original results.

The attached file contains the following columns:
| Original Header (PL) | English Translation |
| :--- | :--- |
| Aktywność fizyczna (ćwiczenia, treningi, spacery co najmniej 20 minut, itp.) | Physical activity (exercises, workouts, walks of at least 20 min, etc.) |
| Ile godzin dziennie spędzasz siedząc (praca, dom, dojazdy)? | How many hours a day do you spend sitting (work, home, commuting)? |
| Ile godzin dziennie spędzasz przy komputerze/telefonie (poza pracą)? | How many hours a day do you spend on a computer/phone (outside of work)? |
| Czy znasz i wykonujesz ćwiczenia profilaktyczne na kręgosłup (np. plank, most, mobilizacje)? | Do you know and perform preventive spine exercises (e.g., plank, bridge, mobility)? |
| Oceń stan swojego kręgosłupa (1–10). | Rate the condition of your spine (1–10). |
| Czy dbasz profilaktycznie o kręgosłup (np. ćwiczenia, ergonomia pracy, przerwy)? | Do you take preventive care of your spine (e.g., exercises, ergonomics, breaks)? |
| Czy ból pleców wpływa na Twój nastrój/stres? | Does back pain affect your mood or stress levels? |
| Czy zdarza Ci się odczuwać drętwienie/mrowienie palców rąk? | Do you experience numbness or tingling in your fingers? |
| Czy wziąłeś/łaś L4 z powodu bólu pleców? | Have you taken sick leave due to back pain? |
| Czy ból pleców uniemożliwił Ci udział w wydarzeniu towarzyskim? | Has back pain prevented you from attending a social event? |
| Czy ból pleców utrudnia Ci sen? | Does back pain interfere with your sleep? |
| Czy ból pleców ogranicza Twoją aktywność zawodową? | Does back pain limit your professional activity? |

In the first approach, I decided to consider the columns **"Physical activity"** (binary) and **"Does back pain affect your mood/stress levels?"** (ordinal).

Since the initial assumptions did not allow me to reject the H0, I decided to perform a more in-depth analysis. In second approach, I examined the simultaneous impact of **multiple ordinal features**.

The binary feature was once again derived from the **"Physical activity"** column. In this approach, I considered the following set of variables:
* Does back pain affect your mood/stress?
* Have you taken sick leave due to back pain?
* Has back pain prevented you from participating in a social event?
* Does back pain interfere with your sleep?
* Does back pain limit your professional activity?
