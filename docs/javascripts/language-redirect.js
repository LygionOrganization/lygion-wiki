(function () {
  "use strict";

  var storageKey = "lygion-wiki-language-redirected";
  var script = document.currentScript;

  if (!script) {
    return;
  }

  var siteRoot = new URL("../", script.src);
  var currentPath = window.location.pathname.replace(/\/index\.html$/, "/");
  var rootPath = siteRoot.pathname.replace(/\/index\.html$/, "/");

  if (currentPath !== rootPath || window.localStorage.getItem(storageKey)) {
    return;
  }

  window.localStorage.setItem(storageKey, "true");

  var browserLanguage = (navigator.language || "").toLowerCase();
  if (!browserLanguage.startsWith("zh")) {
    window.location.replace(new URL("en/", siteRoot).href);
  }
})();
