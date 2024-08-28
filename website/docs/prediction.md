```js
import { utcParse } from 'npm:d3-time-format'
import * as d3 from 'npm:d3'
import { csvFormat } from 'd3-dsv'

// function to correctly process prediction data
const coerceRowPred = d => ({
  date: new Date(d.index),
  'Overall Fatigue': Number(d.cis_subjective_fatigue),
  'Muscle Tiredness': Number(d.extra_muscles_tired),
  'Muscle Soreness': Number(d.hooper_muscles_sore),
  person: d.person,
  model: d.model
})

// function to correctly process survey data
const coerceRowSurvey = d => ({
  date: new Date(Date.parse(d.date)),
  'Overall Fatigue': Number(d.cis_subjective_fatigue),
  'Muscle Tiredness': Number(d.extra_muscles_tired),
  'Muscle Soreness': Number(d.hooper_muscles_sore),
  'Step Count': Number(d.step_count),
  'Sleep Time': d.sleep_time,
  'Alcohol Intake': d.alcohol,
  'Coffee Intake': d.coffee_count,
  person: d.person
})

// read in data
let predictions = FileAttachment('data/predictions.csv')
  .csv({ typed: true })
  .then(D => D.map(coerceRowPred))
let surveyData = FileAttachment('data/pre_processed_survey_features.csv')
  .csv({ typed: true })
  .then(D => D.map(coerceRowSurvey))


// pick person 
const pickPersonInput = Inputs.radio(['Amanda','Johanna'], {value: "Amanda"})
const pickPerson = Generators.input(pickPersonInput)


```

<style type="text/css">
p {
  max-width: null;
}
</style>

# The Study

Amanda and Johanna both did a 35 day self-experiment: every day they would (1) take two muscle measurements (see <a href='/protocol#muscle-data-measurement-protocol'>protocol</a>)  - one in the morning after waking up, one in the evening before going to bed and (2) fill out a questionnaire (see <a href='/protocol#survey'>survey</a>).
Based on this we sought to understand our own bodies better and try to see whether we can predict days of rest.

For the remainder you can pick a person whose data you want to explore: 
```js
view(pickPersonInput)
```
The below plot shows the three main outcomes of interest over time: **overall fatigue**, **muscle soreness** and **muscle tiredness**. Everyday we retrospectively assessed or subjective experience of those. Values range from 1 (= very low) to 7 (= very high). It further shows the levels of some other variables in relation to their respective maximum, e.g. if step count is dark purple, the number of steps on that days was close to the maximum number of daily steps measured during the study period.

```js
// subset data to person picked
let predictions2 = predictions.filter(d => d.person === pickPerson)
let surveyData2 = surveyData.filter(d => d.person === pickPerson)

// pivot data longer
let data = aq
  .from(surveyData2) // create an arquero table from our data
  .fold(aq.not('date'), { as: ['name', 'value'] }) // unpivot/fold the data by date
  .objects()

// get unique model names to choose from
const uniqueNames = [...new Set(predictions.map(item => item.model))]

// pick model name
const pickModelInput = Inputs.radio(uniqueNames.filter(item => item !== 'Ground Truth'), { value: 'Lasso' })
const pickModel = Generators.input(pickModelInput)

// define max and respective color scale for variables
const colorSteps = Plot.scale({color: {range: ['white','#A07ECE'], domain: [0,Math.max(...surveyData.map(obj => obj['Step Count']))]}});
const colorSleep = Plot.scale({color: {range: ['white','#A07ECE'], domain: [0,Math.max(...surveyData.map(obj => obj['Sleep Time']))]}});
const colorAlcohol = Plot.scale({color: {range: ['white','#A07ECE'], domain: [0,Math.max(...surveyData.map(obj => obj['Alcohol Intake']))]}});
const colorCoffee = Plot.scale({color: {range: ['white','#A07ECE'], domain: [0,Math.max(...surveyData.map(obj => obj['Coffee Intake']))]}});

// plot correlation matrix over time
function CorrelationPlot() {
  return Plot.plot({
    marginLeft: 150,
    width: 600,
    y:{label: 'Variable'},
    color: {
      type: 'linear',
      range: ['#819E90', 'white', '#B65F77'],
      domain: [1, 7],
   //   legend: true
    },

    marks: [
      Plot.cell(
        data.filter(item =>
          Array(
            'Overall Fatigue',
            'Muscle Soreness',
            'Muscle Tiredness'
          ).includes(item.name)
        ),
        {
          x: 'date',
          y: 'name',
          fill: ({ value }) => (value === 0 ? NaN : value),
          title: ({ value }) => value,

          inset: 0.5,
       
          //tip:true
        }
      ),
   
      Plot.cell(
        data.filter(item =>
          Array(
            'Step Count',
           
          ).includes(item.name)
        ),

     //   Plot.map(
       // {fill: Plot.normalize("mean"),

        //},
       {
          x: 'date',
          y: 'name',
          fill:   ({value}) => colorSteps.apply(value),
          title: ({ value }) => value,

          inset: 0.5,
       
         // tip:true
        }
    //)
    ),
    ,
   
      Plot.cell(
        data.filter(item =>
          Array(
            'Sleep Time',
           
          ).includes(item.name)
        ),

     //   Plot.map(
       // {fill: Plot.normalize("mean"),

        //},
       {
          x: 'date',
          y: 'name',
          fill:   ({value}) => colorSleep.apply(value),
          title: ({ value }) => value,

          inset: 0.5,
       
        //  tip:true
        }
    //)
    ),

    Plot.cell(
        data.filter(item =>
          Array(
            'Coffee Intake',
           
          ).includes(item.name)
        ),

     //   Plot.map(
       // {fill: Plot.normalize("mean"),

        //},
       {
          x: 'date',
          y: 'name',
          fill:   ({value}) => colorCoffee.apply(value),
          title: ({ value }) => value,

          inset: 0.5,
       
         // tip:true
        }
    //)
    ),

    Plot.cell(
        data.filter(item =>
          Array(
            'Alcohol Intake',
           
          ).includes(item.name)
        ),

     //   Plot.map(
       // {fill: Plot.normalize("mean"),

        //},
       {
          x: 'date',
          y: 'name',
          fill:   ({value}) => colorAlcohol.apply(value),
          title: ({ value }) => value,

          inset: 0.5,
       
         // tip:true
        }
    //)
    ),
      Plot.text(
        data.filter(item =>
          Array(
            'Overall Fatigue',
            'Muscle Soreness',
            'Muscle Tiredness'
          ).includes(item.name)
        ),

        {
          x: 'date',
          y: 'name',
          text: ({ value }) => Math.round(value === 0 ? NaN : value),
        //  tip:true,
          fill: 'black'
        }
      )
    ]
  })
}
```
<div class="grid grid-cols-2" style="max-width:600px">
<div>
<small>Fraction of maximum value</small>
<img src="images/correlation_purple.png" alt="drawing" width="300"/>
</div>
<div>
<small>Fatigue levels</small>

<img src="images/correlation_red_green.png" alt="drawing" width="300"/>
</div>
</div>


```js
display(CorrelationPlot())

// define plot of values over time (currently not shown)
function LinePlot() {
  return Plot.plot({
    y: { domain: [1, 7] },
    width: 1000,
    height: 300,
    marginRight: 150,
    color: {
      range: ['#A07ECE', '#819E90', '#B65F77'],
      domain: ['Overall Fatigue', 'Muscle Soreness', 'Muscle Tiredness'],

      legend: true
    },
    x: {
      ticks: 10,
      //domain: [new Date('2024-7-08'), new Date('2024-08-14')]
    },
    marks: [
      // Plot.dot(predictions2.filter((d) => d.model === "Ground Truth"), {x: "date", y: "value", r:2, symbol: "model"}),
      Plot.lineY(
        data.filter(item =>
          Array(
            'Overall Fatigue',
            'Muscle Soreness',
            'Muscle Tiredness'
          ).includes(item.name)
        ),
        {
          x: 'date',
          y: ({ value }) => (value === 0 ? NaN : value),
          stroke: ({ name }) => name,
          tip: true,
          title: d => `${d.name}: ${d.value}`
        }
      ),

      Plot.axisX({ anchor: 'bottom', label: null, tick: 'day' })
    ]
  })
}

//display(LinePlot())
```

# Predictions based on Survey Data

## Does how we feel today say something about how we will feel tomorrow?

In a first step, we explored whether we can predict subjective experience of fatigue, muscle soreness and muscle tiredness for the next day based on information collected through the <a href='/protocol'>questionnaire </a> the day before. We tested several machine learning models and compared them to (1) our own prediction of how we would feel the next day and (2) always predicting the mean level.



```js
const dataFiltered = predictions2.filter(d => d.model === pickModel)
const dataTrue = predictions2.filter(d => d.model === 'Ground Truth')

const colorDict = {
  'Overall Fatigue': '#A07ECE',
  'Muscle Soreness': '#819E90',
  'Muscle Tiredness': '#B65F77'
}

function calculateMeanDifference(array1, array2, property) {
  if (array1.length !== array2.length) {
    throw new Error('Arrays must have the same length')
  }

  let totalDifference = 0
  let count = 0

  for (let i = 0; i < array1.length; i++) {
    if (array1[i][property] != null && array2[i][property] != null) {
      totalDifference += Math.abs(array1[i][property] - array2[i][property])
      count++
    }
  }

  return count === 0 ? 0 : totalDifference / count
}
let maxDate = Math.max(...predictions2.map(obj => obj.date))
let minDate = Math.min(...predictions2.map(obj => obj.date))

// function for prediction  lineplot
function PredictionPlot(model, variable, width) {
  return Plot.plot({
    x: {
      tickFormat: d3.utcFormat('%b %e'),
      ticks: 5,
      nice: true,
    domain: [new Date(minDate), new Date(maxDate)],
    },
    symbol: { legend: true },
    // marginLeft: 80,
    //marginRight: 150,
    width: width,
    height: 200,
    y: { ticks: 7, domain: [1, 7], label: null },
    marks: [
      Plot.ruleY([0]),
      //Plot.areaY(predictions2.filter((d) => d.model === "Human Prediction"), {x: "date", y: "cis_subjective_fatigue", fillOpacity: 0.2}),
      Plot.lineY(
        predictions2.filter(d => d.model === model),
        {
          x: 'date',
          y: variable,
          stroke: 'grey',
          strokeDasharray: 10,
          title: d => d[variable]
          //tip: true
        }
      ),

      Plot.dot(
        predictions2.filter(d => d.model === 'Ground Truth'),
        { x: 'date', y: variable, r: 2, symbol: 'model' }
      ),
      Plot.dot(
        predictions2.filter(d => d.model === model),
        { x: 'date', y: variable, r: 2, symbol: 'model' }
      ),

      Plot.lineY(
        predictions2.filter(d => d.model === 'Ground Truth'),
        {
          x: 'date',
          y: variable,
          stroke: 'grey',
          title: d => d[variable]
          //tip: true
        }
      ),

      //Plot.text(predictions.filter((d) => d.model === "Ground Truth"), Plot.selectLast({x: "date", y: variable, text: "model", textAnchor: "start", dx: 5, dy: 0})),
      // Plot.text(predictions.filter((d) => d.model === model), Plot.selectLast({x: "date", y: variable, text: "model", textAnchor:"start", dx: 5, dy:0})),

      //Plot.ruleX([parseDate("2024-08-07")]),
      Plot.text(
        [
          'MAE: ' +
            Math.round(
              calculateMeanDifference(dataFiltered, dataTrue, variable) * 100
            ) /
              100
        ],
        {
          frameAnchor: 'top',
          textAnchor: 'start',
          x: new Date(minDate),
          fontSize: 15
        }
      ),
      Plot.areaY(
        predictions2.filter(
          d => d.model === model || d.model === 'Ground Truth'
        ), //  Plot.windowY(
        //  14,
        Plot.groupX(
          {
            y1: Plot.find(d => d.model === model),
            y2: Plot.find(d => d.model === 'Ground Truth')
          },
          {
            x: 'date',
            y: variable <= 0 ? NaN : variable,
            //title: (d) => Math.round(d[variable],2),
            tip: true,
            opacity: 0.3,
            fill: colorDict[variable]
            //positiveFill: "#A07ECE",
            //negativeFill: "#A07ECE",
          }
        )
        // )
      )
      //Plot.lineY(predictions, {x: "date", y: "value"})
    ]
  })
}

if (pickPerson==='Amanda') {
  document.getElementById('text-container').innerHTML = "Generally speaking, Amanda's predictions of her muslce sorness & tiredness levels for the next days, were as accurate as just always predicting the mean value. For the overall fatigue level her own predictions were even worse than that - mostly she is too pessimistic. When it comes to the different models, in terms of absolute error, none of them consistently achieves a lower average than just always predicting the mean. The multiseries models (i.e. time series models the aim to jointly predict future values of multiple outcome variables) generally performed worst - a reason for this could be that those models are trying to reduce the overall prediction error. Thus, they might need to 'compromise' which can be a disadvantage if the additional information gain from including those other variables is small. The best performing models were (1) the single time series gradient boosting model - indicating that we do observe some degree of autocorrelation and (2) the lasso regression model. <br> In an attempt to understand better whats going on we can take a look at the most relevant predictors in the lasso model: <ul> <li> 'I am full of plans' was negatively correlated with all outcomes, i.e. having a lot of plans made it more likely for Amanda to experiences low levels of fatigue, muscle soreness and muscle tiredness on the next day </li> <li>'I didn`t do much during the day' was negatively correlated with muscle soreness, i.e. if Amanda didn't do much on a particular day it was unlikely for her to experience muscle soreness on the next day </li> <li> 'I could concentrate well' was positively correlated with muscle soreness & tiredness, i.e. days were it was easy to concentrate often preceded days with a high level of muscle soreness. This one is somewhat surprising - maybe days where concentration was high usually were somewhat intense work days, which could then lead to stress and then trigger muscle impairment? Interestingly enough it was not relevant for the overall fatigue level prediction. </li> <li> Muscle Soreness & Tiredness: a given days level of muscle soreness and tiredness postively correlated with the next days values, i.e. we observe some autocorrelation </li> <li> Self-predicted fatigue level: the surey takers own prediction of how fatigued they would feel on the next day did have some predictive power for muscle soreness and tiredness, not so for overall fatigue however </li> </ul>"
} else if (pickPerson==='Johanna') {
  document.getElementById('text-container').innerHTML = "Generally speaking, Johanna's own predictions for overall fatigue and muscle tiredness were worse than always just predicting the mean. For muscle soreness, her predictions were fairly accurate - at least better than all machine learning models are simply choosing the mean. <br> When it comes to the different models, standard random forest performed best for overall fatigue and muscle tiredness, lasso worked best for muscle soreness. To understand better what is going on we can take a look a the most relevant predictors in the lasso model as well as the SHAP values of variables in the random forest model: <ul> <li> Self predicted Fatigue - Johanna's prediction of her fatigue level was the most relevant predictor for the actual experienced fatigue (and was also a relevant predictor for muscle sorness & tiredness), indicating that she did have some intuition about how she would feel the next day. </li> <li> Doing HITT, cycling & weightlifting was(non-surprisngly) a relevant predictor for muslce soreness on the next day. Interestingly, however these activiteis did not play a large role in prediction levels of muscle tiredness. </li> <li> 'I felt fit' was negatively correlated with muscle tiredness, i.e. days when Johanna felt very active or fit were often followed by days with high levels of muscle tiredness.</li> <li> Self predicted muscle soreness was a good predictor of actual experienced muscle soreness and tiredness on the next day. However, predicted muscle tiredness was not relevant, indicating that Johanna was better at predicting her levels of muscle soreness compared to muscle tiredness. </li></ul>"
} 


let modelInfo = {"Lasso": "Lasso Regression - A fairly simple, non-temporal model - a specific day's fatigue level is regressed on survey information from the day before",
"Random Forest": "Creates decision trees to predict a specific day's fatigue level based on survey variables from the day before and combines their results by averaging. Only data from the previous day is considered.",
"Random forest time series": "An auto-regressive random forest based model - only takes into account values of the outcome variable from the 5 previous days.",
"Random forest multiseries": "An auto-regressive random forest based model based on multiple time series - also takes into account past values of other variables from the past 5 days and jointly predicts their values for the next day.",
"Gradient Boosting": "Creates sequential decision trees where each new tree tries to correct the errors made by the previous trees. Trys to predict a specific day's fatigue level based on survey variables from the day before.",
"Gradient boosting timeseries": "An auto-regressive gradient boosting model - only takes into account values of the outcome variable from the 5 previous days",
"Gradient boosting multiseries": "An auto-regressive gradient boosting model based on multiple time series - also takes into account past values of other variables from the past 5 days and jointly predicts their values for the next day.",
"Human Prediction": "The self-predicted value of the outcome variable, predicted on the evening before for the next day.",
"Always predicting the mean": "Comparing the mean value to observed values."

}
```

${pickModelInput}

## Model Selected: ${pickModel}
${modelInfo[pickModel]}

<div class="grid grid-cols-3">

 <div class="card">
 <h3> Overall Fatigue</h3>
${resize((width) => PredictionPlot(pickModel, 'Overall Fatigue',width))}

  </div>
<div class="card">
<h3> Muscle Soreness </h3>
${resize((width) => PredictionPlot(pickModel, 'Muscle Soreness',width))}
</div>
<div class="card">
<h3> Muscle Tiredness </h3>
${resize((width) => PredictionPlot(pickModel, 'Muscle Tiredness',width))}

</div>

</div>

## Discussion
### What does all of this tell us?
Well... it seems like fatigue levels and behavior are not too much indicative of the next days' fatigue levels.

<div id='text-container'>


</div>


```js
let rawEMGExample = FileAttachment('data/amanda_raw_emg_example.csv')
  .csv({ typed: true })

let bandpassEMGExample = FileAttachment('data/amanda_bandpass_emg_example.csv')
  .csv({ typed: true })

let rectEMGExample = FileAttachment('data/amanda_rect_emg_example.csv')
  .csv({ typed: true })

let normEMGExample = FileAttachment('data/amanda_norm_emg_example.csv')
  .csv({ typed: true })
```

```js
let startTabata = 32.7
function EMGPlot(data, title,width) {
  
  return Plot.plot({
    //axis: null,
      height: 150,
      width: width,
       grid: true,
  marginRight: 60,
  marginBottom:60,
  facet: {data: data, x: "Signal type", label: title, fontSize: 35,style: {
    fontSize: 30,
  }},
  x:{label:null},
  y:{label: null},
    marks:[
    
        Plot.lineY(
        data,
        {
        x: 'Time',
        y: 'Signal',
        opacity: 0.7,

        }
      ),
    // mark start of sections
    Plot.ruleX(data.filter(d => d['Processing stage'] === 'Normalized signal'), {x: [startTabata], stroke: "#A07ECE", strokeWidth: 2}),
    Plot.ruleX(data.filter(d => d['Processing stage'] === 'Normalized signal'), {x: [startTabata+16], stroke: "#A07ECE", strokeWidth: 2}),
    Plot.ruleX(data.filter(d => d['Processing stage'] === 'Normalized signal'), {x: [startTabata+32], stroke: "#A07ECE", strokeWidth: 2}),
    Plot.ruleX(data.filter(d => d['Processing stage'] === 'Normalized signal'), {x: [startTabata+58], stroke: "#A07ECE", strokeWidth: 2}),
    Plot.ruleX(data.filter(d => d['Processing stage'] === 'Normalized signal'), {x: [startTabata+93], stroke: "#A07ECE", strokeWidth: 2}),


    // label start of sections
    Plot.text(data.filter(d => d['Processing stage'] === 'Normalized signal'), {text:['Relax'], x: startTabata-30, dy:-20,  dx: -10, lineAnchor:'top', rotate: 270,fill: 'black'}),
    Plot.text(data.filter(d => d['Processing stage'] === 'Normalized signal'), {text:['M1'], dy:-20,  dx: -10, lineAnchor:'top', rotate: 270,fill: 'black'}),
    Plot.text(data.filter(d => d['Processing stage'] === 'Normalized signal'), {text:['M2'],  x: startTabata+16, dy:-20,  dx: -10, lineAnchor:'top', rotate: 270,fill: 'black'}),
    Plot.text(data.filter(d => d['Processing stage'] === 'Normalized signal'), {text:['M3'],  x: startTabata+32, dy:-20,  dx: -10, lineAnchor:'top', rotate: 270,fill: 'black'}),
    Plot.text(data.filter(d => d['Processing stage'] === 'Normalized signal'), {text:['Wallsit'],  x: startTabata+58, dy:-20,  dx: -10, lineAnchor:'top', rotate: 270,fill: 'black'}),
    Plot.text(data.filter(d => d['Processing stage'] === 'Normalized signal'), {text:['Relax'],  x: startTabata+93, dy:-20,  dx: -10, lineAnchor:'top', rotate: 270,fill: 'black'}),

    ]
})
}


```

<div class="grid grid-cols-2">
<div>

## Using Muscle Data

In addition to the daily survey data, we also collected sensor data about muscle activity twice a day, using an <a href='/sensor-kit'> EMG & MMG sensor kit </a>, following a strict <a href='/protocol'> protocol </a>. A large body of literature has been trying to use these types of data to assess and/or predict (muscle) fatigue (see <a href='https://dl.acm.org/doi/10.1145/3648679'>here </a> for a great literature review or <a href="/research">here </a> for our summary) - with varying success.

Based on the existing literature, we developed a protocol that we hoped would allow us to gather data with high enough quality to be of use while still being short and easy to follow such that we could integrate it in our daily schedule.

### Pre-Processing

In a first step, the EMG and MMG data was pre-processed. In this case we (1) substracted the mean and applied a bandpass filter with a lower bound of 50 and an upper bound 450 Hz, (2) rectified the signal and (3) performed amplitude normalization. The last plot also shows the starting points of the different phases in the <a href='/protocol'> protocol </a>, where 'M' stands for muscle contraction.

</div>
<div>
 ${resize((width) => EMGPlot(rawEMGExample,'Raw signal', width))}
${resize((width) => EMGPlot(bandpassEMGExample, 'Bandpass filtered signal',width))}
 ${resize((width) => EMGPlot(rectEMGExample, 'Rectified signal',width))}
 ${resize((width) =>EMGPlot(normEMGExample, 'Normalized signal',width))}
    </div>
  </div>

```js
let SignalFeatures = FileAttachment('data/amanda_features_example.csv')
  .csv({ typed: true })
```
```js


function FeaturesPlot(data) {
  
  return Plot.plot({
    //axis: null,
      //height: 150,
     // width: 600,
       grid: true,
  marginRight: 60,
  marginBottom:60,
  fy:{label:null},
  y:{axis:null},
  facet: {data: data, y: "variable",  x:'Signal Type', fontSize: 35,style: {
    fontSize: 30,
  }},
  x:{label:null},
  y:{label: null},
    marks:[
       Plot.axisY({ticks: []}),
    
        Plot.lineY(
        data,
        {
        x: 'START',
        y: 'value',
        opacity: 0.7,

        }
      ),
    ]
  })
}

```


<div class="grid grid-cols-2">
<div>
<h3>Feature Extraction </h3>

</div>
<div>
 ${resize((width) =>FeaturesPlot(SignalFeatures,width))}
 </div>
  </div>