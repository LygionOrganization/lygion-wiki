(function () {
  "use strict";

  var downloadFilePattern = /\.(step|stp|stl|dxf|dwg|zip|7z|rar)(?:[?#].*)?$/i;

  function getFilename(href) {
    try {
      var url = new URL(href, window.location.href);
      var segments = url.pathname.split("/").filter(Boolean);
      return decodeURIComponent(segments[segments.length - 1] || "download");
    } catch (error) {
      var cleanHref = href.split(/[?#]/)[0];
      var parts = cleanHref.split("/");
      return decodeURIComponent(parts[parts.length - 1] || "download");
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("a[href]").forEach(function (link) {
      var href = link.getAttribute("href");

      if (!href || !downloadFilePattern.test(href)) {
        return;
      }

      if (!link.hasAttribute("download") || link.getAttribute("download") === "download") {
        link.setAttribute("download", getFilename(href));
      }
    });
  });
})();
