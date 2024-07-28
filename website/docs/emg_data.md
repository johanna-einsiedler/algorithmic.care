# Data Dashboard


```js
import {utcParse} from "npm:d3-time-format";
import * as d3 from "npm:d3";
import {csvFormat} from "d3-dsv";
const coerceRow = (d) => ({//date: d.date.getDay()+"-"+(d.date.getMonth()+1)+"-"+d.date.getFullYear(),
                        //variable: d.variable,
                        //y: Number(d.y)});
                        id:d.id,
                        time: Number(d.time),
                        signal: Number(d.signal),
                        fatigue: Number(d.fatigue),
});
const data_raw = FileAttachment("data/data_sources/emg_data.csv").csv({typed: true}).then((D) => D.map(coerceRow));

//const surveyData = FileAttachment("./data/study_data.json").json();
//const forecast = FileAttachment("./data/forecast.json").json();
//const surveyData = FileAttachment("./data/study_data.csv").csv().then((D) => D.map(coerceRow));
const surveyData = FileAttachment("data/survey_data.csv").csv({typed: true}).then((D) => D.map(coerceRow));

```
<style>

.col {
  float: left;
  width: 20%;
  margin-left: 0px;
  margin-right: 0px;
  padding-left: 0px;
  padding-right: 0px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}
</style>




```js
//display(data_raw)

display(Plot.plot((() => {
  const n = 5; // number of facet columns
  const keys = Array.from(d3.union(data_raw.map((d) => d.id)));
  const index = new Map(keys.map((key, i) => [key, i]));
  const fx = (key) => index.get(key) % n;
  const fy = (key) => Math.floor(index.get(key) / n);
  return {
    height: 800,
    axis: null,
    y: {insetTop: 10},
    fx: {padding: 0.03},
    color: {
    type: "sequential",
    scheme: "Oranges"
  },
    marks: [
      Plot.lineY(data_raw, Plot.normalizeY("extent", {
        x: "time",
        y: "signal",
        stroke: "fatigue",
        fx: (d) => fx(d.id),
        fy: (d) => fy(d.id)
      })),
      Plot.text(keys, {fx, fy, frameAnchor: "top-left", dx: 6, dy: 6}),
    ]
  };
})()))


// display(
//   Plot.plot({
//       grid: true,
//   inset: 10,
//   width: 928,
//   height: 240,
//      facet: {
//     data: data_raw,
//     x: "date"
//   },
//   marks:[
//   Plot.line(data_raw, {x: "time", y: "signal"})]
//   }))

// function FatiguePlot(data, {width} = {}) {
//   return Plot.plot({
//     //title: "Experienced Fatigue",
//     width,
//     marginRight:0,
//     marginLeft: 75,
//     //marginRight: 70,
//     y: {type: "time", ticks: "day", label: null, inset:48},
//     //x: {grid: true, inset: 10, label: "Level of Fatigue", type:"point",domain: [1,2,3,4, 5]},
//     height: 1000,
//     //y:{grid:true},
//     //facet: {marginRight: 79},
//     marks: [
//         //Plot.gridY({strokeWidth:40, tickSpacing: 96}),
//         //Plot.rectX({length: 1}, {y1: 0, y2: 1.4, fill: "red", fillOpacity: 0.3}),
//         Plot.axisX({label: null, anchor: "top", scale: null}),
//         Plot.lineX(data, {
//         y: "date",
//         x: "fatigue",
//         clip: false
//       }),
//     //Plot.barX(data, {x: "fatigue", y: "steps", fill: "green", dx: -2, dy: -2, facet:"include"})

//     ]
//   });
// }
// function StepPlot(data){

// return Plot.plot({
//   //x: {padding: 0.4},
//   margin:0,
//     x: {domain:[0,15000]},
//     height: 1000,
//      marks: [
//     Plot.axisY({ticks: []}),
//    // Plot.axisX({label: null, anchor: "top"}),
//     //Plot.barY(alphabet, {x: "letter", y: "frequency", dx: 2, dy: 2}),
//     Plot.barX(data, {x: "steps", y: "date", fill: "green", dx: -2, dy: -2})
//   ]
// })
// }
// display(Plot.plot({
//   grid: true,
//   inset: 10,
//   width: 928,
//   height: 240,
//   y: {type: "time", ticks: "day", label: null},
//   facet: {
//     data: surveyData,
//     x: "variable"
//   },
//   marks: [
//     Plot.frame(),
//     Plot.line(surveyData, Plot.normalizeX("extent", {y: "date", x: "y",stroke: "#ccc"})),
//     //Plot.dot(anscombe, {x: "date", y: "y", stroke: "currentColor", fill: "white"})
//   ]
// }))

// display(Plot.plot((() => {
//   const n = 3; // number of facet columns
//   const keys = Array.from(d3.union(surveyData.map((d) => d.variable)));
//   const index = new Map(keys.map((key, i) => [key, i]));
//   const fx = (key) => index.get(key) % n;
//   const fy = (key) => Math.floor(index.get(key) / n);
//   const getMax = (key) => Math.max(key);
//   return {
//     height: 300,
//     axis: null,
//     y: {insetTop: 10},
//     fx: {padding: 0.03},
//     x: {grid:true},
//     //y: {domain: [0, 100], grid: true},
//     //(d) => getMax(d.variable)
//     marks: [
//       Plot.lineY(surveyData, Plot.normalizeY("extent", {
//         x: "date",
//         y: "y",
//         fx: (d) => fx(d.variable),
//         fy: (d) => fy(d.variable)
//      }
//      )
//       ),
//       Plot.text(keys, {fx, fy, frameAnchor: "top-left", dx: 6, dy: 6}),
//       Plot.frame()
//     ]
//   };
// })()))
// new Line(
//        {
//           element: '#viz0',
//          data: { y: survey_data["fatigue"]},
//          margin: { top: 40, left: 40, right: 40, bottom: 40 },
//          axisStrokeWidth: 1,
//          fillWeight: 1,
//          axisRoughness: 1,
//          circle: false,
//        }
//      ); 



//const parseDate = utcParse("%m/%d/%Y");

//const coerceRow = (d) => ({date: parseDate(d)});
//display(survey_data.date.map(parseDate))


// new Line({
//   element: '#viz0',
//   data: (({ fatigue, steps }) => ({ fatigue, steps }))(survey_data),
//   y1: 'fatigue',
//   x: survey_data.date.map(parseDate),
//   interactive: false,
//   //y2: 'cost',
//   //y3: 'profit'
// })

//const features = penguins.map((f) => ({
 // fatigue: f.fatigue
  //magnitude: f.properties.mag,//
  //longitude: f.geometry.coordinates[0],
  //latitude: f.geometry.coordinates[1]
//}));


```
