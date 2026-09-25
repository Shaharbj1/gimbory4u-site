/**
 * Gimbory4U – tiny router in front of the static assets.
 * Runs only for "/" and "/index.html" (see run_worker_first in wrangler.jsonc).
 * Everything else is served straight from ./public, with _redirects and _headers applied.
 */
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // one canonical homepage URL
    if (url.pathname === "/index.html") {
      url.pathname = "/";
      return Response.redirect(url.toString(), 301);
    }

    // serve the homepage file for "/"
    if (url.pathname === "/") {
      url.pathname = "/index.html";
      return env.ASSETS.fetch(new Request(url.toString(), request));
    }

    return env.ASSETS.fetch(request);
  },
};
