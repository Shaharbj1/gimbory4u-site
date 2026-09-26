/**
 * Gimbory4U – tiny router in front of the static assets.
 * 1. http:// → https:// and www.gimbory4u.co.il → gimbory4u.co.il (one 301, keeps path + query)
 * 2. /index.html → / (301) and "/" serves index.html
 * Everything else goes to the static assets (with _redirects and _headers applied).
 */
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    const isLocal = url.hostname === "localhost" || url.hostname === "127.0.0.1";
    if (!isLocal && (url.protocol === "http:" || url.hostname.startsWith("www."))) {
      url.protocol = "https:";
      url.hostname = url.hostname.replace(/^www\./, "");
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname === "/index.html") {
      url.pathname = "/";
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname === "/") {
      url.pathname = "/index.html";
      return env.ASSETS.fetch(new Request(url.toString(), request));
    }

    return env.ASSETS.fetch(request);
  },
};
