(function () {
  "use strict";

  var script = document.currentScript;

  if (!script) {
    return;
  }

  var siteRoot = new URL("../", script.src);
  var currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
  var rootPath = siteRoot.pathname.replace(/\/index\.html$/, "/");

  // Only choose a language from the language-neutral site entry point. Direct
  // links to either the Chinese or English documentation must remain intact.
  if (currentPath !== rootPath) {
    return;
  }

  var browserLanguage = (navigator.language || "").toLowerCase();
  var isSimplifiedChinese =
    browserLanguage === "zh-cn" ||
    browserLanguage === "zh-sg" ||
    browserLanguage.startsWith("zh-hans");

  // Chinese is the default site. Send every browser language other than
  // Simplified Chinese (including Traditional Chinese) to the English entry.
  if (!isSimplifiedChinese) {
    window.location.replace(new URL("en/", siteRoot).href);
  }
})();
