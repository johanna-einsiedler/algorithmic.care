---
title: Study Protocol
---

<link href="https://fonts.googleapis.com/css2?family=Nanum+Gothic&display=swap" rel="stylesheet">
<style>
.row {
  display: flex;
}
.column {
  flex: 50%;
}
</style>

# Study Protocol
## Developing a way to consistenly collect data about our bodies

## Variables to be Collected
- Muscle Data [2x per day - one time in the morning after waking up, one time in the evening]
   - EMG measurements
   - MMG measurements
- Survey data [1x per day - in the evening]
- Step count [1x per day - in the evening]


## Muscle Data Measurement Protocol

We use a  [BITalino (r)evolution board](https://www.pluxbiosignals.com/collections/bitalino/products/bitalino-revolution-plugged-kit-ble-bt) with an EMG sensor, an MMG sensor and a button. See HERE for instructions on how to build your own.

For the protocol time tracking we found it helpful to use an interval time tracking app - in our case we are using ['TotallyTabata'](https://apps.apple.com/us/app/totally-tabata-timer-protocol/id856659483), as the app allows to set custom intervals including voice announcements.

1. Connect Bitalino device to Opensignals
2. Attach electrodes to cables 
3. Clean skin where the electrodes will be positioned, i.e. on the knee cap and the vastus lateralis
4. Position measurement electrodes:
   - Red: ~ 1/3 of the distance between the knee (patella) and the point where the hip bone starts to bend inwards (anterior superior iliac spine)
   - Black: Above the red one, centers of the electrodes should be ~ 2cm apart
   - White: On the bone part of the knee
<div class="grid grid-cols-2">

  <div class="card"> 
  <img src="images/muscle_info.png" alt="drawing" width="200"/>

</div>
 <div class="card"> 
  <img src="images/start.jpeg" alt="drawing" width="300"/>
</div>
</div>



 <!-- as in [Smith et al 2017](https://doi.org/10.1002/mus.25502) - see drawing -->
5. Start Opensignals recording
6. Sit down on the floor, against a wall, legs straight, hands hanging loosly on the side (make sure they don't touch your leg!)
7. Keep muscles relaxed. At the same time start protocol tracking app & push button on the Bitalino device.
9. Follow Protocol:


<div class="row">
  <div class="column"><img src="images/protocol.jpg" alt="drawing" width="400"/></div>
  <div class="column"> 

  <ol>
  <li>Sit relaxed for 30s</li>
  <li>Try to maximally contract your upper leg muscles as much as possible for 3 x  6s with 10s break in between (see also <a href="https://www.sciencedirect.com/science/article/pii/S0165027009002015">Hendrix et al (2009) </a> )</li>
  <li>Stand up and take wall sit position, 90 degree angle (20s) (this is a form of isometric muscle contraction and according to <a href="https://doi.org/10.1145/3648679"> Li et al. 2024 </a>, this is the type of exercise most often used in fatigure detection based on EMG; also wall sit is an <a href="https://www.yourhousefitness.com/blog/exercise-tutorial-wall-sit#google_vignette"> exercise that engages the vastus lateralis </a>; similarly <a href="https://www.aaem.pl/pdf-81716-26429?filename=Differences%20in.pdf"> Gawda et al 2018 </a> ask runners to perform 60s squats to measure fatigue)</li>
  <li>Sit down again, back agains the wall, legs straight (30s)</li>
</ol>
</div>
</div>




<div class="grid grid-cols-4">
  <div class="card"> 
 <center> <h3>Sit Relaxed </h3>
  <img src="images/sit_relaxed.jpeg" alt="drawing" width="300"/></center>
</div>
  <div class="card"> 
  <center> <h3>Wallsit </h3>
  <img src="images/wallsit.jpeg" alt="drawing" width="200"/> </center>
  </div>
  <div class="card"> 
  <center> <h3>Contraction </h3>
  <video src="images/contraction.mp4" alt="drawing" width="300" autoplay muted loop type="video/mp4"> </video></center>
  </div>
</div>

## Survey
The survey has two purposes:
1. measure subjective experience of (muscle) fatigue 
2. gather information about other variables that could influence fatigue levels

### Assesssing Fatigue
We are using an adapted version of the Checklist Individual Strength (CIS) for our questionnaire. This instrument was originally developed for measuring severity of fatigue in hospital studies of chronic fatigue symptom patients but has also been validated in the working population (see [Beurskens et al., 2000](https://oem.bmj.com/content/oemed/57/5/353.full.pdf)). Many other fatigue measurement scales such as e.g. the Fatigue Severity Scale (FSS) ([Krupp et al., 1989](10.1001/archneur.1989.00520460115022)) or the Fatigue Impact Scale (FIS)([Fisk et al 1994](https://pubmed.ncbi.nlm.nih.gov/8148458/)) have either not been validated in healthy individuals or presume the ongoing presence of fatigue and are thus not applicable to our use case. Additionally, the CIS has been proven to have a good internal consistency and has been shown to be sensitive to change in fatigue levels over time (see [Dittner et al. 2004](https://www.sciencedirect.com/science/article/pii/S0022399903003714)).

However,  in its original form the CIS is intended to assess fatigue levels over  time periods of 2 weeks ([Beurskens et al., 2000](https://oem.bmj.com/content/oemed/57/5/353.full.pdf)), we thus adapt the statements to be applicable to the past day as the questionnaire is inteded to be filled out at the end of each day.

The survey has 20 items that are scored on a 7 level agreement scale which we adapted to confirm with standardized Likert scale responses ([Vaigas, 2006](https://cse.iitkgp.ac.in/~mainack/courses/2020-autumn/usesec/slides/Likert-Scale-Examples.pdf)).

- I felt tired
- I felt very active
- Thinking required effort
- Physically I felt exhausted
- I felt like doing all kinds of nice things
- I felt fit
- I did quite a lot today
- When I have been doing something, I was able to concentrate very well
- I felt weak
- I didn't do much during the day
- I could concentrate well
- I felt rested
- I had trouble concentrating
- Physically I felt I am in a bad condition
- I am full of plans
- I got tired very quickly
- I had a low output
- I felt no desire to do anything
- My thoughts easily wandered
- Physically I felt in a good shape

#### Assessing overall wellbeing and muscle soreness
Since our study specifically focuses on muscle fatigue, we incorporated additional items in the questionnaire to better represent this specific dimension as it is not explicitly covered in the CIS. For this we adapted the [Hooper Index](https://pubmed.ncbi.nlm.nih.gov/7898325/) which is regularly used for the assessment of wellbeing in sports studies (e.g. [Clemente et al 2017](https://www.sciencedirect.com/science/article/pii/S003193841631068X?via%3Dihub#bb0110), [Clemente et al 2019](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6714361/#j_hukin-2019-0002_ref_011), [Haddad et al 2013](https://www.sciencedirect.com/science/article/pii/S0031938413002023))
Additional items to focus on muscles:
- Sleep Quality
- Stress Level
- Fatigue Level

We adjusted the answer possibilities to confirm with standardized Likert scale response options for quality ratings. ([Vaigas, 2006](https://cse.iitkgp.ac.in/~mainack/courses/2020-autumn/usesec/slides/Likert-Scale-Examples.pdf)).

The last item in the Hooper Index is muscle soreness - we incorporated this into the CIS questionnaire by adding "My muscles felt sore" as an additional item.

### Additional Questions

To be able to account for potential confounders, taking into consideration other studies on wellbeing, we further record the following measures:
Closed form: 
- How many hours did you sleep last night? - Numeric
- How many coffees have you had today? - Numeric
- Day in menstruation cycle - Numeric
- Alcohol consumption
   - no alcohol
   - one light alcoholic drink (e.g. beer, wine)
   - two light alcoholic drinks or one strong alcoholic drink (e.g. cocktail, shot)
   - more than three alcoholic drinks
- What physical activities did you engage in today?
   - Walking for 30min or longer
   - Yoga
   - Weight Lifting
   - High Intensive Interval Training
   - Running
   - Ball Sports
   - Cycling for 30min or longer
   - Swimming
   - Other: please specify
- Pedometer - Numeric
Free text:
- Did you feel ill? If so, describe the severity and symptoms.
- Have you experienced any significant changes in your mental wellbeing/stress today? Can you describe the situation(s).
- Short, keyword description of what you did today
- Any comments regarding the measurement session today (e.g. bloopers with electrodes etc.)
- Was there anything else that might be relevant?

### Topics not included in the questionnaire
#### Nutrition
While muscle fatigue is a complex phenomenon, most current evidence indicates that muscle fatigue in the context of chronic fatigue or illnesses, is mainly caused by the failures in the central nervous system (CNS) ([Davis & Bailey 1997](https://journals.lww.com/acsm-msse/fulltext/1997/01000/possible_mechanisms_of_central_nervous_system.8.aspx)). The mechanisms that cause CNS fatigue are not well understood, a possible epxlanation are exercise induced alteration in neurotransmitters ([Davis, 1999](http://www.bentrem.sycks.net/NutritionInSport-Ronald-J-Maughan.pdf#page=189)).

While these neurotransmitters are affected by nutritional intake, the relationship is still unclear and is further dependent on other environmental and metabolic factors. Considering this as well as the substantial additional time requirement for recording food intake, we have decided not to include this dimension in our questionnaire.
Also, [Campagnolo et al, 2017](https://onlinelibrary.wiley.com/doi/full/10.1111/jhn.12435) conducted a review of dietary and nutrition interventions for the treatment of chronic fatigue syndrome and 'identified insufficient evidence for the use of nutrtional supplements and elimination or modified diets to relive symptoms'.

#### Environmental Factors
We do not include any questions regarding exposure to pollution, outdoor time or weather. We are considering adding those measurement via the integration of a smartwatch in the future. However, manual reporting of these measures is currently out of scope.
<!--
#### Questions from first trial
- How fatigued were your muscles today? 1 (no fatigue at all) to 7 (extremely fatigued)
   - Level 1: No Fatigue at All: Muscles feel completely fresh, as if you haven't exercised or engaged in any physical activity.
      - No soreness or stiffness.
      - Full range of motion without discomfort.
      - Able to walk and climb stairs with ease and no perceived effort.
      - Able to perfrom all kiinds of common tasks without hinderance.
   - Level 2: Very Mild Fatigue: Muscles are slightly tired, but it’s barely noticeable.
      - Slight sense of tiredness.
      - No pain or soreness.
      - Full range of motion with minimal perceived effort.
   - Level 3: Mild Fatigue: Muscles are tired but still function normally without any significant discomfort.
      - Noticeable but mild tiredness.
      - Minor stiffness or tightness.
      - Able to perform most physical tasks, though with slightly increased effort.
   - Level 4: Moderate Fatigue: Muscles feel tired, and there is a noticeable decrease in performance.
      - Tiredness and some soreness.
      - Reduced strength and endurance.
      - Slight discomfort during movement, but tasks are still manageable.
   - Level 5: Significant Fatigue: Muscles are quite tired, and performing physical tasks is more challenging.
      - Moderate soreness and stiffness.
      - Noticeable drop in strength and endurance.
      - Movement involves a fair amount of effort, and some tasks might be difficult.
   - Level 6: Severe Fatigue: Muscles are very tired, with significant discomfort and reduced ability to perform tasks.
   - Severe soreness and stiffness.
   - Major decrease in strength and endurance.
   - Performing physical tasks is very challenging and uncomfortable.
   - Level 7: Extremely Fatigued: Muscles are exhausted to the point where performing any physical activity is almost impossible.
   - Intense soreness and stiffness.
   - Extremely low strength and endurance.
   - Any movement causes significant discomfort, and even simple tasks are barely achievable.



- Symptoms experienced today 
   - Muscle weakness
   - Trouble climbing stairs
   - Trouble standing from a seated position
   - Active Rash
   - Brain Fog
   - Extreme Fatigue
- How difficult was it to dress and shower today? 1 (no difficulty) to 5 (unable to do).
- How difficult was it to climb stairs today? 1 (no difficulty) to 5 (unable to do).
- <span style="color:red">How difficult was it to complete common daily activities?  1 (no difficulty) to 5 (unable to do). [Kick Out - high correlation with pain] </span>
- How much pain were you in today? 1 (pain at all) to 5 (worst pain experienced).
- Do you have an active and visible rash? 1 (no rash at all) to 5 (very visible rash in DM areas)
- Overall how did you feel today? As an overall "wellness" 1 (horrible, hard to function) to 5 (very well).[Kick Out - high correlation with pain]
- How do you think you will feel tomorrow? As an overall "wellness" 1 (horrible, hard to function) to 5 (very well).


### References
-->
<!---
- Beurskens AJHM, Bültmann U, Kant I, et alFatigue among working people: validity of a questionnaire measureOccupational and Environmental Medicine 2000;57:353-357.
[https://oem.bmj.com/content/oemed/57/5/353.full.pdf](https://oem.bmj.com/content/oemed/57/5/353.full.pdf)
- A.J Dittner, S.C Wessely, R.G Brown, The assessment of fatigue: A practical guide for clinicians and researchers Journal of Psychosomatic Research, Volume 56, Issue 2, 2004, Pages 157-170, ISSN 0022-3999, [https://doi.org/10.1016/S0022-3999(03)00371-4.](https://www.sciencedirect.com/science/article/pii/S0022399903003714)
- Fisk JD, Ritvo PG, Ross L, Haase DA, Marrie TJ, Schlech WF.
Measuring the functional impact of fatigue: initial validation of
the fatigue impact scale. Clin Infect Dis 1994;18(Suppl 1):
S79 – 83. (https://pubmed.ncbi.nlm.nih.gov/8148458/)[https://pubmed.ncbi.nlm.nih.gov/8148458/]
- Hendrix C. Russell , Housh Terry J. , Johnson Glen O. ,  Mielke Michelle, Camic Clayton L. , Zuniga Jorge M. , Schmidt  Richard J., A new EMG frequency-based fatigue threshold test, Journal of Neuroscience Methods, Volume 181, Issue 1, 2009, Pages 45-51, ISSN 0165-0270, [https://doi.org/10.1016/j.jneumeth.2009.04.011.](https://www.sciencedirect.com/science/article/pii/S0165027009002015)
- Gawda P, Ginszt M, Ginszt A, Pawlak H, Majcher P. Differences in myoelectric manifestations of fatigue during isometric muscle actions. Ann Agric Environ Med. 2018 Jun 20;25(2):296-299. doi: [10.26444/aaem/81716.](10.26444/aaem/81716) Epub 2018 Feb 21. PMID: 29936808.
- Hooper SL, Mackinnon LT, Howard A, Gordon RD, Bachmann AW. Markers for monitoring overtraining and recovery. Med Sci Sports Exerc. 1995 Jan;27(1):106-12. PMID: 7898325. [https://pubmed.ncbi.nlm.nih.gov/7898325/](https://pubmed.ncbi.nlm.nih.gov/7898325/)
-  Krupp LB, LaRocca NG, Muir-Nash J, Steinberg AD. The
Fatigue Severity Scale. Application to patients with multiple
sclerosis and systemic lupus erythematosus. Arch Neurol 1989;
46:1121 – 3. doi: [10.1001/archneur.1989.00520460115022.](10.1001/archneur.1989.00520460115022.)

- Na Li, Rui Zhou, Bharath Krishna, Ashirbad Pradhan, Hyowon Lee, Jiayuan He, and Ning Jiang. 2024. Non-invasive Techniques for Muscle Fatigue Monitoring: A Comprehensive Survey. ACM Comput. Surv. 56, 9, Article 221 (September 2024), 40 pages. [https://doi.org/10.1145/3648679](https://doi.org/10.1145/3648679)

- Smith, C.M., Housh, T.J., Hill, E.C., Johnson, G.O. and Schmidt, R.J. (2017), Changes in electromechanical delay during fatiguing dynamic muscle actions. Muscle Nerve, 56: 315-320. [https://doi.org/10.1002/mus.25502](https://doi.org/10.1002/mus.25502)



- Miura N, Watanabe T. Potential of M-Wave Elicited by Double Pulse for Muscle Fatigue Evaluation in Intermittent Muscle Activation by Functional Electrical Stimulation for Motor Rehabilitation. J Med Eng. 2016;2016:6957287. doi: 10.1155/2016/6957287. Epub 2016 Mar 27. PMID: 27110556; PMCID: PMC4826699.
- Sengchuai K, Kanjanaroat C, Jaruenpunyasak J, Limsakul C, Tayati W, Booranawong A, Jindapetch N. Development of a Real-Time Knee Extension Monitoring and Rehabilitation System: Range of Motion and Surface EMG Measurement and Evaluation. Healthcare (Basel). 2022 Dec 15;10(12):2544. doi: [10.3390/healthcare10122544](10.3390/healthcare10122544). PMID: 36554067; PMCID: PMC9778223.

- Hodges PW, van den Hoorn W, Wrigley TV, Hinman RS, Bowles KA, Cicuttini F, Wang Y, Bennell K. Increased duration of co-contraction of medial knee muscles is associated with greater progression of knee osteoarthritis. Man Ther. 2016 Feb;21:151-8. doi: [10.1016/j.math.2015.07.004.](10.1016/j.math.2015.07.004.) Epub 2015 Jul 17. PMID: 26254263.--->





