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
        {name: "N=1", path: "/n=1"},
        {name: "N=2", path: "/n=2"},
         {name: "Protocol", path: "/protocol"},
         {name: "Apricot Sensor-Kit N2", path: "/sensor-kit"},
         {name: "Research", path: "/research"},
         {name: "Code", path: "/code"},
        // {name: "EMG Data", path: "/emg_data"},
       ],
  

     }
   ],
    style: "styles.css",
    pager: false




   //--apricot-200: #fdece2;
   //--apricot-300: #fcddc9;
   //--apricot-400: #FBCEB1;
   //--apricto-800: #f9b080;
   //--apricot-900: #f7a068;
  // Some additional configuration options and their defaults:
  // theme: "default", // try "light", "dark", "slate", etc.
  // header: "", // what to show in the header (HTML)
  // footer: "Built with Observable.", // what to show in the footer (HTML)
  // toc: true, // whether to show the table of contents
  // pager: true, // whether to show previous & next links in the footer
  // root: "docs", // path to the source root for preview
  // output: "dist", // path to the output root for build
  // search: true, // activate search

};
