/**
 * Gimbory4U – tiny router in front of the static assets.
 * 1. www.gimbory4u.co.il → gimbory4u.co.il (301, keeps path + query)
 * 2. /index.html → / (301) and "/" serves index.html
 * Everything else goes to the static assets (with _redirects and _headers applied).
 */
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.hostname.startsWith("www.")) {
      url.hostname = url.hostname.slice(4);
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
