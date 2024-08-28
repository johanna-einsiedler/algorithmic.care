---
toc: false
---

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Barcode+128+Text&display=swap">


<style>
@import url('https://fonts.googleapis.com/css2?family=family=Libre+Barcode+128+Text&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
@import "compass/css3";
@import url("https://fonts.googleapis.com/css2?family=Advent+Pro:ital,wght@0,100..900;1,100..900&display=swap");
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url("https://fonts.googleapis.com/css?family=Glegoo");
:root {
  --apricot-200: #fdece2;
  --apricot-300: #fcddc9;
  --apricot-400: #FBCEB1;
  --apricot-800: #f9b080;
  --apricot-900: #f7a068;
}
@font-face {
  font-family: "Kalam";
  src: url('${await kalam.url()}');
}

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: "Poppins";
  margin: 0rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 4rem 0;
  font-family: "Poppins";
  /*padding-bottom: 5rem;*/
  padding-top: 2rem;
  max-width: none;
  text-align: center;
  /* font-weight: 900; */
  line-height: 1;
  /*background: linear-gradient(30deg, var(   --theme-foreground-faint), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;*/
  font-size: 5em;
  color: 'white';
  text-align: center;

}


.hero h2 {
  margin: 0;
  max-width: 34em;
  font-size: 20px;
  font-style: initial;
  font-weight: 500;
  line-height: 1.5;
  color: var(--apricot-900);
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}
.button {
  position: relative;
  z-index: 1;
  background: var(--apricot-900);
  border: 3px solid;
  border-color: var(--apricot-400);
  border-radius: 0.75rem;
  color: var(--apricot-300);
  padding: 0.75rem 1rem;
  text-decoration: none;
  transition: 250ms ease-in-out;
  transition-property: all;
}

.button:hover,
.button:focus {
  color: var(--apricot-200);
  background-color: var(--apricot-800);
  transform: scale(1.1);
}

.text {
  filter: drop-shadow(0 0 1px currentcolor);
}

.button:after {
  content: "";
  position: absolute;
  z-index: -1;
  inset: 0;
  opacity: 0.6;
  border-radius: inherit;
  box-shadow: 0 0 1em 0.5em var(--apricot-300);
  transition: 250ms ease-in-out;
  transition-property: opacity;
}

.button:hover::after,
.button:focus::after {
  opacity: 0.6;
}


.scroll-container {
  position: relative;
  margin: 1rem auto;
  font-family: var(--sans-serif);
}

.scroll-info {
  position: sticky;
  aspect-ratio: 16 / 9;
  top: calc((100% - 9 / 16 * 100vw) / 2);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 64px;
  transition: ease background-color 0.5s;
  background-color: black;
}

.scroll-info--step-1 {
  background-color:   var(--theme-background);
}

.scroll-info--step-2 {
  background-color:  var(--theme-background)
}

.scroll-info--step-3 {
  background-color:  var(--theme-background)
}

.scroll-info--step-4 {
  background-color:  var(--theme-background);
}

.scroll-section {
  position: relative;
  aspect-ratio: 16 / 8;
  margin: 0rem 0;
  display: flex;
  align-items: start;
  justify-content: center;
 /*border: solid 1px var(--theme-foreground-focus);*/
  background: color-mix(in srgb, var(--theme-foreground-focus) 5%, transparent);
  padding: 0rem;
  ÷box-sizing: border-box;
  background-color:  var(--theme-background);
}

blockquote {
  position: relative;
  margin: 80px auto;
  width: 70%;
  font-size: 30px;
  line-height: 56px;
  padding-left: 40px;
  border-left: 2px solid #7B7B7B;
  font-family: "Open Sans"

}

blockquote span {
  display: block;
  text-align: right;
  font-size: 20px;
  line-height: 30px;
  margin-top: 10px;
  text-transform: uppercase;
}

blockquote.tweet-this:hover a {
  opacity: 0.5;
  transition: opacity 0.2s ease;
  text-decoration: none;
}

blockquote.tweet-this .tweet-quote {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 80%;
  height: 26px;
  margin-top: -13px;
  margin-left: -36px;
  transition: all 0.2s ease;
}


html {
    scroll-behavior: smooth;

}

.arrow {
  border: solid #000000;
  border-width: 0 10px 10px 0;
  display: inline-block;
  padding: 10px;

}

.down {
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);
}

#myVideo {
  position: fixed;
  right: 0;
  top: 0;
  max-height:100%;
 /*min-width: 100%;
  min-height: 100%;*/
}

/* Add some content at the bottom of the video/page */
.content {
  position: fixed;
  top: 0;
  background: rgba(255, 249, 241, .7);
  color: 'black';
  height:100%;
  width: 100%;
}

</style>




<section class="scroll-container">
 <div class="scroll-section" data-step="1" style="padding-bottom: 10rem">
   <div class=" hero">
  <video src="images/watches.mp4" id='myVideo' type="video/mp4" autoplay muted loop controls width='100%' ></video>
  <div class="content">
  <h1 style='color:black'>DO ALGORITMS CARE?</h1>
    <a href="#section2">  <i class="arrow down"></i> </a>
  </div>
    <center>

  </center>
  </div>
  </div>
<div class="scroll-section" data-step="2" id="section2">
<div class="row">
  <div>
  <center>
  <video src="images/contraction_transparent.mp4" alt="drawing" width="300" autoplay muted loop type="video/mp4"> </video></center>
  </center>
  </div>
<p><i>Do Algorithms Care?'</i>  is an interdisciplinary collaboration between artist Amanda Bennetts (AU) and data scientist Johanna Einsiedler (AT). At the core of this project is an N=1 study, typically challenged in scientific circles for its limited generalizability, yet here serves as a critical methodological pivot. Using a DIY smartwatch and EMG (electromyography) and MMG (mechanomyogram) sensor kits, the duo engage in self-monitoring to collect their physiological data. This personalized data collection reflects a methodological shift in research practices, emphasizing the need for individual agency to manage and use biodata. The sensor measurements, smartwatch data and results from a wellbeing questionnaire are fed into a machine-learning model, developed to predict subjective fatigue. 




</p>


  <p>  <a href="/about">More about the project </a> |  <a href="/prediction">The Study</a>  |  <a href="/research">Research </a> |  <a href="/protocol">Protocol </a>  |<a href="/podcast">Podcast </a></p>

<p> DIY Instructions:    <a href="/sensor-kit">Apricot Sensor-Kit N2 </a> |  <a href="/wathch"> Nectar Core Watch </a> | <a href="/code">Open Source Code </a> </p>

<p> The Quantified Self:    <a href="/n=1">N=1 </a> |  <a href="/n=2">N=2 </a> </p>

  <center>
<p> <emph> Want to stay updated? </emp> </p>
<iframe src="https://algorithmiccare.substack.com/embed" width="480" height="320" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe>
</center>
<br>



 

  <div class="column"></div>
</div>
</div>

  <div class="scroll-section" data-step="3" id="section3">
  <blockquote class="tweet-this"><a href = "https://issues.org/limits-of-data-nguyen/">
The wider the user base for the data, the more decontextualized the data needs to be. </a><span><p>- C. Thi Nguyen </span></p>
</div>
  </div>
  </div>
 
  <!-- <div class="scroll-section" data-step="3">STEP 3</div>
  <div class="scroll-section" data-step="4">STEP 4</div> -->
</section>

```js
const info = document.querySelector(".scroll-info");
const targets = document.querySelectorAll(".scroll-section");

const observer = new IntersectionObserver((entries) => {
  for (const target of Array.from(targets).reverse()) {
    const rect = target.getBoundingClientRect();
    if (rect.top < innerHeight / 2) {
      //info.textContent = target.dataset.step;
      info.className = `scroll-info scroll-info--step-${target.dataset.step}`;
      return;
    }
  }
  info.className = "scroll-info";
  //info.textContent = 
}, {
  rootMargin: "-50% 0% -50% 0%"
});

for (const target of targets) observer.observe(target);

invalidation.then(() => observer.disconnect());



$("arrow down").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });;
```

