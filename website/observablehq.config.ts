// See https://observablehq.com/framework/config for documentation.
export default {
  // The project’s title; used in the sidebar and webpage titles.
  title: "Do Algorithms Care?",
  //theme: "deep-space",
  // The pages and sections in the sidebar. If you don’t specify this option,
  // all pages will be listed in alphabetical order. Listing pages explicitly
  // lets you organize them into sections and have unlisted pages.
  pages: [
     {

       name: "",
       pages: [
        {name: "About", path: "/about"},
        {name: 'The Study', path: '/prediction'},
        {name: "N=1", path: "/n=1"},
        {name: "N=2", path: "/n=2"},
         {name: "Protocol", path: "/protocol"},
         {name: "Apricot Sensor-Kit N2", path: "/sensor-kit"},
         {name: "Nectar Core Watch", path: "/watch"},
         {name: "Podcast", path: "/podcast"},
         {name: "Research", path: "/research"},
         {name: "Readings", path:'/readings'},
         {name: "Code", path: "/code"},
         {name: "Get in touch", path: "/contact"},

        // {name: "EMG Data", path: "/emg_data"},
       ],
  

     }
   ],
    style: "styles.css",
    pager: false,




   //--apricot-200: #fdece2;
   //--apricot-300: #fcddc9;
   //--apricot-400: #FBCEB1;
   //--apricto-800: #f9b080;
   //--apricot-900: #f7a068;
  // Some additional configuration options and their defaults:
  // theme: "default", // try "light", "dark", "slate", etc.
  // header: "", // what to show in the header (HTML)
  footer: `<center><p>Want to stay in touch?<br> <a href='mailto:algorithmic.care@gmail.com'> Write us an email</a> or sign up to our email list.</p> <iframe src="https://algorithmiccare.substack.com/embed" width="400" height="100" style="border:1px solid #EEE; background:white;" frameborder="0" scrolling="no"></iframe></cemter>`
   // what to show in the footer (HTML)
  // toc: true, // whether to show the table of contents
  // pager: true, // whether to show previous & next links in the footer
  // root: "docs", // path to the source root for preview
  // output: "dist", // path to the output root for build
  // search: true, // activate search

};
