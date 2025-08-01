/** @type {import('next').NextConfig} */
module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: "/api/ask",
        destination: process.env.BACKEND_URL + "/ask"
      },
      {
        source: "/api/podcast",
        destination: process.env.BACKEND_URL + "/podcast"
      }
    ];
  }
};